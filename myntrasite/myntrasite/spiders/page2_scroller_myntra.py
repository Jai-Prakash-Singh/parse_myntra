from Queue import Queue
from threading import Thread
import time
import logging
import sys
import page2_sub_scroller
from multiprocessing import Process
import multiprocessing

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
		                        )
# page2_scroller_myntra.py, page2_sub_scroller.py




def main3(line):
    try:
        page2_sub_scroller.main(line)

    except:
        pass




def main2(enclosure_queue2):
    
    i= 0 

    for line in enclosure_queue2:
        i = i+1
        p = multiprocessing.Process(name = i, target=main3, args=(line,))
        logging.debug((multiprocessing.current_process(), "started"))
        p.start()
      
        time.sleep(2)  

    del enclosure_queue2[:]



def main():
    f = open("to_extract.txt")
    directory = f.read().strip()
    f.close()

    filename = "%s/%s" %(directory, "cl_cpth_sc_bl_bn_bc.txt")

    f = open(filename)

    enclosure_queue = []

    for line in f:
        enclosure_queue.append(line)

        if len(enclosure_queue) > 100:
            main2(enclosure_queue[:])
            del enclosure_queue[:]
            
    main2(enclosure_queue[:])
    del enclosure_queue[:]     
 
    print "Finished everything...."
    print "num active children:", multiprocessing.active_children()


if __name__=="__main__":
    main()
