birth_year = input('Enter your birth year: ')
age = 2019- int(birth_year)

if age <= 10:
	print(f'Your are {age},So you are children')
elif age >= 12 and age <= 18:
	print(f'You are {age}, You are teenage.')
elif age >= 18 and age <= 27:
	print(f'You are {age},So you are young man')
elif age >= 30 and age <= 50:
	print(f'You are {age}, So you are gentleman')
elif age >= 50 and age <= 70:
	print(f'You are {age}, So you are almost gone')
else:
	print(f'You are {age},dead! man')