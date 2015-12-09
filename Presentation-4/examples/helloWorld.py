'''
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
'''

from multiprocessing import Process

def hello():
	print "hello"

def world():
	print "world"

myProcess1 = Process(target=hello)
myProcess2 = Process(target=world)

myProcess1.start()
myProcess2.start()

myProcess1.join()
myProcess2.join()