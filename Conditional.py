#>90, "A",>80,"B">70,"C", >60,"D", <=60,"F"
mark= int(input("Please enter Grade"))
if mark>90:
    grade="A"
elif mark>80:
    grade="B"
elif mark>70:
    grade="C"
elif mark>60:
    grade="D"
else:
    grade="F"

print (grade)
