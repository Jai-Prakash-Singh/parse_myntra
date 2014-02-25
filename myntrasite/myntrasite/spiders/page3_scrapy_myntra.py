# -*- coding: latin-1 -*-
# -*- coding: iso-8859-15 -*-
# -*- coding: ascii -*-
# -*- coding: utf-8 -*-

from scrapy.spider import Spider
from scrapy.selector import Selector
from bs4 import BeautifulSoup
import time

#page3_scrapy_myntra.py , page3_filedivision_myntra.py 

class DmozSpider(Spider):
    name = "link_to_link"
    allowed_domains = ["myntra.com"]
 
    def __init__(self, pth = None):
       
        self.pth = pth        
        self.pth2 = pth2 = pth.strip().split("/")
        self.target = str(pth2[1]).strip()
	self.category = str(pth2[2]).strip()
	self.subcat = str(pth2[3]).strip()
	self.brand =  str(pth2[4]).strip()

        f = open(pth)
	self.start_urls = f.read().strip().split("\n")
	f.close()
    

    def parse(self, response):
        #sel = Selector(response)
        #title = sel.xpath("/html/body/div/div[2]/section/div[2]/div/div/div[2]/div/div/h1/text()").extract()
        #title = 
        try:
            link = response.url

            page = response.body 

	    soup = BeautifulSoup(page)

	    title = soup.find("h1", attrs={"itemprop":"name"})
	    title = str(title.get_text()).replace("\n", " ").replace("\t", " "). replace("\r", " ").strip()
        
	    sp = soup.find("meta", attrs={"itemprop":"price"})
	    sp = "Rs. %s" %(str(sp.get("content")).replace("\n", '').replace("\t", '').replace("\r", '').replace(" ", "").strip())

	    mrp = soup.find("span", attrs={"class":"strike gray"})
	
	    if mrp:
	        mrp = "Rs. %s" %(str(mrp.get_text()).replace("\n", '').replace("\t", '').replace("\r", '').replace(" ", "").strip())
	    else:
	        mrp = str(mrp).strip()

	    size = soup.find("div", attrs={"class":"options"})
        
            buttons_list = []

            if size:
	        buttons  = size.find_all("button")
            
                for l in buttons:
	            buttons_list.append(str(l.get_text().strip()))

                buttons = str(buttons_list)
            else:
                buttons = "single size"


            vender = soup.find("div", attrs={"id":"vendorDetails"})
            vender = str(vender.get_text()).strip()

	    spec = soup.find("ul", attrs={"class":"mk-pdpv1-product-helper mk-cf"})
	    spec = str(spec).replace("\n", "").replace("\r", "").replace("\t", "").strip()

            image = soup.find("a", attrs={"id":"zoom1"})
            image = str(image.get("href")).strip()


            sku = "None"
	 
      
	    target = self.target
	    category = self.category 
	    subcat  = self.subcat 
 	    brand   = self.brand 
            colour = "None"
            metatitle = "None"
            metadisc = "None"
            desc = "None"
         
            date = str(time.strftime("%d:%m:%Y"))
            status = "None"

            directory = '/'.join(self.pth2[:-1])

            filename = "%s/%s%s" %(directory , self.pth2[-1][:-5],  ".doc")
            f = open(filename, "a+")
	    print >>f, [sku, title, link, sp, category, subcat, brand, image, mrp, 
	                colour, target, link, vender, metatitle, metadisc, buttons, 
		        desc, spec, date, status]
            f.close()

            print[link, "ok"]


        except:
            self.start_urls.append(link)

        
