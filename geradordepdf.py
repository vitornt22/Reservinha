from reportlab.pdfgen import canvas
from reportlab.platypus import Image

class GeraPDF(object):
    def __init__(self,pessoa,sala,horario):
        self.pessoa = pessoa
        self.hora = horario
        self.sala = sala
    def cria(self):
        pdf = canvas.Canvas(self.pessoa.getNome()+".pdf")
        img = 'Ufpi_brasão.jpg'
        pdf.setFont("Helvetica",20)
        pdf.drawString(150, 800, "UNIVERSIDADE FEDERAL DO PÍAUI")
        pdf.setFont("Helvetica",12)
        pdf.drawImage(img,200,550,width=200,height=200)
        pdf.drawString(0, 500, "O Seguinte pessoa está habilitada a utilizar a sala :"+self.sala)
        pdf.drawString(0,450, "Nome: "+self.pessoa.getNome()  )
        pdf.drawString(0,430," CPF: "+self.pessoa.getCpf())
        pdf.drawString(0,410," Horario: " + self.hora + " as " + str(int(self.hora)+2) +" Horas")
        pdf.save()

 
