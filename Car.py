import os
import tkinter
from PIL import Image, ImageTk

class Car:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x_pos = 0
        self.y_pos = 0
        self.rotation = 0
        self.velocity = 0
        self.car_image = self.load_car_image()
        self.photo_image = ImageTk.PhotoImage(self.car_image)
        self.car_ref = canvas.create_image(0,0,anchor=tkinter.NW,image=self.photo_image)


    def load_car_image(self):
        script_dir = os.path.dirname(os.path.realpath("__file__"))
        folder_abs_path = os.path.join(script_dir,"trunk","TrackPieces")

        if script_dir == None: 
            folder_abs_path = "trunk\\TrackPieces"

        car_image_path = os.path.join(folder_abs_path,"WILHELM.png")
 
        return Image.open(car_image_path)

    def position(self):
        return (self.x_pos,self.y_pos)

    def move(self):
        self.y_pos += 1
        self.canvas.move(self.car_ref,0,1)

    
    