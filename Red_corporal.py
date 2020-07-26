import cv2
import numpy as np

img = None
frame =  None

homderx=None
homdery=None
cododerx=None
cododery=None
Munderx=None
Mundery=None
homizqx=None
homizqy=None
codoizqx=None
codoizqy=None
Munizqx=None
Munizqy=None
Tobizx=None
Tobizy=None
Tobderx=None
Tobdery=None
Cadderx=None
Caddery=None
Rodderx=None
Roddery=None
Cadizqx=None
Cadizqy=None
Rodizqx=None
Rodizqy=None

def Codo_derecho():
    global union_art, img 
    union_art = [[0,1], [1,2], [2,3], [3,4], [1,5], [5,6], [6,7], [1,14], [14,8], [8,9], [9,10], [14,11], [11,12], [12,13] ]
    #Se lee la imagen a analizar 
    img= cv2.imread("./fotos_cuerpo/foto_codo_1.png")
    Red_cuerpo()
    cv2.imwrite('./fotos_cuerpo/foto_codo_derecho.png', frame)
def Resultado_codo_derecho(self):
    try:
        pendienteAB=(cododery-Mundery)/(cododerx-Munderx)
        #print(pendienteAB)
        pendienteBC=(homdery-cododery)/(homderx-cododerx)
        #print(pendienteBC)

        numerador=pendienteBC-pendienteAB
        denominador=1+(pendienteBC*pendienteAB)
        num=numerador/denominador
        #print(num)
        ang=(np.arctan(num)*180)/np.pi
        print(ang)
        if ang >= 0:
            print('no tiene hiperlaxitud codo derecho')
            self.codo_der.setText('No')
        else:
            print('si tiene hiperlaxitud codo derecho')
            self.codo_der.setText('Si')
    except ZeroDivisionError:
        print('no tiene hiperlaxitud codo derecho')
        self.codo_der.setText('No')


def Codo_izquierdo():
    global union_art, img 
    union_art = [[0,1], [1,2], [2,3], [3,4], [1,5], [5,6], [6,7], [1,14], [14,8], [8,9], [9,10], [14,11], [11,12], [12,13] ]
     #Se lee la imagen a analizar 
    img= cv2.imread("./fotos_cuerpo/foto_codo_2.png")
    Red_cuerpo()
    cv2.imwrite('./fotos_cuerpo/foto_codo_izquierdo.png', frame)
def Resultado_codo_izquierdo(self):
    try:
        pendienteAB=(codoizqy-homizqy)/(codoizqx-homizqx)
        print(pendienteAB)
        pendienteBC=(Munizqy-codoizqy)/(Munizqx-codoizqx)
        print(pendienteBC)

        numerador=pendienteAB-pendienteBC
        denominador=1+(pendienteBC*pendienteAB)
        num=numerador/denominador
        print(num)
        ang=(np.arctan(num)*180)/np.pi
        print(ang)
        if ang >= 0:
            print('no tiene hiperlaxitud codo izquierdo')
            self.codo_izq.setText('No')
        else:
            print('si tiene hiperlaxitud codo izquierdo')
            self.codo_izq.setText('Si')
    except ZeroDivisionError:
        print('no tiene hiperlaxitud codo izquierdo')
        self.codo_izq.setText('No')



def Rodilla_derecha():
    global union_art, img 
    union_art = [[8,9], [9,10] ]
     #Se lee la imagen a analizar 
    img= cv2.imread("./fotos_cuerpo/foto_rodilla_1.png")
    Red_cuerpo()
    cv2.imwrite('./fotos_cuerpo/foto_rodilla_derecha.png', frame)
def Resultado_rodilla_derecha(self):
    try:
        pendienteAB= (Roddery-Tobdery)/(Rodderx-Tobderx)
        pendienteBC= (Caddery-Roddery)/(Cadderx-Rodderx)
        num=pendienteAB-pendienteBC
        den=1+(pendienteAB*pendienteBC)
        ang=np.arctan(num/den)
        ang=(ang*180)/np.pi
        print(ang)
        if ang >= 0:
            print('no tiene hiperlaxitud rodilla derecha')
            self.rodilla_der.setText('No')
        else:
            print('si tiene hiperlaxitud rodilla derecha')
            self.rodilla_der.setText('Si')
    except ZeroDivisionError:
        print('no tiene hiperlaxitud rodilla derecha')
        self.rodilla_der.setText('No')


def Rodilla_izquierda():
    global union_art, img 
    union_art = [[11,12], [12,13] ]
     #Se lee la imagen a analizar 
    img= cv2.imread("./fotos_cuerpo/foto_rodilla_2.png")
    Red_cuerpo()
    cv2.imwrite('./fotos_cuerpo/foto_rodilla_izquierda.png', frame)
def Resultado_rodilla_izquierda(self):
    try:
        pendienteAB=(Rodizqy-Tobizy)/(Rodizqx-Tobizx)
        pendienteBC=(Cadizqy-Rodizqy)/(Cadizqx-Rodizqx)
        num=(pendienteBC-pendienteAB)
        den=1+(pendienteBC*pendienteAB)
        fraccion=num/den
        ang=(np.arctan(fraccion)*180)/np.pi
        print(ang)
        if ang >= 0:
            print('no tiene hiperlaxitud rodilla izquierda')
            self.rodilla_izq.setText('No')
        else:
            print('si tiene hiperlaxitud rodilla izquierda')
            self.rodilla_izq.setText('Si')
    except ZeroDivisionError:
        print('no tiene hiperlaxitud rodilla izquierda')
        self.rodilla_izq.setText('No')

def Manos_pies():
    global union_art, img 
    union_art = [[0,1], [1,2], [2,3], [3,4], [1,5], [5,6], [6,7], [1,14], [14,8], [8,9], [9,10], [14,11], [11,12], [12,13] ]
     #Se lee la imagen a analizar 
    img= cv2.imread("./fotos_cuerpo/foto_pies_1.png")
    Red_cuerpo()
    cv2.imwrite('./fotos_cuerpo/foto_Manos_pies.png', frame)
def Resultado_manos_pies(self):
    munecasx=(Munderx+Munizqx)/2
    munecasy=(Munizqy+Mundery)/2
    tobillosx=(Tobizx+Tobderx)/2
    tobillosy=(Tobdery+Tobizy)/2

    op=  np.absolute(tobillosy-munecasy) #Valor absoluto eje opuesto
    ady= np.absolute (tobillosx-munecasx) #Valor absoluto eje adyacente

    print(op,ady)
    angulo=np.arctan(op/ady)
    angulo=(np.arctan(angulo)*180)/np.pi
    print(angulo)
    if angulo == 0:
        print('si tiene hiperlaxo manos al piso')
        self.manos_pies.setText('Si')
    else:
        print('no tiene hiperlaxo manos al piso')
        self.manos_pies.setText('No')


def Red_cuerpo():
    global frame, homderx, homdery, cododerx, cododery, Munderx, Mundery, homizqx, homizqy, codoizqx, codoizqy, Munizqx, Munizqy,Tobizx,Tobizy,Tobderx
    global Tobdery, Cadderx, Caddery, Rodderx, Roddery, Cadizqx, Cadizqy, Rodizqx, Rodizqy

    #Se leen los modelos de la red neuronal convolucional preentrenada
    redpre = "./modelo_cuerpo/pose_deploy_linevec_faster_4_stages.prototxt" #Cargamos red  pre 
    pesosred = "./modelo_cuerpo/pose_iter_146000.caffemodel"             #Cargamos pesos red pre
    #Se establece el sistema de puntos a detectar en este caso 15
    numpuntos = 15
    #Union de los puntos con el fin de graficar el esqueleto 
    
    #Redimensionamos la imagen al tamaño de la red preentrenada
    frame= cv2.resize(img,(558,413))
    frameCopy = np.copy(frame)
    frameWidth = frame.shape[1]
    frameHeight = frame.shape[0]
    umbral = 0.1

    net = cv2.dnn.readNetFromCaffe(redpre, pesosred)
    inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (368, 368),
                            (0, 0, 0), swapRB=False, crop=False)

    net.setInput(inpBlob)
    salida = net.forward()

    alto = salida.shape[2]
    ancho = salida.shape[3]

    #Lista para almacenar puntos detectados y posicion x y y de los puntos necesarios 
    puntos = []

    for i in range(numpuntos):
        # Mapa de la parte del cuerpo correspondiente
        probMap = salida[0, i, :, :]

        # Encuentra los maximos globales de el mapa de probabilidad (proMAp)
        minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
        
        # Escala el punto para ajustar el tamaño a la imagen
        x = (frameWidth * point[0]) / ancho
        y = (frameHeight * point[1]) / alto
        
        if i == 2: #Hombro derecho
            homderx=x
            homdery=y
        
        if i == 3: #Codo derecho
            cododerx=x
            cododery=y
        
        if i == 4:   #Muñeca derecha
            Munderx=x
            Mundery=y

        if i == 5: #Hombro izquierdo
            homizqx=x
            homizqy=y
    
        if i == 6: #Codo izquierdo
            codoizqx=x
            codoizqy=y
        
        if i == 7:   #Muñeca izquierda
            Munizqx=x
            Munizqy=y

        if i == 13: #Tobillo izquierdo
            Tobizx=x
            Tobizy=y
    
        if i == 10: #Tobillo derecho
            Tobderx=x
            Tobdery=y

        if i == 8: #Cadera derecha
            Cadderx=x
            Caddery=y
    
        if i == 9: #Rodilla derecha
            Rodderx=x
            Roddery=y
                
        if i == 11: #Cadera izquierda
            Cadizqx=x
            Cadizqy=y
        
        if i == 12: #Rodilla izquierda
            Rodizqx=x
            Rodizqy=y
        

        if prob > umbral : 
            puntos.append((int(x), int(y)))
        else :
            puntos.append(None)
            
    # Grafica cuerpo
    for pair in union_art:
        partA = pair[0]
        partB = pair[1]

        if puntos[partA] and puntos[partB]:
            cv2.line(frame, puntos[partA], puntos[partB], (0, 255, 255), 2)
            cv2.circle(frame, puntos[partA], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)

    #cv2.imshow('Esqueleto pose Codo DERECHO', frame)

    #print(homderx,homdery)
    #print(cododerx,cododery)
    #print(Munderx, Mundery)


    #cv2.waitKey(0)

