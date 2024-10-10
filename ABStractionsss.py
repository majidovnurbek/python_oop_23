from abc import ABC, abstractmethod
class hayotmakoni(ABC):
    @abstractmethod
    def joylash(self):
        pass

class uy(hayotmakoni):
    def joylash(self):
        print("uy joylashgan")


uyobj=uy()
uyobj.joylash()










