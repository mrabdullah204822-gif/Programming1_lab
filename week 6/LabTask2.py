def print_results(students):
    for name in students:
        mark = students[name]

        if mark >= 60:
            print(name, mark, "Pass")
        else:
            print(name, mark, "Fail")


students = {
    "John": 65,
    "Mary": 82,
    "Ali": 55,
    "Sina": 90
}

print_results(students)