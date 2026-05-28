class Calculator:
    def __init__(self, n):
        self.n = n

    def squre(self):
        print(f"The squre is : {self.n*self.n}")

    def cube(self):
        print(f"The Cube is : {self.n*self.n*self.n}")

    def squreroot(self):
        print(f"The squre squre root is : {self.n** 0.5}")


a = Calculator(4)
a.squre()
a.cube()
a.squreroot()

