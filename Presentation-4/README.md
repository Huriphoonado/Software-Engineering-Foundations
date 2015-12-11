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

print "Sequential: %d" % (sequentialEnd - sequentialStart)
print "Concurrent: %d" % (concurrentEnd - concurrentStart)
```

The above code simply counts down to 0 from 100000000 first sequentially and second by two threads started at nearly the same instant. You may think that the two concurrent threads would run faster, or if the GIL is limiting their ability to execute code at the same time, maybe they would take just as long or slightly longer. However, on my machine, the concurrent program takes 33% longer to run than the sequential program:

```
$ python threadPerformance.py
Sequential: 7.768601
Concurrent: 11.758414
```

Beazly did a real-time trace of all GIL acquisitions, releases, conflicts, retries, etc. and argues that this unexpected, major performance dip is the result of Python not having a thread scheduler and leaving that responsibility to the host operating system. There is so much overhead in GIL Thread Signaling that Beazly finds that the sequential program uses 117 Mach System Calls, the concurrent program run on a single core uses about 3.3 Million Mach System Calls and the concurrent program run on two cores uses about 9.5 Million Mach System calls. Beazly concludes that the Python GIL implementation hasn't really changed in over a decade and that it is worth exploring since there is a major performance penalty on using multiple threads especially on multiple cores.

#### Concurrency Libraries

As a result of the Global Intepreter Lock, The Python Standard Library offers a few APIs (supported by different versions of Python) for concurrency: threading, multiprocessing, and concurrent.futures. 

#### Further Reading

* [Nathan Grigg, an engineer at Google, has written a very good, brief discussion of the differences between Python Multithreading and Multiprocessing.](http://nathangrigg.net/2015/04/python-threading-vs-processes/)
* [Jesse Noller, a former chair of PyCon, (among other things), has written a much more in-depth article about Python Threads and the Global Intepreter Lock.](http://jessenoller.com/blog/2009/02/01/python-threads-and-the-global-interpreter-lock) The article also does a good job introducing Python concurrency constructs to Java programmers. (I will continue to reference this paper throughout my overview.)

## Threading

The [Python threading module](https://docs.python.org/2/library/threading.html#module-threading) is a higher-level interface built on top of the lower-level [thread module](https://docs.python.org/2/library/thread.html#module-thread) that has been supported since Python 1.5.2. As was described above, threads in Python are limited by the GIL and are not capable of the same parallelism possible in other languages. However, the GIL is released when doing I/O so threads can still be appropriate for creating responsive applications. 

Python threads have the following properties.

* All threads are within one process and thus share the same memory space and can acess all of the same objects.
* Threads are lightweight meaning they can be spawned quickly.
* Threads should not be abruptly interrupted or killed. (Doing so can cause memory leak or deadlock.)
* Threads can only be run on one core.

A Hello World application for the Python threading module may look something like this:

```
from threading import Thread

def hello():
	print "hello"

def world():
	print "world"

myThread1 = Thread(target=hello)
myThread2 = Thread(target=world)

myThread1.start()
myThread2.start()

myThread1.join()
myThread2.join()
```

* Threads are created by passing a callable object to the constructor, e.g. ```myThread1 = Thread(target=hello)```. The thread constructor may take in a number of arguments including target function to run via a separate thread of control, and a list of the function's arguments.
  * A subclass can also inherit the Thread Object. In this event, only the ```__init__()``` and ```run()``` functions should be overwritten.
  * Threads can be specified as Daemon (```myThread.setDaemon(True)```) or non-Daemon controlling whether they are abruptly stopped at shutdown.
* The ```start()``` method is called only once per thread invoking the thread's ```run()``` method.
* The ```join()``` method blocks the calling thread until the thread whose ```join()``` method is invoked terminates.

Since threads inhabit a shared memory space, the threading module does not protect against many of the concurrency-related problems covered in class. It does however provide some support with similar constructs as other languages to guard against simultaneous access to an object or variable.

#### Race Conditions

Q: Why did the multithreaded chicken cross the road?

A: to To other side. get the

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

#### Locks, Re-entrant Locks, and Condition Objects

[Locks](https://docs.python.org/2/library/threading.html#lock-objects) are the lowest level synchronization primitives available in Python.
* Instantiate a lock with the ```Lock()``` constructor.
* ```Lock.acquire()``` blocks until the lock is unlocked causing it the set the lock to locked and returning True. (```Lock.acquire(False)``` does not block and returns False immediately.)
* ```Lock.release()``` unlocks a lock allowing one of any other blocked threads to aquire it.

[A re-entrant lock](https://docs.python.org/2/library/threading.html#rlock-objects) is similar to a lock, but allows a single thread to aquire it multiple times. Essentially, nested pairs of ```acquire()``` and ```release()``` can exist on multiple levels of recursion, and other threads can only aquire a re-entrant lock once the final ```release()``` has been called. Re-entrant locks (constructed with ```RLock()```) are useful in cases where multiple points of code run in a single thread need to be synchronized.

[Condition Objects](https://docs.python.org/2/library/threading.html#condition-objects) use locks to synchronize threads enabling some threads to set a condition and threads to to wait for that condition before continuing. [An reduced example of the classic Producer-Consumer problem using Condition Objects was taken from a bogotobogo tutorial.](http://www.bogotobogo.com/python/Multithread/python_multithreading_Synchronization_Condition_Objects_Producer_Consumer.php)

```
import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

def consumer(cv):
    logging.debug('Consumer thread started ...')
    with cv:
    	logging.debug('Consumer waiting ...')
        cv.wait()
        logging.debug('Consumer consumed the resource')

def producer(cv):
    logging.debug('Producer thread started ...')
    with cv:
        logging.debug('Making resource available')
        logging.debug('Notifying to all consumers')
        cv.notifyAll()

if __name__ == '__main__':
    condition = threading.Condition()
    cs1 = threading.Thread(name='consumer1', target=consumer, args=(condition,))
    cs2 = threading.Thread(name='consumer2', target=consumer, args=(condition,))
    pd = threading.Thread(name='producer', target=producer, args=(condition,))

    cs1.start()
    time.sleep(2)
    cs2.start()
    time.sleep(2)
    pd.start()
```

The above example uses two consumers and one producer and makes use of the ```notifyAll()``` and ```wait()``` methods.
* More documentation

## Multiprocessing

The Python [multiprocessing library](https://docs.python.org/2/library/multiprocessing.html) is a newer approach to concurrency that has been supported since Python 2.6 and addresses many of the limitations of the threading module. Most importantly, processes work outside of the GIL and can make programs truly parallel through running on multiple CPUs.

A quick addition to the performance code from earlier with processes shows the best yet performance, and checking the activity monitor showed greater than 100% CPU usage.

```
parallelStart = timeit.default_timer()
myProcess1 = Process(target=count, args=(100000000,))
myProcess1.start()

myProcess2 = Process(target=count, args=(100000000,))
myProcess2.start()

myProcess1.join()
myProcess2.join()
parallelEnd = timeit.default_timer()
```

```
$ python examples/threadPerformance.py
Sequential: 8.185330
Concurrent: 11.407094
Parallel: 4.117114

```

Python processes have the following functionality:

* Processes do not share memory meaning some sort of communication may be necessary for processes to divide and conquer a job in parallel.
* Processes have a bit more overhead than threads and take more time to spawn.
* Child processes can be interrupted/killed.
* Processes can take advantage of multiple cores.

A Hello World application for the Python multiprocessing module looks almost identical to the threading module.

'''
from multiprocessing import Process

def hello():
	print "hello"

def world():
	print "world"

if __name__ == '__main__':
	myProcess1 = Process(target=hello)
	myProcess2 = Process(target=world)

	myProcess1.start()
	myProcess2.start()

	myProcess1.join()
	myProcess2.join()
'''

We import the Process class from multiprocessing, create functions that the processes will run, tell the processes to run with ```start()```, and make sure the program ends as the processes terminate with ```join()```.

#### Communication

Processes do share the same synchronization primitives as the threading module, and certain objects enable them to share memory, but as was covered in class it is usually best to avoid shared states. [The multiprocessing library contains a couple primitives for sending messages between processes, pipes and queues.](https://docs.python.org/2/library/multiprocessing.html#exchanging-objects-between-processes)

The ```Pipe()``` function enables two-way communication between processes providing an input into the pipe and an output. Pipes are useful when only two points need to communicate as [ultimately pipes are more efficient than queues.](http://stackoverflow.com/questions/8463008/python-multiprocessing-pipe-vs-queue) (There is the possibility of data corruption if two or more processes are accessing the same end of a pipe at once, though there is no risk is both ends of the pipe are being used simultaneously.)

```
from multiprocessing import Process, Pipe

def life(pEntry):
    pEntry.send(42)
    pEntry.close()

if __name__ == '__main__':
    pEntry, pExit = Pipe()
    p = Process(target=life, args=(pEntry,))
    p.start()
    print pExit.recv()
    p.join()
```

* The ```Pipe()``` object returns a pair of connection objects referring to the ends of a pipe.
* ```send()``` sends a discrete message, either a Python object (pickled) or a buffer.
* ```recv()``` blocks until an object has been sent and returns that object.

Queues are implemented on top of pipes, allow for multiple producers and consumers, and are identical to the standard ```Queue.Queue``` object with ```put()``` and ```get()``` functions. I've written a Producer-Consumer solution using the [JoinableQueue](https://docs.python.org/2/library/multiprocessing.html#multiprocessing.JoinableQueue) which includes a ```task_done()``` function indicating an enqueued task has been completed and a ```join()``` function that blocks until all enqueued items have been processed. JoinableQueues return an error if ```task_done()``` has been called more times than items were put in the queue.

```
from multiprocessing import Process, JoinableQueue
import time

class Consumer(Process):
	def __init__(self, id, q):
		Process.__init__(self)
		self.q = q
		self.id = id

	def run(self):
		while True:
			task = self.q.get()
			if task is None: # Recieved Poison Pill
				print "Consumer %i has finished." % self.id
				self.q.task_done()
				break
			print "Consumer %i consumed Task %i" % (self.id, task)
			self.q.task_done()
		return

class Producer(Process):
	def __init__(self, id, q, numTasks, qSize):
		Process.__init__(self)
		self.q = q
		self.numTasks = numTasks
		self.qSize = qSize
		self.id = id

	def run(self):
		for i in range(self.numTasks):
			self.q.put(i)
			print "Producer %i produced Task %i" % (self.id, i)
		self.q.put(None) # Poison Pill
		print ("Producer %i produced Poison Pill") % self.id
		return

def main():
	numProcesses = 4
	numTasks = 10
	qSize = 20
	q = JoinableQueue(qSize)
	producers = []
	consumers = []

	for i in range(numProcesses):
		producers.append(Producer(i, q, numTasks, qSize))
		producers[i].start()

	for i in range(numProcesses):
		consumers.append(Consumer(i, q))
		consumers[i].start()

	q.join()

if __name__ == '__main__':
	main()
```

#### Other Features

The multiprocessing module has many other features including the following:

* [Synchronization primitives](https://docs.python.org/2/library/multiprocessing.html#synchronization-between-processes) such as locks, events, and barriers with language taken right from the threading API. Synchronization is useful when outputting text for example to make sure it is printed in correct order.
* [Sharing state between processes with shared memory maps such as Values and Arrays, and via shared namespaces created by the manager object.](https://docs.python.org/2/library/multiprocessing.html#synchronization-between-processes)

Particularly cool I think are [Process Pools](https://docs.python.org/2/library/multiprocessing.html#module-multiprocessing.pool), a high-level interface for offloading tasks to a pool of workers. Process pools have the ```map()``` method which takes in a list of values and splits it apart into chunks of tasks (whose size can be specified) for workers to complete. Since this method blocks, there is also ```map_async()``` which can specify a callback function which is applied once a result is available from the ```map_async()``` function.

The following example takes in a list of values and applies a function ```double()``` to them in parallel.

```
from multiprocessing import Pool

def double(x):
    return x*2

if __name__ == '__main__':
    pool = Pool(processes=4)
    pool.map(double, range(1000))
```

#### Further Reading

* [The Python reference manual provides a guide to best practices with Processes.](https://docs.python.org/2/library/multiprocessing.html#multiprocessing-programming)
* [The Python Module of the Week Guide, provides a very comprehensive overview on Communication between Processes.](https://pymotw.com/2/multiprocessing/communication.html#)
* [David Beazly also includes a long lesson (over 150 slides) on threading and multiprocessing.](http://www.dabeaz.com/usenix2009/concurrent/Concurrent.pdf)

## 
