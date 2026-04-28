Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
class Solution:
    def inversionCount(self, arr):
        
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0
            
            mid = len(arr) // 2
            left, inv_left = merge_sort(arr[:mid])
            right, inv_right = merge_sort(arr[mid:])
            
            merged, inv_merge = merge(left, right)
            
            return merged, inv_left + inv_right + inv_merge
        
        
        def merge(left, right):
            i = j = 0
            merged = []
...             inv_count = 0
...             
...             while i < len(left) and j < len(right):
...                 if left[i] <= right[j]:
...                     merged.append(left[i])
...                     i += 1
...                 else:
...                     merged.append(right[j])
...                     inv_count += len(left) - i   # key step
...                     j += 1
...             
...             merged.extend(left[i:])
...             merged.extend(right[j:])
...             
...             return merged, inv_count
...         
...         
...         _, count = merge_sort(arr)
