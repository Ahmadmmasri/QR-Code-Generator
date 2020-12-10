import os
import qrcode 

img=qrcode.make("https://www.youtube.com/watch?v=kM4oZTJaO8k")
img.save("qr.png", "PNG")
os.system("start qr.png")