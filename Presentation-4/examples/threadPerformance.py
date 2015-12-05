from threading import Thread
import time

def count(n):
	while n > 0:
		n = n - 1

sequentialStart = time.clock()
count(100000000)
count(100000000)
sequentialEnd = time.clock()

concurrentStart = time.clock()
myThread1 = Thread(target=count, args=(100000000,))
myThread1.start()

myThread2 = Thread(target=count, args=(100000000,))
myThread2.start()

myThread1.join()
myThread2.join()
concurrentEnd = time.clock()

print "Sequential: %d" % (sequentialEnd - sequentialStart)
print "Concurrent: %d" % (concurrentEnd - concurrentStart)
