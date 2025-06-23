# Zane Ketcham
# Module 2 Lab
# This app determines if a student made the dean's list or honor roll. 

last_name = ''
first_name = ''
gpa = 0
while (last_name != 'ZZZ'):
    last_name = (input("Enter last name (ZZZ to quit): ")).upper()
    if (last_name != 'ZZZ'):
        first_name = input("Enter first name: ")
        gpa = float(input("Enter GPA: "))
        if (gpa >= 3.5):
            print(f'{first_name} {last_name} made the dean\'s list with a GPA of {gpa}.')
        elif (gpa >= 3.25):
            print(f'{first_name} {last_name} made honor roll with a GPA of {gpa}.')
        else:
            print(f'{first_name} {last_name} did not make the dean\'s list or honor roll with a GPA of {gpa}.')

