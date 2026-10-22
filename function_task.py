# def even_odd(num):
#     if num%2==0:
#         return("even")
#     else:
#         return("odd")


# number=int(input("enter anumber"))
# print(even_odd(number))

#2
# def largest(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c


# num1=int(input("enter first number"))
# num2=int(input("enter second number"))
# num3=int(input("enter third number"))
# print("largest number is:",largest(num1,num2,num3))    

#3
# def sum_list(lst):
#     if not lst:
#         return 0
#     else:
#         return lst[0]+sum_list(lst[1:])
# print(sum_list([1,2,3,4,5,6,]))    

#4
# def even(numbers):
#     result=[]
#     for num in numbers:
#         if num %2==0:
#             result.append(num)
#     return result
# num=[1,2,3,4,5,6,7,8,9]
# print(even(num))        

#5
# def sring(text):
#     return len(text)

# word=input("enter a string:")
# print("length of the string is:",sring(word))

#6
# def string_uppercase(text):
#     return text.upper()
# word=input("enter a string")
# print("string_uppercase",string_uppercase(word))

#7
# def numbers(num):
#     if num >0:
#         return "positive"
#     elif num==0:
#         return "zero"
#     else:
#         return "negative"

# numb=int(input("enter a number"))
# print(numbers(numb))

#8
# def multiple(num):
#     if num %3==0 and num%5==0:
#         return "true"
#     else:
#         return "false"


# number=int(input("enter a number"))
# print(multiple(number))    


#9
# def maximum(numbers):
#     return max(numbers)
# num=[10,30,65,37,29]
# print(maximum(num))

#10
# def grade(marks):
#     if marks>=90:
#         return "A"
#     elif marks>=75:
#         return "B"
#     elif marks>=60:
#         return "c"
#     else:
#         return "fail"

# mar=int(input("enter a mark:"))
# print(grade(mar))
    
   #11 
# def dis(price):
#     discount=price *10/100
#     return price - discount

# price=float(input("enter a price:"))
# print("discounted price",dis(price))

#12
# def count(numbers):
#     even=0
#     odd=0

#     for num in numbers:
#         if num%2==0:
#             even +=1
#         else:
#             odd +=1
#     return even,odd
# nums=[1,2,3,4,5,6,7,8,9,10]
# even_count,odd_count=count(nums)
# print("even count",even_count)
# print("odd cound",odd_count)            


#13
# def celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit

# temp = float(input("Enter temperature in Celsius: "))
# print("Temperature in Fahrenheit:", celsius_to_fahrenheit(temp))