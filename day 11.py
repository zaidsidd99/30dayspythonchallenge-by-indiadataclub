
# from datetime import date , datetime

# today= date.today()
# print ("today is:", today)
# print ("day:",today.day)
# print("month:",today.month)
# print("year:",today.year)

# print (today.strftime("%a,%dth,of,%b,%y"))
# print(today.strftime("%A,%dTH,of,%B,%Y"))



# now = datetime.now()
# print (now)

# zaidbirth= datetime.fromisoformat("2002-12-21 01:23:40:000+04:00")
# print ("zaid birth daytime:",zaidbirth)




# Calculate the days between two dates ?

from datetime import date

# Define two dates directly
date1 = date(2002, 12, 21)   # YYYY, MM, DD
date2 = date(2025, 7, 17)

# Calculate the difference
difference = abs((date2 - date1).days)

print("Number of days between the two dates:", difference)

