import re

from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, parse_qs, urlencode
from lib import EstableSession
from crawler import crawler


def getMethod(soup):
    # print("Get method ")
    soup, payload, args = soup
    url, soup = soup
    links = soup.find_all("a", href=True)

    for link in links:
        url = link["href"]
        if url.startswith("http://") is False or url.startswith("https://") is False or url.startswith(
                "mailto:") is False:
            base = urljoin(url, link["href"])
            query = urlparse(base).query
            if query != "":

                query_payload = query.replace(query[query.find("=") + 1:len(query)], payload, 1)
                test = base.replace(query, query_payload, 1)

                query_all = base.replace(query, urlencode({x: payload for x in parse_qs(query)}))

                if not url.startswith("mailto:") and not url.startswith("tel:"):
                    req = EstableSession.estableSession(args)
                    resp = req.get(args)
                    if payload in resp.text or payload in soup.session.get(query_all).text:
                        print("Xss found", url)
                    else:
                        print("Not Found yet", url)
