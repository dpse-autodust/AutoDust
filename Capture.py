import cv2
import subprocess, os

def CaptureProcess():
    
    subprocess.call(r'python yolo.py --image images\img.jpg --yolo yolo-coco',shell=True)

    #C:\Users\aayus\Desktop\PROJECTS\Object Classifier\yolo-object-detection\obj.txt

    def get_obj():
        with open('obj.txt','r') as f:
            obj = f.read()
        os.remove(r'C:\Users\aayus\Desktop\AutoDust\Object Classifier\yolo-object-detection\obj.txt')

        l = obj.split(",")
      
        items = []
        if len(l)==1:
                text = l[0][1:-1].strip()[1:-1]
                items.append(text)
        else:
            for i in range(len(l)):
                if i==0:
                    text = l[i][1:].strip()[1:-1]
                    items.append(text)
                elif i==(len(l)-1):
                    text = l[i][:-1].strip()[1:-1]        
                    items.append(text)
                else:
                    text = l[i].strip()[1:-1]
                    items.append(text)
                
        return items

    objects = get_obj()
    for j in range(objects.count('person')):
        objects.remove('person')

    '''
    #person
    bicycle
    car
    motorbike
    aeroplane
    bus
    train
    truck
    boat
    traffic light
    fire hydrant
    stop sign
    parking meter
    bench
    bird
    cat
    dog
    horse
    sheep
    cow
    elephant
    bear
    zebra
    giraffe
    backpack
    umbrella
    handbag
    tie
    suitcase
    frisbee
    skis
    snowboard
    sports ball
    kite
    baseball bat
    baseball glove
    skateboard
    surfboard
    tennis racket
    bottle
    wine glass
    cup
    fork
    knife
    spoon
    bowl
    banana
    apple
    sandwich
    orange
    broccoli
    carrot
    hot dog
    pizza
    donut
    cake
    chair
    sofa
    pottedplant
    bed
    diningtable
    toilet
    tvmonitor
    laptop
    mouse
    remote
    keyboard
    cell phone
    microwave
    oven
    toaster
    sink
    refrigerator
    book
    clock
    vase
    scissors
    teddy bear
    hair drier
    toothbrush
    '''

    #0-BIO
    #1-NON-BIO

    def dbcreation():
        x = {}
        for i in "bird.cat.dog.horse.sheep.cow.elephant.bear.zebra.giraffe.banana.apple.sandwich.orange.broccoli.carrot.hot dog.pizza.donut.cake.chair.sofa.pottedplant".split("."):
            x[i] = 0

        for i in "bench.parking meter.stop sign.fire hydrant.traffic light.boat.truck.train.bus.aeroplane.motorbike.car.bicycle.backpack.umbrella.handbag.tie.suitcase.frisbee.skis.snowboard.sports ball.kite.baseball bat.baseball glove.skateboard.surfboard.tennis racket.bottle.wine glass.cup.fork.knife.spoon.bowl.bed.diningtable.toilet.tvmonitor.laptop.mouse.remote.keyboard.cell phone.microwave.oven.toaster.sink.refrigerator.book.clock.vase.scissors.teddy bear.hair drier.toothbrush".split("."):
            x[i] = 1

        return x

    db = dbcreation()

    detected = []
    for i in objects:
        try:
            if db[i]==0:
                detected.append(0)            
                #print(i+":"+" Bio"+" 0")
            else:
                detected.append(1)
                #print(i+":"+" Non-Bio" + " 1")
        except:
            detected.append(1)
            #print(i+":"+" Non-Bio" + " 1")


    return objects, detected

