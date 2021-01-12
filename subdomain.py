import requests
import time
subdomainList=[]
def check200(url):
        try:
            # if this raises an ERROR, that means the subdomain does not exist
            requests.get(url)
        except requests.ConnectionError:
            # if the subdomain does not exist, just pass, print nothing
            pass
        else:
            subdomainList.append(url)
def subfinder(domain):
    import threading
    subdomainList.clear()
    # read all subdomains
    file = open("subs.txt")
    # read all words in the file
    wordlist = file.read()
    # split by new lines
    subdomains = wordlist.splitlines()
    mythreads=[]
    # t = threading.Thread(target=check200,kwargs={'url':'https://abc.domain'})
    # t.start()
    for subdomain in subdomains:
        url = f"http://{subdomain}.{domain}"
        t = threading.Thread(target=check200,kwargs={'url':url})
        mythreads.append(t)
        t.start()
    for th in mythreads:
        th.join()
    return subdomainList

