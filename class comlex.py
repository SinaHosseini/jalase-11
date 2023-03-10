class Complex():
    def __init__(self, real, image):
        self.real = real
        self.image = image

    def show(self):
        print(self.real, "+", self.image, "i")

    def sum(self, num):
        new_real = self.real + num.real
        new_image = self.image + num.image
        result = Complex(new_real, new_image)

        return result

    def sub(self, num):
        new_real = self.real - num.real
        new_image = self.image - num.image
        result = Complex(new_real, new_image)

        return result

    def mul(self, num):
        # (ac – bd) + (ad + bc)i
        new_real = self.real * num.real - self.image * num.image
        new_image = self.real * num.image + self.image * num.real
        result = Complex(new_real, new_image)

        return result


a = Complex(5, 8)
a.show()

b = Complex(3, 6)
b.show()

sum = a.sum(b)
sum.show()

sub = a.sub(b)
sub.show()

mul = a.mul(b)
mul.show()
