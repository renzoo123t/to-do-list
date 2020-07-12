from tkinter import *

#setting root window:
root = Tk()
root.title('TO DO LIST')
root.geometry('500x500')
root.config(bg='#CECCBE')
root.iconbitmap('C:/Users/Renzo Tello/Desktop/Python/GUI/images/list.ico')

principal_label = Label(root, text='Hi!, add a new task: ', bg='#CECCBE')

#box to write the tasks
input_box = Entry(root, width=30, borderwidth=3)
input_box.insert(0, 'Task')

#add_task, for add btn
def add_task():
    mycheckbutton = Checkbutton(root, text=input_box.get())
    mycheckbutton.grid(column=0, sticky=W)

#clear, for clear btn
def clear():
    input_box.delete(0, END)

#btn area
add_button = Button(root, text='Add', padx=10, command=add_task, fg='black', bg='#E0E3B6')
clear_button = Button(root, text='Clear', padx=10, command=clear, fg='black', bg='#F2BB2E' )

#to put the widgets
principal_label.grid(row=0, column=0)
input_box.grid(row=0, column=1, padx=10, pady=10)
add_button.grid(row=0, column=2)
clear_button.grid(row=0, column=3)

root.mainloop()