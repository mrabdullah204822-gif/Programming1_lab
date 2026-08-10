num = int(input("How many items to purches today"))
grand_total = 0
for i in range(num):
    item_name= input("Enter item name: ")
    price = float(input("Enter price: "))
    qty = int(input("Enter quantity"))
    total = price*qty
    grand_total=grand_total+ total
print ("Grand total: $", grand_total)

