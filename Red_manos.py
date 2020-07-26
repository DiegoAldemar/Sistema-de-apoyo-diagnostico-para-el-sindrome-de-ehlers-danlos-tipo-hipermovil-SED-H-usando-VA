from __future__ import division
import cv2
import numpy as np
from skimage import exposure
import os
import time

mano = None
frame = None
Munderx=None
Mundery=None
Medioderx=None
Mediodery=None
Puntaderx=None
Puntadery=None
Puntapulgderx=None
Puntapulgdery=None

def Menique_derecho():
    try:
        global mano1, POSE_PAIRS
        POSE_PAIRS = [[0,17],[17,18],[18,19],[19,20] ]
        mano1=cv2.imread('./fotos_manos/foto_menique_1.png')
        Red()
        cv2.imwrite('./fotos_manos/foto_menique_derecho.png', frame)
    except(cv2.error):
        pass
#
def Menique_izquierdo():
    try:
        global mano1, POSE_PAIRS
        POSE_PAIRS = [[0,17],[17,18],[18,19],[19,20] ]
        mano1=cv2.imread('./fotos_manos/foto_menique_2.png')
        Red()
        cv2.imwrite('./fotos_manos/foto_menique_izquierdo.png', frame)
    except(cv2.error):
        pass

def Pulgar_derecho():
    try:
        global mano1, POSE_PAIRS
        POSE_PAIRS = [ [0,1],[1,2],[2,3],[3,4]]
        mano1=cv2.imread('./fotos_manos/foto_pulgar_1.png')
        Red()
        cv2.imwrite('./fotos_manos/foto_pulgar_derecho.png', frame)
    except(cv2.error):
        pass

def Pulgar_izquierdo():
    try:
        global mano1, POSE_PAIRS
        POSE_PAIRS = [ [0,1],[1,2],[2,3],[3,4]]
        mano1=cv2.imread('./fotos_manos/foto_pulgar_2.png')
        Red()
        cv2.imwrite('./fotos_manos/foto_pulgar_izquierdo.png', frame)
    except(cv2.error):
        pass

def Red():
    global frame, Munderx, Mundery, Medioderx, Mediodery, Puntaderx, Puntadery, Puntapulgderx, Puntapulgdery
    protoFilemano = './modelo_manos/pose_deploy.prototxt.txt'
    weightsFilemano = './modelo_manos/pose_iter_102000.caffemodel'
    nPoints = 22
    #Menique_derecho()
    #Pulgar_derecho()
    
    try:
        net = cv2.dnn.readNetFromCaffe(protoFilemano, weightsFilemano)
        
        mano=cv2.resize(mano1, (640, 480))

        frame = mano
        img_original = frame.copy()
        frameCopy = np.copy(frame)
        frameWidth = frame.shape[1]
        frameHeight = frame.shape[0]
        aspect_ratio = frameWidth/frameHeight

        threshold = 0.1

        inHeight = 368
        inWidth = int(((aspect_ratio*inHeight)*8)//8)

        inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight),
                                        (0, 0, 0), swapRB=False, crop=False)

        net.setInput(inpBlob)
        output = net.forward()

        alto = output.shape[2]
        ancho = output.shape[3]

        points = []
        map_prob_t = None  

        for i in range(nPoints):

            probMap = output[0, i, :, :]
            probMap = cv2.resize(probMap, (frameWidth, frameHeight))
            
            minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
            
            # Escala el punto para ajustar el tamaño a la imagen
            x = (frameWidth * point[0]) / ancho
            y = (frameHeight * point[1]) / alto
            
            if i == 0: #Muñeca
                Munderx=x
                Mundery=y
            
            if i == 5: #Mitad mano
                Medioderx=x
                Mediodery=y
            
            if i == 8:   #Punta meñique
                Puntaderx=x
                Puntadery=y
            
            if i == 4: #punta pulgar
                Puntapulgderx=x
                Puntapulgdery=y
                
            if prob > threshold :
                points.append((int(point[0]), int(point[1])))
            else :
                points.append(None)

        for pair in POSE_PAIRS:
            partA = pair[0]
            partB = pair[1]

            if points[partA] and points[partB]:
                cv2.line(frame, points[partA], points[partB], (0, 255, 255), 2)
                cv2.circle(frame, points[partA], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
                cv2.circle(frame, points[partB], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)

    except(cv2.error):
        pass

def Resultado_menique_derecho(self):
    try:
        pendienteAB=(Mediodery-Mundery)/(Medioderx-Munderx)
        pendienteBC=(Puntadery-Mediodery)/(Puntaderx-Medioderx)
        ang= np.arctan(pendienteAB-pendienteBC)/(1+pendienteAB*pendienteBC)
        ang=ang=(ang*180)/np.pi
        ang1 = ang+180
        print(ang1)
        if ang1 > 90:
            self.Menique_der.setText('Si')
        else:
            self.Menique_der.setText('No')
    except ZeroDivisionError:
        pass

def Resultado_menique_izquierdo(self):
    try:
        ady=Puntaderx-Medioderx
        op=Puntadery-Mediodery
        ang= np.arctan(op/ady)
        ang=(np.arctan(ang)*180)/np.pi
        ang1 = ang-180
        print(ang1)
        if ang1 > 90:
            self.Menique_izq.setText('Si')
        else:
            self.Menique_izq.setText('No')
    except ZeroDivisionError:
        pass

def Resultado_pulgar_derecho(self):
    resta=Munderx-Puntapulgderx
    if resta<=10:
        print("SI CUMPLE pulgar dere")
        self.Pulgar_der.setText('Si')
    else:
        self.Pulgar_der.setText('No')
    print(resta)

def Resultado_pulgar_izquierdo(self):
    resta=Munderx-Puntapulgderx
    if resta<=10:
        print("SI CUMPLE")
        self.Pulgar_izq.setText('Si')
    else:
        self.Pulgar_izq.setText('No')