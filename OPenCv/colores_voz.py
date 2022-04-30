import cv2
import pyttsx3

cap = cv2.VideoCapture(0)

engine=pyttsx3.init()

while True:
    success, img = cap.read()

    hsv_frame=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    largo,ancho,_=img.shape

    cx=int(ancho/2)
    cy=int(largo/2)

    pixel_center=hsv_frame[cy,cx]

    color="INDEFINIDO"
   

    if pixel_center[0]<5:
        color="ROJO"
    elif pixel_center[0]<22:
        color="NARANJO"
    elif pixel_center[0]<33:
        color="AMARILLO"
    elif pixel_center[0]<78:
        color="VERDE"
    elif pixel_center[0]<131:
        color="AZUL"
    elif pixel_center[0]<131:
        color="MORADO"
    else:
        color="INDEFINIDO"

    pixel_center_bgr=img[cy,cx]
    b,g,r=int(pixel_center_bgr[0]),int(pixel_center_bgr[1]),int(pixel_center_bgr[2])
    
    cv2.circle(img,(cx,cy),3,(0,225,0),3)
        
    flipmask= cv2.flip(img, 1)
    cv2.putText(flipmask,color,(10,50),0,1,(b,g,r),2)
    cv2.imshow("img", flipmask)

    if cv2.waitKey(1) & 0xFF == ord('w'):
        engine.say(color)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break