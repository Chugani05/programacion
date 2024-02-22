import random
import string

EMPTY = ""

UNEXPLORED = "⬛"
WATER = "🟦"
TOUCHED = "🟧"
SUNKEN = "🟥"


def generate_board(
    size: int = 10,
    ships: tuple[tuple[int, int]] = ((5, 1), (4, 1), (3, 2), (2, 1)),
) -> list[list[str]]:
    board = [[EMPTY for _ in range(size)] for _ in range(size)]
    for ship_size, num_ships in ships:
        placed_ships = 0
        while placed_ships < num_ships:
            ship_id = f"{ship_size}{string.ascii_uppercase[placed_ships]}"
            row, col = random.randint(0, size - 1), random.randint(0, size - 1)
            step = random.choice((-1, 1))
            row_step, col_step = (step, 0) if random.randint(0, 1) else (0, step)
            breadcrumbs = []
            for _ in range(ship_size):
                try:
                    if not (0 <= row < size and 0 <= col < size):
                        raise IndexError()
                    if board[row][col] == EMPTY:
                        board[row][col] = ship_id
                        breadcrumbs.append((row, col))
                    else:
                        raise IndexError()
                    row += row_step
                    col += col_step
                except IndexError:
                    # reset board
                    for bc in breadcrumbs:
                        board[bc[0]][bc[1]] = EMPTY
                    break
            else:
                placed_ships += 1

    return board


def show_board(board: list[list[str]]) -> None:
    for row in board:
        for item in row:
            print(f"[{item:2s}]", end="")
        print()


board = generate_board()

LETTERS = "ABCDEFGHIJ"
TOTAL_SHIPS = 5
game = True
turn = 1
a5_counter = a4_counter = a3_counter = b3_counter = a2_counter = points = 0
a5 = []
a4 = []
a3 = []
b3 = []
a2 = []
warships = ['5A','4A','3A','3B','2A']

game_board = [[UNEXPLORED for _ in range(10)] for _ in range(10)]
while game:
    player_coordinate = input("Enter your coordinates: ")
    if player_coordinate[0] in LETTERS:
        coordinate_x = LETTERS.index(player_coordinate[0].upper())
    else:
        coordinate_x = -1
    coordinate_y = int(player_coordinate[1:]) - 1
    if 0 <= coordinate_x < 10 and 0 <= coordinate_y < 10:
        if game_board[coordinate_y][coordinate_x] == UNEXPLORED:
            cell_content = board[coordinate_y][coordinate_x]
            game_board[coordinate_y][coordinate_x] = TOUCHED
            if cell_content in warships:
                warships.remove(cell_content)
                ship_size = int(cell_content[0])
                if cell_content.endswith("A"):
                    exec(f"a{ship_size}_counter += 1")
                    if eval(f"a{ship_size}_counter") == ship_size:
                        for touched_ship in eval(f"a{ship_size}"):
                            game_board[LETTERS.index(touched_ship[0])][int(touched_ship[1:]) - 1] = SUNKEN
                        points += 4 * ship_size
                        TOTAL_SHIPS -= 1
                        print(f"Barco hundido, quedan {TOTAL_SHIPS} barcos")
            else:
                points -= 1
                print("Has dado a una casilla de agua")
        else:
            print(f"Ya has disparado a la casilla {player_coordinate}")
        
        if TOTAL_SHIPS == 0:
            print(f"Juego terminado, tu puntuación es {points} y tardaste {turn} turnos")
            game = False
        else:
            print("   1  2  3  4  5  6  7  8  9 10")
            for row in range(10):
                row_string = " ".join(game_board[row])
                print(f"{LETTERS[row]}  {row_string}")
            print(f"Tu puntuación actual es: {points}, llevas {turn} rondas y quedan {len(warships)} barcos")
            turn += 1
    else:
        print("Introduzca una coordenada correcta")
