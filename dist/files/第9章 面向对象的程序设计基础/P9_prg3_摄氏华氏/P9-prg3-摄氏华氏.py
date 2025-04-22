class TemperatureCelsius:
    def __init__(self, d):
        self.degree = d
    def ToFahrenheit(self):
        return (self.degree * 9 / 5) + 32
d = float(input("请输入摄氏温度： "))
celsius = TemperatureCelsius(d)
print(celsius.ToFahrenheit())
