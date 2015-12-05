# Concurrency in Python

In class we covered concurrency in a variety of languages including Java, Clojure, and Elixir. Python happens to be my language of choice, but I have only limited experience writing concurrent or parallel programs in Python. This overview will be very useful for me.

#### Overview of Global Interpreter Lock

Python's implementation of concurrency is somewhat unique. In Java and many other programming languages, threads are used for parallel processing. However, in CPython (the most popular implementation of Python), a mechanism called the [Global Interpreter Lock](https://docs.python.org/2/glossary.html#term-global-interpreter-lock) prevents multiple threads from executing a line of Python bytecode (compiled source code) at once. This in effect prevents true parallelism since multiple processors cannot run multiple, simultaneous threads.

The Global Interpreter Lock has some advantages. It helps keep garbage collection since one thread cannot decrement an object's reference count to 0 (tracking counter of references to an object) while another thread is using it, it theoretically increases the speed of single threaded programs since separate objects need not acquire and release locks, and it makes life easier for C programmers working on Python: As it happens, use of the Global Intepreter Lock yields a simpler, clearer implementation of the Python Interpreter so it is easier to maintain and write extensions (and otherwise unsafe, existing C libraries are easier to integrate). 

The Global Interpreter also has downsides. [One well-known example by David Beazly shows that the GIL impedes performance.](http://www.dabeaz.com/python/GIL.pdf) I've adapted his code below:

```
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
```

On my machine, the sequential program runs more than twice as fast as the concurrent program:

```
$ python threadPerformance.py
Sequential: 7
Concurrent: 17
```

Beazly did a real-time trace of all GIL acquisitions, releases, conflicts, retries, etc. and argues that this unexpected, major performance dip is the result of Python not having a thread scheduler and leaving that responsibility to the host operating system. There is so much overhead in GIL Thread Signaling that Beazly finds that the sequential program uses 117 Mach System Calls, the concurrent program run on a single core uses about 3.3 Million Mach System Calls and the concurrent program run on two cores uses about 9.5 Million Mach System calls. Beazly concludes that the Python GIL implementation hasn't really changed in over a decade and that it is worth exploring since there is a major performance penalty on using multiple threads especially on multiple cores.

#### Concurrency Libraries

As a result of the Global Intepreter Lock, The Python Standard Library offers a few APIs (supported by different versions of Python) for concurrency: threading, multiprocessing, and concurrent.futures.

#### Further Reading

* [Nathan Grigg, an engineer at Google, has written a very good, brief discussion of the differences between Python Multithreading and Multiprocessing.](http://nathangrigg.net/2015/04/python-threading-vs-processes/)
* [Jesse Noller, a former chair of PyCon, (among other things), has written a much more in-depth article about Python Threads and the Global Intepreter Lock.](http://jessenoller.com/blog/2009/02/01/python-threads-and-the-global-interpreter-lock) I will continue to reference this paper throughout my overview.

## Threading

Concurrent programs are still possible and threads are useful.

#### Race Conditions

The following code example shows a race condition with the threading API. Ten threads increment a single global variable ```count``` 100 times. Even though the GIL prevents multiple threads from accessing a single line of bytecode at once, incrementing a variable requires multiple lines of bytecode (reading, incrementing, and writing), so it is still entirely possible for threads to step over eachother.

```
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
```

When you run this, ```count``` should total 1000. This happens most of the time, but not always.

```
$ python counter.py
959
$ python counter.py
1000
$ python counter.py
1000
$ python counter.py
974
```

Luckily, with this simple example, the solution is pretty easy. Simply add a lock around the section that is incrementing the counter to make sure the process is atomic.

```
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
```

[A more complicated example of race conditions can be found in Jesse Noller's article](http://jessenoller.com/blog/2009/02/01/python-threads-and-the-global-interpreter-lock) showing that multiple threads moving random amounts of money between accounts in a bank with a fixed total balance can end up changing that balance.

## Multiprocessing

## 
