import requests
discovered = []
def check200(url):
    response = requests.get(url)
    if(response.status_code == 200):
        discovered.append(url)
        # print("[+]discovered asset:",url)

def content_discovery(domain):
    import threading
    #open the content discovery file
    file = open("directory.txt")
    wordlist = file.read()
    contents = wordlist.splitlines()
    discovered.clear()
    for path in contents:
        url = f"https://{domain}/{path}"
        th = threading.Thread(target=check200,kwargs={'url':url})
        th.start()
    th.join()
    return discovered
# content_discovery("shoppinglikes.in")

