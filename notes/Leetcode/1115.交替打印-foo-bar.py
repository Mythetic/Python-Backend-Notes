#
# @lc app=leetcode.cn id=1115 lang=python
#
# [1115] 交替打印FooBar
#

# @lc code=start
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
# @lc code=end

