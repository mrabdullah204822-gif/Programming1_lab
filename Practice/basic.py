all_total_marks=0
students=int(input("How many students: "))
for student in range(1,students+1):
    print("Student ",student)
    total_marks=0
    subject=int(input("How many subjects: "))
    for marks in range(1,subject+1):
        mark=int(input("subject " + str(marks) + " mark "))
        total_marks=total_marks+mark
        average=total_marks/marks
    print("Total marks: ",total_marks)
    print(average)
    all_total_marks=all_total_marks+total_marks
print("All students total marks: ",all_total_marks)