# juego.py · Punto de entrada del proyecto · Traduce el menú de DF1 (Fase 2)
# Requisitos que cubre: RF-01 (elegir modo de juego), RF-02 (dificultad del bot)
# Nota: el bucle de turnos de la partida completa se programa en la Fase 4.
def mostrar_menu():
    """Muestra el menú principal y devuelve la opcion elegida por el usuario"""
    print("==== TRES EN RAYA · CodePlay ====")
    print("1. Jugar")
    print("2. Salir")
    opcion = input("Elige una opción (1 o 2): ")
    return opcion


def main():
    """Bucle del menú: Se repite hasta que el jugador eliga salir (Parte del DF1)."""
    opcion = ""

    # Loop de DF1: se repite mientras la opción no sea "2" (Salir)
    while opcion != "2":
        opcion = mostrar_menu()

        if opcion == "1":
            # Todo (Fase 4): aquí irá el bucle de turnos de la partida completa.
            print(
                "Iniciando partida... (el bucle de turnos se implementa en la Fase 4)"
            )
        elif opcion == "2":
            print("¡Gracias por jugar! Hasta pronto.")
        else:
            # Validación por formato de la opción del menú
            print("Opción inválida. Elige 1 para Jugar o 2 para Salir.")


if __name__ == "__main__":
    main()
