import cv2
import pyttsx3

cap = cv2.VideoCapture(0)

engine=pyttsx3.init()
engine.setProperty("rate",158)

engine.say("INICIANDO PROTOCOLO BACK TU SII")
engine.runAndWait()
engine.say("ESTO TOMARA UNOS SEGUNDOS...")
engine.runAndWait()
engine.say("ACERCATE A EL SONIDO Y MUESTRA TU PRENDA!")
engine.runAndWait()

while True:
    success, img = cap.read()

    hsv_frame=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    largo,ancho,_=img.shape

    cx=int(ancho/2)
    cy=int(largo/2)

    pixel_center=hsv_frame[cy,cx]

    color="INDEFINIDO"

    if pixel_center[0]<179 and pixel_center[1]<255 and pixel_center[2]<59:
        color="NEGRO"
    elif pixel_center[0]<179 and pixel_center[1]<10 and pixel_center[2]<216:
        color="GRIS"
    elif pixel_center[0]<179 and pixel_center[1]<10 and pixel_center[2]<255:
        color="BLANCO"
    elif pixel_center[0]<5 and pixel_center[2]<255:
        color="ROJO"
    elif pixel_center[0]<19 and pixel_center[2]<255:
        color="NARANJO"
    elif pixel_center[0]<35 and pixel_center[2]<255:
        color="AMARILLO"
    elif pixel_center[0]<77 and pixel_center[2]<255:
        color="VERDE"
    elif pixel_center[0]<96 and pixel_center[2]<255:
        color="CELESTE"
    elif pixel_center[0]<130 and pixel_center[2]<255:
        color="AZUL"
    elif pixel_center[0]<143 and pixel_center[2]<255:
        color="MORADO"
    elif pixel_center[0]<165 and pixel_center[2]<255:
        color="ROSADO"
    elif pixel_center[0]<179 and pixel_center[2]<255:
        color="ROJO"
    else:
        color="NO DEFINIDO"
   


    pixel_center_bgr=img[cy,cx]
    b,g,r=int(pixel_center_bgr[0]),int(pixel_center_bgr[1]),int(pixel_center_bgr[2])
    
    cv2.circle(img,(cx,cy),3,(0,225,0),3)
        
    flipmask= cv2.flip(img, 1)
    cv2.putText(flipmask,color,(10,50),0,1,(b,g,r),2)
    cv2.imshow("img", flipmask)

    if cv2.waitKey(1) & 0xFF == ord('w'):
        engine.say(color)
        engine.runAndWait()
        
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        
        engine.say("HASTA LUEGO, RECUERDA QUE ESTO ES SOLO UNA BETA, AúN ESTAMOS TRABAJANDO EN MEJORAR, MUCHAS GRACIAS!")
        engine.runAndWait()
        engine.say("TERMINANDO PROGRAMA...")
        engine.runAndWait()

        break
