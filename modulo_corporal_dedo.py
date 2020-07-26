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

from modulo_corporal_pulgar import *

class Ventana_corporal_dedo(QMainWindow, QThread):
    changePixmap = pyqtSignal(QImage)
    def __init__(self, parent=None):
        super(Ventana_corporal_dedo, self).__init__(parent)
        loadUi('./archivos_ui/VENTANA_CORPORAL_DEDO.ui', self)
        self.cont = 0
        self.Nfoto = 0
        self.inicio = 0 
        self.culito = 1
        self.timer = QTimer()
        self.timer.timeout.connect(self.start_camara)
        self.b_Iniciar.clicked.connect(self.controlTimer)
        self.b_Capturar.clicked.connect(self.tomar_foto)
        self.b_Cancelar.clicked.connect(self.volver)
        self.b_Ver.clicked.connect(self.ver_foto)
        self.b_Borrar.clicked.connect(self.borrar_foto)
        self.b_Continuar.clicked.connect(self.siguiente_ventana)

        movie = QMovie('./imagenes/meñiquegif.gif')
        self.gif_dedo.setMovie(movie)
        movie.start()
        
    def siguiente_ventana(self):
        try:
            self.cap.release()
            self.hide()
            otraventana = Ventana_corporal_pulgar(self)
            otraventana.showMaximized()
        except AttributeError:
            self.hide()
            otraventana = Ventana_corporal_pulgar(self)
            otraventana.showMaximized()
                   
    def start_camara(self):
        '''
        saber = 'foto_%s.png'%(self.cont)
        print(type(saber))
        print(os.path.isfile(saber))
        '''
        fuente = QFont()
        fuente.setPointSize(20)
        if(os.path.isfile('./fotos_manos/foto_menique_1.png')):
            self.Listo.setText('Foto 1/2 (Falta)')
            self.Toma.setText('2) Toma Mano Izquierda')
            self.b_Capturar.setEnabled(True)
        else:
           self.Listo.setText('Foto 0/2 (Falta)')
           self.Toma.setText('1) Toma Mano Derecha')
        if(os.path.isfile('./fotos_manos/foto_menique_2.png')):
            self.Listo.setText('Foto 2/2 (Completo)')
            self.Toma.setText('')
            self.b_Capturar.setEnabled(False)
        self.Listo.setFont(fuente)
        self.Toma.setFont(fuente)

        self.inicio = 1
        try:
            ret, image = self.cap.read()
            foto = cv2.flip(image, 1)
            imageN = cv2.cvtColor(foto, cv2.COLOR_BGR2RGB)
            heigth, width, channel = image.shape
            step = channel * width
            qimg = QImage(imageN.data, width, heigth, step, QImage.Format_RGB888)
            imagem = QPixmap(qimg)
            imagem1 = imagem.scaled(800,600,QtCore.Qt.KeepAspectRatio,QtCore.Qt.FastTransformation)
            self.camara.setPixmap(QPixmap(imagem1))
            self.camara.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            if(self.Nfoto == 2):
                self.cont = self.cont + 1
                cv2.imwrite('./fotos_manos/foto_menique_%s.png'%(self.cont), foto)
                self.Nfoto = 1
        except (AttributeError, UnboundLocalError, cv2.error):
            pass      
    
    def controlTimer(self):
        if not self.timer.isActive():                                    #numero de la camara
            self.cap = cv2.VideoCapture(int(self.N_Camara.currentText())) #N_Camara.currentText() esta funcion extrae el estado del Qcombobox
            self.cap.set(3,640)
            self.cap.set(4,480)
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
            foto_manos_1 = cv2.imread('./fotos_manos/foto_menique_%s.png'%(self.cont), 1) 
            cv2.imshow('foto manos', foto_manos_1) 
        except (cv2.error):
            pass
 
    def borrar_foto(self):
        try:
            cv2.destroyAllWindows()
            os.remove('./fotos_manos/foto_menique_%s.png'%(self.cont))  #nota importante evitar los errores cuando se trabaj python
            self.cont = self.cont - 1
        except FileNotFoundError:
            pass

        
    def volver(self):
        try:
           self.cap.release()
           os.remove('./fotos_manos/foto_menique_1.png')  #nota importante evitar los errores cuando se trabaj python
           os.remove('./fotos_manos/foto_menique_2.png') 
           cv2.destroyAllWindows()
        except (AttributeError, FileNotFoundError):
            pass
        self.parent().show()
        self.close()    
'''
app = QApplication(sys.argv)
main = Ventana_corporal_dedo()
'''