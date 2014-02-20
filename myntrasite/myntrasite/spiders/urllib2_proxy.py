import urllib2
from random import choice

def main(link):
    f = open("/home/user/Desktop/proxy5")
    iplist = f.read().strip().split("\n")
    ip = choice(iplist).strip()
    f.close()

    proxy = urllib2.ProxyHandler({'http': 'http://vinku:india123@'+ip})
    auth = urllib2.HTTPBasicAuthHandler()
    opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    conn = urllib2.urlopen(link)
    return   conn


if __name__=="__main__":
    link = "http://docs.python-requests.org/en/latest/user/quickstart/#response-content"
    page = main(link)
    print page.read()
