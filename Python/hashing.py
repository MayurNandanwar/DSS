
import numpy as np
#! Hashing : it means prestore and fetch  (how many times num available in list )
# ex. i have list and find out that how many times 1 exist ,2 exist  or any number exist in list how to 
# do if we perform looping then if list is large then take long time so we do this 

# import numpy as np

# def find_num_cnt(num,lst):
#     hash_arr = np.zeros(max(lst)+1)
#     for i in lst:
#         hash_arr[i] = hash_arr[i]+1
#     return hash_arr[num]
# lst = [1,2,1,3,4,12]
# cnt = find_num_cnt(2,lst)

# time complexity  = 10^8 = 1 second 
# when use globally array then we can define max 10^7 and inside loop it will be 10^6


# --> how to do for character for character we can do using looping and set counter

# arr = np.zeros(26)
# print('arr:',arr)
# string = 'asaaarew'
# for i in string:
#     val = ord(i)-ord('a')
#     arr[val] = arr[val]+1



# when lower and uppercase available 
# def find_char(x,arr):
#     val = ord(x)
#     count = arr[val] 
#     return count

# # if string = 'AbcSjsdids' that time arr = np.zeros(256)
# string = 'AbcSSjsdids'
# arr = np.zeros(256)
# for i in string:
#     val = ord(i)
#     arr[val] = arr[val]+1

# cnt = find_char('i',arr)
# print(cnt)

#! Note : array stores max size of int = 10^7 globally and inside the function 10^6 so what for more than 10^7
#!for that we use mapping instead of using array for hashing we can use map(dict), and time complexity for this is log n in all cases like good , avh , worst case
#! for unstructure map : avg and best time complexity is O(1), and worst cas O(N) linear time 
#! 2 type of mapping 1) unstructure mapping and mapping

#! note : first use unordered map and if time takes mote then use map 

#! hashing methods
# 1) division method
# 2) Folding method 
# 3) mid Square method


# 1 division method
lst = [2,5,16,28,139]  # here all the values last digit is unique
#if you want to do array hashing you will have to create array of 140 length contain 0 val

#in Hashing (division method)
# arr = np.zeros(10) # 0 to 9 value 
# cnt = 0
# for i in lst:
#     val = i%10
#     arr[val] = cnt+1

# def find_val(x,arr):
#     val = x%10
#     return arr[val]

# cnt = find_val(16)


# what if more than one value has last digit same 

# here we can store value in list {key_0:[],key_1:[]}    
dicti = {}
ex = [1,11,28,228,218,228]
for i in ex:
    val = i%10
    if val in dicti.keys():
        lst = dicti[val]
        print(lst)
        lst.append(i)
        dicti[val] = lst
    else:
        dicti[val] = [i]

print(dicti)
def finc_num_cnt(x,dicti):
    val = x%10
    lst = dicti[val]
    if len(lst)==1:
        cnt = 1
    else:
        cnt = 0
        for i in lst:
            if i==x:
                cnt+=1
    return cnt

count = finc_num_cnt(228,dicti)

print('count::',count)



 





















