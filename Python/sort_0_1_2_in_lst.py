
#! sort 0's, 1's and 2's in list 

# def sort_0_1_2(lst): #! time complexity is for 1st loop O(N) + remaining 3 loop O(N) because [:count_0]+[count_0:count_0+count_1]+ [count_0+count_1:count_0+count_1+count_2] = [:len(lst)]
#     count_0 = 0  #! space complexity = no space using 
#     count_1 = 0
#     count_2 = 0

#     for i in lst:
#         if i==0:
#             count_0+=1
#         if i == 1:
#             count_1+=1
#         if i==2:
#             count_2+=1

#     for i in range(count_0):
#         lst[i]=0
#     once = count_0+count_1
#     for j in range(count_0,once):
#         lst[j]=1
#     twos = once+count_2
#     for k in range(once,twos):
#         lst[k]=2
#     return lst


# lst = [0,1,1,0,1,2,1,2,0,0,0]

# print(lst)


#! using dulch national flag algorithm 0 --> low-1 =0 , low --> mid-1 = 1 mid --> high random 0/1/2 , high+1 --> n-1 = 2
#! now we have to sort only mid --> high 

# lst = [0,1,1,0,1,2,1,2,0,0,0]

# low = 0
# mid = 0
# high =len(lst)-1
# while mid<=len(lst)-1:
#     if lst[mid]==0:
#         tmp = lst[low]
#         lst[low] = lst[mid] 
#         lst[mid] = tmp
#         print(lst)
#         low+=1
#         mid+=1
#     if lst[mid] == 1:
#         mid+=1

#     if  mid ==2:
#         tmp = lst[mid]
#         lst[mid] = lst[high]
#         lst[high] = tmp
#         print(lst)
#         high-=1

# print(lst)

# lst = [0,0,0,0,2,0,1,1,1,0]

lst = [0,1,1,0,1,2,1,2,0,0,0]
mid=0        
low=0
high = len(lst)-1

while mid < len(lst)-1:
    
    print(lst[low])
    print(lst[mid])
    print(lst[high])
    print('\n')
    # mid+=1
    if lst[mid]==0:
        tmp = lst[low]
        lst[low] = lst[mid] 
        lst[mid] = tmp
        low+=1
        mid+=1

    elif lst[mid] == 1:
        mid+=1

    elif lst[mid] ==2:
        tmp = lst[mid]
        lst[mid] = lst[high]
        lst[high] = tmp
        high-=1

print(lst)
        






