
year = int(input("Enter year:-  "))

leap = " is a leap year"
non = " not a leap year"
if (year%4)== 0:
	if(year%100) == 0:
		if(year%400) == 0:
			print(year,leap)
		else:
			print(year,non)
	else:
		print(year,leap)
else:
	print(year,non)
