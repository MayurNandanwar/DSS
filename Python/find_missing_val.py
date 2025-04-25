## find missing value 
lst = [1,2,4,5]
n = 5

#! Brute Solution 
# def missing_val(n): #! time complexity is O(n2) because 2 times loop is running this is worst case , space complexity O(1) only one variable is assign 
#     for i in range(1,n+1):
#         flag=0
#         for j in range(len(lst)):
#             if lst[j]==i:
#                 flag=1
#                 break
#         if flag==0:
#             missing=i
#             return missing

# val = missing_val(n)
# print(val)

#! Better solution 
import numpy 

# def missing_val(n): #! time complexity is for first loop O(N), for second loop O(N) = O(2N)
#     array = numpy.zeros(n+1)  #! space compexity is O(N) because array we assign value to index.

#     for i in lst:
#         array[i]=1

#     for i in range(1,len(array)):
#         if array[i]==0:
#             return i
#     else:
#         return 'no missing val'

# print(missing_val(n))

#! optimal solution 

#! Note : sum of n number is n*(n+1)/2 
# def find_missing(n,lst): #! time-complexity is O(N), space complexity O(1) , this solution in not better when have value 10^5 , that time required long datatype
#     sum = (n * (n+1))/2
#     sum2 = 0
#     for i in lst:
#         sum2+=i
    
#     missing_num = sum-sum2

#     return missing_num

# print(find_missing(5,lst))

# lst = [1,2,4,5]
# n=5
# def find_missing(n,lst): #! time complexity = O(N), space complexity O(1), this solution is better it use integer datatype 
#     xor1 = 0
#     xor2 = 0
#     for i in range(len(lst)):
#         xor2 = xor2^lst[i]
#         xor1 = xor1^(i+1)  #! because this will go till 4 because of length of lst= 4 and we have n=5
#     xor1 = xor1^n #! len of lst is 4 but n=5 thats why 

#     missing_val = xor1^xor2
#     return missing_val

# print(find_missing(5,lst))


#!2) find the number that appear once, and other twise 
# lst = [1,1,2,2,3,4,4]

# #! brute-force approach 
# def find_num_appear_once(lst): #! time complexity O(N) and space complexity O(1)
#     for i in range(len(lst)):
#         num = lst[i]
#         cnt = 0
#         for j in lst:
#             if num == j:
#                 cnt+=1
#         if cnt == 1:
#             return num
  
#! better 

#!hashing 
import numpy as np

# lst = [1,1,2,2,3,4,4]
# def appear_once(lst): #! time complexity is O(2N), splace complexity O(N), not useful when have value 10^5 array max stores this value time increase
#     arr = np.zeros(max(lst)+1)  # number of zero create increases the space  
#     for i in lst:
#         arr[i]+=1

#     for i in range(1,len(arr)):
#         if arr[i]==1:
#             return i

# print(appear_once(lst))


#! what if has negative values [-1,-1,-2,-2,3,4,4] , use mapping 
# lst = [-1,-1,-2,-2,3,4,4] 
# def appear_once(lst): #! time complexity is NlogN + 2nd loop to identify the num once appear (n/2+1) because only one value one time other is available 2 times = O(nlogn)+O(n/2+1), space complexity O((N/2)+1), 
                        #!if unorder map then O(N) is time complexity in worst cas can be O(N2)
#     num_dict = {}
    
#     for key in lst:
#         if key not in num_dict:
#             num_dict[key]=1
#         else:
#             num_dict[key] = num_dict[key]+1

#     for key,val in num_dict.items():
#         if val ==1:
#             return key

# print(appear_once(lst))

#! optimal 
# lst = [1,1,2,2,3,4,4]  #! time complexity O(N), space complexity O(1)
# def appear_once(lst):
#     xor = 0
#     for i in lst:
#         xor = xor^i

#     xor = xor^0
#     return xor

# we can also solve this using mapping , also with hashing but in mapping space complexity increase , also in hashing max 10^5 number we can store 






        






