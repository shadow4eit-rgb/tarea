# 🛒 Simulador de Cesta de Compra en Python
# Autor: Alejandro
# Fecha: Enero 2026
# Objetivo: Programa interactivo para gestionar una cesta de compras

def mostrar_menu():
    print("\n📋 MENÚ PRINCIPAL")
    print("1. ➕ AGREGAR un nuevo elemento")
    print("2. 🧺 MOSTRAR el contenido de la cesta")
    print("3. ❌ ELIMINAR un elemento")
    print("4. 💰 CALCULAR el total de la compra")
    print("5. 👋 RENUNCIAR (salir)")
    print("-" * 40)

def agregar_elemento(cesta):
    nombre = input("👉 Ingresa el nombre del producto: ").strip()
    try:
        precio = float(input("💵 Ingresa el precio del producto: "))
        cantidad = int(input("🔢 Ingresa la cantidad: "))
        cesta.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
        print(f"✅ {cantidad} x {nombre} agregado(s) a la cesta.")
    except ValueError:
        print("⚠️ Error: Ingresa valores numéricos válidos para precio y cantidad.")

def mostrar_cesta(cesta):
    if not cesta:
        print("🛒 Tu cesta está vacía.")
    else:
        print("\n🧺 Contenido de la cesta:")
        for i, item in enumerate(cesta, start=1):
            print(f"{i}. {item['cantidad']} x {item['nombre']} - {item['precio']} $ c/u")

def eliminar_elemento(cesta):
    mostrar_cesta(cesta)
    if cesta:
        try:
            indice = int(input("❌ Ingresa el número del producto a eliminar: "))
            if 1 <= indice <= len(cesta):
                eliminado = cesta.pop(indice - 1)
                print(f"🗑️ {eliminado['nombre']} eliminado de la cesta.")
            else:
                print("⚠️ Número inválido.")
        except ValueError:
            print("⚠️ Ingresa un número válido.")

def calcular_total(cesta):
    if not cesta:
        print("🛒 Tu cesta está vacía, total = 0 $.")
    else:
        total = sum(item['precio'] * item['cantidad'] for item in cesta)
        print(f"💰 El total de tu compra es: {total:.2f} $")

def simulador_cesta():
    cesta = []
    while True:
        mostrar_menu()
        opcion = input("👉 Elige una opción (1-5): ").strip()
        
        if opcion == "1":
            agregar_elemento(cesta)
        elif opcion == "2":
            mostrar_cesta(cesta)
        elif opcion == "3":
            eliminar_elemento(cesta)
        elif opcion == "4":
            calcular_total(cesta)
        elif opcion == "5":
            print("👋 Gracias por usar el simulador. ¡Hasta pronto!")
            break
        else:
            print("⚠️ Opción inválida, intenta de nuevo.")

# 🚀 Ejecutar el programa
if __name__ == "__main__":
    simulador_cesta()

