import random

EMPTY = ""
UNEXPLORED = "⬛"
WATER = "🟦"
TOUCHED = "🟧"
SUNKEN = "🟥"

LETTERS = "ABCDEFGHIJ"
TOTAL_SHIPS = 5
POINTS_PER_SHIP = {"5A": 10, "4A": 8, "3A": 6, "3B": 6, "2A": 4}

def generate_board(size=10, ships=((5, 1), (4, 1), (3, 2), (2, 1))):
    board = [[EMPTY for _ in range(size)] for _ in range(size)]
    for ship_size, num_ships in ships:
        placed_ships = 0
        while placed_ships < num_ships:
            ship_id = f"{ship_size}{placed_ships}"
            row, col = random.randint(0, size - 1), random.randint(0, size - 1)
            orientation = random.choice(["horizontal", "vertical"])
            if can_place_ship(board, row, col, ship_size, orientation):
                place_ship(board, row, col, ship_size, orientation, ship_id)
                placed_ships += 1
    return board

def can_place_ship(board, row, col, size, orientation):
    if orientation == "horizontal":
        return all(board[row][c] == EMPTY for c in range(col, col + size))
    elif orientation == "vertical":
        return all(board[r][col] == EMPTY for r in range(row, row + size))
    return False

def place_ship(board, row, col, size, orientation, ship_id):
    if orientation == "horizontal":
        for c in range(col, col + size):
            board[row][c] = ship_id
    elif orientation == "vertical":
        for r in range(row, row + size):
            board[r][col] = ship_id

def show_board(board):
    print("  ", " ".join(LETTERS))
    for i, row in enumerate(board):
        print(i + 1, " ".join(row))

def get_coords(coord):
    col = LETTERS.index(coord[0])
    row = int(coord[1:]) - 1
    return row, col

def main():
    game_board = [[UNEXPLORED for _ in range(10)] for _ in range(10)]
    ships = generate_board()

    turns = 0
    points = 0

    while True:
        show_board(game_board)
        coordinate = input("Ingrese sus coordenadas (por ejemplo, 'A1'): ").upper()
        row, col = get_coords(coordinate)

        if game_board[row][col] != UNEXPLORED:
            print("Ya has disparado a esta casilla.")
            continue

        if ships[row][col] == EMPTY:
            print("Has dado a una casilla de agua.")
            game_board[row][col] = WATER
        else:
            ship_id = ships[row][col]
            ship_size = int(ship_id[:-1])
            print(f"Has golpeado un barco de tamaño {ship_size}!")
            game_board[row][col] = TOUCHED
            points += POINTS_PER_SHIP[ship_id]

            # Verificar si se ha hundido el barco
            if all(ships[r][c] == ship_id for r in range(10) for c in range(10)):
                print("¡Has hundido un barco!")
                points += POINTS_PER_SHIP[ship_id] * 2
                TOTAL_SHIPS -= 1

                if TOTAL_SHIPS == 0:
                    print(f"Juego terminado. Tu puntuación es {points} y tardaste {turns} turnos.")
                    break

        turns += 1
