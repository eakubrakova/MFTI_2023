date = '05.07.2018 20:15'
month = int(date.split('.')[1])
year = int(date.split('.')[2].split()[0])

if year > 2019 or (year == 2019 and month == 5):
    category = 1
elif year == 2019 and month in [1, 2, 3, 4]:
    category = 2
else:
    category = 3
    
print("CV belongs to category: ", category)
