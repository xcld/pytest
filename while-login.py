i=0
while i<3:
    user = raw_input("user:")
    pwd = raw_input("password:")
    if user=="charles" and pwd=="hyflwj":
        print("pass")
        break
    else:
        print("please try again!")
        i+=1