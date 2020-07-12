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
    mycheckbutton = Checkbutton(root, text=input_box.get(), bg='#CECCBE')
    mycheckbutton.grid(column=0, sticky=W)

#clear, for clear btn
def clear():
    input_box.delete(0, END)

#btn area
add_button = Button(root, text='Add', padx=10, command=add_task, fg='black', bg='#E0E3B6')
clear_button = Button(root, text='Clear', padx=10, command=clear, fg='black', bg='#F2BB2E' )

#adding switch mode
btn_state = False

def switch():
    global btn_state
    if btn_state:
        btn.config(image=off_img, bg="#CECCBE", activebackground="#CECCBE")
        root.config(bg="#CECCBE")
        principal_label.config(text='Hi!, add a new task: ', bg="#CECCBE", fg='#2B2B2B')
        btn_state = False
    else:
        btn.config(image=on_img, bg="#2B2B2B", activebackground="#2B2B2B")
        root.config(bg="#2B2B2B")
        principal_label.config(text='Hi!, add a new task: ', bg="#2B2B2B", fg="#CECCBE")
        btn_state = True

on_img = PhotoImage(file=r'switch-on.png')
off_img = PhotoImage(file=r'switch-off.png')

btn = Button(root, text="OFF", borderwidth=0, command=switch, bg="#CECCBE", activebackground="#CECCBE")
btn.config(image=off_img)

#to put the widgets
principal_label.grid(row=0, column=0)
input_box.grid(row=0, column=1, padx=10, pady=10)
add_button.grid(row=0, column=2)
clear_button.grid(row=0, column=3)
btn.grid(row=0, column=4)

#window in mainloop
root.mainloop()