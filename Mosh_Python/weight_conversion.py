weight = input("Weight: ")
if weight.isdigit():
    is_Lbs = input("(L)bs or (K)g: ")
    if is_Lbs.lower() == "l":
        weight_kg = float(weight) / 2.20462
        print(f"weight in Kg is around: {round(weight_kg)} Kg")
    elif is_Lbs.lower() == "k":
        weight_lbs = float(weight) * 2.20462
        print(f"weight in Lbs is around: {round(weight_lbs)} Lbs")
    else:
        print("Please enter K or L to indicate the weight unit")
else:
    print("Please enter a valid weight in numbers")

