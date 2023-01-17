import random
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


def generate_password(num_characters=20, num_numbers=1, num_symbols=1):
    nr_letters = num_characters - num_numbers - num_symbols

    char_list = []
    for char in range(nr_letters):
        char_list.append(random.choice(letters))
    for char in range(num_numbers):
        char_list.append(random.choice(numbers))
    for char in range(num_symbols):
        char_list.append(random.choice(symbols))

    random.shuffle(char_list)
    return "".join(char_list)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_password(website, username, password):
    new_entry = " | ".join([website, username, password])

    with open("data.txt", mode="a") as data:
        data.write(f"{new_entry}\n")


# ---------------------------- UI SETUP ------------------------------- #
def insert_password():
    password_entry.insert(0, generate_password())


def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Missing details", message="Website, username, and password fields are all required.")
    else:
        message_text = f"Website: {website}\nUsername: {username}\nPassword: {password}\n\nSave this password?"
        is_ok = messagebox.askokcancel(title="Confirm Password Entry", message=message_text)

        if is_ok:
            write_password(website, username, password)
            website_entry.delete(0, END)
            password_entry.delete(0, END)


window = Tk()
window.title("MyPass")
window.minsize(width=WIDTH, height=HEIGHT)
window.columnconfigure(0, weight=0)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=0)
window.config(padx=40, pady=30)

# logo
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=0, row=0, columnspan=3)

# website
website_label = Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1, sticky=W)

website_entry = Entry()
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, pady=2, sticky=EW)


# username
username_label = Label(text="Username/email:", font=FONT)
username_label.grid(column=0, row=2, sticky=W)

username_entry = Entry()
username_entry.insert(0, "name@email.com")
username_entry.grid(column=1, row=2, columnspan=2, pady=2, sticky=EW)

# password
password_label = Label(text="Password:", font=FONT)
password_label.grid(column=0, row=3, sticky=W)

password_entry = Entry()
password_entry.grid(column=1, row=3, padx=(0, 5), pady=2, sticky=EW)

# buttons
generate_button = Button(text="Generate", command=insert_password)
generate_button.grid(column=2, row=3, sticky=EW)

add_button = Button(text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2, padx=16, pady=2, sticky=EW)

window.mainloop()
