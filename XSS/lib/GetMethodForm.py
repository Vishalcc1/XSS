from urllib.parse import urljoin
import EstableSession
from crawler import crawler


def getMethodForm(soup):
    """Try to find a Text,form ,search area for checking xss attack"""
    soup, payload, args = soup
    url, soup = soup
    forms = soup.find_all("form", method=True)

    """traverse form one by one and apply payload..."""

    for form in forms:
        try:
            action = form["action"]
        except KeyError:
            action = url

        if form["method"].lower().strip() == "get":

            keys = {}
            for key in form.find_all(["input", "textarea"]):
                try:
                    if key["type"] == "submit":
                        keys.update({key["name"]: key["name"]})

                    else:
                        keys.update({key["name"]: payload})

                except Exception as e:
                    try:
                        keys.update({key["name"]: payload})
                    except KeyError as e:
                        print("Internal error: " + str(e))

            req = EstableSession.estableSession(args)
            resp = req.get(urljoin(url, action), params=keys)
            if payload in resp.text:
                print("Xss found", url)
            else:
                print("Not Found yet", url)
