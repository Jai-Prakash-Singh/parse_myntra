import page1_myntra
import multiprocessing
import req_proxy
import logging
import time
import threading

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
		                        )


def main3(ntl_pth_cat):
    link1 = ntl_pth_cat[0]
    page = req_proxy.main(link1)     
         
    if not page:
        f = open("page2_to_extract.txt", "a+")
	print >>f, link1
        f.close()
	 
    else:
        print link1



def main2(list_ntl_pth_cat):
    for ntl_pth_cat in list_ntl_pth_cat:
        t = threading.Thread(target=main3,  args = (ntl_pth_cat,))
        t.start()
        time.sleep(1)



def main():
    list_ntl_pth_cat = page1_myntra.main()
    
    length = len(list_ntl_pth_cat)
    
    for val in xrange(40, length, 40):
        p = multiprocessing.Process(target=main2, args = ( list_ntl_pth_cat[:val], ))
	p.start()
	p.join()
        list_ntl_pth_cat = list_ntl_pth_cat[val : ]


    if val < length:
        p = multiprocessing.Process(target=main2, args = ( list_ntl_pth_cat, ))
	p.start()
	p.join()


            	    
 

if __name__=="__main__":
    main()


