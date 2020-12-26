from tkinter import *

window = Tk()
window.title("Bernco GUI")
window.minsize(width=400, height=400)

# label
m_label = Label(text="Hello world", font=("Arial", 14))
m_label.grid(column=1, row=1)


# def button_clicked():
#     m_label.config(text=f"{m_text.get(1.0, END)}")
#

# button
m_button = Button(text="Click me")
m_button.grid(column=2, row=2)

# button
m_button2 = Button(text="Click you")
m_button2.grid(column=3, row=1)

# entry
m_entry = Entry()
m_entry.insert(END, "email: ")
m_entry.grid(column=4, row=3)

window.mainloop()
