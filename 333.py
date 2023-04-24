from tkinter import *
import random
from tkinter import messagebox

# Create a window
window = Tk()
window.title("Omok Game")
window.geometry("600x600")

# Create a canvas
board = Canvas(window, width=450, height=450)
board.pack()

# 오목 판 초기화
board_arr = [[' ' for i in range(19)] for j in range(19)]
    
def computer_move(board, x_click, y_click):
    while True:
        x = random.randint(max(x_click-1, 0), min(x_click+1, 14))
        y = random.randint(max(y_click-1, 0), min(y_click+1, 14))
        if board[y][x] == '-':
            return x, y

# 오목 판 출력
def print_board(board):
    for i in range(15):
        for j in range(15):
            print(board[i][j], end=' ')
        print()

# 돌 놓기
def put_stone(board, x, y, stone):
    board[y][x] = stone
    
# 가로, 세로, 대각선 검사 함수
def check_win(board, x, y):
    stone = board[y][x]
    count = 1

    # 가로 검사
   # 가로 검사
    for i in range(x-1, -1, -1):
        if board[y][i] == stone:
            count += 1
        else:
            break
    for i in range(x+1, 15):
        if board[y][i] == stone:
            count += 1
        else:
            break
    if count >= 5:
        return True

    # 세로 검사
    count = 1
    for i in range(y-1, -1, -1):
        if board[i][x] == stone:
            count += 1
        else:
            break
    for i in range(y+1, 15):
        if board[i][x] == stone:
            count += 1
        else:
            break
    if count >= 5:
        return True

    # 대각선 검사 (좌상단 -> 우하단)
    count = 1
    i, j = x-1, y-1
    while i >= 0 and j >= 0:
        if board[j][i] == stone:
            count += 1
        else:
            break
        i -= 1
        j -= 1
    i, j = x+1, y+1
    while i < 15 and j < 15:
        if board[j][i] == stone:
            count += 1
        else:
            break
        i += 1
        j += 1
    if count >= 5:
        return True

    # 대각선 검사 (우상단 -> 좌하단)
    count = 1
    i, j = x+1, y-1
    while i < 15 and j >= 0:
        if board[j][i] == stone:
            count += 1
        else:
            break
        i += 1
        j -= 1
    i, j = x-1, y+1
    while i >= 0 and j < 15:
        if board[j][i] == stone:
            count += 1
        else:
            break
        i -= 1
        j += 1
    if count >= 5:
        return True

    return False


# 가로, 세로, 대각선 검사
for i in range(15):
    board.create_line(30+i*30, 30, 30+i*30, 450-30, width=2)
    board.create_line(30, 30+i*30, 450-30, 30+i*30, width=2)

# Create a variable to keep track of the turn
turn = 0
placed_coordinates = []

# Create a function to handle a piece being placed
# Create a function to handle a piece being placed
def place_piece(event):
    global turn
    global placed_coordinates

    # Get the coordinates of the click
    x_pos = event.x
    y_pos = event.y

    # Round the coordinates to the nearest intersection
    x_pos = round((x_pos)/30)*30
    y_pos = round((y_pos)/30)*30

    # Check if the coordinates have already been placed
    for coord in placed_coordinates:
        if abs(x_pos - coord[0]) <= 5 and abs(y_pos - coord[1]) <=5:
            return

    # Place a new piece only if it's the current player's turn
    if (turn % 2 == 0 and turn == 0) or (turn % 2 == 1 and turn == 1):
        x = (x_pos - 30) // 30
        y = (y_pos - 30) // 30
        if 0 <= x < len(board_arr) and 0 <= y < len(board_arr):
            if board_arr[y][x] != ' ':
                return
            placed_coordinates.append((x_pos, y_pos))
            board.create_oval(x_pos-12, y_pos-12, x_pos+12, y_pos+12, fill="black", width=1)
            stone = 'o'
            put_stone(board_arr, x, y, stone)

            # Check if the game has ended
            if check_win(board_arr, x, y):
                messagebox.showinfo("Game Over", "Player {} has won!".format(turn%2+1))
                window.quit()
                return
            if len(placed_coordinates) == 19 * 19:
                messagebox.showinfo("Game Over", "The game is a tie!")
                window.quit()
                return

            # Switch to the next turn
            turn += 1

            # Get the computer's move
            if turn % 2 == 1:
                x, y = computer_move(board_arr, x, y)
                placed_coordinates.append(((x+1)*30, (y+1)*30))
                board.create_oval(x*30+18, y*30+18, (x+1)*30-18, (y+1)*30-18, fill="white", width=1)
                stone = 'x'
                put_stone(board_arr, x, y, stone)

                # Check if the game has ended
                if check_win(board_arr, x, y):
                    messagebox.showinfo("Game Over", "Computer has won!")
                    window.quit()
                    return
                if len(placed_coordinates) == 19 * 19:
                    messagebox.showinfo("Game Over", "The game is a tie!")
                    window.quit()
                    return

# Bind the canvas to the mouse click event
board.bind("<Button-1>", place_piece)

# Start the game
window.mainloop()
