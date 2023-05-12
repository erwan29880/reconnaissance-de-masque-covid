# détection de visages et de masques


Application streamlit pour détecter/localiser le ou les visages dans une image, et détecter par la suite la présence ou l’absence du masque pour chaque visage détecté.


## ce que fait l'application :

L'application a été developpée avec une image streamlit Docker. La première commande à faire est donc : 

> docker-compose up -d --build

L'application est alors disponible en localhost sur le port 8888.

Une liste déroulante dans l'application permet de choisir un chargement d'image via une url (jpg, png, jpeg) ou en local. Quelques urls sont proposées pour tester l'application : 
- image du Brest Bretagne Handball avec plusieurs visages
- image avec plusieurs visages et avec masques
- image avec un seul visage

L'application va tout d'abord détecter les visages avec un algorithme disponible avec openCv, puis isoler les visages et les mettre à la bonne dimension afin d'utiliser un modèle d'IA (réseau de neurones à convolutions en transfer learning), et effectuer les prédictions afin de déterminer s'il y a un masque ou non.
