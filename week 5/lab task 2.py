user_info={}
while True:
    name=input("Enter a name: ")
    if name=="Stop":
        break
    phone=input("Enter phone number: ")
    user_info[name]=phone
print (user_info)
