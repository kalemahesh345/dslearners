# 16/07/2025..............
year = int(input("Enter the year"))

if(year%4==0 ) and (year % 100!=0) or ( year % 400 == 0):
    print(year,"is a leap year")

else:
    print(year,"year is not leap")


# git add .
# git commit -m ""
# git push origin main