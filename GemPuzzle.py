import tkinter
import os

IMG_PATH = 'nums'
SIZE = 4

main_window = tkinter.Tk()
main_window.title('Gem Puzzle')

files_list = os.listdir(IMG_PATH)
files_list_path = []
for _file in files_list:
    files_list_path.append(os.path.join(IMG_PATH, _file))

image_list = []
for _image_path in files_list_path:
    image_list.append(tkinter.PhotoImage(file=_image_path))

labels_list = []
for i in range(SIZE):
    for j in range(SIZE):
        x = i * SIZE + j
        _label = tkinter.Label(main_window, image=image_list[x])
        _label.row = i
        _label.column = j
        _label.grid(row=i, column=j)
        labels_list.append(_label)

cur = labels_list[-1]
def upObj(arg):
    return labels_list[(arg.row - 1) * SIZE + arg.column]
def downObj(arg):
    return labels_list[(arg.row + 1) * SIZE + arg.column]
def leftObj(arg):
    return labels_list[arg.row * SIZE + arg.column - 1]
def rightObj(arg):
    return labels_list[arg.row * SIZE + arg.column + 1]

def itemExchange (near):
    x_cur = cur.row * SIZE + cur.column
    x_near = near.row * SIZE + near.column
    cur.row, near.row = near.row, cur.row
    cur.column, near.column = near.column, cur.column
    labels_list[x_cur], labels_list[x_near] = labels_list[x_near], labels_list[x_cur]
    return labels_list[x_cur]
def renderItem(arg):
    arg.grid(row = arg.row, column = arg.column)
def keyPress(arg):
    near = None
    if arg == 'u' and cur.row > 0:
        near = upObj(cur)
    elif arg == 'd' and cur.row < SIZE - 1:
        near = downObj(cur)
    elif arg == 'l' and cur.column > 0:
        near = leftObj(cur)
    elif arg == 'r'and cur.column < SIZE - 1:
        near = rightObj(cur)
    if near:
        near = itemExchange(near)
        renderItem(cur)
        renderItem(near)
        print(cur)
        print(near)

main_window.bind('<Up>', lambda x: keyPress('u'))
main_window.bind('<Down>', lambda x: keyPress('d'))
main_window.bind('<Left>', lambda x: keyPress('l'))
main_window.bind('<Right>', lambda x: keyPress('r'))

main_window.mainloop()
