import os
from typing import List

from fishfish import FishHTTPClient, Domain, Category, URL


def main():
    http: FishHTTPClient = FishHTTPClient(token=os.environ["API_KEY"])
    # http: FishHTTPClient = FishHTTPClient()

    domain: Domain = http.get_domain("steaemcommunnity.com")
    print(domain)

    domains: List[Domain] = http.get_domains(category=Category.SAFE, full=True)
    print(f"{len(domains)=}")
    print(domains[0])

    urls: List[URL] = http.get_urls(full=True)
    print(f"{len(urls)=}")


if __name__ == "__main__":
    main()
