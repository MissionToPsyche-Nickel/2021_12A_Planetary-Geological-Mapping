import numpy as np
import cv2 
import PySimpleGUI as sg
import crater

dt = crater.Detection()


# Making The Blank Image
image = cv2.imread(dt.getImageToDraw())
#image = cv2.imread('/home/user1/Desktop/Capstone/BeerMartianCrater.jpg')
drawing = False
ix = 0
iy = 0
# Adding Function Attached To Mouse Callback
def draw(event,x,y,flags,params):
    dt = crater.Detection()
    global ix,iy,drawing
    # Left Mouse Button Down Pressed
    if(event==1):
        drawing = True
        ix = x
        iy = y
    if(event==0):
        if(drawing==True):
            #For Drawing Line
            cv2.line(image,pt1=(ix,iy),pt2=(x,y),color=(255,255,255),thickness=3)
            ix = x
            iy = y
            # For Drawing Rectangle
            # cv2.rectangle(image,pt1=(ix,iy),pt2=(x,y),color=(255,255,255),thickness=3)
    if(event==4):
        drawing = False



def openDraw():
        try:
            # Making Window For The Image
            cv2.namedWindow("Window")

            # Adding Mouse CallBack Event
            cv2.setMouseCallback("Window",draw)

            # Starting The Loop So Image Can Be Shown
            while(True):

                cv2.imshow("Window",image)

                if cv2.waitKey(20) & 0xFF == ord('q'):
                    break

            cv2.destroyAllWindows()
        except Exception as e:
            print(e)
    