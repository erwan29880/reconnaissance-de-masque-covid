import cv2
import matplotlib.pyplot as plt
import time
import pandas as pd
from datetime import datetime


# varaibles globales
cascade_path =  "./cascades/haarcascade_frontalface_default.xml"
img_path = "./images/001.jpg"
img_path = "./images/002.jpg"

color = (255, 255, 255) #La couleur du carré qui entoure le visage détecté
red = (220, 20, 60) #La couleur du carré qui entoure le visage détecté


src = cv2.imread(img_path,0)
gray = cv2.cvtColor(src,cv2.cv2.COLOR_BAYER_BG2GRAY)
cascade = cv2.CascadeClassifier(cascade_path)
rect = cascade.detectMultiScale(gray)

i = 1
personnes = []
date1 = []
date2 = []

if len(rect) > 0:
    for x, y, w, h in rect:
        cv2.rectangle(src, (x, y), (x+w, y+h), color)
        cv2.rectangle(src, (x,y), (x+w,y+20), red, -1)

        stri = 'personne '+ str(i)
        cv2.putText(src, stri ,(x+5, y+10), cv2.FONT_HERSHEY_SIMPLEX, .5, (0,0,0))
        i = i + 1
        time.sleep(0.1)

        personnes.append(stri)
        timest = time.time()
        dt_object = datetime.fromtimestamp(timest)
        dd = dt_object.strftime('%Y-%m-%d') 
        da = dt_object.strftime('%H:%M:%S') 
        date1.append(dd)
        date2.append(da)
        


df = pd.DataFrame(list(zip(personnes, date1, date2)), columns=('personnes', 'date', 'heure'))
df.to_excel('data.xlsx', index=False)






cv2.imshow('detected', src)
cv2.waitKey(0)
cv2.destroyAllWindows()




