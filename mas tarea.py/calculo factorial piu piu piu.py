def calcular_factorial():
    numero = -1
    while numero < 0:
        numero = int(input("Introduce un número positivo: "))
        if numero < 0:
            print("Error: El número debe ser positivo.")
    
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    
    print(f"El factorial de {numero} es {resultado}")

# calcular_factorial() # Descomentar para probar