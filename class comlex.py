class Complex():
    def __init__(self, real, image):
        self.real = real
        self.image = image


    def show(self):
        print(self.real, "+", "i", self.image)

    def sum(self):
        pass

    def sub(self):
        pass

    


a =Complex(5, 8)
a.show()
