def validate_student(name, age, email):
    name = name.strip()
    age = age.strip()
    email = email.strip()

    if name == "":
        return False, "Name is required"

    if not name.isalpha():
        return False, "Name must contain only letters"

    if age == "":
        return False, "Age is required"

    if not age.isdecimal():
        return False, "Age must be a whole number"

    age = int(age)

    if age < 18 or age > 60:
        return False, "Age must be between 18 and 60"

    if email == "":
        return False, "Email is required"

    if "@" not in email:
        return False, "Email must contain @"

    return True, "Success"


students = [
    ("John", "18", "john@gmail.com"),
    ("Michael", "60", "michael@email.com"),
    ("John", "50", "john@email.com"),
    ("John", "45", "john@email.com"),
    ("John", "23", "john@email.com")
]

for name, age, email in students:
    result, message = validate_student(name, age, email)
    print(name, age, email, "->", result, message)