from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("Tic Tac Toe")

clicked = True
count = 0

buttons = []
for i in range(3):
    row = []
    for j in range(3):
        button = Button(root, text="", font=("Helvetica", 20), height=3, width=6, command=lambda row=i, col=j: click(row, col))
        button.grid(row=i, column=j, sticky="nsew")
        row.append(button)
    buttons.append(row)

# Import DISABLED constant
from tkinter import DISABLED

def click(row, col):
    global clicked, count

    if buttons[row][col]["text"] == "" and clicked == True:
        buttons[row][col]["text"] = "X"
        computer_move()
        count += 1

        # Check for win
        if check_win("X"):
            messagebox.showinfo("Tic Tac Toe", "You won!")
            messagebox.showinfo("Tic Tac Toe", "Click reset to play again")
            disable_all_buttons()

        elif check_win("O"):
            messagebox.showinfo("Tic Tac Toe", "You Lost!")
            messagebox.showinfo("Tic Tac Toe", "Click reset to play again")
        elif count == 9:
            messagebox.showinfo("Tic Tac Toe", "Tie")
            disable_all_buttons()

def disable_all_buttons():
    for row in buttons:
        for button in row:
            button.config(state=DISABLED)

def check_win(player):
    # Check for rows
    for i in range(3):
        if buttons[i][0]["text"] == player and buttons[i][1]["text"] == player and buttons[i][2]["text"] == player:
            highlight_winner_buttons([(i, 0), (i, 1), (i, 2)])
            return True

    # Check columns for win
    for i in range(3):
        if buttons[0][i]["text"] == player and buttons[1][i]["text"] == player and buttons[2][i]["text"] == player:
            highlight_winner_buttons([(0, i), (1, i), (2, i)])
            return True

    # Check diagonals for win
    if buttons[0][0]["text"] == player and buttons[1][1]["text"] == player and buttons[2][2]["text"] == player:
        highlight_winner_buttons([(0, 0), (1, 1), (2, 2)])
        return True
    if buttons[0][2]["text"] == player and buttons[1][1]["text"] == player and buttons[2][0]["text"] == player:
        highlight_winner_buttons([(0, 2), (1, 1), (2, 0)])
        return True

    return False

def highlight_winner_buttons(winning_positions):
    for position in winning_positions:
        i, j = position
        buttons[i][j].config(bg="red")


def evaluate_board():
    score = 0

    # Check rows
    for i in range(3):
        if buttons[i][0]["text"] == "O" and buttons[i][1]["text"] == "O" and buttons[i][2]["text"] == "O":
            score += 10
        elif buttons[i][0]["text"] == "X" and buttons[i][1]["text"] == "X" and buttons[i][2]["text"] == "X":
            score -= 10

    # Check columns
    for i in range(3):
        if buttons[0][i]["text"] == "O" and buttons[1][i]["text"] == "O" and buttons[2][i]["text"] == "O":
            score += 10
        elif buttons[0][i]["text"] == "X" and buttons[1][i]["text"] == "X" and buttons[2][i]["text"] == "X":
            score -= 10

    # Check diagonals
    if buttons[0][0]["text"] == "O" and buttons[1][1]["text"] == "O" and buttons[2][2]["text"] == "O":
        score += 10
    elif buttons[0][0]["text"] == "X" and buttons[1][1]["text"] == "X" and buttons[2][2]["text"] == "X":
        score -= 10

    if buttons[0][2]["text"] == "O" and buttons[1][1]["text"] == "O" and buttons[2][0]["text"] == "O":
        score += 10
    elif buttons[0][2]["text"] == "X" and buttons[1][1]["text"] == "X" and buttons[2][0]["text"] == "X":
        score -= 10

    return score

def heuristic():
    score = 0
# Check rows
    for i in range(3):
        if buttons[i][0]["text"] == "O" and buttons[i][1]["text"] == "O" and buttons[i][2]["text"] == "":
            score += 1
        elif buttons[i][0]["text"] == "X" and buttons[i][1]["text"] == "X" and buttons[i][2]["text"] == "":
            score -= 1

    # Check columns
    for i in range(3):
        if buttons[0][i]["text"] == "O" and buttons[1][i]["text"] == "O" and buttons[2][i]["text"] == "":
            score += 1
        elif buttons[0][i]["text"] == "X" and buttons[1][i]["text"] == "X" and buttons[2][i]["text"] == "":
            score -= 1

    # Check diagonals
    if buttons[0][0]["text"] == "O" and buttons[1][1]["text"] == "O" and buttons[2][2]["text"] == "":
        score += 1
    elif buttons[0][0]["text"] == "X" and buttons[1][1]["text"] == "X" and buttons[2][2]["text"] == "":
        score -= 1

    if buttons[0][2]["text"] == "O" and buttons[1][1]["text"] == "O" and buttons[2][0]["text"] == "":
        score += 1
    elif buttons[0][2]["text"] == "X" and buttons[1][1]["text"] == "X" and buttons[2][0]["text"] == "":
        score -= 1

    return score

def computer_move():
    global count
    empty_cells = []

    for i in range(3):
        for j in range(3):
            if buttons[i][j]["text"] == "":
                empty_cells.append((i, j))

    if empty_cells:
        # Uses one of the 6 algorithms to determine the best move
        row, col = bfs_move(empty_cells)
        buttons[row][col]["text"] = "O"
        count += 1

        if check_win("O"):
            disable_all_buttons()

# Define the 6 algorithms
# BFS Move
def bfs_move(empty_cells):
    for symbol in ["O", "X"]:
        for cell in empty_cells:
            i, j = cell
            buttons[i][j]["text"] = symbol

            if check_win(symbol):
                if symbol == "O":
                    return i, j
                else:
                    buttons[i][j]["text"] = "O"  # Block the winning move
                    return i, j

            buttons[i][j]["text"] = ""  # Undo the move

    return random.choice(empty_cells)



'''# DFS Move
def dfs_move(empty_cells):
    for symbol in ["O", "X"]:
        for cell in empty_cells:
            i, j = cell
            buttons[i][j]["text"] = symbol

            if check_win(symbol):
                if symbol == "O":
                    return i, j
                else:
                    buttons[i][j]["text"] = "O"  # Block the winning move
                    return i, j

            buttons[i][j]["text"] = ""  # Undo the move

    return random.choice(empty_cells)


# IDS Move
def ids_move(empty_cells):
    depth = 1
    while True:
        result = dls_move(empty_cells, depth)
        if result is not None:
            return result
        depth += 1

# DLS Move
def dls_move(empty_cells, depth):
    for symbol in ["O", "X"]:
        for cell in empty_cells:
            i, j = cell
            buttons[i][j]["text"] = symbol

            if check_win(symbol):
                if symbol == "O":
                    return i, j
                else:
                    buttons[i][j]["text"] = "O"  # Block the winning move
                    return i, j

            buttons[i][j]["text"] = ""  # Undo the move

    return random.choice(empty_cells)

# UCS Move
def ucs_move(empty_cells):
    class State:
        def __init__(self, row, col, cost):
            self.row = row
            self.col = col
            self.cost = cost

    moves = [State(row, col, 0) for row, col in empty_cells]

    moves.sort(key=lambda move: move.cost)

    for move in moves:
        i, j, _ = move.row, move.col, move.cost

        # Simulate the computer's move
        buttons[i][j]["text"] = "O"

        # Check if the computer wins
        if check_win("O"):
            return i, j

        # Undo the move
        buttons[i][j]["text"] = ""

    # If no winning move, block the player
    for move in moves:
        i, j, _ = move.row, move.col, move.cost

        # Simulate the player's move
        buttons[i][j]["text"] = "X"

        # Check if the player wins
        if check_win("X"):
            # Block the winning move
            buttons[i][j]["text"] = "O"
            return i, j

        # Undo the move
        buttons[i][j]["text"] = ""

    # If no winning or blocking move, choose a random move
    return random.choice(empty_cells)

# Greedy Move
def greedy_move(empty_cells):
    best_score = float("-inf")
    best_move = None

    for cell in empty_cells:
        i, j = cell
        buttons[i][j]["text"] = "O"
        score = evaluate_board()

        if score > best_score:
            best_score = score
            best_move = (i, j)

        buttons[i][j]["text"] = ""  # Undo the move

    if best_score >= 10:  # Computer wins
        return best_move

    # If no winning move, block the player
    for cell in empty_cells:
        i, j = cell
        buttons[i][j]["text"] = "X"
        score = evaluate_board()

        if score <= -10:  # Player wins
            buttons[i][j]["text"] = "O"  # Block the winning move
            return i, j

        buttons[i][j]["text"] = ""  # Undo the move

    # If no winning or blocking move, choose a random move
    return random.choice(empty_cells)   

# A* Move
def a_star_move(empty_cells):
    best_score = float("-inf")
    best_move = None

    for cell in empty_cells:
        i, j = cell
        buttons[i][j]["text"] = "O"
        score = evaluate_board() + heuristic()

        if score > best_score:
            best_score = score
            best_move = (i, j)

        buttons[i][j]["text"] = ""  # Undo the move

    if best_score >= 10:  # Computer wins
        return best_move

    # If no winning move, block the player
    for cell in empty_cells:
        i, j = cell
        buttons[i][j]["text"] = "X"
        score = evaluate_board() + heuristic()

        if score <= -10:  # Player wins
            buttons[i][j]["text"] = "O"  # Block the winning move
            return i, j

        buttons[i][j]["text"] = ""  # Undo the move

    # If no winning or blocking move, choose a random move
    return random.choice(empty_cells)
'''
# Add a reset function
def reset():
    global clicked, count
    clicked = True
    count = 0

    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""
            buttons[i][j].config(bg="SystemButtonFace", state=NORMAL)


 
 # Create a reset button
reset_button = Button(root, text="Reset", font=("Helvetica", 16), height=2, width=5, command=reset)
reset_button.grid(row=3, column=1, columnspan=3)

root.mainloop()
