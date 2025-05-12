temperature = int(input("Enter the temperature: "))

if temperature > 30:
    print("Too hot!")
elif temperature >= 15 and temperature <= 30:
    print("Nice weather!")
elif temperature < 15:
    print("Too cold!")
