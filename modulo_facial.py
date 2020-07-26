import sys
import cv2
import numpy
import argparse
import imutils
import os
import time
import webbrowser as wb

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QImage, QPixmap, QMovie, QFont
from PyQt5.uic import loadUi
from PyQt5.QtCore import QThread, QTimer, Qt, pyqtSignal, pyqtSlot
from PyQt5 import QtCore

from modulo_corporal_dedo import *

from Red_facial import *

from modulo_generar_pdf import *

#from modulo_corporal_cuerpo import *

class Ventana_facial(QMainWindow, QThread):
    changePixmap = pyqtSignal(QImage)
    def __init__(self, parent=None):
        super(Ventana_facial, self).__init__(parent)
        loadUi('./archivos_ui/VENTANA_FACIAL.ui', self)
        self.cont = 0
        self.Nfoto = 0 
        self.inicio = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.start_camara)
        self.b_Iniciar.clicked.connect(self.controlTimer)
        self.b_Capturar.clicked.connect(self.tomar_foto)
        self.b_Cancelar.clicked.connect(self.volver)
        self.b_Ver.clicked.connect(self.ver_foto)
        self.b_Continuar.clicked.connect(self.siguiente_ventana)
        self.b_Borrar.clicked.connect(self.borrar_foto)

        movie = QMovie('./imagenes/facialgif.gif')
        self.katerine.setMovie(movie)
        movie.start()
        
    def siguiente_ventana(self):
        try:
            Ojos()
            self.cap.release()
            self.hide()
            otraventana = Ventana_reconocimiento(self)
            otraventana.showMaximized()
        except (AttributeError, cv2.error):
            self.hide()
            otraventana = Ventana_reconocimiento(self)
            otraventana.showMaximized()
        
    def start_camara(self):
        if(os.path.isfile('./fotos_facial/foto_facial_1.png')):
            fuente = QFont()
            fuente.setPointSize(20)
            self.Listo.setText('Foto 1/1 (completo)')
            self.Listo.setFont(fuente)
        else:
            fuente = QFont()
            fuente.setPointSize(20)
            self.Listo.setText('Foto 0/1 (Falta)')
            self.Listo.setFont(fuente)
        self.inicio = 1
        try:
           ret, image = self.cap.read()
           #rotated = imutils.rotate_bound(image, 0)
           foto = cv2.flip(image, 1)
           imageN = cv2.cvtColor(foto, cv2.COLOR_BGR2RGB)
           
           heigth, width, channel = imageN.shape
           step = channel * width
           qimg = QImage(imageN.data, width, heigth, step, QImage.Format_RGB888)
           imagem = QPixmap(qimg)
           imagem1 = imagem.scaled(800,480,QtCore.Qt.KeepAspectRatio,QtCore.Qt.FastTransformation)
           self.camara.setPixmap(QPixmap(imagem1))
           self.camara.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
           if(self.Nfoto == 2):
                cv2.imwrite('./fotos_facial/foto_facial_1.png', foto)
                self.Nfoto = 1  
        except (AttributeError, cv2.error):
            pass
            #self.T_error.setText('camara no existe')

    
    def controlTimer(self):
        if not self.timer.isActive():                                     #numero de la camara
            #self.cap = cv2.VideoCapture(int(self.N_Camara.currentText())) #N_Camara.currentText() esta funcion extrae el estado del Qcombobox
            self.cap = cv2.VideoCapture(0)
            self.cap.set(3, 1920)
            self.cap.set(4, 1080)
            self.timer.start(20)
            self.b_Iniciar.setText('Parar')
        else:
            self.timer.stop()
            self.cap.release()
            self.b_Iniciar.setText('Iniciar')
            
    def tomar_foto(self):
        if(self.inicio == 1):
            self.Nfoto = 2
        else:
            return
    
    def ver_foto(self):
        try:
            cv2.destroyAllWindows()
            foto_facial = cv2.imread('./fotos_facial/foto_facial_1.png', 1)
            cv2.imshow('foto facial 1', foto_facial)
        except (cv2.error, AttributeError):
            pass
        
    def borrar_foto(self):
        try:
            os.remove('./fotos_facial/foto_facial_1.png')
            cv2.destroyAllWindows()
        except FileNotFoundError:
            pass
        
    def volver(self):
        try:
            self.cap.release()
            os.remove('./fotos_facial/foto_facial_1.png')
            
            cv2.destroyAllWindows()
        except(AttributeError, FileNotFoundError):
            pass
        self.parent().show()
        self.close()

class Ventana_reconocimiento(QMainWindow, QThread):
    changePixmap = pyqtSignal(QImage)
    def __init__(self, parent=None):
        super(Ventana_reconocimiento, self).__init__(parent)
        loadUi('./archivos_ui/RECONOCIMIENTO_FACIAL.ui', self)
        self.b_Cancelar.clicked.connect(self.volver)
        self.b_Continuar.clicked.connect(self.siguiente_ventana)
        self.b_Analizar.clicked.connect(self.Funcion_Analizar)
        
        self.label_foto.setPixmap(QPixmap('./fotos_facial/foto.png'))
        self.label_foto.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

    def siguiente_ventana(self):
        try:
            Pdf_datos_facial(self)
            #Pdf_guardar()
            self.hide()
            otraventana = Ventana_corporal_dedo(self)
            otraventana.showMaximized()
        except OSError:
            self.hide()
            otraventana = Ventana_corporal_dedo(self)
            otraventana.showMaximized()

    def volver(self): 
            self.parent().show()
            self.close()

    def Funcion_Analizar(self):
        Resultado(self)#hendidura papebral
        Prominente(self)
        Triangular(self)
        

app = QApplication(sys.argv)
main = Ventana_facial()

#main.show()
#sys.exit(app.exe_())
