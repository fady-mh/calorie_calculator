from calorie_calc import CalorieCalc
import csv

class Fish(CalorieCalc):
    #Constructor to instantiate objects
    def __init__(self, cut, calorie_per_meat_gram, protein, fats, carbs, calorie_per_gram):
        self.cut = cut
        self.calorie_per_meat_gram = calorie_per_meat_gram
        self.protein = protein
        self.fats = fats
        self.carbs = carbs
        self.calorie_per_gram = calorie_per_gram

    @classmethod
    def main(cls):
        fish_kinds = []
        with open('csv/fish.csv', 'r') as fishcsv:
            fieldnames = ['cut','calorie_per_meat_gram','protein','calorie_per_gram','fats','calorie_per_gram','carbs','calorie_per_gram']
            fish_csv = csv.DictReader(fishcsv, fieldnames=fieldnames)
            for cut in fish_csv:
                fish_cut = cut['cut']
                fish_calorie = cut['calorie_per_meat_gram']
                fish_protein = cut['protein']
                fish_fats = cut['fats']
                fish_carbs = cut['carbs']
                fish_calorie_per_gram = ['calorie_per_gram']
                # assigning objects to a list
                fish_cuts_objects = Fish(cut = fish_cut, calorie_per_meat_gram=fish_calorie, protein=fish_protein, fats=fish_fats,
                              carbs = fish_carbs, calorie_per_gram=fish_calorie_per_gram )
                fish_kinds.append(fish_cuts_objects)

            user_choice = input("Please input Fish: ")
            for item in fish_kinds:
                if item.cut == user_choice:
                    carb_amount = float(input("Please input amount: "))
                    # instance of calorie_calc
                    fish_calc = CalorieCalc()
                    total_cal = fish_calc.calc_calorie(carb_amount, float(item.calorie_per_meat_gram))
                    print(total_cal)
                    break
            else:
                print("Fish type does not exist")
