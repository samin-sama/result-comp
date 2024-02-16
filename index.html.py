a = float(input("Math result=      "))
b = float(input("Bangla result=    "))
c = float(input("English result=   "))
d = float(input("Science result=   "))
e = float(input("HSS result=       "))
x = float(input("Number of subjects "))
y = a + b + c + d + e
z = float(input("Total marks in each subject="))
print("Percentage of marks in math=", float(a / z * 100), "%")
L = float(a / z * 100)
print("Percentage of marks in bangla=", float(b / z * 100), "%")
N = float(b / z * 100)
print("Percentage of marks in english=", float(c / z * 100), "%")
O = float(c / z * 100)
print("Percentage of marks in science=", float(d / z * 100), "%")
P = float(d / z * 100)
print("Percentage of marks in HSS=", float(e / z * 100), "%")
Q = float(e / z * 100)
t = float(input(("Total marks of exam =")))
print("Percentage=", float(y / t * 100), "%")
M = float(y / t * 100)
if (L or N or O or P or Q) <40:
    print("Grade- F")
else:
    if M in range(40, 49, 1):
        print("Grade-D")
    elif M in range(50, 59, 1):
        print("Grade-C")
    elif M in range(60, 69, 1):
        print("Grade-B")
    elif M in range(70, 79, 1):
        print("Grade-A")
    elif M in range(80,100, 1):
        print("Grade-A+")
