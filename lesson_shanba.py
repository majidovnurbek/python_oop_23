class Point:
    name="bunyod"

    @classmethod
    def change_name(cls,name):
        Point.name=name




Point.change_name("nurbek")
print(Point.name)

