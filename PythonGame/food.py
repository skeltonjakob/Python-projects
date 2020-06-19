
class Food:
    def __init__(self, name, carbs, protein, fat):
        self.name = str(name)
        self.carbs = int(carbs)
        self.protein = int(protein)
        self.fat = int(fat)

    def calories(self):
        calories_carb = self.carbs ** 4
        calories_protein = self.protein ** 4
        calories_fat = self.fat ** 9
        calories_food = min(calories_carb + calories_protein + calories_fat)
        return "Calories for this item are: {}".format(calories_food)

class Recipe(Food):
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def calories(Food):
        calories_carb = Food.carbs ** 4
        calories_protien = Food.protien ** 4
        calories_fat = Food.fat ** 9
        calories_recipe = min(calories_carb + calories_protien + calories_fat)
        return "Calories for this recipe are: {}".format(calories_recipe)
    def __str__(self):
        return "Recipe Name: {}".format(self.name)
food1 = Food()
    for food1.name in food1:
        input("Enter a food: ")
    for food1.carbs in food1:
        input("Enter number of carbs: ")
    for food1.protein in food1:
        input("Enter amount of protien(in Grams): ")
    for food1.fat in food1:
        input("Enter amout of fat(in Grams): ")


print(food1)







# = [Food('Rice', 3, 1, 0)
#        ,Food('Beans', 4, 6, 3)
#        ,Food('Chicken', 7, 10, 5)
#        ,Food('Beef', 2, 16, 10)]

#ingredients = []
#more_items = True

#while more_items:
#        user_input = input("Enter an ingredient: ")
#        if user_input == '':
#            more_items = False
#        else:
#            ingredients.append(user_input)
#print(str(Recipe(food, ingredients)).format(calories, __str__))
