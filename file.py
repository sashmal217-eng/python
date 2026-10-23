# file=open("sample.txt","r")
# content=file.read()
# print(content)
# file.close

# file=open("sample.txt","r")
# line1=file.readline()
# line2=file.readline()
# print(line1)
# print(line2)

# file.close

# file=open("sample.txt","r")
# line=file.readlines()
# print(line)
# file.close


#writing

# file=open("sample.txt","w")
# file.write("hallo world")
# file.close

# file=open("sample.txt","w")
# lines=["hello\n","welcom to python file handling\n" ]
# file.writelines(lines)
# file.close

# appending data
# file=open("sample.txt","a")
# file.write("appented text.\n")
# file.close

#using with statement
# with open("sample.txt","r")as file:
#     content=file.read()
#     print(content)


# file=open("sample.txt","r")
# file.seek(8)
# print(file.read())
# file.close

# file=open("sample.txt","r")
# content=file.read()
# position=file.tell()
# print(file.read())
# file.close