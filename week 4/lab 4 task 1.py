score = float(input("Enter score: "))

while score < 0 or score > 100:
    score = float(input("Enter a score from 0 to 100: "))

if score >= 80:
    print("A")
elif score >= 60:
    print("B")
elif score >= 50:
    print("C")
else:
    print("Fail")
