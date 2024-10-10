class A:
    def __init__(self, name, cycle):
        self.name = name
        self.cycle = cycle

    def info(self):
        return self.name, self.cycle


class B(A):
    def __init__(self, name, cycle, colour):
        super().__init__(name, cycle)
        self.colour = colour

    def info(self):
        return self.name,self.cycle,self.colour

object = B("triangle","uchta burchak","blue")
print(*object.info())