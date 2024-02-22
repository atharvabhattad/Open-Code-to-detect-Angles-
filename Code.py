import cv2
import math

path = 'Untitledpicfinal.jpg'
img = cv2.imread(path)
p = []

def m(temp,x,y,flags,params):
    if temp == cv2.EVENT_LBUTTONDOWN:
        size = len(p)
        if size != 0 and size % 3 != 0:
            cv2.line(img,tuple(p[round((size-1)/3)*3]),(x,y),(0,0,255),2)
        cv2.circle(img,(x,y),5,(0,0,255),cv2.FILLED)
        p.append([x,y])

def gradient(pt1,pt2):
    return (pt2[1]-pt1[1])/(pt2[0]-pt1[0])

def getAngle(p):
    pt1, pt2, pt3 = p[-3:]
    m1 = gradient(pt1,pt2)
    m2 = gradient(pt1,pt3)
    angR = math.atan((m2-m1)/(1+(m2*m1)))
    angD = round(math.degrees(angR))
    cv2.putText(img,str(angD),(pt1[0]-40,pt1[1]-20),cv2.FONT_ITALIC,
                1.5,(0,0,255),2)


while True:
    if len(p) % 3 == 0 and len(p) !=0:
        getAngle(p)


    cv2.imshow('Img',img)
    cv2.setMouseCallback('Img',m)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        p = []
        img = cv2.imread(path)
