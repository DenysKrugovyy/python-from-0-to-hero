scope = int(input("Enter the scope: "))

if scope > 90:
    print("A")
elif 80 <= scope < 90:
    print("B")
elif 70 <= scope < 80:
    print("C")
elif 60 <= scope < 70:
    print("D")
elif scope < 60:
    print("F")
