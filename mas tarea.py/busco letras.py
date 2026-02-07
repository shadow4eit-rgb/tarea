def buscar_caracter(frase, letra):
    contador = 0
    for char in frase.lower():
        if char == letra.lower():
            contador += 1
            
    if contador > 0:
        print(f"La letra '{letra}' aparece {contador} veces.")
    else:
        print(f"Error: La letra '{letra}' no se encuentra en la frase asi que prueba con otra.")

buscar_caracter("Python es dificil", "o")