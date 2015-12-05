'''
# Broken
from threading import Thread

count = 0
numThreads = 10
threads = []

class counterThread(Thread):
	def __init__(self):
		Thread.__init__(self)
	def run(self):
		global count
		for i in range(100):
			count = count + 1

for i in range(numThreads):
	threads.append(counterThread())
	threads[i].start()
for i in range(numThreads):
	threads[i].join()

print count
'''

# Fixed
from threading import Thread, Lock

count = 0
numThreads = 10
threads = []
lock = Lock()

class counterThread(Thread):
	def __init__(self):
		Thread.__init__(self)
	def run(self):
		global count
		for i in range(100):
			lock.acquire()
			try:
				count = count + 1
			finally:
				lock.release()

for i in range(numThreads):
	threads.append(counterThread())
	threads[i].start()
for i in range(numThreads):
	threads[i].join()

print count