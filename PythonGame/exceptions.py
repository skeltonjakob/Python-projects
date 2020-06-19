name = input("Enter your Name: ")
age = input("Please enter your age: ")
try:
    print("Hello {}! You were born in {}".format(name, 2020 - int(age)))
except ValueError:
    print('Unable to calcute the year you were born' \
                                                        +'"{}" is not a number'.format(age))
