from hashlib import sha256
from tkinter import filedialog, StringVar
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()
app.iconbitmap("icons/app_icon.ico")
app.geometry("700x260")
app.title("SHA256 Checker")
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
        a = "The hashes do match!"
        msg.set(a)
        fontColor = "#649c4c"
        
    else:
        msg.set("ATTENTION! The hashes do not match!!!")
        fontColor = "#f76565"
    customtkinter.CTkLabel(master=app, text=msg.get(),font=("Liberation Mono Bold",16),width=700,height=30,text_color=fontColor).place(x=0,y=217)

customtkinter.CTkLabel(app, text="paste hash here:",font=("Liberation Mono",12),width=700,height=30).place(x=0,y=3)
customtkinter.CTkEntry(app, textvariable=hash_2,justify ="center",font=("Liberation Mono",12),width=600,height=30,border_width=1).place(x=50,y=35)
customtkinter.CTkButton(app, text="open file", command=openFile,cursor="hand2",font=("Liberation Mono",12),width=100,height=30).place(x=300,y=73)
customtkinter.CTkLabel(app, text="calculated hash from opend file",font=("Liberation Mono",12),width=700,height=30).place(x=0,y=105)
customtkinter.CTkEntry(app, textvariable=hash_1,justify="center",font=("Liberation Mono",12),width=600,height=30,border_width=1).place(x=50,y=139)
customtkinter.CTkButton(app, text="check Sum", command=checkSum,cursor="hand2",font=("Liberation Mono",12),width=100,height=30).place(x=300,y=177)

app.mainloop()