# Description
Given a string representing a calculation formula, e.g.: " 3+5 / 2 ", return its actual results.

# Solution
Use stack to store the value. When come into * and /, compute the results using the adjacent number and push back to the stack, finally sum up the elements in stack.

一个直接的做法是遍历string，遇到```+, -```就开始将前面得到的数字压栈，遇到```*, /```就再找到后面的数字，计算过后压栈。
但这样写法非常容易出错。参考了网上的答案，比较好的做法应该是：

遍历string, 遇到数字就存储，遇到operator就开始操作：根据之前的operator.
如果是```+, -```就将目前的数字取正负，然后压栈；如果是```*, /```，就取栈底的数字进行计算，然后压栈。同时将当前的operator记录，作为
下一次操作时的之前operator.