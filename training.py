import os.path;
import face_recognition as fr;
import numpy as np;


caminhos = os.listdir('images_missing');

for nome in caminhos:
    caminho = ('images_missing/'+nome);
    pessoas = os.listdir(caminho);
    
    for nomes in pessoas:
        caminho1 = ('images_missing/'+nome+'/'+nomes);
        image = fr.load_image_file(caminho1);
        image_enconding = fr.face_encodings(image)[0];
        caminho2 = ('training_sucsess/'+nome+'/'+nome);
        caminho3  = ('training_sucsess/'+nome);

        if os.path.exists(caminho3):
            print("ja existe");
        else:
            os.mkdir(caminho3);
            with open(caminho2+'.txt', "wb") as f:
                np.savetxt(f, np.column_stack(image_enconding), fmt="%1.10f");