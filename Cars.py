raw_car_data = [
    # make, model, (trims/submodels)
    ("mitsubishi", "lancer", ("es", "gsr", "mr", "gts", "gt")),
    ("honda", "civic", ("si", "lx", "ex", "dx", "exl", "ex-l", "lx-s"))
]


class Car:
    def __init__(self, make, model, trims):
        self.make = make
        self.model = model
        self.trims = trims


c = {}
cars = []

for i in range(len(raw_car_data)):
    c[i] = Car(raw_car_data[i][0], raw_car_data[i][1], (raw_car_data[i][2]))


for x in c.values():
    cars.append(x)

#TODO fix this whole system, i don't like it but it works
