from dataclasses import dataclass, field

# @dataclass
# class person:
#     name: str
#     address: str
#     age: int
#
#
# odam = person("bunyod", 16, "tashkent") # noqa
# print(odam.name)
#

# @dataclass
# class autosalon:
#     year: int
#     name: str
#     model: str
#     address: str
#
#     colour: str
#
# car=autosalon(2023,"malibu","xl","tashkent","black")
# print(car.__dict__)

####################################################     HOMEWORK__1__   ##################################################################### # NOQA
# @dataclass
# class korxona:
#     address: str
#     year: str
#     maydoni: str
#
# farm=korxona("tashkent",2020,"14ga")
# print(farm.year)


# @dataclass
# class autosalon:
#     year: int
#     name: str
#     model: str
#     colour: str
#
# car=autosalon(2023,"malibu","xl","black")
# print(car)
###########################################################################################################################################################################
# @dataclass
# class xodim:
#     name: str
#     age: int
#     city: str =field(init=False,default="Tashkent")
#
# obj=xodim("bunyod",16)
# print(obj.city)
#########################################################################################################################################################################
# @dataclass
# class Person:
#     name:str
#     age:int
#
#     def __hash__(self):
#         return hash((self.name, self.age))
#
#
# person1 = Person("Nurbek", 18)
# person2 = Person("Javohir", 33)
# print(hash(person1))
# print(hash(person2))
# emp = Person("Jamshid", 21)
# print(emp)
#####################################################################################################################################################################################################################################################################
# @dataclass
# class Car:
#     user_passowrd: int
#     user_card: int
#
#     def __hash__(self):
#         return hash((self.user_passowrd, self.user_card))
# object=Car(2008,2294)
# print(hash(object))
##########################################################################################################################################
# from dataclasses import dataclass, field
#
# @dataclass
# class Car:
#     name: str
#     year: int
#
#     address: str = field(init=False, default="Tashkent", repr=True)
#
#
# obj = Car("mers", 18)
# obj2 = Car("bmw", 22)
# print(obj == obj2)
##############################################################################################################################################
# @dataclass
# class Car:
#     name: str
#     year: int
#
#     address: str = field(init=False, default="Tashkent")
#
#
# obj = Car("mers", 18)
# obj2 = Car("bmw", 22)
# print(obj == obj2)

# from create_modul import moduls
#
# q = ["Anvar", "bunyod", "Asalom"]
# s = moduls(q)
# print(s)

from create_modul import moduls
print(moduls(2))