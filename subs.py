import threading
import socket
import requests
def check200(subd):
        try:
            # if this raises an ERROR, that means the subdomain does not exist
            requests.get(url)
        except requests.ConnectionError:
            # if the subdomain does not exist, just pass, print nothing
            pass
        else:
           print("[+] subdomain found : ",url)
    # read all subdomains
file = open("subs.txt")
    # read all wordlist
wordlist = file.read()
    # split by new lines
domain="jiit.ac.in"
subdomains = wordlist.splitlines()
for subdomain in subdomains:
      url = f"http://{subdomain}.{domain}"
      t = threading.Thread(target=check200,args=(url)
      t.start()
