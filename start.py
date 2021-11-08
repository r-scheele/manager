from random import choice, shuffle, randint
from tkinter import *
from tkinter import messagebox
from data import letters, symbols, numbers
import pyperclip
import json

GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
DEFAULT_EMAIL = "Abdulrahmanolamilekan88@gmail.com"

window = Tk()
window.title("Password manager")
window.config(padx=20, pady=10, bg=YELLOW)


# Generate password
def generate_password():
    password_list = [choice(letters) for _ in range(randint(8, 10))] + \
                    [choice(symbols) for _ in range(randint(2, 4))] + \
                    [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)
    my_password = "".join(password_list)
    password_form.insert(0, my_password)
    pyperclip.copy(my_password)


# Save data to a file
def save_input():
    website_text, email_text, password_text = website_form.get(), username_form.get(), password_form.get()
    if len(website_text) == 0 or len(password_text) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any of the fields empty!")
    else:
        new_data = {
            website_text: {
                "email": email_text,
                "password": password_text
            }
        }

        try:
            with open("secure.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("secure.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("secure.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_form.delete(0, END)
            password_form.delete(0, END)


# Search password
def search_password():
    web = website_form.get().strip()
    try:
        with open("secure.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found!")
    else:
        try:
            email, password = data[web]['email'], data[web]['password']
            pyperclip.copy(password)
            messagebox.showinfo(web, message=f"Username/Email:      {email} \nPassword:                 {password}")
        except KeyError as error_message:
            messagebox.showerror(web, message=f"Details for {error_message} not found!")


# UI setup
canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="password.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=1, column=1)

save_password_label = Label(text="Manager", fg=GREEN, bg=YELLOW, width=35, font=(FONT_NAME, 15, "bold"))
save_password_label.grid(column=0, row=1)

website = Label(text="Website", bg=YELLOW, width=35, font=(FONT_NAME, 10))
website.grid(column=0, row=2)

website_form = Entry(width=42)
website_form.grid(column=1, row=2)
website_form.focus()

search_button = Button(text="Search", width=16, border=0, font=(FONT_NAME, 10), command=search_password)
search_button.grid(column=2, row=2)

username_label = Label(text="Email/Username", bg=YELLOW, font=(FONT_NAME, 10))
username_label.grid(column=0, row=3)

username_form = Entry(width=68)
username_form.grid(column=1, row=3, columnspan=2, pady=4)
username_form.insert(0, DEFAULT_EMAIL)
password_label = Label(text="Password", bg=YELLOW, font=(FONT_NAME, 10))
password_label.grid(column=0, row=4)

password_form = Entry(width=41)
password_form.grid(column=1, row=4)

generate_button = Button(text="Generate Password", border=0, font=(FONT_NAME, 10), command=generate_password)
generate_button.grid(column=2, row=4, padx=8)

add_button = Button(text="Add", border=0, width=51, font=(FONT_NAME, 10), command=save_input)
add_button.grid(column=1, row=5, columnspan=2, pady=10)

window.mainloop()
