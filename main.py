class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_grade(self):
        list_grades = []
        for grades_per_course in self.grades.values():
            for grade in grades_per_course:
                list_grades.append(grade)
        if not list_grades:
            return 0
        return sum(list_grades) / len(list_grades)
        
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self) -> str:
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade()}\
                    \nКурсы в процессе изучения: {" ".join(self.courses_in_progress)}\nЗавершенные курсы: {" ".join(self.finished_courses)}'
    
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade() == other.average_grade()
    
    def __ne__(self, other):
        if isinstance(other, Student):
            return self.average_grade() != other.average_grade()
        
    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        
    def __le__(self, other):
        if isinstance(other, Student):  
            return self.average_grade() <= other.average_grade()    


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []       


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        list_grades = []
        for grades_per_course in self.grades.values():
            for grade in grades_per_course:
                list_grades.append(grade)
        if not list_grades:
            return 0
        return sum(list_grades) / len(list_grades)
    
    def __str__(self) -> str:
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{self.average_grade()}'
    
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade() == other.average_grade()
    
    def __ne__(self, other):
        if isinstance(other, Student):
            return self.average_grade() != other.average_grade()
        
    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        
    def __le__(self, other):
        if isinstance(other, Student):  
            return self.average_grade() <= other.average_grade()    


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

    def __str__(self) -> str:
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def student_average_course_grade(student_list, course):
    list_grades = []
    for student in student_list:
        if isinstance(student, Student) and course in student.courses_in_progress:
            list_grades.append(student.average_grade())
    if not list_grades:
        return 0
    return sum(list_grades) / len(list_grades)

def lecturer_average_course_grade(lecturer_list, course):
    list_grades = []
    for lecturer in lecturer_list:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            list_grades.append(lecturer.average_grade())
    if not list_grades:
        return 0
    return sum(list_grades) / len(list_grades)

student_first = Student('Ivan', 'Ivanov', 'Male')
student_first.courses_in_progress += ['Python']

student_second = Student('Petr', 'Petrov', 'Male')
student_second.courses_in_progress += ['Python', 'C++']

lecturer_first = Lecturer('Vasiliy', 'Vasiliev')
lecturer_first.courses_attached += ['C++']

lecturer_second = Lecturer('Michail', 'Michailov')
lecturer_second.courses_attached += ['Python']

reviewer_first = Reviewer('Vasiliy', 'Vasiliev')
reviewer_first.courses_attached += ['C++']

reviewer_second = Reviewer('Michail', 'Michailov')
reviewer_second.courses_attached += ['Python']

reviewer_first.rate_hw(student_second, 'C++', 4.5)
reviewer_second.rate_hw(student_first, 'Python', 4)
reviewer_second.rate_hw(student_second, 'Python', 2)

student_first.rate_lecturer(lecturer_second, 'Python', 5)
student_second.rate_lecturer(lecturer_second, 'Python', 3)
student_second.rate_lecturer(lecturer_first, 'C++', 4)
'''
print(student_first, student_second, lecturer_first, lecturer_second, reviewer_first, reviewer_second, sep='\n \n')
print(f'Средная оценка за домашние задания по курсу Python: {student_average_course_grade([student_first, student_second], "Python")}\
      \nСредная оценка за лекции по курсу Python: {lecturer_average_course_grade([lecturer_first, lecturer_second], "Python")}')
'''