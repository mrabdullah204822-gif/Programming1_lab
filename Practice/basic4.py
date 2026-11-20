players=int(input("How Many players? ")):
for players in range(1,players+1):
    print("Players ",players)
    total=0
    for time in range(1,4):
        time=int(input("Enter time for round " + str(time) + " :"))
        total=total+time
    print("Total ",total)


