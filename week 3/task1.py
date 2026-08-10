c1=float(input("Enter Course1 final mark "))
c2=float(input("Enter Course2 final mark"))
c3=float(input("Enter Course3 final mark"))
c4=float(input("Enter Course4 final mark"))
print ("------Student Result------")
average=(c1+c2+c3+c4)/4

print ("Final Grade: ", average)
if (average>=85):
    print ("Grade: A")
    print ("Remark: Excellent")
elif (average>=75):
    print ("Grade: B")
    print ("Remark: Very Good")
elif (average>=65):
    print ("Grade: C")
    print ("Remark: Good")
elif (average>=50):
    print ("Grade: D")
    print ("Remark: slighty pass")
else :
    print ("Grade: F")
    print ("Remark: Fail")
print("-------------------------")
