import socket
import time
#import cv2, os

s = time.time() #Initiating a stopclock allowing us to gauge image recevial runtime

conn = socket.socket() 
host = '192.168.1.33'
port = 8080
conn.connect((host,port)) #Establishes server-client connection
print("Connected to", host," on port", port) 

def receive_image():
    size = eval(conn.recv(2048).decode()) #returns image size in bytes
    conn.send(b'1') 
    #print(size)
    
    pack_size = 2048 #splitting image receival pack size into smaller packs, allowing complete capture of image
    img_data = b''
    while len(img_data)<size:
        img_data += conn.recv(pack_size) 
        #print(len(img_data))
        conn.send(b'1') #sends a dummy byte to avoid entaglment of image data
        
    with open(r'images\img.jpg','wb') as f:
        f.write(img_data) #write the image data as a .jpg file
    
    e = time.time() #ends stopclock
    print(e-s) #returns the final runtime
    
    '''
    #image = cv2.imread(r'images\img.jpg')

    #os.remove(r'C:\Users\aayus\Desktop\PROJECTS\Object Classifier\yolo-object-detection\img.jpg')

    #return image
    '''
