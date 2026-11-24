# Tres en raya (CodePlay)

Proyecto integrador de primer nivel · Lógica de Programación · UIDE · Paralelo B

Juego por turnos para dos jugadores con modo local y, más adelante, modo multijugador cliente-servidor en red LAN.

## Integrantes

- Marshall Rivadeneira
- Brad Vizcarra

## Cómo ejecutarlo

Requiere Python 3. Desde la carpeta del repositorio:

python juego.py (menú)
python game_logic.py (validación de la jugada y fin de la partida)

## Estructura del repositorio

| Archivo | Qué hace | Estado |
| `juego.py` | Menú que se repite hasta «Salir» (parte de DF1). La opción «Jugar» por ahora solo muestra un mensaje. | Terminado |
| `game_logic.py` | Validación de la jugada (DF2) y fin de la partida (DF3) | Terminado |
| `server.py` | Comentario con lo que hará el servidor (Jugador 1) | Pendiente |
| `client.py` | Comentario con lo que hará el cliente (Jugador 2) | Pendiente |
| `diseno/` | Diagramas `.rap` de la Fase 2 | Subido |

## Del diseño al código

| Diagrama de la Fase 2 | Archivo y líneas | Qué cambió al traducirlo |
| DF1 Partida completa (solo el menú) | `juego.py`, líneas 8-26 | El Loop del menú pasó a ser un `while` que se repite hasta que `opcion` sea 2; el Loop que valida la opción pasó a ser un `while` que vuelve a pedirla mientras no sea 1 o 2. «Jugar» solo muestra un mensaje. |
| DF2 Validación de la jugada | `game_logic.py`, líneas 8-62 | El Loop de RAPTOR pasó a ser un `while` que se repite mientras `valida` no sea 1. `Is_Number(jugada)` se tradujo con la función `es_numero()` (con `try/except`), porque Python no tiene esa función. El tablero sigue en las variables `c1` hasta `c9`, sin listas, igual que en RAPTOR. |
| DF3 Fin de la partida | `game_logic.py`, líneas 68-111 | Las Selections encadenadas pasaron a ser `if`/`elif`/`else`. Las 8 líneas ganadoras se comprueban en una sola condición, igual que en RAPTOR. |

## Video explicativo

[Enlace al video](https://drive.google.com/file/d/19PfGGl7GA_ozZ2sWDMo_84xnaCOdypoA/view?usp=sharing) (máximo 5 minutos: el menú, la validación con una jugada inválida, el fin de la partida y cómo tradujimos un diagrama a código).

## Licencia

Este proyecto se distribuye bajo la licencia MIT. El texto completo está en el archivo `LICENSE`.

## Declaración de autoría

Declaramos que el código de este repositorio fue escrito por los integrantes del equipo, salvo los recursos citados en la sección «Créditos».

## Créditos

| Recurso (código, librería, imagen…) | Autor o fuente | Dónde se usa | Licencia |
| Biblioteca estándar de Python | Python Software Foundation | `juego.py`, `game_logic.py` | PSF License |
| Código de terceros | Ninguno | — | — |

### Uso de IA

| Herramienta | Para qué la usamos | Qué revisamos o cambiamos nosotros |
| Claude | Se utilizo para verificar que se ejecuten correctamente los códigos y que el resultado sea el esperado | Revisamos que todo se encuentre correctamente ordenado y que las salidas de los diagramas y codigos sean correctos |
