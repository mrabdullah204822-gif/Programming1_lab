course1 = float(input("Course1 final mark: "))
course2 = float(input("Course2 final mark: "))
course3 = float(input("Course3 final mark: "))
course4 = float(input("Course4 final mark: "))

average = (course1 + course2 + course3 + course4) / 4

if course1 < 50 or course2 < 50 or course3 < 50 or course4 < 50:
    grade = "F"
    remark = "Fail"
elif average >= 85:
    grade = "A"
    remark = "Excellent"
elif average >= 75:
    grade = "B"
    remark = "Very Good"
elif average >= 65:
    grade = "C"
    remark = "Good"
else:
    grade = "D"
    remark = "Pass"

print("------ STUDENT RESULT ------")
print(f"Course1: {course1:.2f}")
print(f"Course2: {course2:.2f}")
print(f"Course3: {course3:.2f}")
print(f"Course4: {course4:.2f}")
print(f"Final Grade: {average:.2f}%")
print("Grade:", grade)
print("Remark:", remark)
print("----------------------------")