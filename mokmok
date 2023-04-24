import tkinter as tk
from PIL import Image, ImageTk
import random
import tkinter.messagebox as messagebox
# tkinter 윈도우 생성
window = tk.Tk()

# 프레임 생성
frame = tk.Frame(window)
frame.pack()

# 캔버스 생성
canvas = tk.Canvas(frame, width=500, height=500)
canvas.pack()

# 오목판 이미지 로드
black_image = Image.open("흑돌.jpg")
white_image = Image.open("백돌.jpg")
board_image = Image.open("board_1.PNG")
black_photo = ImageTk.PhotoImage(black_image)
white_photo = ImageTk.PhotoImage(white_image)
board_photo = ImageTk.PhotoImage(board_image)

# 바둑판 초기 상태
board = [[0 for _ in range(10)] for _ in range(10)]  # 0: 빈 칸, 1: 검은 돌, 2: 흰 돌
turn = 1  # 현재 차례, 1: 검은 돌, 2: 흰 돌

# 돌을 놓을 때 이벤트 처리 함수
def place_stone(event):
    global turn  # turn 변수는 전역 변수로 사용
    button = event.widget
    row, col = button.grid_info()['row'], button.grid_info()['column']
    
    if board[row][col] != 0:  # 이미 돌이 놓인 위치인 경우
        return
   
    # 돌 놓기
    if turn == 1:
        board[row][col] = 1
        button.configure(image=black_photo)
        turn = 2
        if check_five_in_row(board, 1):  # 5개 이어진 검은 돌이 있는지 확인
            print("Black wins!")
            messagebox.showinfo("게임 종료", "Black wins!")
            window.quit()
            return
           
        # 랜덤한 위치에 백돌 놓기
    empty = [(i, j) for i in range(max(0, row-1), min(10, row+2)) for j in range(max(0, col-1), min(10, col+2)) if board[i][j] == 0]
    if empty:
        row, col = random.choice(empty)
        button = canvas.grid_slaves(row=row, column=col)[0]
        button.configure(image=white_photo)
        board[row][col] = 2
        turn = 1
        if check_five_in_row(board, 2):  # 5개 이어진 흰 돌이 있는지 확인
            print("White wins!")
            messagebox.showinfo("게임 종료", "White wins!")
            window.quit()  # 게임 종료 후 더 이상 돌을 놓을 수 없도록 마우스 클릭 이벤트 제거
            return
    

# 바둑판 버튼 생성 및 캔버스 위에 배치
button_size = 30  # 버튼 크기
for i in range(10):
    for j in range(10):
        button = tk.Button(canvas, width=30, height=30, bd=0, highlightthickness=0, image=board_photo)
        canvas.create_window(button_size*j+button_size//2, button_size*i+button_size//2, window=button, anchor=tk.CENTER)
        button.grid(row=i, column=j)
        button.bind('<Button-1>', place_stone)
    
def check_five_in_row(board, color):
    # 수평으로 5개 이어진 돌이 있는지 확인
    for i in range(10):
        for j in range(6):
            if board[i][j] == color and board[i][j+1] == color and board[i][j+2] == color and board[i][j+3] == color and board[i][j+4] == color:
                return True
    # 수직으로 5개 이어진 돌이 있는지 확인
    for i in range(6):
        for j in range(10):
            if board[i][j] == color and board[i+1][j] == color and board[i+2][j] == color and board[i+3][j] == color and board[i+4][j] == color:
                return True
    # 대각선으로 5개 이어진 돌이 있는지 확인
    for i in range(6):
        for j in range(6):
            if board[i][j] == color and board[i+1][j+1] == color and board[i+2][j+2] == color and board[i+3][j+3] == color and board[i+4][j+4] == color:
                return True
    for i in range(6):
        for j in range(9, 3, -1):
            if board[i][j] == color and board[i+1][j-1] == color and board[i+2][j-2] == color and board[i+3][j-3] == color and board[i+4][j-4] == color:
                return True
    return False    
# 오목돌 이미지 로드
  
window.mainloop()