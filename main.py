from calorie_calc import CalorieCalc
from chicken import Chicken
from meat import Meat
from fish import Fish
from carbs import Carbs
from vegetables import Vegetables

#class Menu(Chicken, Meat, CalorieCalc):

#    def __init__(self, cut, calorie_per_meat_gram, protein, fats, carbs, calorie_per_gram):
#        super().__init__(cut, calorie_per_meat_gram, protein, fats, carbs, calorie_per_gram)


while True:

    print("Calorie Calculator Menu")
    choices = ['1- Chicken', '2- Meat', '3 -Fish','4- Carbs', '5- Vegetables', '0- Quit']
    for choice in choices:
        print(choice)

    user_choice = int(input("Please select from list: "))
    if user_choice == 0:
        break

    print("")

    totals=[]
    match user_choice:
        case 1:
            print("Chicken Calories: ")
            chicken_calc = Chicken.main()
        case 2:
            print("Meat Calories: ")
            Meat.main()
        case 3:
            print("Fish Calories ")
            Fish.main()
        case 4:
            print("Carbs Calories ")
            Carbs.main()
        case 5:
            print("Vegetables Calories: ")
            Vegetables.main()
        case 0:
            print("Program Terminated")

    print("")

    for total in totals:
        print(total)







#if __name__ == "__main__":
#    main()
