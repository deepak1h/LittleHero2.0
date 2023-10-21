import RPi.GPIO as hero
import time


#left motor
left1=16
left2=21
left_en=20

#right motor
right1=14
right2=15
right_en=18

#ultrasonic
trigPin=23
echoPin=24

#mode switch
mode=12
count=0


hero.setwarnings(False)
hero.setmode(hero.BCM)

hero.setup(left1,hero.OUT)
hero.setup(left2,hero.OUT)
hero.setup(left_en,hero.OUT)
hero.setup(right1,hero.OUT)
hero.setup(right2,hero.OUT)
hero.setup(right_en,hero.OUT)
hero.setup(mode,hero.IN)



def forward():
    hero.output(left_en, True)
    hero.output(right_en,True)
    hero.output(left1,True)
    hero.output(left2,False)
    hero.output(right1,True)
    hero.output(right2,False)

def left():
    hero.output(left_en, True)
    hero.output(right_en,True)
    hero.output(left1,False)
    hero.output(left2,True)
    hero.output(right1,True)
    hero.output(right2,False)

def right():
    hero.output(left_en, True)
    hero.output(right_en,True)
    hero.output(left1,True)
    hero.output(left2,False)
    hero.output(right1,False)
    hero.output(right2,True)

def brake():
    hero.output(left_en,False)
    hero.output(right_en,False)
    hero.output(left1,False)
    hero.output(left2,False)
    hero.output(right1,False)
    hero.output(right2,False)

def back():
    hero.output(left_en,True)
    hero.output(right_en,True)
    hero.output(left1,False)
    hero.output(left2,True)
    hero.output(right1,False)
    hero.output(right2,True)


def dis():
    print("UltraSonic")
    
    hero.output(trigPin,False)
    time.sleep(0.02)
    hero.output(trigPin, True)
    time.sleep(0.0001)
    hero.output(trigPin,False)
    
    while hero.input(echoPin)==0:
        time_start=time.time()
    while hero.output(echoPin)==1:
        time_end=time.time()

    duration=time_end-time_start

    distance=duration*17150
    
    return distance

def mode1():
    print("mode1")
    distance=dis()
    if distance<=20:
        left()
    else:
        forward()

def mode2():
    print("mode2")
    distance=dis()
    if distance<=40 and distance>25:
        forward()
    elif distance<=25 and diatance>10:
        back()
    elif distance<10:
        lest()
    else:
        brake()

def mode3():
    print("mode3")
    distance=dis()
    if distance<40:
        print("i'm scared")
        left()
        time.sleep(0.5)
        right()
        time.sleep(0.5)
        back()
        time.sleep(0.5)
    else:
        forward()

if __name__=="__main__":
    while(True):
        if hero.input(mode)==1:
            count+=1
            time.sleep(1)
        if count==0:
            print("press switch to select mode")
            time.sleep(1)
        if count==1:
            mode1()
        if count==2:
            mode2()
        if count==3:
            mode3()
        if count>3:
            count=0
            

    
    
        

    
        






    
