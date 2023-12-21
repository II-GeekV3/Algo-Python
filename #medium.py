#Meduim 
n = int( input("Entre un entier supérieur à 1:")) #par exemple 69 c'est bien 

fibo = [0]*(n)
fibo[0] = 0
fibo[1] = 1

for i in range(2,n):
    fibo[i] = fibo[i-1] + fibo[i-2]

print(fibo)