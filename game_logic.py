# game_logic.py · Traduce DF2 (validación) y DF3 (fin de la partida) de la Fase 2
# Requisitos que cubre: RF-05, RF-06 (validación), RF-08, RF-09 (ganador y empate)


def validar_jugada(jugada, c1, c2, c3, c4, c5, c6, c7, c8, c9):
    """
    DF2: Valida la jugada por formato y por reglas.
    Retorna True si es válida, False si es inválida.
    """
    # Validación por formato (RF-05)
    if not jugada.isdigit() or int(jugada) < 1 or int(jugada) > 9:
        print("Entrada inválida. Escribe un número del 1 al 9")
        return False

    num = int(jugada)

    # Validación por reglas (RF-06): ¿La casilla está libre?
    if num == 1 and c1 != "1":
        print("Casilla ocupada. Elige otra")
        return False
    elif num == 2 and c2 != "2":
        print("Casilla ocupada. Elige otra")
        return False
    elif num == 3 and c3 != "3":
        print("Casilla ocupada. Elige otra")
        return False
    elif num == 4 and c4 != "4":
        print("Casilla ocupada. Elige otra")
        return False
    elif num == 5 and c5 != "5":
        print("Casilla ocupada. Elige otra")
        return False
    elif num == 6 and c6 != "6":
        print("Casilla ocupada. Elige otra")
        return False
    elif num == 7 and c7 != "7":
        print("Casilla ocupada. Elige otra")
        return False
    elif num == 8 and c8 != "8":
        print("Casilla ocupada. Elige otra")
        return False
    elif num == 9 and c9 != "9":
        print("Casilla ocupada. Elige otra")
        return False

    return True


def decidir_fin(c1, c2, c3, c4, c5, c6, c7, c8, c9, jugadas):
    """
    DF3: Decide si gana el Jugador 1 (X), el Jugador 2 (O), hay empate, o continúa.
    Devuelve el estado del juego.
    """
    # ¿Gana el Jugador 1 (X)? (RF-08)
    if (
        (c1 == "X" and c2 == "X" and c3 == "X")
        or (c4 == "X" and c5 == "X" and c6 == "X")
        or (c7 == "X" and c8 == "X" and c9 == "X")
        or (c1 == "X" and c4 == "X" and c7 == "X")
        or (c2 == "X" and c5 == "X" and c8 == "X")
        or (c3 == "X" and c6 == "X" and c9 == "X")
        or (c1 == "X" and c5 == "X" and c9 == "X")
        or (c3 == "X" and c5 == "X" and c7 == "X")
    ):
        return "¡Ganaste Jugador 1! (Perdiste Jugador 2)"

    # ¿Gana el Jugador 2 (O)? (RF-08)
    elif (
        (c1 == "O" and c2 == "O" and c3 == "O")
        or (c4 == "O" and c5 == "O" and c6 == "O")
        or (c7 == "O" and c8 == "O" and c9 == "O")
        or (c1 == "O" and c4 == "O" and c7 == "O")
        or (c2 == "O" and c5 == "O" and c8 == "O")
        or (c3 == "O" and c6 == "O" and c9 == "O")
        or (c1 == "O" and c5 == "O" and c9 == "O")
        or (c3 == "O" and c5 == "O" and c7 == "O")
    ):
        return "¡Ganaste Jugador 2! (Perdiste Jugador 1)"

    # ¿Empate? (RF-09)
    elif jugadas == 9:
        return "Empate"

    # La partida continúa
    else:
        return "La partida continúa"


# ==========================================
# SIMULACIÓN DE ESTADO Y PRUEBAS DE LÓGICA
# ==========================================
if __name__ == "__main__":
    print("--- PRUEBA DF2: VALIDACIÓN DE JUGADA ---")

    # Simulando una entrada no válida por formato
    print("\nValidando entrada 'A':")
    validar_jugada("A", "1", "2", "3", "4", "X", "6", "7", "8", "9")

    # Simulando una entrada no válida por regla (casilla ocupada)
    print("\nValidando casilla ocupada (5):")
    validar_jugada("5", "1", "2", "3", "4", "X", "6", "7", "8", "9")

    # Simulando una entrada válida
    print("\nValidando jugada libre (1):")
    if validar_jugada("1", "1", "2", "3", "4", "X", "6", "7", "8", "9"):
        print("Jugada aceptada.")

    print("\n--- PRUEBA DF3: DECISIÓN DE FIN DE PARTIDA ---")

    # Simulando tablero con victoria de X
    print(
        "\nEvaluando tablero (Victoria X):",
        decidir_fin("X", "X", "X", "4", "O", "O", "7", "8", "9", 5),
    )

    # Simulando tablero con victoria de O
    print(
        "Evaluando tablero (Victoria O):",
        decidir_fin("X", "X", "7", "O", "O", "O", "8", "9", "1", 6),
    )

    # Simulando tablero lleno sin ganador
    print(
        "Evaluando tablero (Empate):",
        decidir_fin("X", "O", "X", "X", "O", "O", "O", "X", "X", 9),
    )

    # Simulando tablero en desarrollo
    print(
        "Evaluando tablero (En curso):",
        decidir_fin("X", "1", "2", "3", "O", "6", "7", "8", "9", 2),
    )
