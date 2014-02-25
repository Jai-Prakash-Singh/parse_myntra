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

num_fetch_threads = 50
#enclosure_queue = Queue()
enclosure_queue = multiprocessing.JoinableQueue()



def main2(i, q):
    #while True:
    for line in iter(q.get, None):
        line = q.get()
	logging.debug((line))
        try:
            page2_sub_scroller.main(line)
        except:
            pass

        time.sleep(2)
	q.task_done()

    q.task_done()


def main():
    f = open("to_extract.txt")
    directory = f.read().strip()
    f.close()

    filename = "%s/%s" %(directory, "cl_cpth_sc_bl_bn_bc.txt")
   
    f = open(filename)
    
    procs = []

    for i in range(num_fetch_threads):
        procs.append(Process(target = main2, args=(i, enclosure_queue,)))
	#worker.setDaemon(True)
	procs[-1].start()

    for line in f:
        enclosure_queue.put((line))

    print '*** Main thread waiting'
    enclosure_queue.join()
    print '*** Done'

    for p in procs:
        enclosure_queue.put( None )

    enclosure_queue.join()

    for p in procs:
        p.join()
 
    



if __name__=="__main__":
    main()
