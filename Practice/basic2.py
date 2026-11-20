secret_number=10
guess=0
while guess != secret_number:
    guess=int(input("Gurss: "))
    if guess<secret_number:
        print("Too low")
    elif guess>secret_number:
        print("Too high")
    else:
        print("Correct")