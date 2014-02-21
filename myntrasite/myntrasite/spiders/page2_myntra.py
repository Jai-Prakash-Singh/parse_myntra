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
def worker():
    print threading.currentThread().getName(), 'Starting'
    time.sleep(2)
    print threading.currentThread().getName(), 'Exiting'


 
def main3(ntl_pth_cat):
    
    page2_clb_myntra.main(ntl_pth_cat)
         



def main2(list_ntl_pth_cat2):
    for ntl_pth_cat in list_ntl_pth_cat2:
        t = threading.Thread(target=main3,  args = (ntl_pth_cat,))
        t.start()
        time.sleep(1)
    
    w = threading.Thread(name='worker', target=worker)
    w.start()
    w.join()

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
