from Queue import Queue
from threading import Thread
import time
import logging
import sys

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
		                        )

num_fetch_threads = 100
enclosure_queue = Queue()



def main2(i, q):
    while True:
        line = q.get()
	logging.debug((line))
        time.sleep(2)
	q.task_done()



def main():
    f = open("to_extract.txt")
    directory = f.read().strip()
    f.close()

    filename = "%s/%s" %(directory, "cl_cpth_sc_bl_bn_bc.txt")
   
    f = open(filename)

    for i in range(num_fetch_threads):
        worker = Thread(target = main2, args=(i, enclosure_queue,))
	worker.setDaemon(True)
	worker.start()

    for line in f:
        enclosure_queue.put((line))

    print '*** Main thread waiting'
    enclosure_queue.join()
    print '*** Done'



if __name__=="__main__":
    main()
