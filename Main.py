import tkinter
import threading
import os
import time
from PIL import Image, ImageTk
from Car import Car



def showWindow(window):
    window.update_idletasks()
    window.update()
    


if __name__ == '__main__':
    window  = tkinter.Tk()
    window.title("Hello")
    #window.geometry("1000x1000")

    track_map = [
        [1,1,1,1,1,1],
        [1,0,0,0,0,1],
        [1,0,1,1,1,1],
        [1,0,1,0,0,1],
        [1,1,1,1,1,None]
    ]

    height_num = len(track_map)
    width_num = len(track_map[0])


    canvas = tkinter.Canvas(window,width = 1000, height = 1000)
    canvas.pack() 



    script_dir = os.path.dirname(os.path.realpath("__file__"))
    folder_abs_path = os.path.join(script_dir,"trunk","TrackPieces")

    if script_dir == None: 
        folder_abs_path = "trunk\\TrackPieces"

    grass_image_path = os.path.join(folder_abs_path,"grass.png")
    straight_image_path = os.path.join(folder_abs_path,"straight_2.png")

    im_grass = Image.open(grass_image_path)
    im_straight = Image.open(straight_image_path)

    xsize, ysize = im_grass.size

    im_track = Image.new('RGB',(xsize*width_num,ysize*height_num))

    for y in range(0,len(track_map)):
        for x in range(0,len(track_map[y])):
            box = (xsize*x,ysize*y)
            im=(im_straight if track_map[y][x] == 1 else im_grass)
            print("paste grass to " + str(box))
            im_track.paste(im=im,box=box)

    #im_track.paste(im=car.car_image,box=car.position())

    #im_track.thumbnail((800,800),Image.ANTIALIAS)

    p_image = ImageTk.PhotoImage(im_track)

    
    canvas.create_image(0,0,anchor=tkinter.NW,image=p_image)  
    
    car = Car(canvas)

    
    while 1:
        showWindow(window)
        car.move()
        time.sleep(0.05)