from threading import Thread
from multiprocessing import Process
import timeit

def count(n):
	while n > 0:
		n = n - 1

sequentialStart = timeit.default_timer()
count(100000000)
count(100000000)
sequentialEnd = timeit.default_timer()

concurrentStart = timeit.default_timer()
myThread1 = Thread(target=count, args=(100000000,))
myThread1.start()

myThread2 = Thread(target=count, args=(100000000,))
myThread2.start()

myThread1.join()
myThread2.join()
concurrentEnd = timeit.default_timer()

parallelStart = timeit.default_timer()
myProcess1 = Process(target=count, args=(100000000,))
myProcess1.start()

myProcess2 = Process(target=count, args=(100000000,))
myProcess2.start()

myProcess1.join()
myProcess2.join()
parallelEnd = timeit.default_timer()

print "Sequential: %f" % (sequentialEnd - sequentialStart)
print "Concurrent: %f" % (concurrentEnd - concurrentStart)
print "Parallel: %f" % (parallelEnd - parallelStart)
