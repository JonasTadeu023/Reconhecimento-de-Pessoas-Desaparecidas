#Importando as ferramentas
import os.path;
import face_recognition as fr;
import numpy as np;

#Caminho onde deve pegar as imagens
caminhos = os.listdir('images_missing');

#percorre o caaminho das imagens
for nome in caminhos:
    caminho = ('images_missing/'+nome);
    pessoas = os.listdir(caminho);
    
    #Percorre o caminho de pessoas
    for nomes in pessoas:
        caminho1 = ('images_missing/'+nome+'/'+nomes);
        image = fr.load_image_file(caminho1);
        image_enconding = fr.face_encodings(image)[0];
        caminho2 = ('training_sucsess/'+nome+'/'+nome);
        caminho3  = ('training_sucsess/'+nome);

        #Verifica se ja existe uma pasta com esse nome
        if os.path.exists(caminho3):
            print("ja existe");
        else:
            #Cria uma pasta com o nome da pessoa desaparecida
            os.mkdir(caminho3);
            #Salva o arquivo com a decodificação da pessoa desaparecida
            with open(caminho2+'.txt', "wb") as f:
                np.savetxt(f, np.column_stack(image_enconding), fmt="%1.10f");