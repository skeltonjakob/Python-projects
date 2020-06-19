def pretty_print(to_print):
    for item in to_print:
        print("* " + str(item))

def pretty_print_ordered(to_print):
    for i in range(len(to_print)):
        print(str(i + 1) + ". " +str(to_print[i]))
def pretty_print_enu(to_print):
    for i, value in enumerate(to_print, 1):
        print(str(i) + ". " + str(value))

favorites = []
more_items = True

while more_items:
        user_input = input("Enter something you like: ")
        if user_input == '':
            more_items = False
        else:
            favorites.append(user_input)

print("Here are the the things you like!")
pretty_print_enu(favorites)
