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
        return round(avg, 2)

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
        return round(avg, 2)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._get_avarage_grade()}'

    def __gt__(self, other_lecturer):
        if isinstance(other_lecturer, Lecturer):
            return self._get_avarage_grade() > other_lecturer._get_avarage_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

smart_lecturer = Lecturer('Tony', 'Stark')
smart_lecturer.courses_attached += ['Python']

genius_reviewer = Reviewer('Bruce', 'Banner')
genius_reviewer.courses_attached += ['Python']

genius_reviewer.rate_hw(best_student, 'Python', 10)
genius_reviewer.rate_hw(best_student, 'Python', 10)
genius_reviewer.rate_hw(best_student, 'Python', 10)

best_student.rate_lecturer(smart_lecturer, 'Python', 10)

print(best_student.grades, end='\n \n')
print(smart_lecturer.grades, end='\n \n')
print(best_student, end='\n \n')