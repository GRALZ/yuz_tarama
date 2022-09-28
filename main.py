import cv2

import face_recognition


kamera=cv2.VideoCapture(0)
m1=face_recognition.load_image_file("resim.jpg")
enm1=face_recognition.face_encodings(m1)[0]
font=cv2.FONT_HERSHEY_SIMPLEX

while True:
     ret,kare=kamera.read()
     kare=cv2.resize(kare,(500,300))

     faceloc=face_recognition.face_location(kare)
     enmt=face_recognition.face_encoding(kare,faceloc)

     if enmt==[]:
        pass
     else:
        matchedfaces=face_recognition.compare_faces(enm1, enmt)
        a=0

     for i in matchedfaces:
      if i== True:
         for (y,x2,y2,x) in [faceloc[a]]:
               cv2.rectangle(kare,(x,y),(x2,y2),(255,0,0),2)
               cv2.putText(kare, "resim", (x.y),font,0.9,(255,0,255),2)
      else:
            for (y,x2,y2,x) in [faceloc[a]]:
                   cv2.rectangle(kare,(x,y),(x2,y2),(255,0,0),2)
                   cv2.putText(kare, "undefined", (x.y),font,0.9,(255,0,255),2)
                   a=a+1         
     cv2. imshow("kamera",kare)
     if cv2.waitKey(1)& 0xFF== ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()