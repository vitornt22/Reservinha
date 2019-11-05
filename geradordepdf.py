from reportlab.pdfgen import canvas
from reportlab.platypus import Image

class GeraPDF(object):
    def __init__(self,nome_arquivo):
        pdf = canvas.Canvas(nome_arquivo+".PDF")
        img = 'Ufpi_brasão.jpg'
        pdf.setFont("Helvetica",20)
        pdf.drawString(150, 800, "UNIVERSIDADE FEDERAL DO PÍAUI")
        pdf.setFont("Helvetica",12)
        pdf.drawImage(img,200,550,width=200,height=200)
        pdf.drawString(0, 500, "O Seguinte pessoa está habilitada a utilizar a sala 809:")
        pdf.drawString(300,500, "José Maria dos Santos Leal CPF: 123.123.123")
        
       
       
        pdf.save()

 
teste = GeraPDF("FORMAT")
