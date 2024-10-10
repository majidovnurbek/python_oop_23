# class Student:
#     def __init__(self, first_name):
#         self.first_name = None
#         # self.last_name = last_name
#         # self.age = age
#
#
#     @staticmethod
#     def to_title(name):
#         return name.title()
#
#
# objects = Student("nurbek")
# print(objects.to_title("nurbek"))


# Users: dict = {}
#
#
# class Register:
#     def __init__(self, name, username, password):
#         self.name = name
#         self.username = username
#         self.password = password
#
#     def get_info(self):
#         return self.name, self.username, self.password
#
#
# user = Register("nurbek","majidov","2008")
# Users["username"]=user.username
# Users["password"]=user.password
#
#
# class Login:
#     def __init__(self, username=None, password=None):
#         self.username = username
#         self.password = password
#
#     def get_login(self):
#         return Users["username"], Users["password"]
#
#
# user1 = Login()
# # print(user1.get_info())
# matn = """
# 1.register
# 2.login
# ------------>>>>>>
# """
#
# while 1:
#     data = int(input(matn))
#     if data == 1:
#         name = input("enter name:")
#         username = input("enter username:")
#         password = input("enter password  :")
#         user = Register(name=name,username=username,password=password)
#
#         Users["username"] = user.username
#         Users["password"] = user.password
#         print("-----------------------------------")
#         print(*user.get_info())
#         print("-----------------------------------")
#
#     if data==2:
#         username = input("enter username:")
#         password = input("enter password  :")
#         if user1.get_login()[0]==username and user1.get_login()[1]==password:
#             print("-----------------------------------")
#             print("---    siz logindan o'tdingiz   ---")
#             print("-----------------------------------")
#             break
#         else:
#             print("-----------------------------------")
#             print("-- error:passowrd or username!  --")
#             print("-----------------------------------")


# class talaba:
#     university_name = "oddiy universitet"
#
#     def __init__(self, name):
#         self.name = None
#
#     @classmethod
#     def change_name(cls, name):
#         talaba.name = name
#
#
# talaba.change_name("nurbek")
#
# print(f"hozir {talaba.change_name()}")

class Point:
    name=None

    @classmethod
    def change_name(cls,nname):
        Point.name=nname




Point.change_name("nurbek")
print(Point.name)