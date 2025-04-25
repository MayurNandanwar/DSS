# Iterator 

# --> iterable: collaction of value enclosed by bracket ex. list, tuple, dict,set on which we can iterate
# --> iterator : its an object of countable value , determined by iter keyword
# iterator has two keyword : iter used to make iterator and next used for print next value
# iterable = [1,2,3,4]
# iterator = iter(iterable)

# 1st method 
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))  
# using above method we can get error 
#   File "C:\Users\G01889\OneDrive\Documents\DSS\iterator_vs_generator.py", line 13, in <module>    
#     print(next(iterator))
#           ^^^^^^^^^^^^^^
# StopIteration

# 2nd method 
# for i in iterator:
#     print(i)
# using for loop method we dint get error and we can run as many as you want

# disadvantage :
#  --> not memory efficient because we store values in list , tuple, dictionary


## Generator 
# --> if function containing the keyword "yield" then we can say that object of this function is Generator
# because when run object with next keyword main thread reach to yield keyword it stops the code available below the yield keyword and 
# goes back to the object and again if call function with next keyword then first start with code exist below yield keyword if available 

# generator has only one keyword which is next
# generator is memory efficient it prints value at time but does not store value memory
# ex.

# def generator():
#     for i in range(10):
#         yield i
# gen = generator()

# print(next(gen)) # after executing last value if we execute again then we get error StopIteration

# for i in gen:
#     print(i)  # we dint get error 


## generator Vs Iterator 
# --> both are similar but generator memory efficient where as iterator is not memory efficient

