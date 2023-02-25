from hashlib import sha256
from tkinter import Tk, filedialog, Button, Entry, Label, StringVar
from PIL import Image, ImageTk

root = Tk()
root.title("SHA256 Checker")
width=720
height=220
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)
svgImage = Image.open("icons/button_light_grey.png")
TkImage = ImageTk.PhotoImage(svgImage)

hash_1 = StringVar()
hash_2 = StringVar()
resultText = StringVar()
msg= StringVar()

def openFile():
    global hash_1
    file = filedialog.askopenfilename()
    with open(file, "rb") as f:
        fileContent = f.read()
        hashObject = sha256(fileContent)
        hexDigit = hashObject.hexdigest()
    hash_1.set(hexDigit)

def checkSum():
    global msg
    fontColor = ""
    firstHash = hash_1.get()
    secondHash = hash_2.get()
    if firstHash == secondHash:
        a = "The values do match!"
        msg.set(a)
        fontColor = "#649c4c"
        
    else:
        msg.set("ATTENTION! The values do not match!!!")
        fontColor = "#f76565"
    Label(root, text=msg.get(),font=("RobotoMono-Regular",12),fg=fontColor).place(x=0,y=200,width=720,height=30)

Label(root, text="paste hash here:",font=("RobotoMono",12)).place(x=10,y=3,width=700,height=30)
Entry(root, textvariable=hash_2,justify ="center",font=("RobotoMono-Regular",12)).place(x=60,y=35,width=600,height=30)
Button(root, text="open file", command=openFile,cursor="hand2",font=("RobotoMono-Regular",12)).place(x=310,y=68,width=100,height=30)
Label(root, text="calculated hash from opend file",font=("RobotoMono-Regular",12)).place(x=0,y=101,width=720,height=30)
Entry(root, textvariable=hash_1,justify="center",font=("RobotoMono-Regular",12)).place(x=60,y=134,width=600,height=30)
Button(root, text="check Sum", command=checkSum,cursor="hand2",font=("RobotoMono-Regular",12)).place(x=310,y=167,width=100,height=30)



root.mainloop()
