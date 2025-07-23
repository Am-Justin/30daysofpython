# Exemple des de chaque different type de données
a = 12; 
b = 1.2; 
c = [1,2,3]; 
d = {"test":"ok", "day":"first"}
e = True
f = ("one", "two", "three")
g = {1,2,3}
h = 1 + 4j
i = "hello world"

liste = [a, b, c, d, e, f, g, h, i]
for i, var in enumerate(liste):
    print(f"le type de {var} est {type(liste[i])}")

# Trouvez une distance euclidienne entre (2, 3) et (10, 8)
print(f"la division euclidienne de (2,3) est : Quotient = {2//3} et le reste = {2%3}")
print(f"la division euclidienne de (8,10) est : Quotient = {10//8} et le reste = {10%8}")

