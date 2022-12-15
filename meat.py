from calorie_calc import CalorieCalc
import csv


class Meat(CalorieCalc):

    def __init__(self, cut, calorie_per_meat_gram, protein, fats, carbs, calorie_per_gram):
        self.cut = cut
        self.calorie_per_meat_gram = calorie_per_meat_gram
        self.protein = protein
        self.fats = fats
        self.carbs = carbs
        self.calorie_per_gram = calorie_per_gram

    @classmethod
    def main(cls):
        meat_cuts = []
        with open('meat_macros.csv', 'r') as meatcsv:
            fieldnames = ['cut','calorie_per_meat_gram','protein','calorie_per_gram','fats','calorie_per_gram','carbs','calorie_per_gram']
            meat_cuts_dict = csv.DictReader(meatcsv, fieldnames=fieldnames)
            for cut in meat_cuts_dict:
                meat_cut = cut['cut']
                calorie_per_meat_gram = cut['calorie_per_meat_gram']
                protein = cut['protein']
                fats = cut['fats']
                carbs = cut['carbs']
                calorie_per_gram = cut['calorie_per_gram']
                meat = Meat(cut = meat_cut, calorie_per_meat_gram=calorie_per_meat_gram, protein = protein, fats=fats,carbs=carbs, calorie_per_gram =calorie_per_gram)
                meat_cuts.append(meat)

            choice_calc = CalorieCalc()
            choice_calc.calculation(meat_cuts)





