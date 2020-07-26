from imutils import face_utils
import dlib
import cv2 as cv
import numpy as np
import time

import numpy as np
from keras.preprocessing.image import load_img, img_to_array
import tensorflow as tf

exterior1 = 0
interior1 = 0
interior2 = 0
exterior2 = 0

def Ojos():
    global exterior1, interior1, interior2, exterior2
    img = cv.imread("./fotos_facial/foto_facial_1.png")
    p = './modelo_hendidura/shape_predictor_68_face_landmarks.dat'
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(p)

# Obtención puntos de interés
# while True:
    cam = img
    cam_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    caras = detector(cam_gray, 0)

    for cara in caras:
        shape = predictor(cam_gray, cara)
        for n in range(36, 48):
            posicion = (shape.part(n).x, shape.part(n).y)
            foto = cv.circle(cam, (posicion), 2, (0, 255, 0), -1)
            if n == 36:
                exterior1 = posicion
            if n == 39:
                interior1 = posicion
            if n == 42:
                interior2 = posicion
            if n == 45:
                exterior2 = posicion
 
    #cv.imshow("cam", foto)
    cv.imwrite('./fotos_facial/foto.png', foto)


def Resultado(self):#hendidura papebral antimongolica
        ady1 = interior1[0]
        ady11 = exterior1[0]
        op1 = interior1[1]
        op11 = exterior1[1]
        
        adyojo1 = ady1-ady11
        opojo1 = op1-op11
        angojo1 = np.arctan(opojo1/adyojo1)

        ady2 = exterior2[0]
        ady22 = interior2[0]
        op2 = exterior2[1]
        op22 = interior2[1]

        adyojo2 = ady2-ady22
        opojo2 = op22-op2
        angojo2 = np.arctan(opojo2/adyojo2)
        if angojo1 >= 0:
            self.Angulo_ojo_1.setText('No')
        else:
            self.Angulo_ojo_1.setText('Si')
        
        if angojo2 >= 0:
            self.Angulo_ojo_2.setText('No')
        else:
            self.Angulo_ojo_2.setText('Si')
        print(angojo1)
        print(angojo2)
        #self.Angulo_ojo_1.setText('ojo angojo1: ' + str(angojo1))
        #self.Angulo_ojo_2.setText('ojo angojo2: ' + str(angojo2))
# if cv.waitKey(1) == ord("q"):
# break

def Prominente(self):
    file = './fotos_facial/foto_facial_1.png'
    longitud, altura= 100,100
    modelo='./modelo_prominente/modelo.h5'
    pesos='./modelo_prominente/pesos.h5'
    cnn=tf.keras.models.load_model(modelo)
    cnn.load_weights(pesos)
    x=load_img(file,target_size=(longitud, altura))
    x=img_to_array(x)
    x=np.expand_dims(x,axis=0)
    arreglo=cnn.predict(x)
    resultado=arreglo[0]
    respuesta=np.argmax(resultado)
    
    if respuesta==0:
        print('No')
        self.Prominente.setText('No')
    elif respuesta==1:
        print('Si')
        self.Prominente.setText('Si')
    return respuesta

def Triangular(self):
    file = './fotos_facial/foto_facial_1.png'
    longitud, altura= 150,150
    modelo='./modelo_triangular/modelo.h5'
    pesos='./modelo_triangular/pesos.h5'
    cnn=tf.keras.models.load_model(modelo)
    cnn.load_weights(pesos)
    x=load_img(file,target_size=(longitud, altura))
    x=img_to_array(x)
    x=np.expand_dims(x,axis=0)
    arreglo=cnn.predict(x)
    resultado=arreglo[0]
    respuesta=np.argmax(resultado)
    if respuesta==0:
        print('No')
        self.Triangular.setText('No')
    elif respuesta==1:
        print('Si')
        self.Triangular.setText('Si')
    return respuesta
