from tkinter import *
from tkinter import messagebox
from manager import generate_password, search_password, save_input

GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
DEFAULT_EMAIL = "Abdulrahmanolamilekan88@gmail.com"

window = Tk()
window.title("Password manager")
window.config(padx=20, pady=10, bg=YELLOW)

manager_label = Label(text="Manager", fg=GREEN, bg=YELLOW, width=35, font=(FONT_NAME, 15, "bold"))
manager_label.grid(column=1, row=1, pady=10)

website_label = Label(text="Website", bg=YELLOW, width=35, font=(FONT_NAME, 10))
website_label.grid(column=0, row=2)

website_form = Entry(width=58)
website_form.grid(column=1, row=2)
website_form.focus()

search_button = Button(text="Search", width=10, border=0, font=(FONT_NAME, 10),
                       command=lambda: search_password(messagebox, website_form))
search_button.grid(column=2, row=2)

username_label = Label(text="Email/Username", bg=YELLOW, font=(FONT_NAME, 10))
username_label.grid(column=0, row=3)

username_form = Entry(width=84)
username_form.grid(column=1, row=3, columnspan=2, pady=4)
username_form.insert(0, DEFAULT_EMAIL)
password_label = Label(text="Password", bg=YELLOW, font=(FONT_NAME, 10))
password_label.grid(column=0, row=4)

password_form = Entry(width=58)
password_form.grid(column=1, row=4)

generate_password_button = Button(text="Generate Password", border=0, font=(FONT_NAME, 10),
                                  command=lambda: generate_password(password_form))
generate_password_button.grid(column=2, row=4, padx=8)

add_button = Button(text="Add", border=0, width=51, font=(FONT_NAME, 10),
                    command=lambda: save_input(website_form, username_form, password_form, messagebox, END))
add_button.grid(column=1, row=5, columnspan=2, pady=10)

window.mainloop()
