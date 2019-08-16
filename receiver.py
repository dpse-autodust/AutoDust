import socket
import time
import cv2, os

s = time.time()

conn = socket.socket()
host = '192.168.1.33'
port = 8080
conn.connect((host,port))
print("Connected to", host," on port", port) 

def receive_image():
    size = eval(conn.recv(2048).decode())
    conn.send(b'1')
    #print(size)
    
    pack_size = 2048
    img_data = b''
    while len(img_data)<size:
        img_data += conn.recv(pack_size)
        #print(len(img_data))
        conn.send(b'1')
        
    with open(r'images\img.jpg','wb') as f:
        f.write(img_data)
    
    e = time.time()
    print(e-s)

    image = cv2.imread(r'images\img.jpg')

    #os.remove(r'C:\Users\aayus\Desktop\PROJECTS\Object Classifier\yolo-object-detection\img.jpg')

    return image
