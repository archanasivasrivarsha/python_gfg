Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> class Solution:
...     def maxSubarraySum(self, arr):
...         max_sum = arr[0]
...         curr_sum = arr[0]
...         
...         for i in range(1, len(arr)):
...             curr_sum = max(arr[i], curr_sum + arr[i])
...             max_sum = max(max_sum, curr_sum)
...         
