import sys
import cv2
import numpy as np
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

from Red_corporal import *
from modulo_generar_pdf import *


class Ventana_corporal_pies(QMainWindow, QThread):
    changePixmap = pyqtSignal(QImage)
    def __init__(self, parent=None):
        super(Ventana_corporal_pies, self).__init__(parent)
        loadUi('./archivos_ui/VENTANA_CORPORAL_PIES.ui', self)
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

        movie = QMovie('./imagenes/pisogif.gif')
        self.gif_pies.setMovie(movie)
        movie.start()
        
    def siguiente_ventana(self):
        try:
            Codo_derecho()
            Codo_izquierdo()
            Rodilla_derecha()
            Rodilla_izquierda()
            Manos_pies()
            self.cap.release()
            self.hide()
            otraventana = Ventana_reconocimiento_cuerpo(self)
            otraventana.showMaximized()
        except AttributeError:
            Codo_derecho()
            Codo_izquierdo()
            Rodilla_derecha()
            Rodilla_izquierda()
            Manos_pies()
            self.hide()
            otraventana = Ventana_reconocimiento_cuerpo(self)
            otraventana.showMaximized()
                   
    def start_camara(self):
        '''
        saber = 'foto_%s.png'%(self.cont)
        print(type(saber))
        print(os.path.isfile(saber))
        '''

        fuente = QFont()
        fuente.setPointSize(20)
        if(os.path.isfile('./fotos_cuerpo/foto_pies_1.png')):
            self.Toma.setText('')
            self.b_Capturar.setEnabled(False)
            
        else:
            self.Toma.setText('1) Toma una Foto')
            self.b_Capturar.setEnabled(True)
        self.Toma.setFont(fuente)
            
        self.inicio = 1
        try:
            ret, image = self.cap.read()
            rotated = imutils.rotate_bound(image, 90)
            #image = ImageQt(rotated)
            image = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
            heigth, width, channel = image.shape
            step = channel * width
            qimg = QImage(image.data, width, heigth, step, QImage.Format_RGB888)
            imagem = QPixmap(qimg)
            imagem1 = imagem.scaled(600,600,QtCore.Qt.KeepAspectRatio,QtCore.Qt.FastTransformation)
            self.camara.setPixmap(QPixmap(imagem1))
            self.camara.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            if(self.Nfoto == 2):
                self.cont = self.cont + 1
                cv2.imwrite('./fotos_cuerpo/foto_pies_%s.png'%(self.cont), rotated)
                self.Nfoto = 1
        except (AttributeError, UnboundLocalError):
            pass
    
    def controlTimer(self):
        if not self.timer.isActive():                                    #numero de la camara
            self.cap = cv2.VideoCapture(int(self.N_Camara.currentText())) #N_Camara.currentText() esta funcion extrae el estado del Qcombobox
            self.cap.set(3,720)
            self.cap.set(4,720)
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
            foto_cuerpo = cv2.imread('./fotos_cuerpo/foto_pies_%s.png'%(self.cont), 1) 
            cv2.imshow('foto cuerpo', foto_cuerpo) 
        except (cv2.error):
            pass
 
    def borrar_foto(self):
        try:
            cv2.destroyAllWindows()
            os.remove('./fotos_cuerpo/foto_pies_%s.png'%(self.cont))  #nota importante evitar los errores cuando se trabaj python
            self.cont = self.cont - 1
        except FileNotFoundError:
            pass

        
    def volver(self):
        try:
           self.cap.release()
           os.remove('./fotos_cuerpo/foto_pies_1.png')  #nota importante evitar los errores cuando se trabaj python
           os.remove('./fotos_cuerpo/foto_pies_2.png') 

           cv2.destroyAllWindows()
        except (AttributeError, FileNotFoundError):
            pass
        self.parent().show()
        self.close()     


class Ventana_reconocimiento_cuerpo(QMainWindow, QThread):
    changePixmap = pyqtSignal(QImage)
    def __init__(self, parent=None):
        super(Ventana_reconocimiento_cuerpo, self).__init__(parent)
        loadUi('./archivos_ui/RECONOCIMIENTO_CORPORAL_CUERPO.ui', self)
        self.b_Cancelar.clicked.connect(self.volver)
        self.b_Continuar.clicked.connect(self.siguiente_ventana)
        self.b_Analizar.clicked.connect(self.Funcion_Analizar_cuerpo)
        
        self.Codo_Derecho.setPixmap(QPixmap('./fotos_cuerpo/foto_codo_derecho.png'))
        self.Codo_Derecho.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.Codo_Izquierdo.setPixmap(QPixmap('./fotos_cuerpo/foto_codo_izquierdo.png'))
        self.Codo_Izquierdo.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        
        self.Rodilla_Derecha.setPixmap(QPixmap('./fotos_cuerpo/foto_rodilla_derecha.png'))
        self.Rodilla_Derecha.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.Rodilla_Izquierda.setPixmap(QPixmap('./fotos_cuerpo/foto_rodilla_izquierda.png'))
        self.Rodilla_Izquierda.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.Manos_Pies.setPixmap(QPixmap('./fotos_cuerpo/foto_manos_pies.png'))
        self.Manos_Pies.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

    def siguiente_ventana(self):
        pdf_datos_corporal_cuerpo(self)
        Pdf_guardar()
        wb.open_new(r'C:\Users\aldei\Desktop\programa final\generar_pdf\Reporte.pdf')
        self.hide()

     
    def volver(self): 
        self.parent().show()
        self.close()

    def Funcion_Analizar_cuerpo(self):
        Resultado_codo_derecho(self)
        Resultado_codo_izquierdo(self)
        Resultado_rodilla_derecha(self)
        Resultado_rodilla_izquierda(self)
        Resultado_manos_pies(self)


        
app = QApplication(sys.argv)
main = Ventana_corporal_pies()
#main.show()
#sys.exit(app.exe_())