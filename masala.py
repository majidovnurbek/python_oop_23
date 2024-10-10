# from uuid import uuid4
# class person:
#     def __init__(self, first_name=None, last_name=None, year=None, address=None):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.year = uuid4()
#         self.address = uuid4()
#
#
#     def get_address(self):
#         return self.address
#
#
# obj = person("nurbek", "majidov", 15, "AB123434")
#
#
# class Student(person):
#     def __init__(self, university_name, student_id, first_name, last_name, year, address):
#         super().__init__(first_name, last_name, year, address)
#         self.university_name = university_name
#         self.student_id = student_id
#
#     def get_address(self):
#         return  self.student_id, self.address,self.university_name,self.last_name,self.first_name
#
#     @property
#     def age(self):
#         return f"{2023 - self.year}"
#
#
# child = Student("pdp university", 344545535, "nurbek", "majidov", 2008, "tashkent")
# print(child.age)
#
#
#
#
#
#
#
