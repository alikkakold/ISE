from abc import ABC, abstractmethod


# абстрактный ученик Воитель
class AbstractStudent(ABC):
	def __init__(self):
		self.skills = []

	def add_skill(self, skill):
		self.skills.append(skill)

	@abstractmethod
	def rank(self) -> str:
		pass


# абастрактный наставник (builder)
class AbstractTeacher(ABC):
	def __init__(self, student: AbstractStudent):
		self.student = student

	@abstractmethod
	def add_first_skill(self):
		pass

	@abstractmethod
	def add_second_skill(self):
		pass


# абстрактная школа Воителей (director)
class AbstractSchool(ABC):
	def __init__(self, teacher: AbstractTeacher):
		self.teacher = teacher

	@abstractmethod
	def graduate(self, student: AbstractStudent):
		pass


# ___________________________________________
# страж
class Guardian(AbstractStudent):
	def rank(self) -> str:
		return f"Я новый страж. Мои умения: {', '.join(self.skills)}"


# конкретный наставник Стражей
class GuardianSchoolTeacher(AbstractTeacher):
	def add_first_skill(self):
		self.student.add_skill("Обоняние")

	def add_second_skill(self):
		self.student.add_skill("Зоркость")


# конкретная школа Стражей
class GuardianSchool(AbstractSchool):
	def graduate(self, student: AbstractStudent):
		self.teacher.add_first_skill()
		self.teacher.add_second_skill()


# ___________________________________________
# охотник
class Hunter(AbstractStudent):
	def rank(self) -> str:
		return f"Я новый охотник. Мои умения: {', '.join(self.skills)}"


# конкретный наставник Охотников
class HunterSchoolTeacher(AbstractTeacher):
	def add_first_skill(self):
		self.student.add_skill("Боевые умения")

	def add_second_skill(self):
		self.student.add_skill("Ловкость")


# конкретная школа Охотников
class HunterSchool(AbstractSchool):
	def graduate(self, student: AbstractStudent):
		self.teacher.add_first_skill()
		self.teacher.add_second_skill()


# тесты

# создадим ученика
guardian = Guardian()

# создадим наставника школы стражей
guardian_teacher = GuardianSchoolTeacher(guardian)

# создадим школу
guardian_school = GuardianSchool(guardian_teacher)

# выпустим из школы нового стража
guardian_school.graduate(guardian)
print(guardian.rank())

# --------------------

# создадим ученика
hunter = Hunter()

# создадим наставника школы стражей
hunter_teacher = HunterSchoolTeacher(hunter)

# создадим школу
hunter_school = HunterSchool(hunter_teacher)

# выпустим из школы нового стража
hunter_school.graduate(hunter)
print(hunter.rank())
