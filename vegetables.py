from calorie_calc import CalorieCalc
from chicken import Chicken
import csv

class Vegetables(CalorieCalc):

    def __init__(self, veggie, calories_per_gram):
        self.veggie = veggie
        self.calories_per_gram = calories_per_gram

    @classmethod
    def main(cls):
        vegetable_list = []
        with open('csv/veggies.csv', 'r') as veggiecsv:
            fieldnames=['veggie', 'calories_per_gram']
            veggies = csv.DictReader(veggiecsv, fieldnames=fieldnames)
            for veggie in veggies: #create objects from the csv
                veggie_kind = veggie['veggie']
                calories_per_gram = veggie['calories_per_gram']
                vegetables_kind = Vegetables(veggie=veggie_kind, calories_per_gram = calories_per_gram)
                vegetable_list.append(vegetables_kind)

            user_choice = input("Please input vegetable: ")
            for item in vegetable_list:
                if user_choice == item.veggie:
                    food_amount = float(input("Please input amount: "))
                    veggie_calc = CalorieCalc()
                    total_cals = veggie_calc.calc_calorie(food_amount, float(item.calories_per_gram))
                    print(total_cals)




