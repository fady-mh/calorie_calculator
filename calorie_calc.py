
class CalorieCalc:

    def calc_calorie(self, grams_of_food, calorie_per_gram): # method to calculate calories
        return grams_of_food * calorie_per_gram

    def macro_amount(self, grams_of_food, macro_per_gram):
        return grams_of_food * macro_per_gram

    def macros_calc(self, macro, calories_per_macro_gram):
        return macro * calories_per_macro_gram

    def calculation(self, cut_type):


        user_choice = input("Please input cut: ")
        for item in cut_type:

            if item.cut == user_choice:
                grams_of_food = float(input("Please input amount in grams: "))
                choice_calc = CalorieCalc()
                total_cal = choice_calc.calc_calorie(grams_of_food, float(item.calorie_per_meat_gram))
                total_protein = choice_calc.macro_amount(grams_of_food, float(item.protein))
                total_fats = choice_calc.macro_amount(grams_of_food, float(item.fats))
                total_carbs = choice_calc.macro_amount(grams_of_food, float(item.carbs))
                print(total_cal)
                print(total_protein)
                print(total_fats)
                print(total_carbs)
                break

        else:
            print("Cut not registered")

#    def calories_from(self):
#
#        macro_energy = {'protein': 4, 'fats': 9, 'carbs': 4}



#        #return macro * calories_per_macro


#item = CalorieCalc()
#item.calories_from()
