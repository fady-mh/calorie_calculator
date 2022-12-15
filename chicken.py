from calorie_calc import CalorieCalc
import csv

class Chicken(CalorieCalc):

    #__init__ constructor to initialize all the
    def __init__(self, cut, calorie_per_meat_gram, protein, fats, carbs, calorie_per_gram):
        self.cut = cut
        self.calorie_per_meat_gram = calorie_per_meat_gram
        self.protein = protein
        self.fats = fats
        self.carbs = carbs
        self.calorie_per_gram = calorie_per_gram


    @classmethod
    def main(cls):
        chicken_cuts = []
        with open('macros.csv') as f:
            fieldnames = ['cut','calorie_per_meat_gram','protein','calorie_per_gram','fats','calorie_per_gram','carbs','calorie_per_gram']
            cuts = csv.DictReader(f, fieldnames = fieldnames)
            for cut in cuts:
                chicken_cut = cut['cut']
                calorie_per_meat_gram = cut['calorie_per_meat_gram']
                protein = cut['protein']
                calorie_per_gram = cut['calorie_per_gram']
                fat = cut['fats']
                carbs = cut['carbs']
                chicken = Chicken(cut = chicken_cut, calorie_per_meat_gram = calorie_per_meat_gram, protein = protein, fats = fat, carbs = carbs, calorie_per_gram = calorie_per_gram)
                chicken_cuts.append(chicken)



#    user_choice = input("Please input cut: ")

#    for item in chicken_cuts:
#        if item.cut == user_choice:
#            grams_of_food = float(input("Please input amount in grams: "))
#            choice_calc = CalorieCalc()
#            total_cal = choice_calc.calc_calorie(grams_of_food, float(item.calorie_per_meat_gram))
#            total_protein = choice_calc.macro_amount(grams_of_food, float(item.protein))
#            total_fats = choice_calc.macro_amount(grams_of_food, float(item.fats))
#            total_carbs = choice_calc.macro_amount(grams_of_food, float(item.carbs))
#            print(total_cal)
#            print(total_protein)
#            print(total_fats)
#            print(total_carbs)

#        else:
#            print("Cut not registered")

        choice_calc = CalorieCalc()
        choice_calc.calculation(chicken_cuts)







