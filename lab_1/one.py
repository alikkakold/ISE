from abc import abstractmethod, ABC

# сщздаем абстрактный класс животного
class Animal(ABC):

	# первичные реализованные методы класса животного
	def move(self):
		print("Перемещение")

	def sleep(self):
		print("Сон")

	# абстрактный, пустой, по обязательный к переопределению метод
	@abstractmethod
	def discover(self):
		pass

	# доп методы, которые могут быть переопределены опционально
	def swimming(self):
		pass

	def hunt(self):
		pass

# основываясь на классе животины, создали кота
class Cat(Animal):
	# переопределили абст метод
	def discover(self):
		print("Обследование терры по-кошачьи")

	# переопр дополнительный метод
	def hunt(self):
		print("Охота по-кошачьи")

# тест
cat = Cat()
cat.sleep()
cat.hunt()
cat.discover()
