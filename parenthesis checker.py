Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> class Solution:
...     def isBalanced(self, s):
...         stack = []
...         
...         pairs = {
...             ')': '(',
...             '}': '{',
...             ']': '['
...         }
...         
...         for ch in s:
...             if ch in '({[':
...                 stack.append(ch)
...             else:
...                 if not stack or stack[-1] != pairs[ch]:
...                     return False
...                 stack.pop()
...         
