import random

# ---------------------------
# prototipo #2 disfrute
# ---------------------------

estado = {
    "espada_1": False,        # primera espada recuperada
    "espada_2": False,        # segunda espada recuperada
    "hacha": True,            # si conservo mi hacha al inicio
    "elfo_vivo": True,        # si el elfo sigue con vida
    "elfo_companero": False,  # si el elfo acompaña
    "info_dragon": False,     # si sé dónde está el dragón a tiempo
    "nombre_rey": "Altair",   # mi nombre (puedes cambiarlo)
}

def narrar(texto):
    """Imprime la narrativa en primera persona con formato."""
    print("\n" + texto + "\n")

def pedir_decision(pregunta, opciones):
    """Pide una decisión hasta que el jugador ingrese una opción válida."""
    opciones_lower = [o.lower() for o in opciones]
    while True:
        decision = input(pregunta).strip().lower()
        if decision in opciones_lower:
            return decision
        else:
            print("⚠️ Opción inválida, intenta otra vez.")

# ---------------------------
# Finales especiales
# ---------------------------

def fin_del_juego():
    print("\n" + "="*50)
    print("🎮 Fin del juego. Si quieres intentarlo de nuevo, reinicia el programa.")
    print("="*50 + "\n")

def final_paliza_admin():
    narrar("Vago por el bosque durante días, sin encontrar salida. La desesperación me consume.")
    narrar("Finalmente regreso al castillo, sin espadas y lleno de rabia.")
    narrar("Encuentro a mi administrador y le doy una paliza por su irresponsabilidad. 👊😡")
    print("☠️ Final malo: No recuperaste las espadas, pero tu administrador aprendió la lección a golpes. 💀\n")
    fin_del_juego()

def final_elfo_gana_juego():
    estado["hacha"] = False
    narrar("El elfo sonríe con suficiencia. Con un gesto me quita el hacha de las manos.")
    narrar("Sin mi hacha y sin la espada, me quedo indefenso en el bosque. El elfo se aleja con una carcajada.")
    print("☠️ Final malo: Perdiste tu hacha. Te quedas sin armas y la aventura termina aquí. 💀\n")
    fin_del_juego()

# ---------------------------
# Minijuego: Piedra Papel Tijeras
# ---------------------------

def juego_piedra_papel_tijeras():
    opciones = ["piedra", "papel", "tijeras"]
    jugador = pedir_decision("Elige: PIEDRA, PAPEL o TIJERAS > ", opciones)
    elfo = random.choice(opciones)
    print(f"🧝‍♂️ Elfo elige: {elfo.upper()} — Tú eliges: {jugador.upper()}")

    if jugador == elfo:
        print("🤝 Empate. Vuelven a jugar.")
        return juego_piedra_papel_tijeras()

    gana_jugador = (
        (jugador == "piedra" and elfo == "tijeras") or
        (jugador == "tijeras" and elfo == "papel") or
        (jugador == "papel" and elfo == "piedra")
    )
    return gana_jugador

# ---------------------------
# Niveles y rutas
# ---------------------------

def nivel1():
    print("\n" + "="*90)
    narrar("LA AVENTURA DEL REY DE LAS ESPADAS ༼ つ ◕_◕ ༽つ  ()>>>>>>>>>>>>>>>>>|()|)))))))))))))))))))))))))))")
    narrar("Soy Altair, señor de estas tierras. Mi administrador perdió mis dos espadas en una noche de borrachera.")
    narrar("Llevo mi hacha y mi mapa. Me adentro en el bosque y, tras horas caminando, escucho que algo gigante se acerca...")
    decision1 = pedir_decision("¿Qué haré? Me Escondo, Lo Desafío o Huyo > ", ["escondo", "desafio", "huyo"])

    if decision1 == "escondo":
        nivel2_escondo()
    elif decision1 == "desafio":
        nivel2_desafio()
    else:
        nivel2_huyo()

# ---------------------------
# Nivel 2: Me escondo
# ---------------------------

def nivel2_escondo():
    narrar("Encuentro un tronco hueco y me acomodo con mis cosas. La cosa se acerca; la adrenalina me recorre.")
    decision2 = pedir_decision("¿Qué hago? INVESTIGO o ESPERO > ", ["investigo", "espero"])

    if decision2 == "espero":
        narrar("Espero en silencio. Tras un rato, eso se va. Salgo del escondite y ya no hay nada.")
        print("☠️ Final malo: Me pierdo en el bosque y quedo atrapado en una trampa mágica para siempre. 💫🔒\n")
        # En este final malo adicional, tras quedar atrapado, termino regresando y dándole una paliza al administrador
        final_paliza_admin()
    else:
        narrar("Asomo la cabeza: solo es un elfo alto con ojos como rubíes. En su cintura lleva una de mis espadas.")
        decision3 = pedir_decision("¿Lo Ataco por sorpresa o intento Dialogar? > ", ["ataco", "dialogar"])

        if decision3 == "ataco":
            narrar("Salto desde mi escondite para atacarlo por sorpresa, pero el elfo reacciona con rapidez.")
            print("☠️ Final malo: Fallo el ataque sorpresa; el elfo escapa con mi espada y me deja malherido. 💀\n")
            fin_del_juego()
        else:
            nivel3_dialogo_con_elfo()

# ---------------------------
# Nivel 3-1: Diálogo con el elfo
# ---------------------------

def nivel3_dialogo_con_elfo():
    narrar("Me acerco con calma y le digo que la espada es mía; él responde que se la ganó en un juego.")
    decision = pedir_decision("¿INTIMIDAR o JUEGO (piedra-papel-tijeras)? > ", ["intimidar", "juego"])

    if decision == "intimidar":
        narrar("Mi presencia impone. El elfo cede y me devuelve la espada, pero se marcha sin decir nada del dragón.")
        estado["espada_1"] = True
        narrar("Llego un poco tarde a la montaña, pero aún así me encuentro con el dragón... (puede ser peligroso).")
        estado["info_dragon"] = False
        nivel_montana()
    else:
        narrar("Acepto jugar. Si gano, me devuelve la espada y me dice dónde está el dragón; si pierdo, me quita el hacha.")
        gano = juego_piedra_papel_tijeras()
        if gano:
            estado["espada_1"] = True
            estado["info_dragon"] = True
            narrar("Gané el juego. El elfo cumple su palabra: me devuelve la espada y me revela la ubicación y me dice que le lleve flores xd .")
            # Según tu petición, ganar aquí puede llevar directamente al nivel 6 (cita/boda)
            nivel6_boda()
        else:
            # El elfo gana: pierdes el hacha (final malo (⓿_⓿))
            final_elfo_gana_juego()

# ---------------------------
# Nivel 2-1: Lo desafío
# ---------------------------

def nivel2_desafio():
    narrar("Salgo con valentía. El elfo se sorprende y se prepara para pelear: «¡Humano insolente!»")
    narrar("Comienza el combate entre mi hacha y la agilidad élfica.")
    decision = pedir_decision("¿Quieres MATARLO o DEJARLO VIVIR? > ", ["matarlo", "dejarlo vivir"])

    if decision == "matarlo":
        estado["elfo_vivo"] = False
        estado["espada_1"] = True
        narrar("Lo derroto y recupero una de mis espadas, pero nadie me dice dónde está la otra.")
        narrar("Llego a la montaña tarde; el dragón ya se fue con mi otra espada.")
        print("☠️ Final malo: Sin pistas, el dragón desaparece con mi espada. Fracaso en la misión. 💀\n")
        fin_del_juego()
    else:
        estado["elfo_companero"] = True
        estado["espada_1"] = True
        estado["info_dragon"] = True
        narrar("Bajo el arma. El elfo, sorprendido por mi honor, me devuelve la espada y ofrece su ayuda.")
        narrar("«El dragón negro atacó el campamento y voló hacia la montaña que esta al norte . Te acompañaré.»")
        nivel_montana()

# ---------------------------
# Nivel 2-2: Huyo
# ---------------------------

def nivel2_huyo():
    narrar("Corro sin mirar atrás. El suelo cede se quiebra a mis pies...")
    print("☠️ Final inmediato: Caigo por un barranco y me rompo el cuello. 💀🕳️\n")
    fin_del_juego()

# ---------------------------
# Nivel de Montaña (encuentro con Alduin) 🦕
# ---------------------------

def nivel_montana():
    narrar("Tras un día y medio, alcanzo el pico. El viento corta como cuchillas. Un rugido sacude el cielo (⊙ˍ⊙).")
    narrar("«¡HUMANO, CÓMO TE ATREVES A VENIR A MI DOMINIO!» resuena entre las rocas.")
    if estado["elfo_companero"]:
        narrar("El elfo se coloca a mi lado: «No estás solo, Altair.»")
        narrar("Juntos enfrentamos al dragón. El elfo distrae a la bestia; yo recupero la segunda espada.")
        estado["espada_2"] = True
        narrar("Con ambas espadas, espantamos a la criatura con una epica paliza, que al final huye herida hacia el horizonte.")
        final_taberna()
    else:
        if estado["info_dragon"]:
            narrar("Con la información que obtuve, entro con decisión. El dragón me observa y su figura cambia...")
            nivel6_boda()
        else:
            narrar("Llegué sin elfo y sin información. La ventaja es del dragón.")
            decision = pedir_decision("¿Intento PERSUADIR o ATACAR? > ", ["persuadir", "atacar"])
            if decision == "persuadir":
                narrar("Intento dialogar y ofrecer tregua. El dragón baja la guardia y me propone algo inesperado.")
                nivel6_boda()
            else:
                narrar("Cargo con valentía, pero el terreno :v me traiciona.")
                print("☠️ Final malo: Resbalo hacia por grieta ; el dragón me observa decepcionado y me desaparece de un golpe de su cola hacia el horizonte de un golpe. 💀🌋\n")
                fin_del_juego()

# ---------------------------
# Nivel 6: Alduin (cita / boda)
# ---------------------------

def nivel6_boda():
    narrar("La criatura desciende envuelta en llamas candentes. Su silueta se transforma ante mí.")
    narrar("Ante mí aparece Alduin, de mirada dominante y poderosa: es una dragona que puede tomar forma humana.")
    narrar("Alduin: «Tu valor y tu corazón me han conmovido. ¿Compartirías una cita conmigo, Altair  (❤ ω ❤) ?»")
    decision = pedir_decision("¿ACEPTAS la cita o RECHAZAS? > ", ["aceptas", "rechazas"])

    if decision == "aceptas":
        narrar("La cita transcurre entre historias y risas. Alduin me devuelve la espada restante pero le digo que la conserve.")
        estado["espada_2"] = True
        narrar("Con el tiempo, nace un vínculo profundo entre ella y yo y una boda legendaria ,une al rey y a la dragona (❤ ω ❤). 💍🔥")
        print("🎉🏆 Final épico: Me caso con Alduin. El reino ,El bosque y las montañas viven en paz. (❤ ω ❤) (❤ ω ❤) 🏰🌋\n")
        fin_del_juego()
    else:
        narrar("Rechazo con respeto. Alduin asiente y se aleja, devolviéndome la espada por mi honestidad.")
        estado["espada_2"] = True
        narrar("Parto con ambas espadas, pero con la sensación de haber dejado pasar un destino singular (￣┰￣*) .")
        print("🏆 Final neutral: Recupero mis espadas y regreso al reino, pensativo. 🗡️🗡️\n")
        fin_del_juego()

# ---------------------------
# Final rumba con el elfo
# ---------------------------

def final_taberna():
    narrar("Con el dragón espantado y las espadas recuperadas, el elfo y yo bajamos de la montaña.")
    narrar("En la taberna, brindamos por la victoria y por la improbable amistad. Bebemos hasta que las historias se vuelven leyenda ┌( ಠ_ಠ)┘ (￣﹏￣；).")
    print("🏆 Final camarada: El rey y el elfo se van a beber, riendo de las hazañas del día (★‿★). 🥳\n")
    fin_del_juego()

# ---------------------------
# Inicio del juego disfrute mi rey
# ---------------------------

def start_game():
    narrar("Camino por el bosque con mi hacha y mi mapa. Estoy decidido a recuperar mis espadas.")
    nivel1()

if __name__ == "__main__":
    start_game()
