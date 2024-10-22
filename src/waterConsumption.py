
print("Water Consumption")
print("-" * 20)

def waterConsumption(weight):
    maleCalculate = int(weight * 0.04)
    femaleCalculate = int(weight * 0.03)
    
    gender = input("Enter your gender(Female/Male): ").lower()
    
    if gender == "female":
        print("-" * 20)
        print("Your gender is:", gender)
        print(f"You should drink {femaleCalculate} liters of water.")
        print("-" * 20)
        
    elif gender == "male":
        print("-" * 20)
        print("Your gender is:", gender)
        print(f"You should drink {maleCalculate} liters of water.")
        print("-" * 20)
                          
getWeight = int(input("Enter your weight(kg): "))
waterConsumption(getWeight)