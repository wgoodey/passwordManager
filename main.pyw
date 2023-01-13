from tkinter import *

WIDTH = 500
HEIGHT = 375
FONT = ("Arial", 11, "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
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
website_entry.grid(column=1, row=2, columnspan=2, pady=2, sticky=EW)

# username
username_label = Label(text="Username/email:", font=FONT)
username_label.grid(column=0, row=2, sticky=W)

username_entry = Entry()
username_entry.grid(column=1, row=1, columnspan=2, pady=2, sticky=EW)

# password
password_label = Label(text="Password:", font=FONT)
password_label.grid(column=0, row=3, sticky=W)

password_entry = Entry()
password_entry.grid(column=1, row=3, padx=(0, 5), pady=2, sticky=EW)

# buttons
generate_button = Button(text="Generate")
generate_button.grid(column=2, row=3, sticky=EW)

add_button = Button(text="Add")
add_button.grid(column=1, row=4, columnspan=2, padx=16, pady=2, sticky=EW)


window.mainloop()
