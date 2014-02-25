import subprocess
import multiprocessing
import logging
from scrapy import cmdline

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
		                        )

#page3_scrapy_myntra.py , page3_filedivision_myntra.py 

num_fetch_threads = 2
enclosure_queue = multiprocessing.JoinableQueue()



def main3(pth):
    #print pth
     cmdline.execute(['scrapy',  'runspider',  'page3_scrapy_myntra.py',  '-a',  'pth=%s' %(pth)])


def main2(output):
    i = 0
    for pth in output:
        i = i+1
        p = multiprocessing.Process(name = i, target=main3, args=(pth,))
        logging.debug((multiprocessing.current_process().name, 'Starting'))
	p.start()



def main():
    f = open("to_extract.txt")
    directory = f.read().strip()
    f.close()
 
    output = subprocess.check_output(["find",  directory,  "-name",  "*.docx"])
    output = output.strip().split("\n")
     
    #print  output

    length = len(output)
    
    val = length / 100

    mod = length % 100

    i = 0 
    for l in xrange(100, length, 100):
        l2 = l-100
	i = i+1
	p = multiprocessing.Process(name = i, target=main2, args=(output[l2: l],))
	p.start()
        logging.debug('Starting')
	p.join()
        #main2(output[l2: l])

    p = multiprocessing.Process(name = "mod", target=main2, args=(output[mod: ], ))
    p.start()
    logging.debug('Starting')
    p.join()
    #main2(output[mod: ])
     
    
    print "Finished everything...."
    print "num active children:", multiprocessing.active_children()

    
    



if __name__=="__main__":
    main()
