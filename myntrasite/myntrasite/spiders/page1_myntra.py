#!/usr/bin/env python 
import req_proxy
import profile
from bs4 import BeautifulSoup 
from urlparse import urlparse
from urlparse import urlparse
import phan_proxy
# page1_myntra.py  page2_myntra.main()


def menucollection(a):
    parsed = urlparse(a.get("href"))
    
    if len(parsed.netloc) == 0:
        if a.get("href")[0] == "/":
            link = "http://www.myntra.com/%s" %(a.get("href"))[1:]
        else:
            link = "http://www.myntra.com/%s" %(a.get("href"))
    else:
        link = a.get("href")
    
    parsed2 = urlparse(link)
    
    
    if (len(parsed.path) > 2) and (a.get_text() != "View All") and (parsed2.netloc == "www.myntra.com"):
        return  link, parsed.path, a.get_text()
    


def main():
    link = "http://www.myntra.com/"
    page  = req_proxy.main(link) 
    #page = phan_proxy.main(link)
   
    
    if  not page:
        main()
    
    soup = BeautifulSoup(page)

    tag_mklevel2 = soup.find_all("a", attrs={"class":"mk-level2 "})
    
    #print len(filter(None,  map(menucollection, tag_mklevel2)))    
    return   filter(None,  map(menucollection, tag_mklevel2))
    



if __name__=="__main__":
    print main()
    #profile.run("main()")     
