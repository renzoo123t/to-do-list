from tkinter import *

#setting root window:
root = Tk()
root.title('TO DO LIST')
width_value = int((root.winfo_screenwidth())/2)
height_value = int((root.winfo_screenheight())/2)
root.geometry(f'{width_value}x{height_value}+0+0')
root.config(bg='#CECCBE')
root.iconbitmap('./images/list.ico')

on_img = PhotoImage(file=r'./images/switch-on.png') 
off_img = PhotoImage(file=r'./images/switch-off.png')

principal_label = Label(root, text='Hi!, add a new task: ', bg='#CECCBE')

#box to write the tasks
input_box = Entry(root, width=30, borderwidth=3)
input_box.insert(0, 'Task')

a = [ ]
#add_task, for add btn
def add_task():
    global a      
    mycheckbutton = Checkbutton(root, text=input_box.get(), bg='#CECCBE')
    mycheckbutton.grid(column=0, sticky=W)
    a.append(mycheckbutton)
    
#clear, for clear btn
def clear():
    input_box.delete(0, END)

def switch():
    global btn_state
    
    if btn_state:
        btn.config(image=off_img, bg="#CECCBE", activebackground="#CECCBE")
        root.config(bg="#CECCBE")
        principal_label.config(text='Hi!, add a new task: ', bg="#CECCBE", fg='#2B2B2B')
        for i in a:
            i.config(bg="#CECCBE", fg='#2B2B2B')
        btn_state = False
    else:
        btn.config(image=on_img, bg="#2B2B2B", activebackground="#2B2B2B")
        root.config(bg="#2B2B2B")
        principal_label.config(text='Hi!, add a new task: ', bg="#2B2B2B", fg="#CECCBE")
        for i in a:
            i.config(bg="#2B2B2B", fg="#CECCBE")
        btn_state = True

#adding switch mode
btn_state = False

#btn area
add_button = Button(root, text='Add', padx=10, command=add_task, fg='black', bg='#E0E3B6')
clear_button = Button(root, text='Clear', padx=10, command=clear, fg='black', bg='#F2BB2E' )
btn = Button(root, bd=0, command=switch, bg="#CECCBE", activebackground="#CECCBE")
btn.config(image=off_img)

#to put the widgets
principal_label.grid(row=0, column=0)
input_box.grid(row=0, column=1, padx=10, pady=10)
add_button.grid(row=0, column=2, padx=2)
clear_button.grid(row=0, column=3, padx=2)
#btn.grid(row=0, column=4, padx=2)
btn.place(relx=1.0, rely=0.0, anchor="ne", bordermode=OUTSIDE)

#window in mainloop
root.mainloop()