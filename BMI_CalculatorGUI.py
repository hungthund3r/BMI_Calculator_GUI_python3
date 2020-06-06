'''
Name: Alfredo Hung
E-mail: hung_m@icloud.com
'''

from tkinter import *


root = Tk()
root.title('BMI Calculator')
root.iconbitmap('icons/balanza.ico') 
root.geometry('350x620+500+45') 
root.resizable(0, 0) # Avoid the user resize the window.


# ---------------------------------------------------------------
# ================= Reset Function =============================#
# ---------------------------------------------------------------
entryName = StringVar()
entryAge = StringVar()
entryWeight = StringVar()
entryHeight = StringVar()

def resetButton():
    '''Will reset all the entries to 0'''

    varOption.set(False)
    entryName.set('')
    entryAge.set('')
    entryWeight.set('')
    entryHeight.set('')

# ---------------------------------------------------------------
# ================= Frame 1 ====================================#
# ---------------------------------------------------------------
frame_1 = Frame(root) 
frame_1.pack(fill = X) 
frame_1.config(bg = '#f95959')

my_label = Label(frame_1, height = 2, text='BMI Calculator',
    bg='#f95959', fg='white', font = ("Helvetica", "18"))
my_label.grid(row = 0, column = 1)

photo_1 = PhotoImage(file="icons/heart.png")
label_img = Label(frame_1, image=photo_1, bg = '#f95959')
label_img.grid(row = 0, column = 0, padx = 10)


# ---------------------------------------------------------------
# ================= Frame 2 ====================================#
# ---------------------------------------------------------------
frame_2 = Frame(root)
frame_2.pack(fill=X)
frame_2.config(bg='#FBFBFB')

label_top = Label(frame_2, text= 'Find out your BMI', bg='#FBFBFB')
label_top.pack()
label_top.config( font=('Helvetica', 14), fg='#818080', pady=15)


# ---------------------------------------------------------------
# ====================== Frame 3 ===============================#
# ---------------------------------------------------------------
frame_3 = Frame(root)
frame_3.pack(fill=BOTH, expand=True)
frame_3.config(bg='#FBFBFB')


# ---------------------------------------------------------------
# ================= Silhouettes ================================#
# ---------------------------------------------------------------
photo_2 = PhotoImage(file="icons/male.png")
label_img_2 = Label(frame_3, image=photo_2, bg='#FBFBFB')
label_img_2.grid(row = 0, column =1 )

photo_3 = PhotoImage(file="icons/female.png")
label_img_3 = Label(frame_3, image=photo_3, bg='#FBFBFB')
label_img_3.grid(row = 0, column =2)


# ---------------------------------------------------------------
# ===================== Labels ================================#
# ---------------------------------------------------------------
gender_label = Label(frame_3, text = 'Gender', font = ("Helvetica", 13,'bold'),
    bg='#FBFBFB', fg='#737171')
gender_label.grid(row=1, column=0, sticky='e', padx=10, pady=10)

name_label = Label(frame_3, text = 'Name', font = ("Helvetica", 13,'bold'),
    bg='#FBFBFB', fg='#737171')
name_label.grid(row=2, column=0, sticky='e', padx=10, pady=10)

age_label = Label(frame_3, text='Age', font = ("Helvetica", 13,'bold'),
bg='#FBFBFB', fg='#737171')
age_label.grid(row=3, column=0, sticky='e', padx=10, pady=10)

weight_label = Label(frame_3, text='Weight', font = ("Helvetica", 13,'bold'), 
    bg='#FBFBFB', fg='#737171')
weight_label.grid(row=4, column=0, sticky='e', padx=10, pady=10)

height_label = Label(frame_3, text='Height', font = ("Helvetica", 13,'bold'), 
    bg='#FBFBFB', fg='#737171')
height_label.grid(row=5, column=0, sticky='e', padx=10, pady=10)


# ---------------------------------------------------------------
# ===================== RadioButtons ===========================#
# ---------------------------------------------------------------
varOption = IntVar()

radioButton1 = Radiobutton(frame_3, value=1, bg='#FBFBFB', variable=varOption)
radioButton1.grid(row=1, column=1)
radioButton1.config(activebackground='#FBFBFB')

radioButton2 = Radiobutton(frame_3, value=2, bg='#FBFBFB', variable=varOption)
radioButton2.grid(row=1, column=2)
radioButton2.config(activebackground='#FBFBFB')


# ---------------------------------------------------------------
# ===================== Entry Boxes ============================#
# ---------------------------------------------------------------
entry_name = Entry(frame_3, textvariable=entryName)
entry_name.grid(row=2, column=1, columnspan=2 , ipady=3, ipadx=2, padx=15, pady=10) 
entry_name.config(bd=2, width=13, justify='center', font=('Helvetica',16,'bold'))

entry_age = Entry(frame_3, textvariable=entryAge)
entry_age.grid(row=3, column=1, columnspan=2 , ipady=3, ipadx=2, padx=15, pady=10) 
entry_age.config(bd=2, width=13, justify='center', font=('Helvetica',16,'bold'))

entry_weight = Entry(frame_3, textvariable=entryWeight)
entry_weight.grid(row=4, column=1, columnspan=2 , ipady=3, ipadx=2, padx=15, pady=10) 
entry_weight.config(bd=2, width=13, justify='center', font=('Helvetica',16,'bold'))

entry_height = Entry(frame_3, textvariable=entryHeight)
entry_height.grid(row=5, column=1, columnspan=2 , ipady=3, ipadx=2, padx=15, pady=10) 
entry_height.config(bd=2, width=13, justify='center', font=('Helvetica',16,'bold'))


# ---------------------------------------------------------------
# ===================== Calculate Button =======================#
# ---------------------------------------------------------------
my_button = Button(frame_3, text='CALCULATE BMI', cursor='hand2')
my_button.config(font=('Helvetica',18), bg='#f95959', fg='#ecf0e9', padx=15)
my_button.place(relx=0.5, rely=0.75, anchor=CENTER)


# ---------------------------------------------------------------
# ===================== Reset Button ===========================#
# ---------------------------------------------------------------
reset_button = Button(frame_3, text='Reset', cursor='hand2', command=resetButton)
reset_button.config(font=('Helvetica',16), bg='#f95959', fg='#ecf0e9', padx=15)
reset_button.place(relx=0.5, rely=0.88, anchor=CENTER)


# ---------------------------------------------------------------
# ===================== Frame 4 ===========================#
# ---------------------------------------------------------------
frame_4 = Frame(root)
frame_4.pack(fill = X)
frame_4.config(bg = '#f95959', height = 30)

root.mainloop()