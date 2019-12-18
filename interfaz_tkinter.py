from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import functions as f
import PIL.Image




HEIGHT = 800
WIDTH = 800
root = Tk()
root.title("DETECTING AND COUNTING PEOPLE IN IMAGES")
canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# background

image = PIL.Image.open("./Imagenes/background.png")
background_image = ImageTk.PhotoImage(image)
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# title
label = Label(root, text="WHERE ARE YOU?", fg="#2DBFA6", bg="white", width=200)
label.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
label.config(font=("Phosphate", 50))


# button - upload image
frame = Frame(root, bg='#29BFA5', bd=5)
frame.place(relx=0.3, rely=0.9, relwidth=0.4, relheight=0.05, anchor='n')

button = Button(frame, text="⤓ UPLOAD IMAGE",font="Courier 19 bold", command=lambda: f.meter_foto(root))
button.place(relx=0, relheight=1, relwidth=1)
button.configure(foreground='#29BFA5', relief='sunken')


# button - predict no of persons
frame = Frame(root, bg='#29BFA5', bd=5)
frame.place(relx=0.7, rely=0.9, relwidth=0.4, relheight=0.05, anchor='n')

button = Button(frame, text="PREDICT No. OF PEOPLE",
                font="Courier 19 bold", command=lambda: keras_model.train_model(face_cascade))
button.place(relx=0, relheight=1, relwidth=1)
button.configure(foreground='#29BFA5', relief='sunken')
'''
# button - open signatures database
frame = Frame(root, bg='#001b52', bd=5)
frame.place(relx=0.5, rely=0.7, relwidth=0.75, relheight=0.08, anchor='n')

button = Button(frame, text="► Open signatures database",
                font="Helvetica 19 bold", command=lambda: functions_app.open_mySQLWorkbench())
button.place(relx=0, relheight=1, relwidth=1)
button.configure(foreground='#001b52', relief='solid')

# button - reset signatures database
frame = Frame(root, bg='#001b52', bd=5)
frame.place(relx=0.5, rely=0.8, relwidth=0.75, relheight=0.08, anchor='n')

button = Button(frame, text="► Reset signatures database",
                font="Helvetica 19 bold", command=lambda: functions_app.reset_mySQLTable(db, cursor))
button.place(relx=0, relheight=1, relwidth=1)
button.configure(foreground='#001b52', relief='solid')

# logo
img = ImageTk.PhotoImage(PIL.Image.open("./images/logo_white.png"))
label = Label(root, image=img, bg='#001b52')
label.place(relx=0.82, rely=0.1, relwidth=0.1, relheight=0.1, anchor='n')
'''
root.mainloop()