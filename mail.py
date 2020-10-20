import os.path
import json
import pandas as pd
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


#Caminho onde deve pegar as imagens
caminhos = os.listdir('recognized');

#percorre o caminho das imagens
for nome in caminhos:
    caminho = ('recognized/'+nome);
    pessoas = os.listdir(caminho);
    
    #Percorre o caminho de pessoas
    for nomes in pessoas:
        #var nome = email que deve ser enviado
        fromaddr = "seu email"
        toaddr = nome
        msg = MIMEMultipart()

        msg['From'] = fromaddr 
        msg['To'] = toaddr
        msg['Subject'] = "Uma pessoa cadastrada por você foi reconhecida!!!"

        body = "\nNosso sistema acabou de reconhecer, tal pessoa na data tal. Em anexo irá a foto do reconhecido"

        msg.attach(MIMEText(body, 'plain'))

        filename = 'recognized/jonastadeu006@gmail.com/Jonas.png'

        attachment = open(filename,'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(part)

        attachment.close()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "sua_senha")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
