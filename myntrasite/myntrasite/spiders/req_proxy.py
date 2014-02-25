import requests
from random import choice
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',)


def main(link):
    #f = open("/home/user/Desktop/mygoodproxy2.txt")
    #f = open("/home/desktop/mygoodproxy3.txt")
    f = open("/home/desktop/proxy5")
    pass_ip_list = f.read().strip().split("\n")    
    f.close()

    page = None 

    loop = True
    i = 0 

    while i < 6 and loop is True:
        pass_ip = choice(pass_ip_list).strip()

	i = i + 1

 	try: 
            #http_proxy = "http://" + pass_ip
            http_proxy = "http://" + "vinku:india123@" + pass_ip
            proxyDict = {"http"  :http_proxy}

            r = requests.get(link,  proxies=proxyDict)

            if r.status_code in [200, 301]:
                page = r.text

                r.cookies.clear()
                r.close()

		loop = False

	except:
	    loop = True

    return page



if __name__=="__main__":
    link = "http://docs.python-requests.org/en/latest/user/quickstart/#response-content"
    page = main(link)
    print page
    
        
    

