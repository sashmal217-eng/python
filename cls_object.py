# class car:
#     def __init__(self,make,model,year):
#         self.m=make
#         self.mo=model
#         self.y=year

#     def display_info(self):
#         print(f"car:{self.m} {self.mo} {self.y}")

# my_car=car("toyota","corola",2021)
# car2=car("ford","mustang",2023)
# my_car.display_info()   
# car2.display_info()     

# my_car.y=2020
# my_car.display_info()


# class dog:
#     def __init__(self,breed,name):
#         self.br=breed
#         self.n=name

#     def bark(self):
#         print(f"{self.n} says wooof")

# dog1=dog("labor","buddy")

# print(dog1.br)

# dog1.bark()


# class book:
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author

#     def __str__(self):
#         return f"{self.title}'by {self.author}"
# book=book(1984,"george orwell")
# print(book)
        


# class employee:
#     company="ABC corp"

#     def __init__(self,name,position):
#         self.name=name
#         self.position=position

# employee1=employee("jhon", "manager")
# emp2=employee("alice","developer")

# print(employee1.company)
# print(emp2.company)

# print(employee1.name)
# print(emp2.name)
        


# class student:
#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark

#     def display_grade(self):
#         if self.mark>=90:
#             result ="A"
#         elif self.mark>=70 and self.mark <90:
#             result ="b"  

#         elif self.mark>=50 and self.mark<75:
#             result="c"
#         else:
#             result="fail"    

#         print(f"{self.name}'s grade: {result}")
# stu1=student("alice",80)
# stu2=student("john",95)

# stu1.display_grade()
# stu2.display_grade()


        