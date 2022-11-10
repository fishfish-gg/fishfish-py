from typing import Optional, overload, List, Literal, Dict

import httpx

from fishfish import (
    APIStatus,
    Domain,
    Category,
    URL,
    Unauthorized,
    Forbidden,
    ServerError,
    FishFishException,
)
from fishfish.jwt import JWT


# TODO Client side checks for authenticated routes
class Http:
    def __init__(self, *, token: str):
        self.__refresh_token: str = token
        self.__current_session_token: Optional[JWT] = None
        self.__session: httpx.Client = httpx.Client(
            base_url="https://api.fishfish.gg/v1"
        )

        self._ensure_token()

    def cleanup(self) -> None:
        """Cleans up the underlying resources."""
        self.__session.close()

    def _ensure_token(self):
        if (
            self.__current_session_token
            and not self.__current_session_token.has_expired
        ):
            return

        r = self.__session.post(
            "/users/@me/tokens",
            headers={"Authorization": self.__refresh_token},
        )
        data = r.json()
        self.__current_session_token = JWT(data["token"], data["expires"])
        self.__session.headers = httpx.Headers(
            {"Authorization": self.__current_session_token.token}
        )

    def _request(
        self,
        method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"],
        url: str,
        *,
        json: Optional[Dict] = None,
    ) -> httpx.Response:
        self._ensure_token()
        if json:
            r = self.__session.request(method, url, json=json)
        else:
            r = self.__session.request(method, url)

        # TODO Provide more information within exceptions
        if r.status_code == 401:
            raise Unauthorized

        elif r.status_code == 403:
            raise Forbidden

        elif r.status_code >= 500:
            raise ServerError

        return r

    def api_status(self) -> APIStatus:
        """Get the status of the API."""
        raise FishFishException(
            "This route is currently undocumented, and is therefore not yet implemented."
        )

    def create_domain(
        self,
        domain: str,
        *,
        description: str,
        category: Category,
        target: Optional[str] = None,
    ) -> Domain:
        """Insert a new domain into the database."""
        body = {"category": category.value, "description": description}
        if target:
            body["target"] = target

        r = self._request(
            "POST",
            f"/domains/{domain}",
            json=body,
        )
        return Domain.from_dict(r.json())

    def update_domain(
        self,
        domain: str,
        *,
        target: Optional[str] = None,
        description: Optional[str] = None,
        category: Optional[Category] = None,
    ) -> Domain:
        """Update a domain in the database."""
        body = {}
        if target:
            body["target"] = target

        if description:
            body["description"] = description

        if category:
            body["category"] = category.value

        r = self._request(
            "PATCH",
            f"/domains/{domain}",
            json=body,
        )
        return Domain.from_dict(r.json())

    def delete_domain(self, domain: str) -> None:
        """Delete a domain from the database."""
        self._request("DELETE", f"/domains/{domain}")

    def get_domain(self, domain: str) -> Domain:
        """Get a single domain from the database.

        Parameters
        ----------
        domain : str
            The domain you wish to fetch from the API

        Returns
        -------
        Domain
            The domain object

        Raises
        ------
        Unauthorized
            ...
        Forbidden
            ...
        ServerError
            ...
        """
        r = self._request("GET", f"/domains/{domain}")
        return Domain.from_dict(r.json())

    @overload
    def get_all_domains(self) -> List[str]:
        ...

    @overload
    def get_all_domains(
        self,
        *,
        full: bool = True,
        category: Optional[Category] = None,
    ) -> List[Domain]:
        ...

    @overload
    def get_all_domains(
        self,
        *,
        full: bool = False,
        category: Optional[Category] = None,
    ) -> List[str]:
        ...

    def get_all_domains(
        self,
        *,
        full: bool = False,
        category: Optional[Category] = None,
    ):
        """Get all domains from the database."""
        prepended_category = f"category={category.value}&" if category else ""
        r = self._request(
            "GET", f"/domains?{prepended_category}full={str(full).lower()}"
        )
        data = r.json()
        return [Domain.from_dict(d) for d in data] if full else data

    def create_url(
        self,
        url: str,
        *,
        description: str,
        category: Category,
        target: Optional[str] = None,
    ) -> URL:
        """Create a new URL in the database."""
        body = {"category": category.value, "description": description}
        if target:
            body["target"] = target

        r = self._request(
            "POST",
            f"/urls/{url}",
            json=body,
        )
        return URL.from_dict(r.json())

    def update_url(
        self,
        url: str,
        *,
        target: Optional[str] = None,
        description: Optional[str] = None,
        category: Optional[Category] = None,
    ) -> URL:
        """Update a URL in the database."""
        body = {}
        if target:
            body["target"] = target

        if description:
            body["description"] = description

        if category:
            body["category"] = category.value

        r = self._request(
            "PATCH",
            f"/urls/{url}",
            json=body,
        )
        return URL.from_dict(r.json())

    def delete_url(self, url: str) -> None:
        """Delete a URL from the database."""
        self._request("DELETE", f"/urls/{url}")

    def get_url(self, url: str) -> URL:
        """Get a single URL from the database."""
        r = self._request("GET", f"/urls/{url}")
        return URL.from_dict(r.json())

    @overload
    def get_all_urls(self) -> List[str]:
        ...

    @overload
    def get_all_urls(
        self,
        *,
        full: bool = True,
        category: Optional[Category] = None,
    ) -> List[URL]:
        ...

    @overload
    def get_all_urls(
        self,
        *,
        full: bool = False,
        category: Optional[Category] = None,
    ) -> List[str]:
        ...

    def get_all_urls(
        self,
        *,
        full: bool = False,
        category: Optional[Category] = None,
    ):
        """Get all URL's from the database."""
        prepended_category = f"category={category.value}&" if category else ""
        r = self._request("GET", f"/urls?{prepended_category}full={str(full).lower()}")
        data = r.json()
        return [URL.from_dict(d) for d in data] if full else data
