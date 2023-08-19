# Figure out where someone should go to school by age

age = eval(input("Enter your age: "))

if age == 5:
    print("You belong in Kindergarten.")
elif (age >= 6) and (age <=17):
    grade = str(age - 5)
    print("You should be in grade " + grade + ".")
elif age > 17:
    print("You should be in college.")
else:
    print("I don'd know where you belong.")
