def compute_mongo_age(birthYear, birthMonth, birthDay, currentYear, currentMonth, currentDay):
    years = 390*(currentYear - birthYear)
    months = 26*(currentMonth - birthMonth)
    days = currentDay - birthDay
    ageInDays = years + months + days
    age = (float((ageInDays)/390))
    return (age)

print(compute_mongo_age(2879,8,11,2892,2,21)) 
