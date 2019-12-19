from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import Adam, Adadelta
from keras import backend as K
import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt
import json
from keras.models import model_from_json



def loadImageAsGray(imagePath):
    im = cv2.imread(imagePath)
    return cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

def resizeRecortada(filepath):
    im = loadImageAsGray(filepath)
    im = cv2.resize(im, (128,128))
    cv2.imwrite(filepath,im)


path = "./Imagenes/PennFudanPed/PNGImages/FudanPed00001.png"
resizeRecortada(path)
img = loadImageAsGray(path)
img = img / 255
x , y = img.shape

stop_x = x
stop_y = y

def getWindow(x,y,size=64,step=32):
    ventanas = []
    for j in range(0,x-step,step):
        if j+size > x:
            j=x-size
        for i in range(0,y-step,step):
            if i+size > y:
                i=y-size
            window = {
                'xmin': j,
                'xmax': j+size,
                'ymin': i,
                'ymax': i+size
            }
            yield window

with open('Model_0.991304337978363_16-15-46.h5.json','r') as f:
    model_json = json.load(f)
model = model_from_json(model_json)
model.load_weights('Model_0.991304337978363_16-15-46.h5')

def applyModel(path):
    img = loadImageAsGray(path) #La leo y la cambio a blanco y negro
    original_shape = img.shape #Guardo su shape original en una variable para el futuro
    img2 = img.copy() #Me hago una copia de la imagen con la que voy a trabajar
    img2 = cv2.resize(img2, (128,128)) #Le hago un resize a la copia, para pasarla a tamaño 128x128 (la foto entera)
    resultados = []
    for i in getWindow(x,y,size=32,step=16): #Obtengo las coordenadas de las ventanas
        crop = img[i['xmin']:i['xmax'], i['ymin']:i['ymax']] #Saco las coordenadas de cada ventana 
        crop_128 = cv2.resize(crop, (128,128))
        plt.imshow(crop)
        #print(crop)
        #print(crop.shape)
        #print(crop_128.shape)
        
        prepared_data = np.expand_dims(np.expand_dims(crop_128,axis=3),axis=0)
        pred = model.predict(prepared_data)[0]
        
        if pred[1]>pred[0]:
            print(i)
            #print("Probability that there is a person in window -> Yes:{1:.5f}".format(pred[1]))
            print("Probs -> No:{0:.5f} Yes:{1:.5f}".format(pred[0],pred[1]))
            resultados.append((i, "Probs -> No:{0:.5f} Yes:{1:.5f}".format(pred[0],pred[1])))
    
    return resultados


