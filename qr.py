import os
import qrcode
import sys
def __init__():
    print('Welcome')
    
def start():
    try:
        link=input("enter link to generate qr code: ")
        if not link=="":
            img=qrcode.make(link)
            img.save("qr.png", "PNG")
            os.system("start qr.png")
        else:
            print('insert link')
            start()
    except:
        print('someting wrong happend')
start()

print('Qr code generated seccesfully')
inp=input('to generate another code press 1 to end press 2')
if int(inp)==1:
    start()
else:
    sys.exit()

