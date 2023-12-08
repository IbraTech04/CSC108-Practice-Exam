class A:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c__ = 3
        self.d__ = 4
        self.e__ = 5
        self.f__ = 6
        self.g__ = 7

    def method(self):
        print(self.a)
        print(self.b)
        print(self.c__)
        print(self.d__)
        print(self.e__)
        print(self.f__)
        print(self.g__)
        
        
class B:
    def __init__(self):
        self.a = 1
        self.b = 2

    def method(self):
        print(self.a)
        print(self.b)

a = B()
A.method(a)