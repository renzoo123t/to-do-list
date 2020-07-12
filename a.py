from tkinter import *

root = Tk()
root.title('TO DO LIST')
root.geometry('500x500')
root.iconbitmap('C:/Users/Renzo Tello/Desktop/Python/GUI/images/list.ico')

principal_label = Label(root, text='Hi!, add a new task: ')

input_box = Entry(root, width=30, borderwidth=3)
input_box.insert(0, 'Task')

def add_task():
    mylabel = Label(root, text=input_box.get())
    mylabel.grid(column=0)

def clear():
    input_box.delete(0, END)

add_button = Button(root, text='Agregar', padx=10, command=add_task, fg='black', bg='#E0E3B6')
clear_button = Button(root, text='Clear', padx=10, command=clear, fg='black', bg='#F2BB2E' )

principal_label.grid(row=0, column=0)
input_box.grid(row=0, column=1, padx=10, pady=10)
add_button.grid(row=0, column=2)
clear_button.grid(row=0, column=3)

root.mainloop()