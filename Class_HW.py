class Cars:
	def __init__(self, model, price, color, stock):
		self.model = model
		self.price = price
		self.color = color
		self.stock = stock

	def print_info(self):
		print("Car:", self.model + "\ncolor:", self.color, "\ncosts:", self.price, "\nНа стоке:", self.stock)


tesla = Cars("TESLA", 30000, "RED", 4)
nissan = Cars("NISSAN", 10000, "BLUE/WHITE", 3)
audi = Cars("AUDI", 20000, "BLACK", 2)
myCars = [tesla, nissan, audi]


class Salon:
	def buy(self):
		if self.stock == 0:
			return "No more cars on stock"
		else:
			self.stock -= 1
		return self.print_info()

for i in myCars:
	i.print_info()




def selectCar():
	while True:
		x = input("Choose a car: ")
		if x == "tesla".lower():
			res = myCars[0]
			return res
		elif x == "audi".lower():
			res = myCars[1]
			return res
		elif x == "nissan".lower():
			res = myCars[2]
			return res
		else:
			print("Try again")



Salon.buy(selectCar())
