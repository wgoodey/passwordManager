import random
import pyperclip
from tkinter import *
from tkinter import messagebox

WIDTH = 500
HEIGHT = 375
FONT = ("Arial", 11, "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password(length=20, num_numbers=1, num_symbols=1):
    num_letters = length - num_numbers - num_symbols

    letters_list = [random.choice(letters) for _ in range(num_letters)]
    numbers_list = [random.choice(numbers) for _ in range(num_numbers)]
    symbols_list = [random.choice(symbols) for _ in range(num_symbols)]

    char_list = letters_list + numbers_list + symbols_list

    random.shuffle(char_list)
    return "".join(char_list)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_to_file(website, username, password):
    new_entry = " | ".join([website, username, password])

    with open("data.txt", mode="a") as data:
        data.write(f"{new_entry}\n")


# ---------------------------- UI SETUP ------------------------------- #
def insert_password():
    password_length = int(length_spinbox.get())
    num_numbers = int(numbers_spinbox.get())
    num_symbols = int(symbols_spinbox.get())

    if num_symbols + num_numbers > password_length:
        messagebox.showerror(title="Incorrect Parameters",
                             message="The password length must be greater than or equal to the total numbers and "
                                     "symbols.")
    else:
        password_entry.delete(0, END)
        password_entry.insert(0, generate_password(password_length, num_numbers, num_symbols))
        pyperclip.copy(password_entry.get())


def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Missing details",
                             message="Website, username, and password fields are all required.")
    else:
        message_text = f"Website: {website}\nUsername: {username}\nPassword: {password}\n\nSave this password?"
        is_ok = messagebox.askokcancel(title="Confirm Password Entry", message=message_text)

        if is_ok:
            write_to_file(website, username, password)
            website_entry.delete(0, END)
            password_entry.delete(0, END)


window = Tk()
window.title("MyPass")
window.minsize(width=WIDTH, height=HEIGHT)
window.columnconfigure(0, weight=0)
window.columnconfigure(1, weight=0)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=0)
window.columnconfigure(4, weight=0)
window.columnconfigure(5, weight=0)
window.columnconfigure(6, weight=0)
window.columnconfigure(7, weight=0)
window.config(padx=40, pady=30)

# logo
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=0, row=0, columnspan=7)

# website
website_label = Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1, columnspan=2, sticky=W)

website_entry = Entry()
website_entry.focus()
website_entry.grid(column=2, row=1, columnspan=2, pady=2, sticky=EW)

# username
username_label = Label(text="Username/email:", font=FONT)
username_label.grid(column=0, row=2, columnspan=2, sticky=W)

username_entry = Entry()
username_entry.grid(column=2, row=2, columnspan=2, pady=2, sticky=EW)

# password
password_label = Label(text="Password:", font=FONT)
password_label.grid(column=0, row=3, columnspan=2, sticky=W)

password_entry = Entry()
password_entry.grid(column=2, row=3, columnspan=2, pady=2, sticky=EW)

# password options
# length of password
length_label = Label(text="Length:", font=FONT)
length_label.grid(column=0, row=4, padx=(1, 1), sticky=W)

length_default = StringVar(window)
length_default.set("20")
length_spinbox = Spinbox(window, width=3, from_=6, to=30, textvariable=length_default)
length_spinbox.grid(column=1, row=4, padx=(1, 1), sticky=W)

# number of numbers in password
numbers_label = Label(text="Numbers:", font=FONT)
numbers_label.grid(column=0, row=5, padx=(1, 1), sticky=W)

symbols_default = StringVar(window)
symbols_default.set("2")
numbers_spinbox = Spinbox(window, width=3, from_=0, to=6, textvariable=symbols_default)
numbers_spinbox.grid(column=1, row=5, padx=(1, 1), sticky=W)

# number of symbols in password
symbols_label = Label(text="Symbols:", font=FONT)
symbols_label.grid(column=0, row=6, padx=(1, 1), sticky=W)

symbols_default = StringVar(window)
symbols_default.set("2")
symbols_spinbox = Spinbox(window, width=3, from_=0, to=6, textvariable=symbols_default)
symbols_spinbox.grid(column=1, row=6, padx=(1, 1), sticky=W)

# buttons
generate_button = Button(text="Generate", command=insert_password)
generate_button.grid(column=2, row=4, pady=2)

add_button = Button(text="Add", command=save)
add_button.grid(column=2, row=6, columnspan=2, padx=16, pady=2, sticky=EW)

window.mainloop()
