#
# @lc app=leetcode.cn id=1116 lang=python
#
# [1116] 打印零与奇偶数
#

# @lc code=start
import threading

class ZeroEvenOdd(object):
    def __init__(self, n):
        self.n = n
        self.zeroS = threading.Semaphore(1)
        self.oddS = threading.Semaphore(0)
        self.evenS = threading.Semaphore(0)
        
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.n + 1):
            self.zeroS.acquire()
            printNumber(0)
            if i % 2:
                self.oddS.release()
            else:
                self.evenS.release()      
        
        
    def even(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.n + 1):
            if i % 2 == 0:
                self.evenS.acquire()
                printNumber(i)
                self.zeroS.release()     
        
        
    def odd(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.n + 1):
            if i % 2:
                self.oddS.acquire()
                printNumber(i)
                self.zeroS.release()   
        
                
# @lc code=end

