from reportlab.pdfgen import canvas
class GeraPDF(object):
    def __init__(self,nome_arquivo):
        pdf = canvas.Canvas(nome_arquivo+".PDF")
        pdf.drawString(0, 800, "O Monitor vai ficar na sala de 12 até as 14 horas")
        pdf.save()



