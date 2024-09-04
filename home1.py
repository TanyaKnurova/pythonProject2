class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    # Выставление оценок лекторам (Задача № 2)
    def rate_lec(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress and
                course in lecturer.courses_attached):
            if course in lecturer.grades_for_lecturer:
                lecturer.grades_for_lecturer[course] += [grade]
            else:
                lecturer.grades_for_lecturer[course] = [grade]
        else:
            return 'Ошибка'

    # Перезагрузка __str__ (Задача № 3)
    def __str__(self):
        grades_count = 0
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        for i in self.grades:
            grades_count += len(self.grades[i])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        result = f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за домашние задания: {self.average_rating:.1f} \n' \
               f'Курсы в процессе изучения: {courses_in_progress_str} \n' \
               f'Завершенные курсы: {finished_courses_str} \n'
        return result

    # Сравнение студентов по средней оценке за ДЗ (Задача № 3)
    def __lt__(self, other):
        if not isinstance(other, Student):
          print('Некорректное сравнение')
        return self.average_rating < other.average_rating


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached and
                course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Создание класса Reviewer (Задача № 1)
class Reviewer(Mentor):

    # Выставление студентам оценок за ДЗ (Задача № 2)
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached and
                course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

        super().rate_hw(student, course, grade)

    #  Перезагрузка __str__ (Задача № 3)
    def __str__(self):
        return f'Имя: {self.name}' \
               f'Фамилия: {self.surname}'


# Создание класса Lecturer (Задача № 1)
class Lecturer(Mentor):

    def __init__(self, name, surname):
        self.grades_for_lecturer = {}
        self.average_rating = float()
        super().__init__(name,surname)

    #  Перезагрузка __str__ (Задача № 3)
    def __str__(self):
        grades_count = 0
        for i in self.grades_for_lecturer:
            grades_count += len(self.grades_for_lecturer[i])
        self.average_rating = (sum(map(sum, self.grades_for_lecturer.values())) /
                               grades_count)
        result = f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за лекции: {self.average_rating:.1f}'
        return result

    # Сравнение лекторов по средней оценке за лекции (Задача № 3)
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
          print('Некорректное сравнение')
        return self.average_rating < other.average_rating

# Создание экземпляров класса Lecturer и закрепление их за курсом (Задача № 4)
lecturer_1 = Lecturer('Михаил', 'Смирнов')
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer('Александр', 'Петров')
lecturer_2.courses_attached += ['Git']

# Создание экземпляров класса Reviewer и закрепление их за курсом (Задача № 4)
reviewer_1 = Reviewer('Иван', 'Иванов')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']
reviewer_2 = Reviewer('Андрей', 'Сидоров')
reviewer_2.courses_attached += ['Git']
reviewer_2.courses_attached += ['Pyton']

# Создание экземпляров класса Student и определение для них изучаемых и
# завершенных курсов (Задача № 4)
student_1 = Student('Татьяна', 'Кнурова', 'женский')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Java']
student_2 = Student('Алексей', 'Белов', 'мужской')
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Java']

# Выставление оценок
student_1.rate_lec(lecturer_1, 'Python', 10)
student_1.rate_lec(lecturer_1, 'Python', 9)
student_1.rate_lec(lecturer_1, 'Python', 10)
student_1.rate_lec(lecturer_2, 'Python', 5)
student_1.rate_lec(lecturer_2, 'Python', 7)
student_1.rate_lec(lecturer_2, 'Python', 8)
student_1.rate_lec(lecturer_1, 'Python', 9)
student_1.rate_lec(lecturer_1, 'Python', 8)
student_1.rate_lec(lecturer_1, 'Python', 10)
student_2.rate_lec(lecturer_2, 'Git', 10)
student_2.rate_lec(lecturer_2, 'Git', 8)
student_2.rate_lec(lecturer_2, 'Git', 6)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Git', 9)
reviewer_2.rate_hw(student_2, 'Git', 9)
reviewer_2.rate_hw(student_2, 'Git', 6)

# Вывод характеристик студентов
print(f'Студенты:\n{student_1}\n{student_2}')

# Вывод характеристик лекторов
print(f'Лекторы:\n{lecturer_1}\n{lecturer_2}')

# Вывод результата сравнения студентов по средним оценкам за ДЗ
print(f'Результат сравнения студентов по средней оценке за ДЗ): '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = '
      f'{student_1 < student_2}')

# Вывод результат сравнения лекторов по средним оценкам за лекции
print(f'Результат сравнения лекторов по средней оценке за лекции): '
      f'{lecturer_1.name} {lecturer_1.surname} < {lecturer_2.name} {lecturer_2.surname} ='
      f' {lecturer_1 < lecturer_2}')

# Создание списков студентов и лекторов
student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]

# Функция для подсчета средней оценки за ДЗ по всем студентам (Задача № 4)
def student_rating(student_list, course_name):
    sum_all = 0
    count_all = 0
    for stud in student_list:
       if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

# Функция для подсчета средней оценки за лекции всех лекторов (Задача № 4)
def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

# Вывод средней оценки для всех студентов
print(f"Средняя оценка за домашние задания для студентов курса {'Python'}: "
      f"{student_rating(student_list, 'Python'):.1f}")
# Вывод средней оценки для всех лекторов
print(f"Средняя оценка за лекции для лекторов в рамках курса {'Python'}: "
      f"{lecturer_rating(lecturer_list, 'Python'):.1f}")

