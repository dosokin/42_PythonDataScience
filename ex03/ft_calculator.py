class calculator:

    def __init__(self, lst):
        """init calculator"""
        self.elements = lst

    def __add__(self, object) -> None:
        """addition"""
        self.elements = [x + object for x in self.elements]
        print(self.elements)

    def __mul__(self, object) -> None:
        """multiplication"""
        self.elements = [x * object for x in self.elements]
        print(self.elements)

    def __sub__(self, object) -> None:
        """substraction"""
        self.elements = [x - object for x in self.elements]
        print(self.elements)

    def __truediv__(self, object) -> None:
        """division"""
        if not object:
            print("Error: division by 0 invalid")
            return
        self.elements = [x / object for x in self.elements]
        print(self.elements)
