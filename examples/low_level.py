import os
from typing import List

from fishfish import Http, Domain, Category


def main():
    http: Http = Http(token=os.environ["API_KEY"])

    domain: Domain = http.get_domain("steamncommunty.ru")
    print(domain)

    domains: List[Domain] = http.get_all_domains(category=Category.SAFE, full=True)
    print(f"{len(domains)=}")
    print(domains[0])


if __name__ == "__main__":
    main()
