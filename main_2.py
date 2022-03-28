from tkinter import Canvas, messagebox, Tk, Label, LEFT
from PIL import Image, ImageTk  # to resize the board to a smaller image
import tkinter.simpledialog

FONT = ("Courier", 120, "bold")

window = Tk()
window.title("SecureMedjay TicTacToe")
window.minsize(width=50, height=50)

player1_avatar = Label(text=f"Player 1: ", justify=LEFT, width=25)
player1_avatar.grid(row=0, column=0)
player2_avatar = Label(text=f"Player 2: ", justify=LEFT, width=25)
player2_avatar.grid(row=0, column=1)

turn = 0
grid = []
win = False

# create a canvas of tic-tac-toe board
canvas = Canvas(width=500, height=500)
board = ImageTk.PhotoImage(
    Image.open('board.gif').resize(size=(500, 500)))  # resize the size of the image to 500px by 500px
canvas.create_image(250, 250, image=board)

canvas.grid(row=1, column=0, columnspan=2)

# get users avatar
entry = tkinter.simpledialog.askstring("Player 1", "Select your avatar, 'X' or 'O'")

# tell users their avatar
if entry.upper() == "X":
    player1_avatar.config(text="Player 1: X", fg="red")
    player2_avatar.config(text="Player 2: O", fg="blue")
    turn = 1
elif entry.upper() == "O":
    player1_avatar.config(text="Player 1: 0", fg="blue")
    player2_avatar.config(text="Player 2: X", fg="red")
else:
    messagebox.showerror(title="Error", message="You have entered an invalid input")


def get_boxes(list_item):
    box_avatar_dict = {}
    boxes = {
        "box_1": [95, 65],
        "box_2": [210, 65],
        "box_3": [325, 65],
        "box_4": [95, 210],
        "box_5": [210, 210],
        "box_6": [325, 210],
        "box_7": [95, 355],
        "box_8": [210, 355],
        "box_9": [325, 355],
    }
    for item in list_item:
        for box, post in boxes.items():
            if post == item[0]:
                box_avatar_dict[box] = item[1]
    check_win(box_avatar_dict)


# get a winner or a draw
def check_win(matrix):
    global win
    try:
        if matrix["box_1"] == matrix["box_2"] == matrix["box_3"]:
            win = True
            messagebox.showinfo(title="Winner!", message=f"Player {matrix['box_1']} wins!")
    except KeyError:
        pass
    try:
        if matrix["box_4"] == matrix["box_5"] == matrix["box_6"]:
            win = True
            messagebox.showinfo(title="Winner!", message=f"Player {matrix['box_4']} wins!")
    except KeyError:
        pass
    try:
        if matrix["box_7"] == matrix["box_8"] == matrix["box_9"]:
            win = True
            messagebox.showinfo(title="Winner!", message=f"Player {matrix['box_7']} wins!")
    except KeyError:
        pass
    try:
        if matrix["box_1"] == matrix["box_4"] == matrix["box_7"]:
            win = True
            messagebox.showinfo(title="Winner!", message=f"Player {matrix['box_1']} wins!")
    except KeyError:
        pass
    try:
        if matrix["box_2"] == matrix["box_5"] == matrix["box_8"]:
            win = True
            messagebox.showinfo(title="Winner!", message=f"Player {matrix['box_2']} wins!")
    except KeyError:
        pass
    try:
        if matrix["box_3"] == matrix["box_6"] == matrix["box_9"]:
            win = True
            messagebox.showinfo(title="Winner!", message=f"Player {matrix['box_3']} wins!")
    except KeyError:
        pass
    try:
        if matrix["box_1"] == matrix["box_5"] == matrix["box_9"]:
            win = True
            messagebox.showinfo(title="Winner!", message=f"Player {matrix['box_1']} wins!")
    except KeyError:
        pass
    try:
        if matrix["box_3"] == matrix["box_5"] == matrix["box_7"]:
            win = True
            messagebox.showinfo(title="Winner!", message=f"Player {matrix['box_3']} wins!")
    except KeyError:
        pass
    if len(matrix) == 9 and not win:
        messagebox.showinfo(title="Draw", message="It is a draw!")


# Switch turns, select the right avatar
def left_click(event):
    global turn

    box_1 = [range(83, 189), range(41, 173)]
    box_2 = [range(197, 302), range(41, 173)]
    box_3 = [range(311, 418), range(41, 173)]
    box_4 = [range(83, 189), range(184, 317)]
    box_5 = [range(196, 302), range(184, 317)]
    box_6 = [range(311, 416), range(184, 317)]
    box_7 = [range(83, 189), range(326, 459)]
    box_8 = [range(197, 302), range(326, 459)]
    box_9 = [range(311, 416), range(326, 459)]

    if event.x in box_1[0] and event.y in box_1[1]:
        if turn % 2 != 0:
            game = Label(window, text="X", font=FONT, fg="red", bd=0)
            game.place(x=95, y=65)
        else:
            game = Label(window, text="O", font=FONT, fg="blue", bd=0)
            game.place(x=95, y=65)

    if event.x in box_2[0] and event.y in box_2[1]:
        if turn % 2 != 0:
            game = Label(window, text="X", font=FONT, fg="red", bd=0)
            game.place(x=210, y=65)
        else:
            game = Label(window, text="O", font=FONT, fg="blue", bd=0)
            game.place(x=210, y=65)

    if event.x in box_3[0] and event.y in box_3[1]:
        if turn % 2 != 0:
            game = Label(window, text="X", font=FONT, fg="red", bd=0)
            game.place(x=325, y=65)
        else:
            game = Label(window, text="O", font=FONT, fg="blue", bd=0)
            game.place(x=325, y=65)

    if event.x in box_4[0] and event.y in box_4[1]:
        if turn % 2 != 0:
            game = Label(window, text="X", font=FONT, fg="red", bd=0)
            game.place(x=95, y=210)
        else:
            game = Label(window, text="O", font=FONT, fg="blue", bd=0)
            game.place(x=95, y=210)

    if event.x in box_5[0] and event.y in box_5[1]:
        if turn % 2 != 0:
            game = Label(window, text="X", font=FONT, fg="red", bd=0)
            game.place(x=210, y=210)
        else:
            game = Label(window, text="O", font=FONT, fg="blue", bd=0)
            game.place(x=210, y=210)

    if event.x in box_6[0] and event.y in box_6[1]:
        if turn % 2 != 0:
            game = Label(window, text="X", font=FONT, fg="red", bd=0)
            game.place(x=325, y=210)
        else:
            game = Label(window, text="O", font=FONT, fg="blue", bd=0)
            game.place(x=325, y=210)

    if event.x in box_7[0] and event.y in box_7[1]:
        if turn % 2 != 0:
            game = Label(window, text="X", font=FONT, fg="red", bd=0)
            game.place(x=95, y=355)
        else:
            game = Label(window, text="O", font=FONT, fg="blue", bd=0)
            game.place(x=95, y=355)

    if event.x in box_8[0] and event.y in box_8[1]:
        if turn % 2 != 0:
            game = Label(window, text="X", font=FONT, fg="red", bd=0)
            game.place(x=210, y=355)
        else:
            game = Label(window, text="O", font=FONT, fg="blue", bd=0)
            game.place(x=210, y=355)

    if event.x in box_9[0] and event.y in box_9[1]:
        if turn % 2 != 0:
            game = Label(window, text="X", font=FONT, fg="red", bd=0)
            game.place(x=325, y=355)
        else:
            game = Label(window, text="O", font=FONT, fg="blue", bd=0)
            game.place(x=325, y=355)

    turn += 1
    x_coord = int(game.place_info()["x"])
    y_coord = int(game.place_info()["y"])
    text = game["text"]
    play = [[x_coord, y_coord], text]
    grid.append(play)
    if len(grid) > 4:
        get_boxes(grid)


window.bind("<Button-1>", left_click)
window.mainloop()
