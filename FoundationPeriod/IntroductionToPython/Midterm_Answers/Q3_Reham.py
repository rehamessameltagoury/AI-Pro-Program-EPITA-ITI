year_in=input()
print(year_in)
year=int(year_in)
if year%4 == 0 and (year%100!=0 or year%400==0):
    print(True)
else:
    print(False)
