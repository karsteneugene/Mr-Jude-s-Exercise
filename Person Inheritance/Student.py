from Person import Person


class Student(Person):
    def __init__(self, name: str, address: str, numCourses: int = 0, courses: list = [], grades: list = []):
        super().__init__(name, address)
        self.numCourses = numCourses
        self.courses = courses
        self.grades = grades

    def addCourseGrade(self, course: str, grade: int):
        self.courses.append(course)
        self.grades.append(grade)
        self.numCourses += 1

    def printGrades(self):
        for i in range(0, len(self.courses)):
            print(f'{self.courses[i]}: {self.grades[i]}')

    def getAverageGrade(self):
        return sum(self.grades) / self.numCourses

    def toString(self):
        return f'Student: {super().toString()}'
