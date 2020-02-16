# coding=utf-8

"""
写一个程序，输出从 1 到 n 数字的字符串表示。

1. 如果 n 是3的倍数，输出“Fizz”；

2. 如果 n 是5的倍数，输出“Buzz”；

3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。

示例：

n = 15,

返回:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fizz-buzz
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    # ans list
    ans = []

    for num in range(1, n + 1):

        divisible_by_3 = (num % 3 == 0)
        divisible_by_5 = (num % 5 == 0)

        num_ans_str = ""

        if divisible_by_3:
            # Divides by 3
            num_ans_str += "Fizz"
        if divisible_by_5:
            # Divides by 5
            num_ans_str += "Buzz"
        if not num_ans_str:
            # Not divisible by 3 or 5
            num_ans_str = str(num)

        # Append the current answer str to the ans list
        ans.append(num_ans_str)

    return ans


def fizzBuzz2(n):
    """
    :type n: int
    :rtype: List[str]
    """
    # ans list
    ans = []

    # Dictionary to store all fizzbuzz mappings
    fizz_buzz_dict = {3: "Fizz", 5: "Buzz"}

    for num in range(1, n + 1):

        num_ans_str = ""

        for key in fizz_buzz_dict.keys():

            # If the num is divisible by key,
            # then add the corresponding string mapping to current num_ans_str
            if num % key == 0:
                num_ans_str += fizz_buzz_dict[key]

        if not num_ans_str:
            num_ans_str = str(num)

        # Append the current answer str to the ans list
        ans.append(num_ans_str)

    return ans


if __name__ == "__main__":
    print(fizzBuzz(15))
