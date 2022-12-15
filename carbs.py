from calorie_calc import CalorieCalc
import csv

class Carbs(CalorieCalc):
    pass
    # constructor to instantiate objects

    def __init__(self, cut, calorie_per_carb_gram,protein , fats, carbs, calorie_per_gram):
        self.cut = cut
        self.calorie_per_carb_gram = calorie_per_carb_gram
        self.protein = protein
        self.fats = fats
        self.carbs = carbs
        self.calorie_per_gram = calorie_per_gram
    # create objects from csv and create def main()

    @classmethod
    def main(cls):
        carb_kinds = []
        with open('csv/carbs.csv', 'r') as carbscsv:
            fieldnames = ['cut','calorie_per_carb_gram','protein','calorie_per_gram','fats','calorie_per_gram','carbs','calorie_per_gram']
            carbs_csv = csv.DictReader(carbscsv, fieldnames=fieldnames)
            for cut in carbs_csv:
                carb_cut = cut['cut']
                carb_calorie = cut['calorie_per_carb_gram']
                carb_protein = cut['protein']
                carb_fats = cut['fats']
                carb_carbs = cut['carbs']
                carb_calorie_per_gram = ['calorie_per_gram']
                # assigning objects to a list
                carbs = Carbs(cut = carb_cut, calorie_per_carb_gram=carb_calorie, protein=carb_protein, fats=carb_fats,
                              carbs = carb_carbs, calorie_per_gram=carb_calorie_per_gram )
                carb_kinds.append(carbs)

            user_choice = input("Please input carb: ")
            for item in carb_kinds:
                if item.cut == user_choice:
                    carb_amount = float(input("Please input amount: "))
                    # instance of calorie_calc
                    carb_calc = CalorieCalc()
                    total_cal = carb_calc.calc_calorie(carb_amount, float(item.calorie_per_carb_gram))
                    print(total_cal)
                    break
            else:
                print("Carb does not exist")



