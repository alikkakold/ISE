from collections.abc import Iterator, Iterable

# клсаа итератора переборщика

class CatIterator(Iterator):
	# инициализация класса
	def __init__(self, collection, reverse):
		self.collection = collection
		self.reverse = reverse
		# начальная позиц перебора при обычном порядке - 0
		# а при обратном - ласт эл-т
		self.position = 0 if reverse == False else -1

	# Метод __next __() должен вернуть следующий элемент в последовательности.
	def __next__(self):

		try:
			value = self.collection[self.position]
			self.position += -1 if self.reverse else 1
		except IndexError:
			raise StopIteration()

		return value

# класс коллекции
class CatCollection(Iterable):

	def __init__(self, collection):
		self.collection = collection

	# возрат объект инетарора данной кол-ции (в обычном порядке)
	def __iter__(self):
		return CatIterator(self.collection, False)

	# метод возр колл в обратный порядок
	def get_reverse_iterator(self):
		return CatIterator(self.collection, True)

collection = CatCollection(["охотник", "воитель", "страж"])
print("\n".join(collection))
print()
print("\n".join(collection.get_reverse_iterator()))
