from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
EMAIL = ''

with open('data/passwords.txt', 'a') as create_file:
    pass

with open('data/passwords.txt', 'r') as file:
    first_line = file.readline()
    if first_line != "":
        contents = first_line.split(' | ')
        EMAIL = contents[1]


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(END, password)
    copy_to_clip = messagebox.askyesno(title="Password", message=f'Copy password to clipboard?')
    if copy_to_clip:
        pyperclip.copy(password)
        messagebox.showinfo(title="Password", message=f'Password {password} copied to the clipboard')


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = web_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    if website == "" or email == "" or password == "":
        messagebox.showerror(title="Oops", message='Fields left empty')
    else:
        is_ok = messagebox.askokcancel(title=f'Website: {website}', message=f'Details entered: \n\n'
                                                                            f'Email: {email} \n'
                                                                            f'Password: {password} \n')
        if is_ok:
            with open('data/passwords.txt', 'a') as data:
                data.write(f'{website} | {email} | {password}\n')
                web_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(pady=50, padx=50)
window.title('Password Manager')

# Create a Canvas
canvas = Canvas(width=200, height=200)
my_pass_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=my_pass_img)
canvas.grid(column=1, row=0)

# Web Label
web_label = Label(text='Website:')
web_label.grid(column=0, row=1)
web_entry = Entry()
web_entry.focus()
web_entry.grid(column=1, row=1, columnspan=2, sticky='EW')

# Email Label
email_username_label = Label(text='Email/Username:')
email_username_label.grid(column=0, row=2)
email_username_entry = Entry()
email_username_entry.grid(column=1, row=2, columnspan=2, sticky='EW')
email_username_entry.insert(END, EMAIL)

# Pass Label
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky='EW')

# Generate Password Button
gen_pass_button = Button(text='Generate Password', command=password_gen)
gen_pass_button.grid(column=2, row=3, sticky='EW')

# Add Button
add_button = Button(text='Add', command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky='EW')

window.mainloop()
