# O(nlogn)
def using_sort(arr):
    n = len(arr)
    
    arr.sort()
    
    for i in range(n-2, -1, -1):
        if arr[i] != arr[n-1]:
            return arr[i]
    
    return -1
# O(2n)
def two_pass_search(arr):
    n = len(arr)
    largest = secondLargest = -1
    
    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]
    
    for i in range(n):
        if arr[i] > secondLargest and arr[i] != largest:
            secondLargest = arr[i]
    
    return secondLargest
            
# O(n)
def one_pass_search(arr):
    n = len(arr)
    largest = secondLargest = -1
    
    for i in range(n):
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]
        elif arr[i] < largest and arr[i] > secondLargest:
            secondLargest = arr[i]
    
    return secondLargest
    
    