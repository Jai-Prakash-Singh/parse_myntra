import page1_myntra
import multiprocessing
import req_proxy
import logging
import time
import threading
import phan_proxy
import sys
import page2_clb_myntra
from Queue import Queue
from threading import Thread
import time


# page1_myntra.py  page2_myntra.main() page2_clb_myntra.py

logging.basicConfig(level=logging.DEBUG,
                     format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                                         )

num_fetch_threads = 20
enclosure_queue = Queue()



def main2(i, q):
    while True:
        ntl_pth_cat = q.get()
        page2_clb_myntra.main(ntl_pth_cat)
        time.sleep(i + 2)
        q.task_done()
    


def main():
    list_ntl_pth_cat = page1_myntra.main()
   
    length = len(list_ntl_pth_cat)

    for i in range(num_fetch_threads):
        worker = Thread(target=main2, args=(i, enclosure_queue,))
        worker.setDaemon(True)
        worker.start()

    for ntl_pth_cat in list_ntl_pth_cat:
        enclosure_queue.put(ntl_pth_cat) 
         
    print '*** Main thread waiting'
    enclosure_queue.join()
    print '*** Done'
    


if __name__=="__main__":
    main()
