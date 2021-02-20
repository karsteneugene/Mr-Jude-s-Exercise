total_class1 = int(input("Input the number of students for the FIRST class: "))
divisions_class1 = int(input("Input the desired number of groups for the FIRST class: "))

total_class2 = int(input("Input the number of students for the SECOND class: "))
divisions_class2 = int(input("Input the desired number of groups for the SECOND class: "))

total_class3 = int(input("Input the number of students for the THIRD class: "))
divisions_class3 = int(input("Input the desired number of groups for the THIRD class: "))

students_per_group1, leftover1 = divmod(total_class1, divisions_class1)
students_per_group2, leftover2 = divmod(total_class2, divisions_class2)
students_per_group3, leftover3 = divmod(total_class3, divisions_class3)

print("Number of students in each group:")
print("Class 1:", students_per_group1)
print("Class 2:", students_per_group2)
print("Class 3:", students_per_group3)
print("")
print("Number of students leftover:")
print("Class 1:", leftover1)
print("Class 2:", leftover2)
print("Class 3:", leftover3)
