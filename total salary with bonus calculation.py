salary=int(input("enter value:"))
print("salary:",salary)
gender=str(input("enter M or F"))
if gender=="M":
    bonus=salary*(10/100)
    print("bonus:",bonus)
    print("total:",salary+bonus)
else:
    bonus=salary*(12/100)
    print("bonus:",bonus)
    print("total:",salary+bonus)
                  
