from bs4 import BeautifulSoup
import req_proxy
import phan_proxy
import urllib2_proxy
import logging
import time




# page1_myntra.py  page2_myntra.main() page2_clb_myntra.py

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

dte = time.strftime("%d%m%Y")



def main3(ntl_pth_cat, a):
    bnbc = a.find("span", attrs={"class":["mk-filter-display"]})
    bnbc = str(bnbc.get_text()).replace("\n", " ").replace("\t", " ").replace("\r", " ").strip()
    #bl = "http://www.myntra.com%s" %(a.get("href"))
    br = bnbc.split("[")[0].strip()
    bl = "%s#!brands=%s" %(ntl_pth_cat[0], br)

    #print [ntl_pth_cat[0], ntl_pth_cat[1], ntl_pth_cat[2], bl, bnbc]
    filename = "dir%s/%s" %(time.strftime("%d%m%Y"), "cl_cpth_sc_bl_bn_bc.txt")
 
    f = open(filename, "a+")
    print >>f, ','.join([ntl_pth_cat[0], ntl_pth_cat[1], ntl_pth_cat[2], bl, bnbc])
    f.close()

    logging.debug([ntl_pth_cat[0], ntl_pth_cat[1], ntl_pth_cat[2], bl, bnbc])
    


def main2(ntl_pth_cat, page):
    soup = BeautifulSoup(page)
    tag_a = soup.find_all("a", attrs={"data-key":"brands"})
     
    if tag_a: 
        for a in tag_a:
            main3(ntl_pth_cat, a)



def main(ntl_pth_cat):
    link = ntl_pth_cat[0]
    page = req_proxy.main(link)

    #page = phan_proxy.main(link)

    if not page:
        main(ntl_pth_cat)
    
    filename = "dir%s/%s" %(time.strftime("%d%m%Y"), "cl_cpth_sc_bl_bn_bc_links_extracted.txt")
     
    #filename = "dir23022014/cl_cpth_sc_bl_bn_bc_links_extracted.txt"  
    f = open(filename, "a+")
    print >>f, link
    f.close()

    main2(ntl_pth_cat, page)
    
    

if __name__=="__main__":
    ntl_pth_cat = ('http://www.myntra.com/shopping-offer7?nav_id=1092&src=tn', '/shopping-offer7', u'Footwear under Rs. 999')
    main(ntl_pth_cat)
    
    
