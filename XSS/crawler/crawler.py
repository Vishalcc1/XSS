import concurrent.futures

from bs4 import BeautifulSoup
from csv import reader
import requests
import json
import pandas as pd


def urlParser(append_url, url):
    """Checking for external link and try to avoid it"""
    if append_url[0:4] == 'http':
        if append_url.split('.', 2)[1] == url.split('.', 2)[1]:
            return append_url
        else:
            return -1
    if append_url == "#":
        return url
    """Checking to mail link"""
    if append_url[0:7] == "mailto:":
        return -1
    if append_url[0:11] == "javascript:":
        return -1
    """append a link into a url"""
    if append_url[0] == '/':
        return url + append_url
    return url + '/' + append_url


class crawler:
    isVisited = {}
    url, temp = [], []
    args = None
    depth = 1

    @classmethod
    def session(self):
        req = requests.Session()
        req.proxies = self.args.proxy
        req.headers = self.args.header
        req.cookies.update(json.loads(self.args.cookie))
        return req

    @classmethod
    def fetchPage(self, url):

        req = self.session()
        r = req.get(self.args.url)
        soup = BeautifulSoup(r.content, 'html.parser')
        self.isVisited[url] = soup.__copy__()

        for obj in soup.find_all("a", href=True):
            url = obj["href"]
            finalurl = urlParser(url, self.args.url)
            if finalurl == -1:
                continue
            if finalurl not in self.isVisited:
                self.temp.append(finalurl)

    @classmethod
    def crawler(self, args):
        self.args = args
        self.url.append(args.url)
        # print(len(self.url))
        """Start a crawler and store the soup"""
        while len(self.url) > 0 and self.depth != args.depth:
            self.depth = self.depth + 1
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(self.fetchPage, self.url)
            self.url = self.temp
            self.temp = []
            """checking a single web parse if True then break"""
            if args.single:
                break
        return self.isVisited
