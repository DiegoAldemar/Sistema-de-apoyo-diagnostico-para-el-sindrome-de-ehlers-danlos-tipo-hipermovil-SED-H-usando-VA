#Código para ejecutar la aplicacion de SED_h 
#los archivos .ui siempre los guardo en mayusculas y dentro
#trae una class en minuscula.
#cada class de este codigo es una ventana distinta, en ellas tendremos def y cada uno de ellos hara una funcion
#ya sea abrir, cerrar o hacer eventos que se pueden realizar desde dicha ventana(class) en la que estamos.
#los botones siempre inician con "b_nombre del boton"
import sys
import cv2
import numpy
import argparse
import imutils
import os
import shutil #remover varchivos con carpetas
import time
import webbrowser as wb
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QImage, QPixmap, QMovie, QFont
from PyQt5.uic import loadUi
from PyQt5.QtCore import QThread, QTimer, Qt, pyqtSignal, pyqtSlot
from reportlab.pdfgen import  canvas
from modulo_generar_pdf import *

from modulo_facial import *
#from modulo_corporal_manos *
#from modulo_corporal_cuerpo *

class INICIO(QMainWindow): #ventana prinsipal 
    def __init__(self):
        super(INICIO, self).__init__()
        loadUi('./archivos_ui/INICIO.ui', self)  #cargamos el archivo .ui
        self.b_Analisis.clicked.connect(self.abrir_iniciar_analisis) #eventos para abrir ventana de registro del boton b_registrarse
        self.b_Manual.clicked.connect(self.abrir_manual_posicionamiento) #eventos para abrir ventana sed_h botnon b_enviar
    
    def abrir_iniciar_analisis(self):
        #self.hide() #cierra la ventana en la que estabamos
        otraventana=Ventana_iniciar_analisis(self) 
        otraventana.showMaximized() #abre ventana VENTANA_REGISTRARSE, es decir otra class

        #remover fotos 
        try:
            shutil.rmtree('fotos_facial')
            shutil.rmtree('fotos_cuerpo')
            shutil.rmtree('fotos_manos')
        except OSError:
            pass

    def abrir_manual_posicionamiento(self):
        #self.hide()
        wb.open_new(r'C:\Users\aldei\OneDrive\proyecto\programa final\manual\Manual_usuario.pdf')
        
        
 
class Ventana_iniciar_analisis(QMainWindow):
    def __init__(self, parent=None):
        super(Ventana_iniciar_analisis, self).__init__(parent)
        loadUi('./archivos_ui/INICIAR_ANALISIS.ui', self)
        self.b_Cancelar.clicked.connect(self.volver_ventana_prinsipal)
        self.b_Continuar.clicked.connect(self.abrir_ventana_facial)
        
    def volver_ventana_prinsipal(self):
        self.parent().show()
        self.close()
        
    def abrir_ventana_facial(self):
        Pdf_datos_analisis(self)
        self.hide()
        otraventana = Ventana_facial(self)
        otraventana.showMaximized()
        
        os.mkdir('fotos_manos')
        os.mkdir('fotos_facial')
        os.mkdir('fotos_cuerpo')
        
#cada boton de dicha ventana de entorno contiene sus botones el cual son 
#variables llamadas asi: b_nombre del boton, con su inisial en mayuscula. ej del boton Iniciar: b_Iniciar


#mi primer repositorio subiendo a github

#Ventana_facial()
#Ventana_reconocimiento()
 
#Ventana_corporal_cuerpo()  


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = INICIO()
    main.showMaximized()
    sys.exit(app.exec_())
