# class Person:
#     def __init__(self, name, age, millati):
#         self.name = name
#         self.age = age
#         self.millati = millati
#
#
# @property
# def super_person_info(self):
#     return self.name, self.age, self.millati
#
#
# obj = Person("matiz", "2011", "white")
#
#
# class superPerson(Person):
#     def __init__(self, name, viloyati, year,sinfi, maktabi, millati):
#         super().__init__(name, viloyati, millati)
#         self.maktabi = maktabi
#         self.year = year
#         selfsinfi =sinfi
#
#     @property
#     def super_person_info(self):
#         return self.name, self.age, selfsinfi, self.millati, self.maktabi, self.year
#
#
# max_obj = superPerson("malibu ", "xl", 2023, 250, 10_000, "black")
# print(*max_obj.super_person_info)
#


########################################################################################################################


# class Person:
#     def __init__(self, name, age, millati):
#         self.name = name
#         self.age = age
#         self.millati = millati
#
#
# @property
# def super_person_info(self):
#     return self.name, self.age, self.millati
#
#
# obj = Person("matiz", "2011", "white")
#
#
# class superPerson(Person):
#     def __init__(self, name, viloyati, year,sinfi, maktabi, millati):
#         super().__init__(name, viloyati, millati)
#         self.maktabi = maktabi
#         self.year = year
#         selfsinfi =sinfi
#
#     @property
#     def super_person_info(self):
#         return self.name, self.age, selfsinfi, self.millati, self.maktabi, self.year
#
#
# max_obj = superPerson("mers ", "c class", 2023, 250, 10_000, "black")
# print(*max_obj.super_person_info)

#############################################################
# class Person:
#     def __init__(self, name, age, millati):
#         self.name = name
#         self.age = age
#         self.millati = millati
#
#
# @property
# def super_person_info(self):
#     return self.name, self.age, self.millati
#
#
# obj = Person("nurbek", "15", "uzbek")
#
#
# class superPerson(Person):
#     def __init__(self, name, viloyati, year,sinfi, maktabi, millati):
#         super().__init__(name, viloyati, millati)
#         self.maktabi = maktabi
#         self.year = year
#         self.sinfi =sinfi
#
#     @property
#     def super_person_info(self):
#         return self.name, self.age, self.sinfi, self.millati, self.maktabi, self.year
#
#
# max_obj = superPerson("bunyod ", "tashkent", 2008, 9, "pdp", "uzbek")
# print(*max_obj.super_person_info)
#
###################################################################################################################
# class Car:
#     def __init__(self, name, age, colour):
#         self.name = name
#         self.age = age
#         self.colour = colour
#
#
# @property
# def car_change(self):
#     return self.name, self.age, self.colour
#
#
# obj = Car("cobalt", "4", "white")
#
#
# class superCar(Car):
#     def __init__(self, name, model, year, speed, km, colour):
#         super().__init__(name, model, colour)
#         self.km = km
#         self.year = year
#         self.speed = speed
#
#     @property
#     def car_change(self):
#         return self.name, self.age, self.speed, self.colour, self.km, self.year
#
#
# max_obj = superCar("gentra ", "1.5", 2023, 250, 10_000, "black")
# print(*max_obj.car_change)






# class Shaxs:
#     def __init__(self, ism, yosh):
#         self.ism = ism
#         self.yosh = yosh
#
#
# class talaba(Shaxs):
#     def __init__(self, ism, yosh, manzil, idcard):
#         super().__init__(ism, yosh)
#         self.manzil = manzil
#         self.idcard = idcard
#
#
# talab=talaba("bunyod",16,"tashkent","ab12486")
# print(talab.ism)
