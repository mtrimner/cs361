from api import foodSearch
import inquirer
import asyncio
import math

def main():
    print("")
    print("Hello! Welcome to NutritionFinder!")
    print("")
    print("To use the app, simply enter the name of a food below and hit ENTER. Then, select whether you want a branded food (ex: restaurant items, Tyson Chicken, Kemps milk, etc...), or a generic food (ex: chicken, milk, etc...).")
    print("")
    print("Then select from a menu of food options to get the carbs, fat, protein, and calories of that food.")
    print("")
    prompting = True
    nutrientMap = {
        'calories': '208',
        'fat': '204',
        'protein': '203',
        'carbs': '205',
        # 'sugar': '269' 
    }
    while prompting:
        foodQuestion = [
            inquirer.Text("food", message="Please enter a food"),
            inquirer.List("type", message = "Is this a generic food? Or a branded food? (navigate with arrow keys)", choices=[("Generic", "common"), ("Branded", "branded")])
        ]
        foodAnswers = inquirer.prompt(foodQuestion)
        response = foodSearch(foodAnswers["food"])
        # print(response)
        
        continueSearch = [inquirer.Confirm("continue", message=f"Would you like to search for {foodAnswers['food']}? (y = yes | n = try again)")]
        continueAnswer = inquirer.prompt(continueSearch)
        if not continueAnswer["continue"]:
            continue
        # else:
            # print("See you next time!")
            # print("")
            # break

        # SWITCH THIS AROUND. IF <= 0 RESTART THE LOOP. ALSO, ADD A LOOP.
        if len(response[foodAnswers["type"]]) >= 8:
            listLength = 8
        else:
            listLength = len(response[foodAnswers["type"]])
        if len(response[foodAnswers["type"]]) > 0:
            foodList = []
            for i in range(listLength):
                foodList.append(response[foodAnswers["type"]][i]["food_name"])
            
            foodChoices = [inquirer.List("selected", message="Select a food (navigate with arrow keys).", choices=foodList)]
            foodSelect = inquirer.prompt(foodChoices)
        else:
            print("Sorry! No foods were found with that name")
            continueSearch = [inquirer.Confirm("continue", message="Would you like to try again")]
            continueAnswer = inquirer.prompt(continueSearch)
            if continueAnswer["continue"]:
                continue
            else:
                print("See you next time!")
                print("")
                break
        
        nutrientList = response[foodAnswers["type"]][foodList.index(foodSelect["selected"])]["full_nutrients"]
        print(f"{foodSelect['selected']} has the following nutrition info per serving:")
        for key, value in nutrientMap.items():
            for i in nutrientList:
                # print(f"{i['attr_id']}, {value}")
                if i["attr_id"] == int(value):
                    print(f"{key}: {math.trunc(i['value'])}")
        print("")

        continueSearch = [inquirer.Confirm("continue", message="Would you to search for another food?")]
        continueAnswer = inquirer.prompt(continueSearch)
        if continueAnswer["continue"]:
            continue
        else:
            print("See you next time!")
            print("")
            break


if __name__ == '__main__':
    main()