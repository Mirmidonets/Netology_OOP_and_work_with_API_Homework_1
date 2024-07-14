class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and (course in self.courses_in_progress or course in self.finished_courses)
                and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _get_avarage_grade(self):
        list_grades = []
        for each_cource in self.grades:
            list_grades += self.grades[each_cource]

        avg = sum(list_grades) / len(list_grades)
        return round(avg, 1)

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: '
                f'{self._get_avarage_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def __gt__(self, other_student):
        if isinstance(other_student, Student):
            return self._get_avarage_grade() > other_student._get_avarage_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _get_avarage_grade(self):
        list_grades = []
        for each_cource in self.grades:
            list_grades += self.grades[each_cource]

        avg = sum(list_grades) / len(list_grades)
        return round(avg, 1)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._get_avarage_grade()}'

    def __gt__(self, other_lecturer):
        if isinstance(other_lecturer, Lecturer):
            return self._get_avarage_grade() > other_lecturer._get_avarage_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and (course in student.courses_in_progress
                or course in student.finished_courses):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


student_1 = Student('Peter', 'Parker', 'male')
student_1.finished_courses += ['Python base', 'Git']
student_1.courses_in_progress += ['OOP and work with API']

student_2 = Student('Mary', 'Jane', 'female')
student_2.finished_courses += ['Python base']
student_2.courses_in_progress += ['Git']

lecturer_1 = Lecturer('Tony', 'Stark')
lecturer_1.courses_attached += ['Python base', 'Git']

lecturer_2 = Lecturer('Bruce', 'Banner')
lecturer_2.courses_attached += ['Git', 'OOP and work with API']

reviewer_1 = Reviewer('Wanda', 'Maximoff')
reviewer_1.courses_attached += ['Python base', 'Git']
reviewer_1.rate_hw(student_1, 'Python base', 10)
reviewer_1.rate_hw(student_1, 'Python base', 9)
reviewer_1.rate_hw(student_1, 'Python base', 10)
reviewer_1.rate_hw(student_1, 'Git', 10)
reviewer_1.rate_hw(student_1, 'Git', 10)
reviewer_1.rate_hw(student_2, 'Python base', 9)
reviewer_1.rate_hw(student_2, 'Python base', 8)
reviewer_1.rate_hw(student_2, 'Python base', 7)
reviewer_1.rate_hw(student_2, 'Git', 9)
reviewer_1.rate_hw(student_2, 'Git', 8)

reviewer_2 = Reviewer('Steve', 'Rogers')
reviewer_2.courses_attached += ['Git', 'OOP and work with API']
reviewer_2.rate_hw(student_1, 'Git', 10)
reviewer_2.rate_hw(student_1, 'Git', 9)
reviewer_2.rate_hw(student_1, 'OOP and work with API', 9)
reviewer_2.rate_hw(student_1, 'OOP and work with API', 10)
reviewer_2.rate_hw(student_2, 'Git', 9)
reviewer_2.rate_hw(student_2, 'Git', 9)
reviewer_2.rate_hw(student_2, 'OOP and work with API', 9)
reviewer_2.rate_hw(student_2, 'OOP and work with API', 7)

student_1.rate_lecturer(lecturer_1, 'Python base', 8)
student_1.rate_lecturer(lecturer_1, 'Git', 9)
student_1.rate_lecturer(lecturer_2, 'Git', 10)
student_1.rate_lecturer(lecturer_2, 'OOP and work with API', 9)

student_2.rate_lecturer(lecturer_1, 'Python base', 10)
student_2.rate_lecturer(lecturer_1, 'Git', 10)
student_2.rate_lecturer(lecturer_2, 'Git', 9)
student_2.rate_lecturer(lecturer_2, 'OOP and work with API', 10)

print(student_1, end='\n \n')
print(student_2, end='\n \n')
print(lecturer_1, end='\n \n')
print(lecturer_2, end='\n \n')
print(reviewer_1, end='\n \n')
print(reviewer_2, end='\n \n')

print(student_1 > student_2)
print(lecturer_1 > lecturer_2)
print('')

list_students = [student_1, student_2]
list_lecturers = [lecturer_1, lecturer_2]


def avg_hw_all_students(students_list, course):
    list_grades = []
    for student in students_list:
        if course in student.grades:
            list_grades.extend(student.grades[course])

    return round(sum(list_grades) / len(list_grades), 1)


def avg_hw_all_lecturers(lecturers_list, course):
    list_grades = []
    for lecture in lecturers_list:
        if course in lecture.grades:
            list_grades.extend(lecture.grades[course])

    return round(sum(list_grades) / len(list_grades), 1)


print(f'Средняя оценка за домашние задания по всем студентам в рамках курса "Python base": '
      f'{avg_hw_all_students(list_students, "Python base")}')

print(f'Средняя оценка за лекции всех лекторов в рамках курса "Git": '
      f'{avg_hw_all_lecturers(list_lecturers, "Git")}')

print(f'Средняя оценка за лекции всех лекторов в рамках курса "OOP and work with API": '
      f'{avg_hw_all_lecturers(list_lecturers, "OOP and work with API")}')
