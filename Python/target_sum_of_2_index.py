
#! you have given a list and target sum value find out the index of 2 values sum of which is target 

#! brute approach
# def element_sum_equals_target(lst,target):#! time complexity is O(N2)
#     for i in range(len(lst)):
#         for j in range(i+1,len(lst)):
#             if i==j :# if index same then nothing happen 
#                 continue
           
#             if lst[i]+lst[j]  ==  target:
#                 return i,j
#     else:
#         return "not found"
    
# lst = [1,2,3,8,5] 
# target=9

# print(element_sum_equals_target(lst,target))


#! better approach

# def element_sum_equals_target(lst, target): #! time complexity ordered map is NlogN for unordered map worst case O(N2), space complexity = O(N)
#     dicti = {}
#     for i in range(len(lst)):
#         val = target - lst[i]
#         if val not in dicti.keys():
#             dicti[lst[i]] = i 
#         else:
#             return i,dicti[val] 
#     else:
#         return "not found"
    
# lst = [1,2,3,8,5] 
# target=9

# print(element_sum_equals_target(lst,target))


#! optimal 
#Note two pointer approach, first sort the list and then one pointer start from left and 2nd pointer from right 
# if sum of 2 pointer is < target then move the left pointer right side , if sum of 2 pointer is > target then move right pointer left side

# def element_sum_equals_target(lst,target): #! two pointer approach , time complexity for pointer movement O(N) + sorting the array O(NlogN) = 2NlogN, space complexity here we are doing sorting so O(N)
#     lst = sorted(lst)
#     i =0 
#     j = len(lst)-1
   
#     while i<j:
#         sum = lst[i]+lst[j] 
#         if sum < target:
#             i+=1
#         elif sum > target:
#             j-=1
#         elif sum == target:
#             return i,j
#     return "not found"

# lst = [2,5,6,8,11] 

# target=14

# print(element_sum_equals_target(lst,target))
    


        
