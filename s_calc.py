#Sandrah Lewa 
#SCT211-0090/2022

name = input ("Enter your name: ")
print ("Welcome to my calculator", name)
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum = num1 + num2
print ("The sum of ", num1 ," and ", num2 ,"is ", num1+num2,name)

def calculate_age(year_of_birth):
    today= date.today()
    age= today.year - year_of_birth
    months = today.month - 1 if today.day < birth_date.day else today.month
    days = today.day if today.day < birth_date.day else today.day - 1
    return age,months,days
year_of_birth=int(input("Enter your year of birth: "))
age,months,days=calculate_age(year_of_birth)
print(f"You are {age} years, {months} months,and {days} days old")