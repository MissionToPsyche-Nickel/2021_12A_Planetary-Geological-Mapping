import pycda
from pycda.sample_data import get_sample_image
import PySimpleGUI as sg
from pycda import load_image
import numpy as np
import cv2 

class Detection:

    def showImage(self):
        image = get_sample_image()
        #image.show()
        cda = pycda.CDA()
        prediction = cda.get_prediction(image, verbose = True)
        prediction.show()
    
    def getImage(self):
        try:

            layout = [  [sg.Text('Filename')],
                [sg.Input(), sg.FileBrowse(key="-IN-")], 
                [sg.OK(), sg.Exit()]] 

            window = sg.Window('Get filename', layout)

            event, values = window.read()
            window.close()

            if event == 'Exit':
                window.close()
            else:

                image = load_image(values["-IN-"])
                cda = pycda.CDA()
                prediction = cda.get_prediction(image, verbose = True)
                prediction.show()
                prediction.to_csv('/home/aurelio/Desktop/CapstoneFinal/CSVs/results1.csv')
        except:
            print()
        
    def getImageToDraw(self):
        layout = [  [sg.Text('Filename')],
            [sg.Input(), sg.FileBrowse()], 
            [sg.OK(), sg.Cancel()]] 

        window = sg.Window('Get filename', layout)

        event, values = window.read()
        print(values['Browse'])
        value = values['Browse']
        print(value)
        #return value
        window.close()
        return value
