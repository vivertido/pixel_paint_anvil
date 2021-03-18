import anvil.server
from sense_hat import SenseHat
from time import sleep
import datetime


sense = SenseHat()
sense.clear()

@anvil.server.callable
def clear_sense_hat():

    sense.clear()

    pass

@anvil.server.callable
def save_pixels(pixels):
    
    
    sense.clear()
    sense.show_message("saving")
    sleep(2)
    sense.set_pixels(pixels)
    
    #appends to a text file, create if non-existent. 
    with open("my_designs.txt", 'a+') as f:
        ct = datetime.datetime.now() 
        f.write(""+str(ct))
        f.write("\n\n")
        
        current_image = sense.get_pixels()
        f.write(str(current_image) + "\n\n")
        f.write("------------------------------------------------------------------------------" + "\n")
    return "success"

@anvil.server.callable
def paint_pixel(data):
   
    
    color = data["color"]
    x = data["coord"][0]
    y = data["coord"][1]
   
    sense.set_pixel(x, y, color)

    pass

anvil.server.connect("3VXLGUC3VPLYMBYZ5ZNLACP2-JCMXMGJ2VZRZ3MXS")
anvil.server.wait_forever()