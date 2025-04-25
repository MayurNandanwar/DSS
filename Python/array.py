
#! find second largest eliment in array (max value in array stored = 10^6 in function , globally we can store values in array 10^7)
import numpy as np
# arr = np.array([1,3,2,4,5,2,8,8])
# print(arr)

# largest = arr[0] 
# second_largest = -1

# for i in range(1,len(arr)):
#     if arr[i]>largest:
#         second_largest = largest
#         largest = arr[i]

# print(largest,second_largest)


#! check array is sorted:
# def sorted_check(arr):

#     for i in range(1,len(arr)):
#         if arr[i-1]>arr[i]:
#             return 'false'
#         else:
#             continue
#     else:
#         return 'true'

# arr = np.array([1,2,3,4,5])
# print(sorted_check(arr))

#! remove duplicates from sorted array 
# arr = np.array([1,2,2,3,4,4,5])
# print(set(arr))


#! left rotate the array by one place
# arr = np.array([1,2,2,3,4,4,5])
# def d_rotate(arr,num):
#     d =  num%10
#     tmp1 = arr[:d]
#     tmp2 = arr[d:]
#     res = np.append(tmp2,tmp1)
#     return res
    
# array = d_rotate(arr,3)

# print(array)

def d_rotate(arr,num):
    d = num%(len(arr)-1)
    print(d)

    if d == 0:
        print('in')
        return arr
    else:
        tmp = arr[:d].copy()
        print(tmp)
        for i in range(d,len(arr)):
            arr[i-d] = arr[i]
        arr[(len(arr)-d):] = tmp
        return arr

arr = np.array([1,2,2,3,4,4,5])
res = d_rotate(arr,28)
print(res)











        


    
