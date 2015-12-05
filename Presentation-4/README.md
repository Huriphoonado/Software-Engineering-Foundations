# Concurrency in Python

In class we covered concurrency in a variety of languages including Java, Clojure, and Elixir. Python happens to be my language of choice, but I have only limited experience writing concurrent or parallel programs in Python. This overview will be very useful for me.

Python's implementation of concurrency is somewhat unique. In Java and many other programming languages, threads are used for parallel processing. However, in CPython (the most popular implementation of Python), a mechanism called the [Global Interpreter Lock](https://docs.python.org/2/glossary.html#term-global-interpreter-lock) prevents multiple threads from executing a line of Python bytecode (compiled source code) at once. This in effect prevents true parallelism since multiple processors cannot run multiple, simultaneous threads.

The Global Interpreter Lock has some advantages. It helps keep garbage collection since one thread cannot decrement an object's reference count to 0 (tracking counter of references to an object) while another thread is using it, it theoretically increases the speed of single threaded programs since separate objects need not acquire and release locks, and it makes life easier for C programmers working on Python: As it happens, use of the Global Intepreter Lock yields a simpler, clearer implementation of the Python Interpreter so it is easier to maintain and write extensions (and otherwise unsafe, existing C libraries are easier to integrate). 

The Global Interpreter also has downsides. One well-known example by David Beazly shows that the GIL impedes performance. It is also worth

As a result of the Global Intepreter Lock, The Python Standard Library offers a few APIs (supported by different versions of Python) for concurrency: threading, multiprocessing, and concurrent.futures.

#### Further Reading

* [Nathan Grigg, an engineer at Google, has written a very good, brief discussion of the differences between Python Multithreading and Multiprocessing.](http://nathangrigg.net/2015/04/python-threading-vs-processes/)
* 

## Threading

Concurrent programs are still possible and threads are useful.

This example shows a race condition with threading.

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

## Multiprocessing

## 
