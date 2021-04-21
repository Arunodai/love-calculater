year = int(input("which year you want to check its leap year  "))


#here is the logic
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("its leap year")
        else:
            print("its not leap year")
    else:
        print("its leap year")
    
    
else:
    print("not leap year")

    
    
