from abc import ABC, abstractmethod

# класс посетитель - Нарушитель
class Impostor:
	def visit(self):
		print("Посещаем лагерь...")

# класс лагерного объекта
class CampTerritory(ABC):
	# абстракт метод принятия посетителя
	@abstractmethod
	def accept(self, obj):
		pass

# класс ХТ в лагере
class HerbStorage(CampTerritory):
	# переопр класс принятия посетителя
	def accept(self, impostor: Impostor):
		impostor.visit()

im = Impostor()
hs = HerbStorage()
hs.accept(im)