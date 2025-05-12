temperature = int(input("Enter the temperature: "))

if temperature > 30:
    print("Too hot!")
elif 15 <= temperature <= 30:
    print("Nice weather!")
elif temperature < 15:
    print("Too cold!")
