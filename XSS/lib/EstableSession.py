import requests
import json

def estableSession(args):
    req=requests.Session()
    req.proxies=args.proxy
    req.headers = args.header
    req.cookies.update(json.loads(args.cookie))
    return req

