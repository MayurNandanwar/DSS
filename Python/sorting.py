#! sort the array 1) selection sort 2)bubble short 3)insertion sort
#! 1) selection sort : push minimum to first
#!step: by looping take 2 value and compare a< b then continue else reverse

# lst = [13,42,115,24,53,9,56,3,23,39]

# for i in range(len(lst)): 
#     for j in range(i+1,len(lst)): 
#         if lst[i]<lst[j]:
#             continue
#         else:
#             i_index = lst.index(lst[i])
#             # print(i_index)
#             j_index = lst.index(lst[j])
#             # print(j_index)
#             a = lst[i]
#             b = lst[j]
#             lst[i_index] = b
#             lst[j_index] = a
# print(lst)

#! time complexity : n+ n-1+n-2+n-3+n-4....+0 n(n-1)/2 = n2 + n/2  ~= O(n2)

#!2) bubble sort : push maximum to last 

# lst = [115,12,80,9,23,43,50]

# for i in range(len(lst)-1,-1,-1):
#     for j in range(i-1,-1,-1):
#         # print(lst[i],lst[j])
#         if lst[i]<lst[j]:
#             index_i = lst.index(lst[i])
#             index_j = lst.index(lst[j])
#             a = lst[i]
#             b = lst[j]
#             lst[index_i] = b
#             lst[index_j] = a
#         else:
#             continue
# print(lst)
#! time complexity = O(n2)  n+n-1+n-2+n-3+...0 = n(n+1)/2 = n2 but if already sorted array then O(n) see example below

# lst = [115,12,80,9,23,43,50]

# lst = [9, 12, 23, 43, 50, 80, 115]
# swap = 0
# for i in range(len(lst)-1,-1,-1):
#     for j in range(0,i):
#         # print(lst[i],lst[j])
#         if lst[j]>lst[j+1]:
#             temp = lst[j]
#             lst[j] = lst[j+1]
#             lst[j+1] = temp    # use this way
#             swap+=1

#         else:
#             continue


#! in insertion sort : take one element at a time and place it in correct way 
# lst = [115,12,80,9,23,43,50]
# for i in range(len(lst)):
#     j = i
#     while j>0 and lst[j-1]>lst[j]:
#         tmp =  lst[j-1]
#         lst[j-1] = lst[j]
#         lst[j] = tmp
#         j-=1
# print(lst)


import math
# merge sort:: divide and merge
lst = [1,8,2,5,4]

low=0
high = len(lst)-1
mid = math.floor((low+high)/2)
lst =[]


def merge_sort(low,high,lst):
    low=0
    mid = math.floor((low+high)/2)

    if low>=high:
        return 0
    
    merge_sort(low,mid,[]) #0,2 #0,1 # 0,0 

    merge_sort(mid+1,high,[]) # 2,4 # 2,3 # 2,2

    merge(low,mid,high)




















    









