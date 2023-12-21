# Fonction cubique
def f(x):
    return x**3 + 3

#Dérivé de la fonction cubique 
def df(x):
    return 3*x**2

a = 2.5 # On part d'un point aléatoire
# On applique la formule sur plusieurs itérations... Disons 10
for i in range(10):
    a = a - f(a)/df(a)
    print(a)