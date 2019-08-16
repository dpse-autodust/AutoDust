from tkinter import *
from PIL import Image, ImageTk
import cv2
from Capture import *
from receiver import *
import socket

image = receive_image()

tup = CaptureProcess()
objects = tup[0]
detected = tup[1]

main = Tk()
main.attributes('-fullscreen', True)
main.title("AutoDust Server")
main.configure(bg='light cyan')
fnt = ('Courier New', 35, "bold")
head = Label(main, text="AUTODUST", font=fnt, bg='light cyan', fg='navy')
head.grid(row=0, column=0, columnspan=5, padx=570, pady=30)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
img = Image.fromarray(image)
img = img.resize((750, 500), Image.ANTIALIAS)
tk_image = ImageTk.PhotoImage(img)
image = Label(main, image=tk_image, width=750, height=500, bg="black")
image.grid(row=1, column=0, padx=0, pady=30, rowspan=7)

txt2 = Label(main, text='RESULT:-', font=('Courier New', 20, "bold"), bg='light cyan', fg='navy')
txt2.grid(row=1,column=1)

if len(objects)!=0:
    st=""
    for i in objects[0].split(" "):
        st += (i.capitalize() + " ")
else:
    st = "No Waste"
    
detect = 'Detected Waste: {}'.format(st)
txt3 = Label(main, text=detect, font=('Courier New', 20), bg='light cyan', fg='navy')
txt3.grid(row=2, column=1)

if len(objects)!=0:
    if detected[0] == 0:
        f = "BioDegrabdable"
    else:
        f = "Non-BioDegradable"
else:
    f = "-N/A-"
    
result = 'Waste Type:- {}'.format(f)
txt4 = Label(main, text=result, font=('Courier New', 20), bg='light cyan', fg='navy')
txt4.grid(row=3, column=1, padx=0)

'''conn = socket.socket()
host = '192.168.1.33'
port = 8080
conn.connect((host,port))
print("Connected to", host," on port", port)'''

print(detected, objects)
if len(detected)>0:
    conn.send(str(detected[0]).encode('utf-8'))
else:
    conn.send(b'2')

motor_status = "Idle"
txt5 = Label(main, text='Motor Status: {}'.format(motor_status), font=('Courier New', 20), bg='light cyan', fg='navy')
txt5.grid(row=4, column=1, padx=0)

main.mainloop()
