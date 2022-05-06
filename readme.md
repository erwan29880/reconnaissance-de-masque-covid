# détection de visages et de masques


> Contexte du projet

Nous cherchons à améliorer l’application qui a été développée lors de dernier Brief. Il faudra développer une application Streamlit qui sera capable à détecter/localiser le ou les visages dans une image, et détecter par la suite la présence ou l’absence du masque pour chaque visage détecté.

​

## ce que fait l'application :

L'application a été developpée avec une image streamlit Docker. La première commande à faire est donc : 

> docker-compose up --build

Je déconseille le mode détaché, afin de pouvoir récupérer l'url de l'application sur le réseau local.​

Une liste déroulante dans l'application vous permet de choisir un chargement d'image via une url (jpg, png, jpeg) ou via votre ordinateur. Quelques urls sont proposées pour tester l'application : 
- image du BBH avec plusieurs visages
- image avec plusieurs visages et avec masques
- image avec un seul visage

L'application va tout d'abord détecter les visages ; quand les visages sont masqués, la détection de visages n'est pas optimale.

L'application va ensuite isoler les visages et les mettre à la bonne dimension afin d'utiliser un modèle d'IA créé lors d'un exercice précédent*, et effectuer les prédictions afin de déterminer s'il y a un masque ou non.

Le fichier d'IA, sous forme .h5 (tensorflow), n'est pas disponible sur github (1.5GB). Je le mets à disposition <a href="http://erwan-diato.com/mod2.h5">ici</a> (<i>note : chrome bloque le téléchargement</i>)



* https://github.com/erwan29880/mask_recognition
