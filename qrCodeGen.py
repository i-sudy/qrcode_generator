#SD 08/05/2020 QR Code generator 
# installation pip install pillow qrcode
from PIL import Image , ImageDraw
from datetime import datetime
import qrcode
val = input("Enter your value: ")
data = val
image = qrcode.make(data)
image.save(val +"_"+datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ".png")

