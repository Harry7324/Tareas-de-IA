import math

# Imprime el tablero de juego
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Revisa si hay un ganador
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

# Revisa si hay empate
def is_draw(board):
    return all(cell != " " for row in board for cell in row)

# Devuelve los movimientos disponibles
def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

# Implementación del algoritmo minimax
def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for r, c in get_available_moves(board):
            board[r][c] = "O"
            score = minimax(board, False)
            board[r][c] = " "
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for r, c in get_available_moves(board):
            board[r][c] = "X"
            score = minimax(board, True)
            board[r][c] = " "
            best_score = min(best_score, score)
        return best_score

# Encuentra el mejor movimiento para la IA
def best_move(board):
    best_score = -math.inf
    move = None
    for r, c in get_available_moves(board):
        board[r][c] = "O"
        score = minimax(board, False)
        board[r][c] = " "
        if score > best_score:
            best_score = score
            move = (r, c)
    return move

# Juego principal
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Bienvenido a Tic-Tac-Toe. Tú juegas con 'X'.")
    print_board(board)

    while True:
        # Turno del jugador
        while True:
            try:
                row = int(input("Ingresa la fila (0, 1, 2): "))
                col = int(input("Ingresa la columna (0, 1, 2): "))
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Esa casilla ya está ocupada. Intenta de nuevo.")
            except (ValueError, IndexError):
                print("Entrada inválida. Intenta de nuevo.")

        print_board(board)

        if check_winner(board):
            print("¡Ganaste!")
            break
        if is_draw(board):
            print("Es un empate.")
            break

        # Turno de la IA
        print("Turno de la IA...")
        r, c = best_move(board)
        board[r][c] = "O"
        print_board(board)

        if check_winner(board):
            print("¡La IA ganó!")
            break
        if is_draw(board):
            print("Es un empate.")
            break

# Ejecuta el juego
play_game()
