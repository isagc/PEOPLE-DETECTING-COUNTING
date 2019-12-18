from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import functions as f
import PIL.Image



def meter_foto(root):
        global pic
        global tkimage

        pic = filedialog.askopenfilename()


        img = Image.open(pic)
        #img = cv2.resize(img,(128,128))
        img.thumbnail((128,128), Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(img)
        bsalir= Label(root, image=tkimage)
        bsalir.place(relx=0.275, rely=0.1, relwidth=0.3, relheight=0.4, anchor='ne')


