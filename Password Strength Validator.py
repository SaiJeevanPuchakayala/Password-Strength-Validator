# Importing the required modules
import re
from tkinter import *
import pandas as pd


# loading the common passwords and words datasets
common_passwords = list(pd.read_csv("common_userpasswords.txt"))
common_words = list(pd.read_csv("commonly_used_words.txt",header=None,squeeze=True))


# Strong Password Regexes
pass_length_regex = re.compile(r'.{8,}')       # >= 8 characters

pass_upper_regex = re.compile(r'[A-Z]')        # Contains an upper case letter

pass_lower_regex = re.compile(r'[a-z]')        # Contains a lower case letter

pass_digit_regex = re.compile(r'[0-9]')        # Contains a digit

pass_character_regex = re.compile(r'[$&+,:;=?@#|.^*()%!-]')    # Contains a special character


#calling Tk() method
root = Tk()

#title() method is used to change the title 
root.title(" Jeevan's Password Strenght Validator ")

#geometry() method is used to resize the Gui Window
root.geometry("400x200")

#Sets the Tkinter Window Background Color
root.configure(bg='orange')

#Sets Window Icon in Tkinter
root.iconbitmap('icon.ico')

# Lable() function creates a label widget
l =  Label(root, text="🔒 Password Strenght Validator 🔒",font=('verdana',12,'bold'),fg="black",bg="orange")
l.place(x=50,y=10)

# Lable() function creates a label widget
l1 = Label(root, text = "Password:",font=('verdana',12,'bold'),fg="black",bg="orange")
l1.place(x=10,y=60)

# entry widgets, used to take entry from user
Password = Entry(root, font=("Helvetica", 10, "bold"))
Password.pack(fill=None, padx = 120,pady=60,ipadx = 200,ipady = 3)


def tick() :
    if var.get() == 1 :
        Password.configure(show = "x")
    elif var.get() == 0 :
        Password.configure(show = "")
var = IntVar()  
bt = Checkbutton(root,cursor='hand2', command = tick,text = "Hide", offvalue = 0, onvalue = 1, variable = var,font=('Helvetica',10),bg="orange",fg="black")
bt.place(x = 300, y = 60)


def passwrd_strength_checker(text):
    p = None
    if len(text) == 0:
        p = "Password can not be Blank _______________________!"
        checkStrLab.config(text = p)
        return False
    
    if text.lower() in common_passwords:
        p = "__Password Must not be a common user password!___"
        checkStrLab.config(text = p)
        return False
    
    if text.lower() in common_words:
        p = "_____Password Must not be a common Word!______"
        checkStrLab.config(text = p)
        return False
    
    if pass_length_regex.search(text) is None:
        p = "Password Must Contain atleast More Than 8 characters!"
        checkStrLab.config(text = p)
        return False
    
    if pass_upper_regex.search(text) is None:
        p = "Password Must Contain atleast one UPPER CASE letter!"
        checkStrLab.config(text = p)
        return False
    if pass_lower_regex.search(text) is None:
        p = "Password Must contain atleast one LOWER CASE letter!"
        checkStrLab.config(text = p)
        return False
    if pass_digit_regex.search(text) is None:
        p = "Password  Must contain atleast one Numerical Number!"
        checkStrLab.config(text = p)
        return False
    if pass_character_regex.search(text) is None:
        p = "Password Must contain atleast one Special Character!"
        checkStrLab.config(text = p)
        return False
    else:
        return True
    
    
def checkPassword():
    r = None
    lower_password = None
    password = Password.get().replace(" ","")
    lower_password = password.lower()
    if passwrd_strength_checker(password) is True:
        p = "______Remember to use it for one site only.________"
        r = '[Perfect] *Strong Password* [Perfect]'
        checkStrLab.config(text = p)
        checkStrLab1.config(text = r)
    else:
        r = '[Warning] *!Weak Password!* [Warning]'
        checkStrLab1.config(text = r)

    

checkStrBtn = Button(root, text="✔ CHECK", command=checkPassword,font=('verdana',10,'bold'),bg="gray",fg="white",cursor='hand2')
checkStrBtn.place(x=250,y=150)


checkStrLab = Label(root,font=('Helvetica',9,'bold'),bg="orange",fg="blue2")
checkStrLab.place(x=35,y=100)


checkStrLab1 = Label(root,font=('Helvetica',10,'bold'),bg="orange",fg="red2")
checkStrLab1.place(x=70,y=120)


# Button for closing 
exit_button = Button(root, text="X EXIT", command=root.destroy,font=('verdana',10,'bold'),bg="gray",fg="white",cursor='hand2') 
exit_button.place(x=70,y=150)


# Disables resizing in a Tkinter Window.
root.resizable(False, False) 


#mainloop() is used to load the GUI Window
root.mainloop()

input("Press Enter to exit")
