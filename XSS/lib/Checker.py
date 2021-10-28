from concurrent import futures
from lib import PostMethod
from lib import GetMethodForm
from lib import GetMethod
def main(args,urlSoup):
    """Finding the level and then load the payload ..."""
    payload=[args.payload]
    if(args.level==2):
        myfile=open("lib/level2.txt")
        for line in myfile:
            payload.append(line)
    elif(args.level==3):
        myfile = open("lib/level3.txt")
        for line in myfile:
            payload.append(line)
    elif(args.level==4):
        myfile = open("lib/level4.txt")
        for line in myfile:
            payload.append(line)

    """take url one by one and add all payload on it"""
    urlwithload=[]
    for u in urlSoup.items():
        for p in payload:
            urlwithload.append((u,p,args))

    with futures.ThreadPoolExecutor() as executor:
        print("ok futures")
        if(args.method == 0):
            """In this method try to find using a Get Method"""
            executor.map(GetMethod.getMethod, urlwithload)
            executor.map(GetMethodForm.getMethodForm, urlwithload)
        elif(args.method==1):
            """In this method try to find using a Post Method"""
            executor.map(PostMethod.postMethod,urlwithload)
        else:
            """It contain both method Get and Post"""
            executor.map(GetMethod.getMethod, urlwithload)
            executor.map(GetMethodForm.getMethodForm, urlwithload)

            executor.map(PostMethod.postMethod, urlwithload)
