#Install zbar and Pyzbar (pyzbar only if you are using Python version 3 or later)
#!pip install zbar
#!pip install pyzbar

#Import libraries 
import cv2 as cv
import numpy as np
import pyzbar.pyzbar as pzb
#from pyzbar.pyzbar import decode


# Create a function to detect Qrcode and Barcode
webcam = cv.VideoCapture(1)
def detector(webcam):
    
    while(True):
      
        # Capture the video frame by frame
        video, frame = webcam.read()
        
        # Find barcodes and Qr
        for barcode in pzb.decode(frame):
            
            # Print the data got from the barcode lecture
            #print(barcode.data)
            
            # Convert de data from bytes to string
            mydata = barcode.data.decode('utf-8')
            print(mydata)
            
            # Add bounding box to qr codes and barcodes
            points = np.array([barcode.polygon], np.int32)
            
            # Print the possition of the qr code or barcode
            #print(points)
            
            points = points.reshape (-1,1,2)
            cv.polylines(frame, [points], True, (255,0,0),5) #draw a polygon on an image
            
            # Add text over the bounding box
            points2 = barcode.rect
            cv.putText(frame, mydata, (points2[0], points2[1]), cv.FONT_HERSHEY_SIMPLEX,
                      0.9, (255,0,0), 2)
  
        # Display the resulting frame
        cv.imshow('frame', frame)
      
        #the 'd' button is set as the quitting button
        if cv.waitKey(1) & 0xFF == ord('d'):
            webcam.release()
            cv.destroyAllWindows()
            break

#Main             
if __name__ == '__main__':
    webcam = cv.VideoCapture(0)


#To execute the function run:
detector(webcam)
