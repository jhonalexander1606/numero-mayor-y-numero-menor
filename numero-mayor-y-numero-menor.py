# programa para identificar el numero mayor entre dos numeros 

print("-------------------------------------")
print("----numero mayor y numero menor------")
print("-------------------------------------")


#input

print("inserte un numero")
n1 = int(input("numero 1: " ))
n2 = int(input("numero 2: " ))

#processing
numero = n1 > n2

#output

if n1 == n2:
    print("los numeros son iguales")

elif numero == True:
    print("el numero" , n1, "es mayor que" , n2, )

else:
    print("el numero" , n1, "es mayor que" , n2, )
     