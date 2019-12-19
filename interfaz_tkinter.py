from tkinter import filedialog, scrolledtext
from tkinter import *
from PIL import Image
from PIL import ImageTk
import functions as f
import predict as p 








class App():
    def __init__(self):
        self.root = Tk()
        self.root.title("DETECTING AND COUNTING PEOPLE IN IMAGES")
        self.canvas = Canvas(self.root, height=800, width=800)
        self.canvas.pack()

        # background
        self.image = Image.open("./Imagenes/background.png")
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background_label = Label(self.root, image=self.background_image).place(relwidth=1, relheight=1)

        # title
        self.label = Label(self.root, text="WHERE ARE YOU?", fg="#20A58E", bg="white", width=200)
        self.label.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
        self.label.config(font=("Phosphate", 50))
        #"#2DBFA6"

        # button - upload images
        self.frameUP = Frame(self.root, bg='#20A58E', bd=5)
        self.frameUP.place(relx=0.3, rely=0.9, relwidth=0.4, relheight=0.05, anchor='n')
        self.buttonUP = Button(self.frameUP, text="⤓ UPLOAD AN IMAGE",font="Courier 21 bold", command=self.meter_foto)
        self.buttonUP.place(relx=0, relheight=1, relwidth=1)
        self.buttonUP.configure(foreground='#20A58E', relief='sunken')


        # button - predict no of persons
        self.framePRED = Frame(self.root, bg='#20A58E', bd=5)
        self.framePRED.place(relx=0.7, rely=0.9, relwidth=0.4, relheight=0.05, anchor='n')
        self.buttonPRED = Button(self.framePRED, text="PREDICT No. OF PEOPLE",
                        font="Courier 19 bold", command=self.pred)
        self.buttonPRED.place(relx=0, relheight=1, relwidth=1)
        self.buttonPRED.configure(foreground='#20A58E', relief='sunken')

        

    def meter_foto(self):
        self.pic = filedialog.askopenfilename()
        self.img = Image.open(self.pic)
        self.img.thumbnail((128,128), Image.ANTIALIAS)
        self.tkimage = ImageTk.PhotoImage(self.img)
        self.bsalir= Label(self.root, image=self.tkimage)
        self.bsalir.place(relx=0.125, rely=0.05, relwidth=0.1, relheight=0.4, anchor='ne')

    
    def pred(self):
        self.respuesta = p.applyModel(self.pic)
        # OUTPUT - Scrolling text box
        self.txt = scrolledtext.ScrolledText(self.root, undo=True)
        self.txt.place(relx=0.656, rely=0.06,relwidth=0.35, relheight=0.2,anchor='nw')
        print(self.respuesta)
        self.txt.insert(INSERT, '\n'.join([str(e) for e in self.respuesta]))
        #self.txt.pack()
        #self.root.update_idletasks()
        #self.salir= Label(self.root, image=self.respuesta)
        #self.salir.place(relx=0.275, rely=0.1, relwidth=0.3, relheight=0.4, anchor='nw')
    


app = App()
app.root.mainloop()