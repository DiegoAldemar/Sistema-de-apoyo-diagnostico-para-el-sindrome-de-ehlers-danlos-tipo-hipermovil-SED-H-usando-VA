####PDF

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

#from programa import Ventana_iniciar_analisis
c=canvas.Canvas("./generar_pdf/Reporte.pdf")

def Pdf_datos_analisis(self):
    
    ###ANCHO DE LINEA
    c.setLineWidth(.3)
    #Fuente y tamaño a utilizar
    c.setFont('Helvetica',14)
    ##dibujo de texto en x,y 1pto=1/72 pulgadas
    c.drawString(130,760,"RESULTADOS SISTEMA DE APOYO DIÁGNOSTICO SED-H")
    #POSICION X1 Y1 X2 Y2
    c.line(50,730,550,730)
    c.line(50,705,550,705)
    c.drawString(180,740,"Síndrome de Ehlers-Danlos tipo Hipermóvil")
    c.drawString(245,710,"Datos del Paciente")
    c.drawString(50,680,"Nombres: " + str(self.Nombre.text()))
    c.drawString(300,680,"Apellidos: " + str(self.Apellido.text()))
    c.drawString(50,660,"Edad:" + self.Edad.text() + "  Años         Género:" + self.Genero.currentText() + 
    "            Altura:" +self.Altura.text() +"  cm        Peso:"+self.Peso.text()+'  kg') 
    

def Pdf_datos_facial(self):
    c.line(50,655,550,655)
    c.drawString(250,630,"FASE FACIAL")
    c.drawString(50,600,"Hendidura Palpebral Antimongoloide " +'    Ojo Derecho:' +self.Angulo_ojo_2.text()+ '      Ojo Izquierdo:'+ self.Angulo_ojo_1.text())
    c.drawString(50,580,"Rostro Triangular: "+self.Prominente.text())
    c.drawString(50,560,"Orejas Aladas (Atípicas): "+self.Prominente.text())
    c.drawImage("./fotos_facial/foto.png", 150, 300, width= 320, height=240)
    c.showPage()

def pdf_datos_corporal_manos(self):
    c.drawString(220,800,"FASE CORPORAL - MANOS")
    c.drawString(50,770,"Meñique Derecho: "+self.Menique_der.text())
    c.drawString(50,750,"Meñique Izquierdo: "+self.Menique_izq.text())
    c.drawString(50,730,"Pulgar derecho: "+self.Pulgar_der.text())
    c.drawString(50,710,"Pulgar izquierdo: "+self.Pulgar_izq.text())
    c.drawImage("./fotos_manos/foto_menique_derecho.png", 100, 510, width= 160, height=120)
    c.drawImage("./fotos_manos/foto_menique_izquierdo.png", 320, 510, width= 160, height=120)
    c.drawImage("./fotos_manos/foto_pulgar_derecho.png", 100, 350, width= 160, height=120)
    c.drawImage("./fotos_manos/foto_pulgar_izquierdo.png", 320, 350, width= 160, height=120)
    c.showPage()


def pdf_datos_corporal_cuerpo(self):
    c.drawString(240,800,"FASE CORPORAL")
    c.drawString(50,770,"Codo Derecho: "+self.codo_der.text())
    c.drawString(50,750,"Codo Izquierdo: "+self.codo_izq.text())
    c.drawString(50,730,"Rodialla derecha: "+self.rodilla_der.text())
    c.drawString(50,710,"Rodilla izquierda: "+self.rodilla_izq.text())
    c.drawString(50,690,"Pose Manos-Pies: "+self.manos_pies.text())
    c.drawImage("./fotos_cuerpo/foto_codo_derecho.png", 100, 480, width= 120, height=160)
    c.drawImage("./fotos_cuerpo/foto_codo_izquierdo.png", 340, 480, width= 120, height=160)
    c.drawImage("./fotos_cuerpo/foto_rodilla_derecha.png", 100, 290, width= 120, height=160)
    c.drawImage("./fotos_cuerpo/foto_rodilla_izquierda.png", 340, 290, width= 120, height=160)
    c.drawImage("./fotos_cuerpo/foto_Manos_pies.png", 220, 100, width= 120, height=160)
    c.showPage()

def Pdf_guardar():
    #guardamos
    c.save()