from Person import Person
from Student import Student
from Teacher import Teacher


def main():
    new_person = Person('John', 'San Francisco')    # Creating person for the Person class
    print(Person.getName(new_person))   # Get the new person's name
    print(Person.getAddress(new_person))    # Get the new person's address
    new_person.setAddress('Los Angeles')    # Set a new address for the new person
    print(new_person.toString())    # Prints out name and address of person with formant: 'name(address)'

    print("")

    new_student = Student('Alex', 'Jakarta')    # Creating a student for Student class
    # Add a few courses and the grades to the new student's lists
    new_student.addCourseGrade('Maths', 90)
    new_student.addCourseGrade('English', 80)
    new_student.addCourseGrade('Science', 90)
    new_student.addCourseGrade('Chinese', 80)
    new_student.printGrades()   # Prints out all the course with their grades
    print(new_student.getAverageGrade())    # Prints out the average grade for the new student
    print(new_student.toString())   # Prints out name and address of student with format: 'Student: name(address)'

    print("")

    new_teacher = Teacher('Mr. Jude', 'Address of Mr. Jude')
    print(new_teacher.addCourse('ITP'))     # Testing to see if it returns True as there is no ITP course added yet
    print(new_teacher.addCourse('ITP'))     # Testing to see if it returns False as there is already an ITP course
    print(new_teacher.removeCourse('ITP'))  # Testing to see if it returns True since ITP course exists
    print(new_teacher.removeCourse('ITP'))  # Testing to see if it returns False since ITP course no longer exists
    print(new_teacher.toString())   # Prints out name and address of teacher with format: 'Teacher: name(address)'


if __name__ == '__main__':
    main()
