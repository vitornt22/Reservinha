import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
from geradordepdf import GeraPDF

def send_an_email():
    gerador = GeraPDF("TESTE") #GERA PDF
    
    toaddr = 'j-maria-lima2015@bol.com.br'  # Aqui é quem vai receber
    me = 'jm452532@gmail.com' #Aqui é quem vai enviar
    subject = "RESERVA DE SALA" #TITULO DO EMAIL

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = toaddr
    msg.preamble = "teste " 
    #msg.attach(MIMEText(text))

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("TESTE.pdf", "rb").read()) #arquivo que vai ser aberto
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="TESTE.PDF"') 
    msg.attach(part)

    
    s = smtplib.SMTP('smtp.gmail.com', 587)
    
    s.starttls()
    s.login('EMAIL da conta GMAIL','SENHA DO GMAIL')

    #no campo logn vc coloca seu email e senha, o email e senha deve ser do gmail
    # e o acesso deve ser permitido atraves de uma configuração de conta do gmail
    # sendo que esse codigo esta totalmente funcional
    #s.send_message(msg)
    s.sendmail(me, toaddr, msg.as_string())
    s.quit()
    
    
send_an_email()
