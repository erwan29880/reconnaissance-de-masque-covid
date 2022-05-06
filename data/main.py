from distutils.file_util import move_file
import re
import streamlit as st
import pandas as pd
import cv2
import matplotlib.pyplot as plt
import time
import pandas as pd
from datetime import datetime
import urllib.request
import numpy as np
import keras



def affichage(src):

    modelMasque = keras.models.load_model("./modele/mod2.h5")   

    
    # cette fonction prend en entrée un tableau numpy en 3 dimensions
    # elle affiche une image avec détection de visages et de masques
    # elle affiche le nombre de personnes détectées
    # elle affiche les dernières personnes détectées (mais cela n'est pas très correct déontologiquement)
    

    color = (255, 255, 255)             # La couleur du carré qui entoure le visage détecté
    red = (220, 20, 60)                 # La couleur du carré qui entoure le visage détecté
    i = 1                               # le nombre de personnes détectées, pour incrémentation
    df = pd.read_csv('data.csv')        # le dataframe des personnes détectées, avec jour et heure
    cascade_path =  "./cascades/haarcascade_frontalface_default.xml"
   


    # détection des visages
    cascade = cv2.CascadeClassifier(cascade_path)
    rect = cascade.detectMultiScale(src)


    
    
    
    
    # tracé des rectangles autour des visages
    # tracé de l'identifiant des personnes
    if len(rect) > 0:
        for x, y, w, h in rect:
            cv2.rectangle(src, (x, y), (x+w, y+h), color)
            cv2.rectangle(src, (x,y-10), (x+w,y-40), red, -1)

            # slicing pour la reconnaissance de masque
            roi_color = src[y:y + h, x:x + w]


            stri = 'p.'+ str(i)
            cv2.putText(src, stri ,(x+5, y-15), cv2.FONT_HERSHEY_SIMPLEX, .5, (0,0,0))
            i = i + 1


            capture = cv2.resize(roi_color, (224, 224))
            st.image(capture)
            capture = capture.reshape((1, capture.shape[0], capture.shape[1], capture.shape[2]))
            predict = modelMasque.predict(capture)
            pasDeMasque = predict[0][0]
            avecMasque = predict[0][1]
            # Interpretation de la prediction
            if (pasDeMasque > avecMasque):
                st.text('masque non détecté !')
            else:
                st.text('masque détecté !')



            # pour que le timestamp soit un peu différent
            time.sleep(0.1)
           
            # récupérer le timestamp unix
            timest = time.time() + (2*3600)                 # fuseau horaire docker par défaut, il faut ajouter 2h
            dt_object = datetime.fromtimestamp(timest)      # transformer le timestamp en date
            dd = dt_object.strftime('%Y-%m-%d')             # récupérer Y M D à partir de la date
            da = dt_object.strftime('%H:%M:%S')             # récupérer l'heure à partir de la date
            
            # créer un dataframe "ligne" et le concaténer avec l'existant
            df_new_line = pd.DataFrame([[stri, dd, da]], columns=('personnes', 'date', 'heure') )
            df = pd.concat([df,df_new_line], ignore_index=True)
   



    # enregistremet du csv
    df.to_csv('data.csv', index=False)

    # affichage de l'image

    if src.shape[0] > src.shape[1]:
        st.image(src, width=400)
    else:
        st.image(src, width=800)

    # affichage du nombre de personnes détectées et changement du texte en fonction du nombre
    if i-1 > 1:
        st.subheader(str(i-1) + ' personnes ont été détectées !')
    elif i-1 == 1:
        st.subheader(str(i-1) + ' personnes a été détectée !')
    elif i-1 == 0:
        st.subheader('Aucune personne détectée !')


    # affichage des dernières entrées du dataframe
    st.subheader('Dernières personnes détectées :')
    st.write(df.tail())


# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------
# début de l'affichage ------------------


st.title('Reconnaissance faciale')

st.text('Si les personnes ont des masques, parfois le visage n\'est pas reconnu !')


# sidebar de choix :
activities = ['----\/----','télécharger par url', 'télécharger de votre ordinateur']
choice = st.sidebar.selectbox("Votre choix :", activities) # selectbox



if choice=="----\/----":
    st.text('choisissez une option !')
    st.text('c\'est par là <<----- !')

elif choice == 'télécharger par url':
    st.text('Exemple d\'urls que vous pouvez utiliser : ')
    st.text('https://i0.wp.com/www.femmesdesport.fr/wp-content/uploads/2021/05/bbh8.jpg?resize=720%2C405&ssl=1')
    st.text('http://www.pharmaciedugrandjardin.com/wp-content/uploads/2020/05/Masques-1024x1024.png')

    url = st.text_input("Ouvrir une image d'internet :", 'https://www.elle.be/fr/wp-content/uploads/2018/07/skincare-480x545.jpg') 
    if(st.button('Valider')): 
        result = url.title() 
        st.success(result) 
   
        if 'jpg' in url:
            nom = './images/gfg.jpg'
        elif 'jpeg' in url:
            nom = './images/gfg.jpeg'
        elif 'png' in url:
            nom = './images/gfg.png'

        urllib.request.urlretrieve(url, nom)
        img_path = cv2.imread(nom)
        img_path = cv2.cvtColor(img_path, cv2.COLOR_BGR2RGB)
        st.sidebar.image(img_path, width=240)
                  
        affichage(img_path)

        

elif choice == 'télécharger de votre ordinateur':

    image_file = st.file_uploader("Upload image", type=['jpeg', 'jpg', 'png']) # streamlit function to upload file
    if image_file is not None:        
        st.sidebar.image(image_file, width=240)
        image_file = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), 1)
        image_file = cv2.cvtColor(image_file, cv2.COLOR_BGR2RGB)
        affichage(image_file)