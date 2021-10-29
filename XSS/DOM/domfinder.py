import requests
import concurrent.futures
from lib import EstableSession

args1 = []
sourcelist, sinklist = [], []


def sourceadder():
    try:
        file = open("DOM/source.txt")
        """Fetch a source file and add all vulnerable keyword into soup"""
        for line in file:
            sourcelist.append(line.strip('\n'))
            # print(sourcelist[-1])
        file.close()
    except:
        print("File not Found...")


def sinkadder():
    try:
        file = open("DOM/sink.txt")
        """Fetch a sink file and add all vulnerable keyword into soup"""
        for line in file:
            sinklist.append(line.strip('\n'))
            # print(sourcelist[-1])
        file.close()
    except:
        print("File not found...")


def checker(url):
    url, soup = url
    req = requests.get(url)
    for source in sourcelist:
        if source != '' and source in req.text:
            print("DOM Base vulnerability :- [", source, "] find in ", url)
    for sink in sinklist:
        if sink != '' and sink in req.text:
            print("DOM Base vulnerability :- [", sink, "] find in ", url)


def finder(args, collection):
    global args1
    arg1 = args
    sourceadder()
    sinkadder()
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.thread) as executor:
        executor.map(checker, collection.items())
