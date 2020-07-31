#
# @lc app=leetcode.cn id=1114 lang=python
#
# [1114] 按序打印
#
# @lc code=start
from threading import Lock
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
# @lc code=end

