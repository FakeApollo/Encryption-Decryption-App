from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    password = code.get()
    if password == "1122":
        screen2 = Toplevel(screen)
        screen2.title("DECRYPTION")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")
        
        message = text1.get(1.0,END)
        decode_message = message.encode("ascii")
        base64_byte = base64.b64decode(decode_message)
        decrypt = base64_byte.decode("ascii")
        
        
        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
        text2 = Text(screen2, font="Robote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        
        text2.insert(END,decrypt)
    
    elif password == "":
        messagebox.showerror("decryption", "Input Password")
    elif password != "1122":
        messagebox.showerror("decryption", "Invalid Password")

        
def encrypt():
    password = code.get()
    if password == "1122":
        screen1 = Toplevel(screen)
        screen1.title("ENCRYPTION")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")
        
        message = text1.get(1.0,END)
        encode_message = message.encode("ascii")
        base64_byte = base64.b64encode(encode_message)
        encrypt = base64_byte.decode("ascii")
        
        
        Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Robote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        
        text2.insert(END,encrypt)
    
    elif password == "":
        messagebox.showerror("encryption", "Input Password")
    elif password != "1122":
        messagebox.showerror("encryption", "Invalid Password")
        

def main_screen():
    global screen
    global code
    global text1
    screen = Tk()
    screen.geometry("600x400")
    
    #icons
    image_icon = PhotoImage(file="icon.png")
    screen.iconphoto(False,image_icon)
    
    def reset():
        code.set("")
        text1.delete(1.0,END)
        
    
    screen.title("PctApp")
    
    Label(text="Enter text for Encryption or Decryption", fg="black", font=("calbri",14)).place(x=10,y=10)
    text1 = Text(font="Robote 12", bg="white", relief=GROOVE,wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=580, height=100)
    
    Label(text="Enter secret key for encryption and decryption", fg="black", font=("calibri", 14)).place(x=10, y=170)
    code = StringVar()
    Entry(textvariable=code,width=10,bd=0,font=("arial", 25),show="*").place(x=10,y=200)
    
    Button(text="ENCRYPT", height="2", width=35,bg="#ed3833", fg="white", bd=0,command=encrypt).place(x=10,y=250)
    Button(text="DECRYPT", height="2", width=35,bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=330, y=250)
    Button(text="RESET", height="2", width=80,bg="#1089ff", fg="white", bd=0,command=reset).place(x=10, y=300)
    
    
    
    screen.mainloop()
    
main_screen()