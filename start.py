from random import choice, shuffle, randint
from tkinter import *
from tkinter import messagebox
from data import letters, symbols, numbers
import pyperclip

GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

window = Tk()
window.title("Password manager")
window.config(padx=10, pady=10, bg=YELLOW)


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
    website_text, username_text, password_text = website_form.get(), username_form.get(), password_form.get()
    is_empty = not bool(website_text and password_text)
    if not is_empty:
        is_okay = messagebox.askokcancel(title=website_text,
                                         message=f"These are the details entered: \nEmail: {username_text} "
                                                 f"\nPassword: {password_text} \nIs it okay to save?")
        if is_okay:
            with open("secure.txt", "a") as file:
                file.write(f"{website_text} | {username_text} | {password_text}\n")
                website_form.delete(0, END)
                password_form.delete(0, END)
    else:
        messagebox.showinfo(title="Oops", message="Please don't leave any of the fields empty!")


# Get data from file
def password():
    get_password_for = get_password_form.get()
    print(get_password_for)


# UI setup
canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="password.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

save_password_label = Label(text="Save Password", fg=GREEN, bg=YELLOW, width=35, font=(FONT_NAME, 10, "bold"))
save_password_label.grid(column=1, row=1)

website = Label(text="Website", bg=YELLOW, width=35, font=(FONT_NAME, 10))
website.grid(column=0, row=2)

website_form = Entry(width=68)
website_form.grid(column=1, row=2, columnspan=2)
website_form.focus()
username_label = Label(text="Email/Username", bg=YELLOW, font=(FONT_NAME, 10))
username_label.grid(column=0, row=3)

username_form = Entry(width=68)
username_form.grid(column=1, row=3, columnspan=2, pady=4)
username_form.insert(0, "Abdulrahmanolamilekan88@gmail.com")
password_label = Label(text="Password", bg=YELLOW, font=(FONT_NAME, 10))
password_label.grid(column=0, row=4)

password_form = Entry(width=41)
password_form.grid(column=1, row=4)

generate_button = Button(text="Generate Password", border=0, font=(FONT_NAME, 10), command=generate_password)
generate_button.grid(column=2, row=4, padx=8)

add_button = Button(text="Add", border=0, width=51, font=(FONT_NAME, 10), command=save_input)
add_button.grid(column=1, row=5, columnspan=2, pady=10)

# Get password UI
# Add entry for the website you need to get its details
# Button to get the password
# Label to display it
# Copy the password and username to the clipboard

recover_password_label = Label(text="Get Password", bg=YELLOW, fg=GREEN, width=35, font=(FONT_NAME, 10, "bold"))
recover_password_label.grid(column=1, row=6, pady=10)

get_password_label = Label(text="Website", bg=YELLOW, width=35, font=(FONT_NAME, 10))
get_password_label.grid(column=0, row=7)

get_password_form = Entry(width=68)
get_password_form.grid(column=1, row=7, columnspan=2)

get_password_button = Button(text="Get Password", border=0, width=51, font=(FONT_NAME, 10), command=password)
get_password_button.grid(column=1, row=8, columnspan=2, pady=5)

window.mainloop()
