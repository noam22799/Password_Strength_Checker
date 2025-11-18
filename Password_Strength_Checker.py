#Checks password length
def length_password(password):
    length=len(password)
    if length < 8:
        return 0
    elif length < 11:
        return 1
    return 2

#checks password complexity
def complexity_password(password):
    conditions={"small_let":False,"big_let":False,"number":False,"special":False}
    for tav in password:
        if tav >= 'a' and tav <= 'z':
            conditions["small_let"]=True
        elif tav >= 'A' and tav <= 'Z':
            conditions["big_let"]=True
        elif tav >= '0' and tav <= '9':
            conditions["number"]=True
        else:
            conditions["special"]=True
    summ=[1 for val in conditions.values() if val]
    return sum(summ)

#Checks for common password words
def Common_words(password):
    if "123456" in password or "admin" in password:
        return -2
    return 0

#Calculates the final score and returns how strong the password is
def Final_rank(password):
    summ=0
    summ+=length_password(password)
    summ+=complexity_password(password)
    summ+=Common_words(password)
    if summ <= 0:
        print("Weak password")
    elif summ <= 3:
        print("Medium password")
    else:
        print("Strong password")

if __name__=="__main__":
    password=input("write your password")
    Final_rank(password)


            