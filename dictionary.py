# my_dict={"name":"john","age":30,"city":"new york"}
# print(my_dict)

# my_dicy={"name":"john","age":30}
# print(my_dicy["name"])

# my_dict={"name":"john","age":30,}
# print(my_dict.get("age"))

#changing dict item

# my_dict={"name":"john","age":30,}
# my_dict["age"]=32
# print(my_dict)

#adding item to dict
# my_dict={"name":"john","age":30,}
# my_dict["city"]="new york"
# print(my_dict)

#removing item from a dict
# #pop
# my_dict={"name":"john","age":30,"city":"new york"}
# age=my_dict.pop("age")
# print(my_dict)

#popitem
# my_dict={"name":"john","age":30}
# last_item=my_dict.popitem()
# print(my_dict)
# print(last_item)
         
# del statement
# my_dict={"name":"john","age":30}
# del my_dict["age"]
# print(my_dict)

# clear
# my_dict={"name":"john","age":30,"city":"new york"}
# my_dict.clear()
# print(my_dict)

# copying a dict
# a={"name":"john","age":30,"city":"new york"}
# copy_dict=a.copy()
# print(copy_dict)

# a={"name":"john","age":30,"city":"new york"}
# copy_dict=dict(a)
# print(copy_dict)

# # nested dict
# nested_dict={
#    "p1":{"name":"john","age":30},
#     "p2":{"name":"nafil","age":21}
# }
# print(nested_dict["p1"]["age"])

#dict methods
# my_dict={"name":"john","age":30,"city":"new york"}
# print(my_dict.values())

# my_dict={"name":"john","age":30,"city":"new york"}
# print(my_dict.keys())

# my_dict={"name":"john","age":30}
# my_dict.update({"city":"new york"})
# print(my_dict)

# keys=["name","age","city"]
# new_dict=dict.fromkeys(keys,"unkown")
# print(new_dict)

# my_dict={"name":"john","age":30}
# city=my_dict.setdefault("city","new york")
# print(my_dict)
