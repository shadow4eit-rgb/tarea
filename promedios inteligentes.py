
def procesar_calificaciones(Notas): 
    total = 0
    for Nota in Notas:
            total = total + Nota
    promedio = total / len (Notas)
        
    if promedio > 20:
        print("Aprovado mi rey")
    else:
        print("Desaprovado ,vuelva a estudiar")

mis_notas = [70, 80, 50, 90]
procesar_calificaciones(mis_notas)