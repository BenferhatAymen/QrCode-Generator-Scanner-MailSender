import cv2
from pyzbar.pyzbar import decode
import json
import numpy as np 
import time
from mailCsv import writecsv
with open("db/mails.json",encoding="UTF-8") as f:
    mails = json.load(f)
mails.setdefault("mails",{})
participants = mails["mails"].keys()
print(participants)
Camera = cv2.VideoCapture(0)
Camera.set(3,640) 
Camera.set(4,480)
enabledCamera = True
while True:
 
    success, img = Camera.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        
 
        if myData in participants:
            myOutput = 'Authorized'
            myColor = (0,255,0)
            mails["mails"][myData]="true"
            with open('db/mails.json','w') as f:
                json.dump(mails, f, ensure_ascii=False, indent=4)
            writecsv('newcsv.csv',{myData : "true"})



        else:
            myOutput = 'Un-Authorized'
            myColor = (0, 0, 255)
 
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,myColor,5)
        pts2 = barcode.rect
        cv2.putText(img,myOutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,myColor,2)
        
        
 
    cv2.imshow('GDSC SCANNER',img)
    cv2.waitKey(1)
