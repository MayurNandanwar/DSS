
#! max length subarray with sum = k 
# ex. sum = 3 , lst =[1,1,1,2,1,3,0,0,0,0,1,1]

# lst =[1,1,1,2,1,3,0,0,0,0,1,1]
# k = 3
# def max_len_sub_array(lst,k): #! time complexity O(N2) , space complexity os O(1)
#     len_1 = 0
#     for i in range(len(lst)):
#         sum= 0
#         for j in range(i,len(lst)):
#             sum+=lst[j]

#             if sum == k:
#                 len_1 = max(len_1,(j-i)+1)   # j-i mean ex. at index j=2 sum =3,index i =0 then 2-0 = 2 but [1,1,1] len = 3 thats why (j-i)+1

# max_len_sub_array(lst,3)


#! better 
# logic : store sum as key and index as value and check if sum > k then only find abs(sum-k) present in dicti if 
# yes then get the index and substanct from current index (i) we get the lenth comapare with previous length

# k=4
# lst =[1,1,1,2,1,3,0,0,0,0,1,1]
# def max_len_sub_array_sum_k(lst,k):#! time complexity is NlogN for ordered map, sutable for negative , zeros and positive
#     #! for unorder map O(1) but if any colission happen then O(n2), space complexity for hashmap = O(N)
#     len_1 = 0
#     sum = 0
#     dicti = {}
#     for i in range(len(lst)):
#         sum+=lst[i] # 9
#         if sum>k: 
#             print(i)
#             if sum not in dicti.keys():
#                 dicti[sum]= i
#                 print(dicti)
#             sum_key = abs(sum-k)
#             if sum_key in dicti.keys():  
#                 index =  dicti[sum_key]
#                 len_1 = max(len_1,i-index)
#         else:
#             print(i)
#             if sum not in dicti.keys():
#                 dicti[sum]= i
#                 print(dicti)
#             if sum == k:
#                 len_1 = i+1
#     return len_1

# print(max_len_sub_array_sum_k(lst,k)) #! this is optimal solution for positive, negative and zero

#! optimal solution for positive and zero
# lst = [1,2,3,2,1,1,1,3,3]

# def max_len_sub_array_sum_k(lst,k): #!time complexity is O(2N) because inside loop is oftenly run depends on when sum >k, space complexity O(1)
#     i=0
#     len_1 = 0
#     sum = 0
#     for j in range(len(lst)):
#         sum+=lst[j]
#         while sum>k and i<=j:   # this loop will often run 
#             sum-=lst[i]
#             i+=1
#         if sum == k:
#             len_1 = max(len_1,(j-i+1))
#     return len_1

# max_len_sub_array_sum_k(lst,3)










    

