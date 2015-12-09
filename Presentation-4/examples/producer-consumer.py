from multiprocessing import Process, JoinableQueue, Queue
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
			#if self.q.qsize() < qSize:
			self.q.put(i)
			print "Producer %i produced Task %i" % (self.id, i)
		self.q.put(None) # Poison Pill
		print ("Producer %i produced Poison Pill") % self.id
		return


def main():
	numProcesses = 4
	numTasks = 10
	qSize = 20
	q = JoinableQueue()
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