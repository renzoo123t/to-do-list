from tkinter import *

root = Tk()
root.title('TO DO LIST')
root.geometry('500x500')

principal_label = Label(root, text='Hi!, add a new task: ')

input_box = Entry(root, width=30, borderwidth=3)
input_box.insert(0, 'Task')

def add_task():
    mylabel = Label(root, text=input_box.get())
    mylabel.grid(column=0)

mybutton = Button(root, text='Agregar', padx=10, command=add_task, fg='black', bg='#E0E3B6')


principal_label.grid(row=0, column=0)
input_box.grid(row=0, column=1, padx=10, pady=10)
mybutton.grid(row=0, column=2)

root.mainloop()