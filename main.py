# class shaxs:
#     ism = ""
#     yil = 0
#     yosh = 0
#     lens = 0
#
#     def get_info(self):
#         return f"{self.ism}\n{self.yil}\n{self.yosh}\n{self.lens}"
#
#
# person = shaxs()
# person.yosh = 15
# person.yil = 2008
# person.ism = "nurbek"
# person.lens = 1.70
# print(person.get_info())






class talaba:
    first_name = ""
    last_name = ""
    username = ""
    age = 0
    course = ""
    def ge_info(self):
        return f"ismi: {self.first_name}\nfamiliya: {self.last_name}\nyosh: {self.age}\nkursi: {self.course}"

student = talaba()
student.first_name="nurbek"
student.last_name="majidov"
student.age=15
student.course="IT"
print(student.ge_info())
print("#######################################################################################################################")

class Car:
    car_name = ""
    colour = ""
    year = ""
    price = 0

    def get_info(self):
        return f"nomi: {self.car_name} \nrangi: {self.colour} \nyili: {self.year}\nnarxi: {self.price}$"


electro_car = Car()  # object 1

electro_car.car_name = "BYD"
electro_car.colour = "black"
electro_car.year = 2022
electro_car.price = 40000
print(electro_car.get_info())
print("#######################################################################################################################")
class shaxs:
    ism = ""
    surname = ""
    yil = 0
    yosh = 0
    lens = 0
    school=""

    def get_info(self):
        return f"ismi: {self.ism}\nfamiliyasi: {self.surname}\ntugilgan yili: {self.yil}\nyoshi: {self.yosh}\nboy uzuznligi: {self.lens} metr\nmaktabi: {self.school} "


person = shaxs()
person.yosh = 15
person.yil = 2008
person.ism = "nurbek"
person.lens = 1.70
person.surname = "majidov"
person.school="PDP"
print(person.get_info())
