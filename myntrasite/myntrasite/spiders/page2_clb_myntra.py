from bs4 import BeautifulSoup
import req_proxy
import phan_proxy

def main2(page):
    soup = BeautifulSoup(page)
    tag_jspan = soup.find_all("div", attrs={"class":"jspPane"})
    print tag_jspan 



def main(link):
    #page = req_proxy.main(link)
    page = phan_proxy.main(link)
    main2(page)

    
if __name__=="__main__":
    link = "http://www.myntra.com/women-watches?nav_id=1004&src=tn"
    main(link)
    
    
