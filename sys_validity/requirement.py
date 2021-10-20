import sys

"""Checking system requirement for import library"""
def check():
    if(int(sys.version[0])<3):
        print("Xss is not comptible to version < 3.4")
        exit(1)
    import os
    import concurrent.futures
    from urllib.parse import urlparse

    try:
        import bs4
    except ImportError:
        print("Beautiful soap NOT FOUND...")
        os.system('pip3 install bs4')
        print("Beautiful soap install successfully")



