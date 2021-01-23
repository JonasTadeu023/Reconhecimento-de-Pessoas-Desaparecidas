import os.path
import json
import pandas as pd
import numpy as np
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
        past = caminho+'/'+nomes
        past2 = caminho+'/'+nome+'.json'
        if past == past2:
            with open(past, 'r') as arq:
                obj = json.load(arq)
                email = obj['Nome']
                data = obj['Data']
        else: 
            image = 'recognized/'+nome+'/'+nomes

    fromaddr = "pytest006@gmail.com"
    toaddr = email
    msg = MIMEMultipart()

    msg['From'] = fromaddr 
    msg['To'] = toaddr
    msg['Subject'] = "Uma pessoa cadastrada por você foi reconhecida!!!"

    body = "\nNosso sistema acabou de reconhecer uma pessoa que foi cadastrada por você. Em anexo irá a foto da pessoa encontrada em "+data

    msg.attach(MIMEText(body, 'plain'))

    filename = image

    attachment = open(filename,'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    attachment.close()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "gremio3590")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
