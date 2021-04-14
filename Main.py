import tkinter
import threading
import os

def showWindow():
    window  = tkinter.Tk()
    window.title("Hello")
    window.geometry("800x800")



    canvas = tkinter.Canvas(window)



    script_dir = os.path.dirname(os.path.realpath("__file__"))
    abs_path = os.path.join(script_dir,"trunk","TrackPieces","grass.png")

    print ("dir:" + script_dir)
    print (abs_path)

    if script_dir == None: 
        abs_path = "trunk\\TrackPieces\\grass.png"

    img = tkinter.PhotoImage(file=abs_path)

    for x in range(0,1):
        for y in range(0,1):
            canvas.create_image((x*300,y*300),anchor=tkinter.NW,image=img)  

    canvas.pack(
            # fill="both"
            # ,
            expand=True
            )

    window.mainloop()
    

print ("Hellow, world!")


t2 = threading.Thread(target = showWindow)
t2.start()


print("hello, again!")


