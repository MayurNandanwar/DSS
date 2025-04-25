
#! max_consecutive_once = 1   near to each other ex [1,2,1,1,1,3,2,1,1,1,1] here max consecutive number = 4 times 1 near to each other 
#! max_consecutive_2 = means max time 2 near to eachother in list or array 


#!1) max_consecutive_once
# lst = [1,1,0,1,1,1,0,1,1,1,1,0,0]
# def max_consecutive(n,lst): #! timecomplexity O(N), space complexity = O(1)
#     max_len = 0
#     count = 0
#     for i in lst:
#         if i == n:
#             count+=1
#             max_len = max(max_len,count)
#         else:
#             count = 0
#     return max_len

# print(max_consecutive(1,lst))

#! max_consecutive_two
lst = [1,2,1,2,2,1,3,4,2,2,2]

def max_consecutive(n,lst): #! timecomplexity O(N), space complexity = O(1)
    max_len = 0
    count = 0
    for i in lst:
        if i == n:
            count+=1
            max_len = max(max_len,count)
        else:
            count = 0
    return max_len

print(max_consecutive(2,lst))
