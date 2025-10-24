total_kg = 100  # Total weight of the present
country = input("Enter country (US or AU): ").strip().upper()

if country == "US":
    if total_kg < 50:
        cost = 50
    elif total_kg <= 100:
        cost = 25
    elif total_kg >= 150:
        cost = 5
    else:
        cost = 0  # free
    print(f"Shipping cost to US is ${cost}")

elif country == "AU":
    if total_kg <= 50:
        cost = 100
    else:
        cost = 0
    print(f"Shipping cost to AU is ${cost}")

else:
    print("Invalid country selected.")