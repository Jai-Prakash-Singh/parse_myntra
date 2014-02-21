from selenium import webdriver
import logging
from  random  import choice

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
		                        )



def main(line):
    line = line.split(",")
    bl = line[-2]
    #print bl
    
    #f2 = open("/home/desktop/mygoodproxy3.txt")
    f2 = open("/home/user/Desktop/mygoodproxy2.txt")
    proxy_list = f2.read().strip().split("\n")
    f2.close()

    loop = True

    while loop is True:
        try:
            ip_port = choice(proxy_list).strip()
            
            user_pass = ip_port.split("@")[0].strip()
            prox = "--proxy=%s"%ip_port.split("@")[1].strip()
            service_args = [prox, '--proxy-auth='+user_pass, '--proxy-type=http', '--load-images=no']
            driver = webdriver.PhantomJS(service_args = service_args)

            driver.get(bl)

            if str(driver.current_url).strip() == "about:blank":
                continue

            else:
                loop = False
        
        except:
            pass
   
    #page = driver.page_source
    #print page

   >>> driver = webdriver.PhantomJS()
>>> driver.get(link)
>>> driver.execute_script("return $(document ).height();")
3194
>>> driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
>>> driver.execute_script("return $(document ).height();")
5136
>>> driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
>>> driver.execute_script("return $(document ).height();")
7116
>>> driver.execute_script("return $(document ).height();")
7116
>>> driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
>>> driver.execute_script("return $(document ).height();")
7116
>>> driver.execute_script("window.scrollBy(0,-450)", "")
>>> driver.find_element_by_xpath("/html/body/div/div[2]/section/div[3]/div[2]/div/div[6]/a").click()
>>> driver.execute_script("return $(document ).height();")
9096
>>> driver.find_element_by_xpath("/html/body/div/div[2]/section/div[3]/div[2]/div/div[6]/a").click()
>>> driver.execute_script("return $(document ).height();")
11076
>>> driver.find_element_by_xpath("/html/body/div/div[2]/section/div[3]/div[2]/div/div[6]/a").click()
>>> driver.execute_script("return $(document ).height();")
13056
>>> driver.find_element_by_xpath("/html/body/div/div[2]/section/div[3]/div[2]/div/div[6]/a").click()
>>> driver.execute_script("return $(document ).height();")
15036
>>> driver.find_element_by_xpath("/html/body/div/div[2]/section/div[3]/div[2]/div/div[6]/a").click()
>>> driver.execute_script("return $(document ).height();")
17016
>>> driver.find_element_by_xpath("/html/body/div/div[2]/section/div[3]/div[2]/div/div[6]/a").click()
>>> driver.execute_script("return $(document ).height();")
18996
>>> driver.find_element_by_xpath("/html/body/div/div[2]/section/div[3]/div[2]/div/div[6]/a").click()
>>> driver.execute_script("return $(document ).height();")
20976
>>> driver.find_element_by_xpath("/html/body/div/div[2]/section/div[3]/div[2]/div/div[6]/a").click()
#






if __name__=="__main__":
    line = "http://www.myntra.com/sale-women-accessories?nav_id=633&src=tn,/sale-women-accessories,Accessories,http://www.myntra.com/yelloe?src=lnb,yelloe [9]"
    main(line)
