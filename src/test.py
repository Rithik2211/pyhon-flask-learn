class Fruits:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def myfunc(self):
        print("My name is " + self.name)

class Children(Fruits):
    def __init__(self, name, color):
        super().__init__(name, color)

a = Children("apple","red")
a.myfunc()
