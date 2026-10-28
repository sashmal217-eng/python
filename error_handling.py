#zerodivisionerror
# a=10
# b=0
# print(a/b)

#type error
# a=10
# b="hallo"
# print(a+b)

#value error
# a=int('hai')
# print(a)

#intex error
# a=[1,2,3]
# print(a[3])

# key error
# a={"name":"jhon","age":22}
# print(a["city"])

#file not found error
# a=open("stu.tt","r")
# print(a.read())

#error handling

#zerodivisionerror
# a=10
# b=0
# try:
#     print(a/b)
# except:ZeroDivisionError
# print("canot divided by zero")    


# type error
# a=10
# b="hallo"
# try:
#   print(a+b)
# except:TypeError
# print("type error")  


#value error
# try:
#     a=int('hai')

#     print(a)
# except:ValueError
# print("invalid")    


#intex error
# try:
#     a=[1,2,3]
#     print(a[3])
# except:IndexError
# print("index not found")

#  key error
# try:
#     a={"name":"jhon","age":22}
#     print(a["city"])
# except:KeyError
# print("key not found")



#file not found error
# try:
#     a=open("stu.tt","r")
#     print(a.read())
# except:FileNotFoundError
# print("file not found")