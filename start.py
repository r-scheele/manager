from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

window = Tk()
window.title("Password manager")
window.config(padx=10, pady=20, bg=YELLOW)

# UI
canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="password.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website = Label(text="Website", bg=YELLOW, width=35, font=(FONT_NAME, 10))
website.grid(column=0, row=1)

website_form = Entry(width=68)
website_form.grid(column=1, row=1, columnspan=2)

username = Label(text="Email/Username", bg=YELLOW, font=(FONT_NAME, 10))
username.grid(column=0, row=2)

username_form = Entry(width=68)
username_form.grid(column=1, row=2, columnspan=2, pady=4)

password = Label(text="Password", bg=YELLOW, font=(FONT_NAME, 10))
password.grid(column=0, row=3)

password_form = Entry(width=41)
password_form.grid(column=1, row=3)

generate_button = Button(text="Generate Password", border=0, font=(FONT_NAME, 10))
generate_button.grid(column=2, row=3, padx=8)

add_button = Button(text="Add", border=0, width=51, font=(FONT_NAME, 10))
add_button.grid(column=1, row=4, columnspan=2, pady=10)

window.mainloop()
