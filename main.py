#import
import tkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
import random
import pyperclip

#screen
home = tkinter.Tk()
home.geometry("250x350")
home.title("Myzer - Gen")
mainmenu = tkinter.Menu(home)

# Définir la taille minimale et maximale de la fenêtre
home.minsize(250, 350)
home.maxsize(250, 350)

# Couleurs pour le thème dark
dark_bg = "#1f1f1f"
dark_fg = "#FFFFFF"
dark_button_bg = "#333333"
dark_button_fg = "#FFFFFF"

# Configuration des couleurs pour les widgets spécifiques
home.configure(bg=dark_bg)
home.option_add("*Font", "Arial")
home.option_add("*Background", dark_bg)
home.option_add("*Foreground", dark_fg)
home.option_add("*Button.Background", dark_button_bg)
home.option_add("*Button.Foreground", dark_button_fg)


# Définir le chemin de l'icône personnalisée (.ico)
icone_path = "myzer.ico"

# Vérifier si le fichier .ico existe avant de l'utiliser comme icône
try:
    home.iconbitmap(icone_path)
except tkinter.TclError:
    print("Impossible de trouver l'icône personnalisée. L'icône par défaut sera utilisée.")

mainmenu = tkinter.Menu(home)

#label
l1 = Label(text="Bienvenue sur", font="Arial")
l2 = Label(text="My Password Generator", font="Arial")
l1.pack(pady="10")
l2.pack()

#def
def exit():
    quit()

def generate():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "[]{}()';/,._-!@"
    all = lower + upper + numbers + symbols
    length = 16
    password = "".join(random.sample(all, length))
    password_entry.delete(0, END)  # Effacer le texte précédent
    password_entry.insert(0, password)

def copy_password():
    generated_password = password_entry.get()
    if generated_password:
        pyperclip.copy(generated_password)

def toggle_password_visibility():
    password_entry.config(show="" if show_password.get() else "*")

#Bouton
bouton_generate = Button(text="Générer un Mot de Passe", font="Arial", command=generate)
bouton_generate.pack(pady="10")

show_password = IntVar()
show_password_checkbox = Checkbutton(text="Afficher le mot de passe", variable=show_password, command=toggle_password_visibility)
show_password_checkbox.pack()

password_entry = Entry(show="*", font="Arial", fg=dark_fg)  # Ajoutez fg=dark_fg pour définir la couleur du texte
password_entry.pack(pady="10")

bouton_copy = Button(text="Copier le mot de passe", font="Arial", command=copy_password)
bouton_copy.pack()

bouton_exit = Button(text="Quitter", font="Arial", command=exit)
bouton_exit.pack()

l3 = Label(text="Développé par Myzer")
l3.pack(pady="35")

#Menu
frst = tkinter.Menu(mainmenu)
frst.add_radiobutton(label="Quitter", command=exit)

#MainMenu
mainmenu.add_cascade(label="Fichier", menu=frst)

#loop
home.config(menu=mainmenu)
home.mainloop()
