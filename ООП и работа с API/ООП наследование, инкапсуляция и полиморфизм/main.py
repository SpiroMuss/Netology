def find_average(dictionary, key):
    average = []
    for i in dictionary[key]:
        average.append(i)
    return sum(average) / len(average)


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: '
                f'{find_average(self.grades, 'Python')}\nКурсы в процессе изучения: '
                f'{', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}')

    def __gt__(self, other):
        a1 = find_average(self.grades, 'Python')
        a2 = find_average(other.grades, 'Python')
        return a1 > a2

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {find_average(self.grades, 'Python')}'

    def __gt__(self, other):
        a1 = find_average(self.grades, 'Python')
        a2 = find_average(other.grades, 'Python')
        return a1 > a2


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

worst_student = Student('Some', 'Student', 'your_gender')
worst_student.courses_in_progress += ['Python', 'Git']
worst_student.finished_courses += ['Введение в программирование']

lecturer1 = Lecturer('Some', 'Lecturer')
lecturer1.courses_attached += ['Python']
lecturer2 = Lecturer('Another', 'Lecturer')
lecturer2.courses_attached += ['Python']

reviewer = Reviewer('Some', 'Reviewer')
reviewer.courses_attached += ['Python']

reviewer.rate_hw(best_student, 'Python', 9.9)
reviewer.rate_hw(worst_student, 'Python', 1)
best_student.rate_hw(lecturer1, 'Python', 9.9)
worst_student.rate_hw(lecturer2, 'Python', 7)

print(best_student, lecturer1, reviewer, best_student > worst_student, lecturer1 > lecturer2, sep='\n\n')
