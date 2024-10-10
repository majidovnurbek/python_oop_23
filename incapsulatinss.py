# from uuid import uuid4
#
#
# class Bank:
#     def __init__(self, name, date, bank_id, bank_cart, bank_balance):
#         self.bank_id = uuid4()
#         self.name = name
#         self.date = date
#         self.bank_cart = uuid4()
#         self.bank_balance = uuid4()
#
#     @property
#     def get_bank_cart(self):
#         return self.bank_cart, self.bank_balance, self.bank_id, self.name, self.date
#
#
# obj = Bank("nurbek", "09.12.2023", 2343564656, 986012304530384, "20000$")
# print(obj.bank_id)


# class Card(Bank):
#     def __init__(self, first_name, last_name, phone, card, date, balance, password):
#         super().__init__(self, first_name, last_name, phone, card)
#         self.balance = uuid4()
#         self.password = uuid4()
#         self.first_name = first_name
#         self.last_name = last_name
#         self.phone = phone
#         self.card = card
#         self.date = date
#
#     def get_card(self):
#         return self.first_name, self.last_name, self.phone, self.card, self.date, self.balance, self.password
#
#
# objs = Card("nurbekjon", "majidov", "+998939255504", 23456543245, "dekabr", "2mln", 12324)
# print(objs.last_name)

# class Shaxs:
#     def __init__(self, ism, yosh, idcard):
#         self.ism = ism
#         self.yosh = yosh
#         self.__idcard = idcard
#
# shaxss=Shaxs("bunyod",16,"AA23484")
# print(shaxss.ism)