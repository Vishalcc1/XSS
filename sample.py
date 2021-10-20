import concurrent.futures
import os
import sys
import time

def chcek(soup):
    a=1
    for i in soup:
       a=soup[i]
       break
    form = a.find_all
