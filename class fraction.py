
class Fraction():
    def __init__(self, ss, mm):
        self.s = ss
        self.m = mm

    def sum(self, f1):
        result_s = self.s * f1.m + f1.s * self.m
        result_m = self.m * f1.m
        output = Fraction(result_s, result_m)

        return output

    def mul(self, f1):
        result_s = self.s * f1.s
        result_m = self.m * f1.m

        output = Fraction(result_s, result_m)
        return output

    def sub(self, f1):
        result_s = self.s * f1.m - f1.s * self.m
        result_m = self.m * f1.m
        output = Fraction(result_s, result_m)

        return output

    def div(self, other):
        result_s = self.s * other.m
        result_m = self.m * other.s
        output = Fraction(result_s, result_m)

        return output

    def fraction_to_number(self, other):
        number = self.s / self.m
        number1 = other.s / other.m
        output = Fraction(number, number1)

        return output

    def show(self):
        print(self.s, "/", self.m)


user_input1_s = int(input("sorat kasr aval ro vared kon: "))
user_input1_m = int(input("makhraj kasr aval ro vared kon: "))
user_input2_s = int(input("sorat kasr dovom ro vared kon: "))
user_input2_m = int(input("makhraj kasr dovom ro vared kon: "))


a = Fraction(user_input1_s, user_input1_m)
a.show()
b = Fraction(user_input2_s, user_input2_m)
b.show()

z = a.mul(b)
z.show()

y = a.sum(b)
y.show()

w = a.sub(b)
w.show()

d = a.div(b)
d.show()

f = a.fraction_to_number(b)
f.show()
