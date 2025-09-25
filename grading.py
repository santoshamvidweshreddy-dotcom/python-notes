marks = int(input("enter marks:"))

if marks>90:
    Grade = "A"
elif marks>80:
    Grade = "B"
elif marks>70:
    Grade = "C"
elif marks>60:
    Grade = "D"
else:
    Grade = "F"

print("grade: ",Grade)