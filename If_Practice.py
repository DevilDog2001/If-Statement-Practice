grade = int(input("Enter your Grade ranging from 0 - 100: "))
if grade < 25:
    print("F")
elif grade == 25 or grade < 45:
    print("E")
elif grade == 45 or grade < 50:
    print("D")
elif grade == 50 or grade < 60:
    print("C")
elif grade == 60 or grade < 80:
    print("B")
else:
    print("A")