print("Por favor, ingresa tres números:")
n1 = float(input("Ingresa el primer número: "))
n2 = float(input("Ingresa el segundo número: "))
n3 = float(input("Ingresa el tercer número: "))
if n1 >= n2 and n1 >= n3:
    mayor = n1
    if n2 >= n3:
        medio = n2
        menor = n3
    else:
        medio = n3
        menor = n2
elif n2 >= n1 and n2 >= n3:
    mayor = n2
    if n1 >= n3:
        medio = n1
        menor = n3
    else:
        medio = n3
        menor = n1
else:
    mayor = n3
    if n1 >= n2:
        medio = n1
        menor = n2
    else:
        medio = n2
        menor = n1
print("\n--- Resultados ---")
print(f"los numeros ordenados de mayor a menor serian : {mayor}, {medio}, {menor}")