from data import letters, symbols, numbers
from random import choice, shuffle, randint
import pyperclip
import json


def generate_password(password_form):
    password_list = [choice(letters) for _ in range(randint(8, 10))] + \
                    [choice(symbols) for _ in range(randint(2, 4))] + \
                    [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)
    my_password = "".join(password_list)
    password_form.insert(0, my_password)
    pyperclip.copy(my_password)


def search_password(messagebox, website_form):
    web = website_form.get().strip()
    if len(web) != 0:
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
    else:
        messagebox.showerror(title="Manager", message="Website cannot be empty!")


def save_input(website_form, username_form, password_form, messagebox, end):
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
            website_form.delete(0, end)
            password_form.delete(0, end)
