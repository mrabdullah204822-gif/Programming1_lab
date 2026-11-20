students={}
name=input("Student name: ")
while name!="done":
    mark=int(input("Student mark: "))
    name = input("Student name: ")
    students[name]=mark
total=0

for student in students:
    print(student, students[student])
    total=total+students[student]
print (total)


