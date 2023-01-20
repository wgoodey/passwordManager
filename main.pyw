import random
import string
import json
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

WIDTH = 500
HEIGHT = 375
FONT = ("Arial", 11, "normal")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password(length=20, num_numbers=1, num_symbols=1):
    num_letters = length - num_numbers - num_symbols

    char_list = random.choices(string.ascii_letters, k=num_letters) + \
                random.choices(string.digits, k=num_numbers) + \
                random.choices(string.punctuation, k=num_symbols)

    random.shuffle(char_list)
    return "".join(char_list)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def load_data():
    with open("data.json", mode="r") as file:
        return json.load(file)


def write_to_file(website, username, password):
    def write_new_file():
        with open("data.json", mode="w") as new_file:
            json.dump(new_entry, new_file, indent=4)

    new_entry = {
        website: {
            "username": username,
            "password": password
        }
    }

    try:
        data = load_data()

    except FileNotFoundError:
        print("New file Created.")
        write_new_file()

    except json.decoder.JSONDecodeError:
        is_ok = messagebox.askokcancel(title="JSON file error",
                                       message='The data file "data.json" could not be decoded. '
                                               'Would you like to create a new one for this entry?')
        if is_ok:
            write_new_file()
        else:
            return False

    else:
        data.update(new_entry)
        with open("data.json", mode="w") as file:
            json.dump(data, file, indent=4)
            return True


def delete_entry(site_name):
    data = load_data()
    data.pop(site_name)

    with open("data.json", mode="w") as file:
        json.dump(data, file, indent=4)


# ---------------------------- UI SETUP ------------------------------- #
def clear_details():
    website_combobox.delete(0, END)
    password_entry.delete(0, END)


def insert_password():
    password_length = int(length_spinbox.get())
    num_numbers = int(numbers_spinbox.get())
    num_symbols = int(symbols_spinbox.get())

    if num_symbols + num_numbers > password_length:
        messagebox.showerror(title="Incorrect Parameters",
                             message="The password length must be greater than or equal to the total numbers and "
                                     "symbols.")
    else:
        # insert password into text field
        password_entry.delete(0, END)
        password_entry.insert(0, generate_password(password_length, num_numbers, num_symbols))

        # copy password to clipboard
        password_entry.clipboard_clear()
        password_entry.clipboard_append(password_entry.get())


def save():
    website = website_combobox.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Missing details",
                             message="Website, username, and password fields are all required.")

    if website in get_websites_list():
        is_ok = messagebox.askokcancel(title="Entry already exists",
                                       message=f"An entry for {website} already exists. "
                                               f"Do you want to overwrite it?")
        if not is_ok:
            return

    if write_to_file(website, username, password):
        messagebox.showinfo(title="Success", message=f"Entry for {website} successfully added.")

        clear_details()
        website_combobox.config(values=get_websites_list())


def get_websites_list():
    try:
        with open("data.json", mode="r") as file:
            websites = [key for key in json.load(file)]
            websites.sort(key=str.lower)
            return websites

    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        return []


def delete():
    site_name = website_combobox.get()
    try:
        delete_entry(site_name)
    except KeyError:
        pass
    else:
        clear_details()
        messagebox.showinfo(title="Entry deleted", message=f"Entry for {site_name} has been deleted.")
        website_combobox.config(values=get_websites_list())


def website_selected(event):
    with open("data.json", mode="r") as file:
        data = json.load(file)
        selected_entry = data[website_combobox.get()]

        username_entry.delete(0, END)
        password_entry.delete(0, END)
        username_entry.insert(0, selected_entry["username"])
        password_entry.insert(0, selected_entry["password"])


window = Tk()
window.title("MyPass")
window.minsize(width=WIDTH, height=HEIGHT)
window.columnconfigure(0, weight=0)
window.columnconfigure(1, weight=0)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=0)
window.config(padx=40, pady=30)

# logo
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=0, row=0, columnspan=4)

# website
website_label = Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1, columnspan=2, sticky=W)

selected_website = StringVar()
website_combobox = ttk.Combobox(textvariable=selected_website, values=get_websites_list())
website_combobox.bind('<<ComboboxSelected>>', website_selected)
website_combobox.focus()
website_combobox.grid(column=2, row=1, pady=2, sticky=EW)

delete_button = Button(text="Delete", command=delete)
delete_button.grid(column=3, row=1, padx=(4, 0), sticky=E)

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
symbols_default.set("4")
numbers_spinbox = Spinbox(window, width=3, from_=0, to=6, textvariable=symbols_default)
numbers_spinbox.grid(column=1, row=5, padx=(1, 1), sticky=W)

# number of symbols in password
symbols_label = Label(text="Symbols:", font=FONT)
symbols_label.grid(column=0, row=6, padx=(1, 1), sticky=W)

symbols_default = StringVar(window)
symbols_default.set("4")
symbols_spinbox = Spinbox(window, width=3, from_=0, to=6, textvariable=symbols_default)
symbols_spinbox.grid(column=1, row=6, padx=(1, 1), sticky=W)

# buttons
generate_button = Button(text="Generate", command=insert_password)
generate_button.grid(column=3, row=4, pady=2, sticky=E)

add_button = Button(text="Add", command=save)
add_button.grid(column=2, row=6, padx=16, pady=2, sticky=EW)

clear_button = Button(text="Clear", command=clear_details)
clear_button.grid(column=3, row=6, sticky=E)

window.mainloop()
