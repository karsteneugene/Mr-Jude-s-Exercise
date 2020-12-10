from Person import Person


class Teacher(Person):
    def __init__(self, name: str, address: str, numCourses: int = 0, courses: list = []):
        super().__init__(name, address)
        self.numCourses = numCourses
        self.courses = courses

    def addCourse(self, course: str):
        if course not in self.courses:
            self.courses.append(course)
            self.numCourses += 1
            return True
        else:
            return False

    def removeCourse(self, course: str):
        if course in self.courses:
            self.courses.remove(course)
            return True
        else:
            return False

    def toString(self):
        return f'Teacher: {super().toString()}'
