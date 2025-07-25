#  1 & 2
age, height = 20, 50.10

# 3
cplx = 1 + 5j

# 4
base = int(input("Enter base: "))
height = int(input("Enter height:"))
print(f"The area of the triangle is {0.5*base*height}")

# 5
a = input("Enter side a:")
b = input("Enter side b:")
c = input("Enter side c:")

print(f"The perimeter of the triangle is {int(a)+int(b)+int(c)}")

# 6
length = int(input("Enter side lenght :"))
width = int(input("Enter side width :"))

print(f"l'aire est : {length + width}")
print(f"le perimetre est : {2 * (length + width)}")

# 7
raduis = int(input("Entrez le rayon du cercle :"))
print(f"l'aire du cercle est :{3.14*raduis *raduis}")

# 8
x = int(input("Entrez la valeur de x pour calculer la pente :"))
y = 2*x -2
print(f"la pente est : {y}")

# 9
y = int(input("Entrez la valeur y du premier point :"))
x = int(input("Entrez la valeur x du premier point :"))
m1 = (y*2-y*1)/(x*2-x*1)
print(f"la pente pour le premier point est {m1}")

y = int(input("Entrez la valeur y du second point :"))
x = int(input("Entrez la valeur x du second point :"))
m2 = (y*2-y*1)/(x*2-x*1)
print(f"la pente pour le second point est {m2}")

print(f"la division eucludienne du point point (2, 2) et le point (6,10) est que le quotient est {m1 // m2} et le reste est {m1 % m2}")

# 10
print(y==m1==m2)

# 11
x = int(input("Entrez une valeur de x :"))
y = x**2 + 6*x + 9
print(f"la valeur de y est : {y}")
if y == 0:
    print(f"la valeur de x pour lequel y == 0 est : {x}")

# 12
print(len("python") > len("dragon"))

# 13
print("on" in "python" and "dragon")

# 14
print("jargon" in "I hope this course is not full of jargon.")

# 15
print(("on" not in "dragon") and ("on" in "python"))

# 16
print( str(float(len("python"))))

# 17
number = int(input("Donner un nombre pour verifier s'il est pair :"))
print("Nombre paire ?", number % 2 == 0)

# 18
print((7//3)==int(2.7))

# 19
print(type('10')== type(10))

# 20
print(int(9.8)==10)

# 21
hours = int(input("Enter hours :"))
rate = float(input("enter rate per hours :"))
print(f"Your weeklu earning is :{hours*rate}")

# 22
years = int(input("Entrez votre année :"))
print(f"You have lived for {years * 31536000} seconds.")

# 23

for i in range(1,6):
    print(i, 1, i*1, i*2, i*4)