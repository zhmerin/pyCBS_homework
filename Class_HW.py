class Cars:
	def __init__(self, model, price, color, stock):
		self.model = model
		self.price = price
		self.color = color
		self.stock = stock

	def __str__(self):
		stri = self.model + ' ' + self.price
		return stri


class Salon:
	def __init__(self, *args):
		self.cars = args

	def __str__(self):
		counter = 1
		strcar = ""
		print(f"Сейчас на стоке находятся такие машины:")
		for car in self.cars:
			strcar += f"{counter}. Модель: {car.model}\n цвет: {car.color}\n цена: {car.price}\n кол-во: {car.stock}" \
				f"\n------------\n"
			counter += 1
		return strcar

	def sale(self, model):
		for car in self.cars:
			if model.lower() == car.model.lower() and car.stock > 0:
				print("SOLD! " + car.model + '\n')
				car.stock -= 1
			elif model.lower() == car.model.lower() and car.stock == 0:
				print("Машины нет в наличии! Выбери другую")
				continue
			else:
				print("Нет такой машины!")


car1 = Cars("TESLA", 50000, "Red", 3)
car2 = Cars("BMW", 20000, "Grey", 2)
car3 = Cars("Lada", 530000, "Gold", 1)
myCars = [car1, car2, car3]

def buycar():
	while True:
		print(Salon(car1, car2, car3))
		x = input("Какую машину хочешь купить?: ")
		Salon(car1, car2, car3).sale(x)

buycar()
