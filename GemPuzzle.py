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
print(files_list_path)
label_1 = tkinter.Label(main_window, text = 'Hello World!')
label_1.pack()
main_window.mainloop()
