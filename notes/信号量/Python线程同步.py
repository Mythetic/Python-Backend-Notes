# coding:utf-8

from threading import Lock

# 依次执行三个函数
class Foo(object):
	def __init__(self):
		self.firstJobDone = Lock()
		self.secondJobDone = Lock()
		self.firstJobDone.acquire()
		self.secondJobDone.acquire()

	def first(self, printFirst):
		"""
		:type printFirst: method
		:rtype: void
		"""
		# printFirst() outputs "first". Do not change or remove this line.
		printFirst()

		self.firstJobDone.release()

	def second(self, printSecond):
		"""
		:type printSecond: method
		:rtype: void
		"""
		with self.firstJobDone:
			# printSecond() outputs "second". Do not change or remove this line.
			printSecond()

			self.secondJobDone.release()

	def third(self, printThird):
		"""
		:type printThird: method
		:rtype: void
		"""
		with self.secondJobDone:
			# printThird() outputs "third". Do not change or remove this line.
			printThird()
		self.firstJobDone.acquire()
		self.secondJobDone.acquire()

def printFirst():
	print("fff")

def printSecond():
	print("jjj")

def printThird():
	print("sss")

#test = Foo()

# for i in range(10):
# 	test.first(printFirst)
# 	test.second(printSecond)
# 	test.third(printThird)


import threading

empty = threading.Semaphore(1)  # empty信号量初始值设为1  空缓冲区数量
full = threading.Semaphore(0)  # full 信号量初始值设为0  满缓冲区数量
'''信号量为0时，不可被减，同时信号量不设上限
所以需要两个信号量empty、full共同监测两个边界[0,1]'''


class FooBar(object):
	def __init__(self, n):
		self.n = n

	def foo(self, printFoo):
		for i in range(self.n):
			empty.acquire()  # empty-1，申请一个空缓冲区，有空位时应执行生产者活动
			printFoo()
			full.release()  # full+1，释放一个满缓冲区

	def bar(self, printBar):
		for i in range(self.n):
			full.acquire()  # full-1, 申请一个满缓冲区，当缓冲区有商品时才能实现消费者行为
			printBar()
			empty.release()  # empty+1，释放一个空缓冲区

test = FooBar(10)

def printFoo():
	print("Foo")

def printBar():
	print("Bar")

thread1 = threading.Thread(target=test.foo, args=(printFoo,))
thread2 = threading.Thread(target=test.bar, args=(printBar,))
thread1.start()
thread2.start()



