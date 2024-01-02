from tkinter import *
import random

price1 = random.randint(1, 500)
price2 = ""
chance = 10


def close():
    window.destroy()


def essai():
    global entry, price1, price2, chance, chancetxtvar
    price2 = entry.get()

    if price2.isdigit():
        price2 = int(price2)

        if price2 > price1:
            etattxtvar.set("Moins")
            chance -= 1
            chancetxtvar.set(f"Tentatives : {chance}")

        elif price2 < price1:
            etattxtvar.set("Plus")
            chance -= 1
            chancetxtvar.set(f"Tentatives : {chance}")

        else:
            chancetxtvar.set(f"Tentatives : {chance}")
            button.configure(state=DISABLED)
            entry.configure(state=DISABLED)
            etattxtvar.set(f"Vous avez gagné c'est bien {price1}")
            window.after(2500, close)

    else:
        etattxtvar.set("Vous devez entrer un nombre")

    if chance < 1:
        chance = 0
        button.configure(state=DISABLED)
        entry.configure(state=DISABLED)
        chancetxtvar.set(f"Tentatives : {chance}")
        etattxtvar.set(f"Vous avez perdu c'était {price1}")
        window.after(2500, close)


window = Tk()
window.geometry("600x450")
window.title("Juste-prix")
window.config(background="#2977CA")

frame = Frame(window)
frame2 = Frame(frame, bg="#2977CA")

title = Label(
    frame2,
    text="Choisir un nombre (1-500)",
    bg="#2977CA",
    fg="white",
    font=("Courrier", 30),
)
title.pack(pady=10)

entry = Entry(frame2, bg="#D1F9F2", fg="#2977CA", font=("Courrier", 28))
entry.pack(pady=10)

etattxtvar = StringVar()
etattxtvar.set("Bonne chance !")

text = Label(
    frame2, textvariable=etattxtvar, bg="#2977CA", fg="white", font=("Courrier", 25)
)
text.pack(pady=10)

chancetxtvar = StringVar()
chancetxtvar.set("Tentatives : 10")

text_chance = Label(
    frame2, textvariable=chancetxtvar, bg="#2977CA", fg="white", font=("Courrier", 20)
)
text_chance.pack()

button = Button(
    frame2,
    text="Submit",
    bg="#52B245",
    fg="white",
    font=("Courrier", 20),
    command=essai,
)
button.pack(pady=30)

frame2.grid(row=0, column=1, sticky=W)
frame.pack(expand=YES)

window.mainloop()
