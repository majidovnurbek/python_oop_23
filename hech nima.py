# from googlesearch import search
#
# query = "uzbekistan prime minister 2023"
# for url in search(query):
#     print(url)
#

# class Login:
#     def __init__(self, first_name, year):
#         self.first_name = first_name
#         self.year = year
#         # self.name =mersedes_benz
#         # self.email = email
#
#     def get_info(self):
#         return f"{self.first_name} {self.year}"
#
#
# w = []
# a = str(input("first_name:"))
# b = str(input("year:"))
# w.append(a)
# w.append(b)
# # c = str(input("name:"))
# # d = str(input("email:"))
# inson = Login("a", "b")
#
# print(w[0],w[1] )
#
# class persons:
#     def __init__(self, first_name, year):
#         self.first_name = first_name
#         self.year = year
#         # self.brand = brand
#
#     def get_info(self):
#         return f"{self.first_name} {self.year}"
#
#
# inson = persons("nurbek", "2008")
# a=inson.get_info()
# # print(inson.get_info())
# print(a[0], a[1])
# if w[0] and w[1] ==a[0] and a[1]:
#     print("royaatdan otdingiz")
# else:
#     print("notogri")


# class Point:
#     def __init__(self, a, y):
#         self.a = a
#         self.y = y
#
#     def get_info(self):
#         return self.a, self.y
#
#
# point = Point(2, 4)
# print(*point.get_info())
#
# class Point:
#     def __new__(cls, a, y):
#         instance = super(Point, cls).__new__(cls)
#         instance.a = a
#         instance.y = y
#         return instance
#
#
# point = Point(2, 4)
# print(point.a, point.y)
#
#


# class ResourceHandler:
#     def __init__(self, resource_name):
#         self.resource_name = resource_name
#         self.open_resource()
#
#     def open_resource(self):
#         print(f"resursni ochish:{self.resource_name}")
#
#     def close_resource(self):
#         print(f"resursni yopish:{self.resource_name}")
#
#     def __del__(self):
#         self.close_resource()
#         print(f"resurni ishlovchi uchun{self.resource_name}yo'q qilinmoqda")
#
#
# resource = ResourceHandler("example_resource")
# del resource


# class avto:
#     def __init__(self, rangi, narxi, yili):
#         self.rangi = rangi
#         self.narxi = narxi
#         self.yili = yili
#
#     def get_info(self):
#         return f" rangi : {self.rangi}\n narxi : {self.narxi}\n yili : {self.yili}"
#
#
# car = avto("black", 20000, 2023)
# print(car.get_info())
#


# class join_car:
#     def __init__(self,nomi, narxi):
#         self.nomi = nomi
#         self.narxi = narxi
#     def get_info(self):
#         return f"{self.nomi} {self.narxi} successful join"
# b = str(input("Nomi: "))
# d = int(input("Narxi: "))
# s = join_car(b,d)
# print(s.get_info())
# a = input("kiting")


#
#
#
# class car:
#     university_name = "2021"
#
#     def __init__(self, name, address, age):
#         self.name = name
#         self.address = address
#         self.age = age
#
#     @classmethod
#     def change_car(cls, age):
#         print(f"avval {car.university_name}")
#         car.university_name = age
#
#     # setter example
#     def get_address(self, value):
#         self.age = value
#
#
#
# car.change_car(age=2023)
# print(car.university_name)
#
#
#
# class Student:
#     def __init__(self, name, address, age):
#         self.name = name
#         self.address = address
#         self.age = age
#
#     def get_address(self):
#         return self.address
#
#
# odam = Student("nurbek", "samarkand", 15)
# print(f" getter: {odam.get_address()}")
#
#
#
#

class Person:
    def __init__(self, age, name, year):
        self.age = age
        self.name = name
        self.year = year

    def get_info(self):
        return self.age, self.name, self.year

    def change_name(cls, name):
        Person.name = name


Person.change_name("nurbek")

    def
object = Person(16, "Bunyod", 2008)
print(f"{Person.change_name}")
