import page1_myntra
import multiprocessing
import req_proxy
import logging
import time
import threading
import phan_proxy
import sys
import page2_clb_myntra

# page1_myntra.py  page2_myntra.main() page2_clb_myntra.py

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
		                        )


def main3(ntl_pth_cat):
    link1 = ntl_pth_cat[0]
    page = req_proxy.main(link1)     
         
    if not page:
        f = open("page2_extract_no.txt", "a+")
	print >>f, link1
        f.close()
	 
    else:
       f = open("page2_extracted_yes.txt", "a+")
       print >>f, link1
       f.close()




def main2(list_ntl_pth_cat2):
    for ntl_pth_cat in list_ntl_pth_cat2:
        t = threading.Thread(target=main3,  args = (ntl_pth_cat,))
        t.start()
        time.sleep(1)



def main():
    list_ntl_pth_cat = page1_myntra.main()
   
    length = len(list_ntl_pth_cat)

    mod  = -(length % 50)
     
    #print mod, len(list_ntl_pth_cat[mod:])

    if mod:
        p = multiprocessing.Process(target=main2, args = ( list_ntl_pth_cat[mod:], ))
        p.start()
        p.join()

    val2 = 50

    for val in xrange(50, length, 50):
        p = multiprocessing.Process(target=main2, args = ( list_ntl_pth_cat[:val2], ))
    	p.start()
        list_ntl_pth_cat = list_ntl_pth_cat[val2 : ]
     	p.join()
        #print val, len(list_ntl_pth_cat)

       
    print "Finished everything...."
    print "num active children:",multiprocessing.active_children()
            	    
 

if __name__=="__main__":
    main()
