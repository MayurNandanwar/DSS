
#! --> extract number from the last  one by one ex 1223 to 3, 2, 2, 1

# x = 1334455

# while x>0:
#     n1 = x%10
#     print(n1)
#     x = int(x/10)



#! --> reverse the number 

# lst = []
# x = 1334455
# while x>0:
#     n1 = x%10
#     lst.append(str(n1))
#     x = int(x/10)   #! time complexity is O(log10(x)) because iteration depends on value of x

# print(int(''.join(lst)))

# lst = []
# x = 1334455
# rev_num = 0
# while x>0:
#     lst_num = x%10
#     lst.append(str(lst_num))
#!     x=int(x/10)  # time complexity os O(log10(x)) if x = int(x/5) then timecomplexity = O(log5(x))
#     rev_num=(rev_num*10) + lst_num

# print(''.join(lst))




#! palendrom number : reverse of number is same ex. 121 , reverse of 121 = 121, 7 reverse of 7 is =7

#! armstrong number: any number sum of cube of each degits = number ex. 371= 3**3 + 7**3 + 1**3 , 1634 = 1**3+ 6**3+ 3**3+ 4**3

#! print all the divisors :
# ex 36: is divided by 1, 2,3,4,6,9,12,18,36 
# lst = []
# n=36
# for i in range(1,int((n*n)+1)):
#     if n%i == 0:
#         lst.append(str(i))
#         lst.append(str(int(n/i)))

#! print(set(lst))  # time complexity is when we sort the  list or any thing is n log n

#! prime number : number that has exactly 2 factor 1 and itself 
import math
# cnt = 0
# n = 11

# for i in range(n+1):

#     if n/i == 0:
#         cnt+=1
# if len(cnt==2):
#     print(n)
# #! time complexity is == O(n)

#! GCD or HCF greatest common divisor or highest common factor : highest number  which divides both number
#! To find GCD euclidian algorithm says that GCD(a,b) = GCD(a-b,b) when  a>b 
# ex(12,9) provide highest common factor or greatest common divisor 
    #  for 9 factor is 1,3 , for 12 1,3 so here GCD/HCF is 3
# a = 12 
# b = 9
# n = min(12,9)
# gcd = 0
# for i in range(1,n):
#     if (a%i==0) and (b%i==0):
#         gcd = i

#! print(gcd) # time complexity = O(min(a,b))

# using eculidian Algorithm : 
# ex GCD(20,15) = GCD(20-15=5,15)
#  GCD(5,15) = GCD(15,5) = GCD(10,5)
# GCD(10,5) = GCD(5,5)
# GCD(5,5) = GCD(0,5) # here 5 is GCD/HCF   
# #! this takes lot time if have larger number one of the value is large  when large number then can also done by GCD(a,b) = GCD(a%b,b)    # time complexity = log(fi-sign)(min(a,b))    


    
#! fectorial 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) #! time complexity O(n)


        




    













