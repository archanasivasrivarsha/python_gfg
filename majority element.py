Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
class Solution:
    def majorityElement(self, arr):
...         
...         # Step 1: Find candidate
...         count = 0
...         candidate = None
...         
...         for num in arr:
...             if count == 0:
...                 candidate = num
...                 count = 1
...             elif num == candidate:
...                 count += 1
...             else:
...                 count -= 1
...         
...         # Step 2: Verify candidate
...         if arr.count(candidate) > len(arr) // 2:
...             return candidate
...         
