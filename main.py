import os
import shutil
from tkinter import filedialog
from tkinter import *


def arrange():
    file = filedialog.askdirectory()
    files = os.listdir(file)
    for i in files:
        if os.path.splitext(i)[1] in [".txt", ".docx", ".pdf", ".doc", ".rtf", ".tex", ".wpd"]:
            if "Documents" not in os.listdir(file):
                os.mkdir(f"{file}/Documents")
            shutil.move(f"{file}/{i}", f"{file}/Documents")
        elif os.path.splitext(i)[1] in [".jpeg", ".jpg", ".png", ".gif", ".tiff", ".psd", ".raw"]:
            if "Photos" not in os.listdir(file):
                os.mkdir(f"{file}/Photos")
            shutil.move(f"{file}/{i}", f"{file}/Photos")
        elif os.path.splitext(i)[1] in [".mp4", ".mov", ".avi", ".wmv", "f4v", "flv", "swf"]:
            if "Videos" not in os.listdir(file):
                os.mkdir(f"{file}/Videos")
            shutil.move(f"{file}/{i}", f"{file}/Videos")
        elif os.path.splitext(i)[1] in [".csv",".xlsx"]:
            if "Spreadsheets" not in os.listdir(file):
                os.mkdir(f"{file}/Spreadsheets")
            shutil.move(f"{file}/{i}", f"{file}/Spreadsheets")
        elif os.path.splitext(i)[1] in [".ppt"]:
            if "Presentations" not in os.listdir(file):
                os.mkdir(f"{file}/Presentations")
            shutil.move(f"{file}/{i}", f"{file}/Presentations")
        else:
            if "Others" not in os.listdir(file):
                os.mkdir(f"{file}/Others")
            shutil.move(f"{file}/{i}", f"{file}/Others")


root = Tk()
root.title("File Organizer")
root.geometry("1100x200")
btn = Button(root,text="Select Folder", bg="black", font="lucid 16 bold", foreground="white", command=arrange)
btn.pack()
frame = Frame(root).pack(side="top")
t1 = Label(frame,text="Usage:", font="Arial 16 bold").pack(side="top")
t2 = Label(frame,text="1. Select the folder in which you want to organize the files", font="Arial 16 bold").pack(side="top")
t3 = Label(frame,text="2. After selecting the folder the files of the folder will be arranged in their corresponding "
                      "sub folders", font="Arial 16 bold").pack(side="top")
root.mainloop()
