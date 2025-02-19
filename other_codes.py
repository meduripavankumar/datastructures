# count vowels
def count_vowels(st):
    vowels = "aeiouAEIOU"
    return sum(1 for char in st if char in vowels)

strings = ["apple","banana","kiwi"]

# find sum pairs

def find_sum_pairs(nums,target):
    sum_index = {0:-1}
    cur_sum = 0
    for index,value in enumerate(nums):
        cur_sum += value
        if cur_sum - target in sum_index:
            return [sum_index[cur_sum-target]+1,index]
        sum_index[cur_sum] = index
    return []
nums = [1,2,3,4,5,6,7]
print(find_sum_pairs(nums,target= 12))

# contagious sub array

def contagious_subarray_sum(nums,target):
    my_hash = {}
    cur = 0
    for index,num in enumerate(nums):
        cur += num
        diff = target-cur
        if diff in my_hash:
            return (my_hash[diff],index+1)
        my_hash[cur] = index
    return []

nums = [1, 2, 3, 4, 5]
target = 9
print ( contagious_subarray_sum(nums, target) )

# bubble sort

def bubble_sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] < nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums

# K largest 

import heapq
def find_k_largest(nums,k):
    heap = nums[:k]
    heapq.heapify(heap)
    for i in nums[k:]:
        if i > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap,i)
    return heap[0]


#  k smallest

import heapq
def find_k_smallest(nums,k):
    heap = [-num for num in nums[:k]]
    heapq.heapify(heap)
    for num in nums[k:]:
        if -num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap,-num)
    return -heap[0]













