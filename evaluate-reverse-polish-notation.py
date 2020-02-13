# coding=utf-8

"""
根据逆波兰表示法，求表达式的值。

有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

说明：

整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
示例 1：

输入: ["2", "1", "+", "3", "*"]
输出: 9
解释: ((2 + 1) * 3) = 9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/evaluate-reverse-polish-notation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def evalRPN(tokens):
    stack = list()
    for t in tokens:
        if t not in '+-*/':
            stack.append(int(t))
        else:
            right = stack.pop()
            left = stack.pop()
            if t == '+':
                stack.append(left + right)
            elif t == '-':
                stack.append(left - right)
            elif t == '*':
                stack.append(left * right)
            elif t == '/':
                stack.append(int(left / right))

    return stack[0]


if __name__ == "__main__":
    tokens = ["2", "1", "+", "3", "*"]
    print(evalRPN(tokens))