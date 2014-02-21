from bs4 import BeautifulSoup
import req_proxy
import phan_proxy
import urllib2_proxy

# page1_myntra.py  page2_myntra.main() page2_clb_myntra.py


def bnbcbl(a):
    bnbc = a.find("span", attrs={"class":["mk-filter-display"]})
    bnbc = str(bnbc.get_text()).replace("\n", " ").replace("\t", " ").replace("\r", " ").strip()

    bl = "http://www.myntra.com%s" %(a.get("href"))

    print bl, bnbc
    


def main2(page):
    soup = BeautifulSoup(page)
    tag_jspan = soup.find_all("div", attrs={"class":"jspPane"})
   
    for l in  tag_jspan:
        tag_brands = l.find_all("a", attrs={"data-key":"brands"})

	if tag_brands:
	     map(bnbcbl, tag_brands)



def main(link):
    #page = req_proxy.main(link)
    #page = urllib2_proxy.main(link)
    #page = page.read()
    page = phan_proxy.main(link)

    if not page:
        main(link)

    main2(page)
    
    

    
    
if __name__=="__main__":
    link = "http://www.myntra.com/women-watches?nav_id=1004&src=tn"
    main(link)
    
    
