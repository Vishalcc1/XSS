from sys_validity import requirement
from crawler import crawler
import argparse
import sample
from lib import Checker


def ValidCheck(s):
    try:
        value = int(s)
    except ValueError:
        raise argparse.ArgumentTypeError("Expected Integer")
    if value not in [1, 2, 0]:
        raise argparse.ArgumentTypeError("Expected Integer are 0,1,2 ")


collect_soup = 1


def start():
    """Our program start from here..."""

    """Parse the argument"""
    parse = argparse.ArgumentParser()
    parse.add_argument("-u", "--url", help="Target url like {amazon.in}", required=True)
    parse.add_argument("--payload", help="Load payload  ",
                       default="<script>alert(2005)</script>")
    parse.add_argument("--method", help="Method setting(s): \n\t0: GET\n\t1: POST\n\t2: GET and POST (default)",
                       default=2,
                       type=ValidCheck)
    parse.add_argument("--single", help="Single scan. Don't use crawling", type=bool, default=False)
    parse.add_argument("--proxy", default=None, help="Set proxy ")

    parse.add_argument('--header', help='add headers ')
    parse.add_argument("--depth", type=int, help="Input for crawler. Default: 3", default=3)

    parse.add_argument("--cookie", help="Set cookie", default='''{"ID":"1094200543"}''')

    parse.add_argument("--level", help="Difficulty of payload", default=1, type=int)
    args = parse.parse_args()
    global collect_soup

    if args.level > 1:
        args.single = True
    collect_soup = crawler.crawler.crawler(args)
    sample.chcek(collect_soup)
    Checker.main(args, collect_soup)


if __name__ == "__main__":
    requirement.check()
    start()
