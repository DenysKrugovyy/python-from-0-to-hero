temperature = float(input("Enter water temperature: "))

if temperature >= 100:
    print("Water is boiling")
elif 0 <= temperature < 100:
    print("Water is liquid")
elif temperature < 0:
    print("Water is frozen")
