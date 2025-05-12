speed = int(input("Enter the speed: "))

if speed > 130:
    print("Too fast!")
elif 100 <= speed <= 130:
    print("Fast")
elif 60 <= speed < 100:
    print("Normal")
elif 30 <= speed < 60:
    print("Slow")
elif speed < 30:
    print("Too slow")
