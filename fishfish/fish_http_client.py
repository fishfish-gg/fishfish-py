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
from fishfish.exceptions import ObjectDoesntExist, AuthenticatedRoute
from fishfish.jwt import JWT


class FishHTTPClient:
    """
    All public methods can raise the following:

    :py:class:`FishFishException`
    :py:class:`Unauthorized`
    :py:class:`Forbidden`
    :py:class:`ObjectDoesntExist`
    :py:class:`ServerError`

    If a route also requires authentication it may raise:
    :py:class:`AuthenticatedRoute`
    """

    def __init__(self, *, token: Optional[str] = None):
        """
        Parameters
        ----------
        token : Optional[str]
            Your FishFish session token to use in authenticated requests.
            This is generated via the FishFish bot
        """
        self.__refresh_token: Optional[str] = token
        self.__current_session_token: Optional[JWT] = None
        self.__session: httpx.Client = httpx.Client(
            base_url="https://api.fishfish.gg/v1"
        )

        self._ensure_token()

    def cleanup(self) -> None:
        """Cleans up the underlying resources."""
        self.__session.close()

    @property
    def _is_authenticated_instance(self) -> bool:
        """Does this Http instance appear to have authorization?"""
        return bool(self.__refresh_token)

    def _ensure_token(self):
        if (
            self.__current_session_token
            and not self.__current_session_token.has_expired
        ) or not self.__refresh_token:
            return

        r = self.__session.post(
            "/users/@me/tokens",
            headers={"Authorization": self.__refresh_token},
        )
        if r.status_code == 401:
            raise Unauthorized("Your provided FishFish token is invalid.")

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

        if r.status_code == 401:
            raise Unauthorized

        elif r.status_code == 403:
            raise Forbidden

        elif r.status_code == 404:
            raise ObjectDoesntExist

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
        """Insert a new domain into the database.

        Parameters
        ----------
        domain : str
            The domain you wish to create.
        description : str
            A description of the domain
        category : Category
            The category this domain fits into
        target : Optional[str]
            The target of this domain

        Returns
        -------
        Domain
            The newly created domain
        """
        if not self._is_authenticated_instance:
            raise AuthenticatedRoute

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
        """Update a domain in the database.

        Parameters
        ----------
        domain : str
            The domain to update
        target : Optional[str]
            The target for the domain
        description : Optional[str]
            The description for the domain
        category : Optional[str]
            The category for the domain

        Returns
        -------
        Domain
            The updated domain

        Raises
        ------
        ValueError
            You failed to pass any arguments to modify.
        """
        if not self._is_authenticated_instance:
            raise AuthenticatedRoute

        body = {}
        if target:
            body["target"] = target

        if description:
            body["description"] = description

        if category:
            body["category"] = category.value

        if not body:
            raise ValueError("Expected at least one value to modify.")

        r = self._request(
            "PATCH",
            f"/domains/{domain}",
            json=body,
        )
        return Domain.from_dict(r.json())

    def delete_domain(self, domain: str) -> None:
        """Delete a domain from the database.

        Parameters
        ----------
        domain : str
            The domain you wish to delete
        """
        if not self._is_authenticated_instance:
            raise AuthenticatedRoute

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
        """
        r = self._request("GET", f"/domains/{domain}")
        return Domain.from_dict(r.json())

    @overload
    def get_domains(self) -> List[str]:
        ...

    @overload
    def get_domains(
        self,
        *,
        full: bool = True,
        category: Optional[Category] = None,
    ) -> List[Domain]:
        ...

    @overload
    def get_domains(
        self,
        *,
        full: bool = False,
        category: Optional[Category] = None,
    ) -> List[str]:
        ...

    def get_domains(
        self,
        *,
        full: bool = False,
        category: Optional[Category] = None,
    ):
        """Get all domains from the database.

        Parameters
        ----------
        full : bool
            Whether or not to return full domain objects.
            This parameter requires auth.
        category : Optional[Category]
            The category of domains to return.
            This defaults to phishing & malware if full=false

        Returns
        -------
        List[str]
            A list of the domain names if full is False
        List[Domain]
            A list of domain objects if full is True
        """
        if full is True and not self._is_authenticated_instance:
            raise AuthenticatedRoute(
                "Requesting all domains with full=True requires authentication."
            )

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
        """Insert a new URL in the database.

        Parameters
        ----------
        url : str
            The url you wish to create.
        description : str
            A description of the url
        category : Category
            The category this url fits into
        target : Optional[str]
            The target of this url

        Returns
        -------
        URL
            The newly created url
        """
        if not self._is_authenticated_instance:
            raise AuthenticatedRoute

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
        """Update a URL in the database.

        Parameters
        ----------
        url : str
            The url to update
        target : Optional[str]
            The target for the url
        description : Optional[str]
            The description for the url
        category : Optional[str]
            The category for the url

        Returns
        -------
        URL
            The updated url

        Raises
        ------
        ValueError
            You failed to pass any arguments to modify.
        """
        if not self._is_authenticated_instance:
            raise AuthenticatedRoute

        body = {}
        if target:
            body["target"] = target

        if description:
            body["description"] = description

        if category:
            body["category"] = category.value

        if not body:
            raise ValueError("Expected at least one value to modify.")

        r = self._request(
            "PATCH",
            f"/urls/{url}",
            json=body,
        )
        return URL.from_dict(r.json())

    def delete_url(self, url: str) -> None:
        """Delete a URL from the database.

        Parameters
        ----------
        url : str
            The url you wish to delete
        """
        if not self._is_authenticated_instance:
            raise AuthenticatedRoute

        self._request("DELETE", f"/urls/{url}")

    def get_url(self, url: str) -> URL:
        """Get a single URL from the database.

        Parameters
        ----------
        url : str
            The url you wish to fetch from the API

        Returns
        -------
        URL
            The url object
        """
        r = self._request("GET", f"/urls/{url}")
        return URL.from_dict(r.json())

    @overload
    def get_urls(self) -> List[str]:
        ...

    @overload
    def get_urls(
        self,
        *,
        full: bool = True,
        category: Optional[Category] = None,
    ) -> List[URL]:
        ...

    @overload
    def get_urls(
        self,
        *,
        full: bool = False,
        category: Optional[Category] = None,
    ) -> List[str]:
        ...

    def get_urls(
        self,
        *,
        full: bool = False,
        category: Optional[Category] = None,
    ):
        """Get all urls from the database.

        Parameters
        ----------
        full : bool
            Whether or not to return full url objects.
            This parameter requires auth.
        category : Optional[Category]
            The category of domains to return.
            This defaults to phishing & malware if full=false

        Returns
        -------
        List[str]
            A list of the urls if full is False
        List[Url]
            A list of url objects if full is True
        """
        if full is True and not self._is_authenticated_instance:
            raise AuthenticatedRoute(
                "Requesting all urls with full=True requires authentication."
            )

        prepended_category = f"category={category.value}&" if category else ""
        r = self._request("GET", f"/urls?{prepended_category}full={str(full).lower()}")
        data = r.json()
        return [URL.from_dict(d) for d in data] if full else data
