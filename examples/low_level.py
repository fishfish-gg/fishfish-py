import os
from typing import List

from fishfish import Client, Domain, Category


def main():
    client: Client = Client(token=os.environ["API_KEY"])

    domain: Domain = client.get_domain("steamncommunty.ru")
    print(domain)

    domains: List[Domain] = client.get_all_domains(category=Category.SAFE, full=True)
    print(f"{len(domains)=}")
    print(domains[0])


if __name__ == "__main__":
    main()
