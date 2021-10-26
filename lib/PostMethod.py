import re

from bs4 import BeautifulSoup
from lib import EstableSession
from crawler import crawler
def postMethod(soup):
    """Try to find a Text,form ,search area for checking xss attack"""
    soup,payload,args=soup
    url,soup=soup
    forms=soup.find_all("form",method=True)

    """traverse form one by one and apply payload..."""

    for form in forms:
        """Check for method type it Get or Post """
        if form["method"].strip().upper() == "POST":
            # print("gotm1")
            postData={}
            for inputField in form.find_all(["input","textarea"]):
                try:
                    """Every inputField are submit button or text area"""
                    if(inputField["type"]=="submit"):
                        postData[inputField["name"]]=inputField["name"]
                    else:
                        postData[inputField["name"]]=payload
                except :
                    continue
            req=EstableSession.estableSession(args)
            try:
                req=req.post(crawler.urlParser(form['action'],url),data=postData)
            except:
                """send request into same url"""
                req=req.post(url, data=postData)

            """req hand over to BeautifulSoap"""
            reqSoup=BeautifulSoup(req.content,'html.parser')
            # print(reqSoup)
            if(len(reqSoup.body.findAll(text=re.compile("2005"),limit=1))):
                print("Xss found",url)
            else:
                print("Not Found yet",url)