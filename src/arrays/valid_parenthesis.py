"""
Valid Parentheses
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true
Example 2:

Input: s = "([{}])"

Output: true
Example 3:

Input: s = "[(])"

Output: false
Explanation: The brackets are not closed in the correct order.
"""

# def func_split(s: str):
#     # convert to list
#     open_to_close = {"(": ")", "{": "}", "[": "]"}
#     close_to_open = {v: k for k, v in open_to_close.items()}
#     stack = list(s)
#     min_len = (len(stack) // 2) - 1
#     print(f"min_len: {min_len} and stack: {stack}")
#     result = []
#     for i in range(min_len):
#         if open_to_close[stack[min_len - i]] == stack[min_len + 1 + i]:
#             result.append(True)
#         else:
#             result.append(False)

#     return all(result)


def func_split2(s: str):
    open_to_close = {"(": ")", "{": "}", "[": "]"}
    close_to_open = {v: k for k, v in open_to_close.items()}
    stack = []
    # check if the first element are open
    if s[0] not in open_to_close.keys():
        return False
    for elem in s:
        if elem in close_to_open.keys():
            if stack and stack[-1] == close_to_open[elem]:
                stack.pop()
            else:
                return False

        else:
            stack.append(elem)

    return True if not stack else False


# the way to solve this problem is to use a stack to keep track of the open brackets and then check if the close brackets are in the correct order and have the corresponding open brackets of the same type in the stack to pop them out of the stack and return True if the stack is empty else return False if the stack is not empty at the end of the loop iteration of the string s passed to the function func_split2 above and the time complexity of the function is O(n) where n is the length of the string s passed to the function func_split2 above


if __name__ == "__main__":
    print(func_split2("[]"))  # this should pass
    # print(func_split("([{}])"))
    # print(func_split("[(])"))
    # print(func_split("([)]"))
    # print(func_split("{[]}"))
    # print(func_split("{{[]}"))
    print(func_split2("()[]{}"))  # this should pass
    print(func_split2("([)]"))  # this should fail
    print(func_split2(")()"))  # this should fail
