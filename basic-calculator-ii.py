# coding=utf-8

"""
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

示例 1:

输入: "3+2*2"
输出: 7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/basic-calculator-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def calculate(s):
    num = 0
    stack = list()
    op = '+'
    for i, c in enumerate(s):
        if c.isnumeric():
            num = num * 10 + int(c)
        if c in '+-*/' or i == len(s) - 1:
            if op == '+':  # 上一个符号
                stack.append(num)
            if op == '-':
                stack.append(-num)
            if op == '*':
                stack.append(stack.pop() * num)
            if op == '/':
                stack.append(int(stack.pop() / num))
            op = c
            num = 0
        print(stack)
    return sum(stack)




if __name__ == "__main__":
    print(calculate("-5-2 * 3"))