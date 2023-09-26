from tkinter import *
from tkinter import messagebox
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random


def generatePass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char
    passwordEntry.delete(0, END)
    passwordEntry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    if website.get() == "" or passwordEntry.get() == "":
        messagebox.showerror(title="Empty field", message="you have left some fields empty")
    else:
        info = {
            website.get(): {
                "password": passwordEntry.get(),
                "email": email.get(),
            }
        }
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(info)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(info, file)
        else:
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
                website.delete(0, END)
                passwordEntry.delete(0, END)
        finally:
            messagebox.showinfo(title="Successful!", message="Successfully Saved")


def search():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            p = data[website.get()]["password"]
            e = data[website.get()]["email"]
        email.delete(0 , END)
        email.insert(0, e)
        passwordEntry.delete(0, END)
        passwordEntry.insert(0, p)
    except FileNotFoundError:
        messagebox.showerror(title="Empty", message="no data")
    except KeyError as key:
        messagebox.showerror(message=f"{key} is not found")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(width=200, height=200, padx=50, pady=50)
canvas = Canvas(width=200,height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

l1 = Label(text="Website:")
l1.grid(column=0, row=1)
l2 = Label(text="Email/Username")
l2.grid(column=0, row=2)
l3 = Label(text="password")
l3.grid(column=0, row=3)

searchB = Button(text="search", width=10, command=search)
searchB.grid(column=2, row=1)
add = Button(text="Add", width=30, command=save)
add.grid(column=1, row=4, columnspan=2)
generate = Button(text="Generate pass", command=generatePass)
generate.grid(column=2, row=3)

website = Entry(width=21)
website.focus()
website.grid(column=1, row=1)
email = Entry(width=35)
email.insert(0, "hyasat.mohannad@gmail.com")
email.grid(columnspan=2, column=1, row=2)
passwordEntry = Entry(width=21)
passwordEntry.grid(column=1, row=3)









window.mainloop()