class Temperature:
    def __init__(self, d):
        self.degree = d
    def ToCelsius(self):
        return (self.degree - 32) * 5 / 9
d1 = float(input("请输入华氏温度： "))
celsius = Temperature(d1)
print(celsius.ToCelsius())
