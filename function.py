#function definition
# def meet():
#     print("hallo world")
# meet()    #function call


# parameter,argument
# def meet(name):
#     print(f"hallo,{name}!")

# meet("raju")
# meet("lalu")    


# def meet(name, place,age):
#     print(f"hallo, {name} from {place}.you are {age} year old!")
# meet("alice",  "new york",25)    

#type of arguments
#positional arguments
# def add(a,b):
#     print(a)
#     print(b)
# add(20,30)

#keyword arguments
# def greet(name,age,place):
#     print(f"hallo, {name} your age is {age} and your place is {place}")
# greet(age=22,name="raju",place="palakkad")


#default arguments
# def greet(name, place="kochi"):
#     print(f"hallo,{name} your place is {place}")
# greet("raju")
# greet("nafil","palakkad")    

#arbitrary arguments
# def numbers(*a):
#     print(a)

# numbers(1,2,3,4,5,6,7,8,9,)    
    
#arbitary keyword argument
# def details(**a):
#     print(a)

# details(name="nafi", age=22, place="palakkad")    
    

#return statement
# def add(a,b):
#     return(a+b)
# c=add(10,20)
# print(c)

#docstring in functions
# def add(a,b):
#     """this function add two numbers"""
#     return a+b
# print(add.__doc__)

#lambda functuion 
# add=lambda a,b:a+b
# print(add(10,20))


#lambda function wuth map()
# numbers=[1,2,3,4]
# squared=map(lambda x:x**2,numbers)
# print(list(squared))

#using with filter
# numbers=[1,2,3,4,5,6]
# even_numbers=filter(lambda x:x %2==0,numbers)
# print(list(even_numbers))

# using with reduce
# from functools import reduce
# numbers=[1,2,3,4]
# sum_result=reduce(lambda x,y:x+y,numbers)
# print(sum_result)

#function scop
# x=10 #global scop
# def greet():
#     x=5 #enclosing scop
#     def greet1():
#         x=2 #local scop
#         print(x)
#     greet1()

# greet()
# print(x)        

#recursive function for factorial
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n* factorial(n-1)
# print(factorial(5))

#recursive function for fibonacci
# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(6))
    

#iterative factorial

# def iterative_factorial(n):
#     result=1
#     for i in range(1,n+1):
#     result+=i
#     return result

#recursive funtion for sum
# def sum_list(lst):
#     if not lst:
#         return 0
#     else:
#         return lst[0]+sum_list(lst[1:])
# print(sum_list([1,2,3,4,5]))

