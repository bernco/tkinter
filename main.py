from tkinter import *

window = Tk()
window.title("Bernco GUI")
window.minsize(width=400, height=400)

# label
m_label = Label(text="Hello world", font=("Arial", 14))
m_label.pack()


def button_clicked():
    m_label.config(text=f"{m_text.get(1.0, END)}")


# button
m_button = Button(text="Click me", command=button_clicked)
m_button.pack()

# entry
m_entry = Entry()
m_entry.insert(END, "email: ")
m_entry.pack()

# Text
m_text = Text(height=4, width=20)
m_text.focus()
m_text.insert(END, "enter")
m_text.pack()


# spinbox
m_spinbox = Spinbox(width=6,from_=0, to=10)
m_spinbox.pack()

# scale
def scale_read(value):
    print(value)
m_scale = Scale(from_=100, to=0, command=scale_read)
m_scale.pack()


# checkbutton
def check_read():
    print(check.get())
check = IntVar()
m_checkbutton = Checkbutton(text="yes", command=check_read, variable=check)
# check.get()
m_checkbutton.pack()

# radiobutton
radio_state = IntVar()
m_radiobutton_1 = Radiobutton(text="on", variable=radio_state, value=1)
m_radiobutton_2 = Radiobutton(text="off", variable=radio_state, value=2)
m_radiobutton_1.pack()
m_radiobutton_2.pack(side="left")


# Listbox
def list_select(event):
    print(m_listbox_1.get(m_listbox_1.curselection()))


m_listbox_1 = Listbox(height=3, width=22)
listed_names = ["adam", "Emanuela", "paul", "josh"]

for names in listed_names:
    m_listbox_1.insert(listed_names.index(names), names)
m_listbox_1.bind("<<ListboxSelect>>", list_select)
m_listbox_1.pack(side="left")

window.mainloop()
