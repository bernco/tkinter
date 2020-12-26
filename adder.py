def add_guy(*args):
    total = 0
    for n in args:
        total += n
    print(total)

# add_guy(1,3,2,10,100)


# def calculate(n, **kwargs):
#     # print(kwargs)
#     # for (key,value) in kwargs.items():
#     #     print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     n /= kwargs["divide"]
#     print(n)
#
# calculate(2, add=1,multiply=5, divide=4)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("colour")

m_car = Car(make="toyota", colour="white")
print((m_car.color, m_car.make, m_car.model))