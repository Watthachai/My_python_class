year = int(input("Enter Year : "))
if year <= 0:
    print("ERROR")
else:    
 if(year %4) == 0:
  if(year %100) == 0:
     if(year %400)== 0 :
         print("This year is leap year.")
     else:
         print("This year is not leap year.")
  else:
     print("This is leap year.")
 else:
    print("This is not leap year.")
