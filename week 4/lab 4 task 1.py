while True:
    score = int(input("Enter score: "))

    if 0 <= score <= 100:
        break
    else:
        print ("Invalid score")

if score >= 80:
    print ("Grade: A")
elif score >= 60:
    print("Grade: B")
elif score >= 50:
    print ("Grade: C")
else:
    print ("Grade: Fail")
