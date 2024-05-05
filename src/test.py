class Fruits:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def myfunc(self):
        print("My name is " + self.name)

a = Fruits("apple","red")
a.myfunc()
