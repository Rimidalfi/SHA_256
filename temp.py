from hashlib import sha256
from tkinter import Tk, filedialog, Button, Entry, Label, StringVar
import customtkinter


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("720x240")
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
        a = "The values do match!"
        msg.set(a)
        fontColor = "#649c4c"
        
    else:
        msg.set("ATTENTION! The values do not match!!!")
        fontColor = "#f76565"
    customtkinter.CTkLabel(master=app, text=msg.get(),font=("RobotoMono-Regular",12),width=720,height=30).place(x=0,y=200)
    
# button = customtkinter.CTkButton(master=app, text="CTkButton", command=checkSum)
# button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
# entry_ = customtkinter.CTkEntry()


# root = Tk()
# root.title("SHA256 Checker")
# width=720
# height=220


customtkinter.CTkLabel(app, text="paste hash here:",font=("RobotoMono",12),width=700,height=30).place(x=10,y=3,)
customtkinter.CTkEntry(app, textvariable=hash_2,justify ="center",font=("RobotoMono-Regular",12),width=600,height=30).place(x=60,y=35)
customtkinter.CTkButton(app, text="open file", command=openFile,cursor="hand2",font=("RobotoMono-Regular",12),width=100,height=30).place(x=310,y=68)
customtkinter.CTkLabel(app, text="calculated hash from opend file",font=("RobotoMono-Regular",12),width=720,height=30).place(x=0,y=101)
customtkinter.CTkEntry(app, textvariable=hash_1,justify="center",font=("RobotoMono-Regular",12),width=600,height=30).place(x=60,y=134)
customtkinter.CTkButton(app, text="check Sum", command=checkSum,cursor="hand2",font=("RobotoMono-Regular",12),width=100,height=30).place(x=310,y=167)


app.mainloop()