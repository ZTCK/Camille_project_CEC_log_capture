from __future__ import print_function
import asyncio
import os.path
import os
import websockets
import time  #delete
import cec
import datetime
import serial
from cec_translate import cec_translate
import RPi.GPIO as GPIO
import threading
greeting = ''
now = datetime.datetime
webpage = 0    #1 = ceclogcapture  2 = function debug
start_flag = 2
exitThread = 0
print(cec)
print(websockets)
async def echo(websocket,path):
    global greeting, start_flag, webpage, exitThread
    array = []
    print("\n",websocket)
    print(path)
    ms = '0'
    while 1:
        time.sleep(0.1)
        prewebpage = webpage
        if ms == '1' :
            webpage = 1
            exitThread = 0
        elif ms == '2' : webpage = 2
        if prewebpage != webpage and prewebpage != 0 :
            greeting = ''
            if(start_flag == 1) :
                start_flag = 0
        await websocket.send(str(greeting))
        ms = await websocket.recv()
        print(ms)
        
        if(ms[0:4] == 'save') :
            try : 
                save_path = '/media/usb0/'
                if(os.access(save_path, os.W_OK)) :
                    completeName = os.path.join(save_path, ms[4:ms.find(".txt") + 4]) 
                    file = open(completeName, "w")
                    file.write(ms[ms.find(".txt") + 5:])
                    file.close()
            except :
                greeting += "Save on USB Failed, Save on your PC or phone by create file button"
            cec.remove_callback(cb, cec.EVENT_ALL & ~cec.EVENT_LOG)
            cec.remove_callback(log_cb, cec.EVENT_ALL)
            if(start_flag == 1) :
                start_flag = 0 
            
            
        if webpage == 1 :
            if(ms[0:5] == 'start') :
                greeting = 'start log capture\n'
                if start_flag == 0 :
                    cec.add_callback(cb, cec.EVENT_ALL & ~cec.EVENT_LOG)
                    cec.add_callback(log_cb, cec.EVENT_LOG)
                elif start_flag == 2 :
                    cec.add_callback(cb, cec.EVENT_ALL & ~cec.EVENT_LOG)
                    cec.add_callback(log_cb, cec.EVENT_LOG)
                    cec.init()
                start_flag = 1
                
            elif(ms[0:4] == 'stop') :
                greeting += 'stop log capture\n'
                cec.remove_callback(cb, cec.EVENT_ALL & ~cec.EVENT_LOG)
                cec.remove_callback(log_cb, cec.EVENT_ALL)
                if(start_flag == 1) :
                    start_flag = 0
                
            elif(ms[0:2] == 'tx') :
                print(len(ms))
                print(ms[6:8])
                print(type(ms))
                #try: 
                if(len(ms) <= 8 and len(ms) >= 6) :
                    cec.transmit(int("0x" + ms[4], 16), int("0x" + ms[6:8], 16))
                elif(len(ms) >= 9) :
                    array = []
                    n = 9
                    while(n < len(ms)) :
                        array.append(int("0x" + ms[n:n+2] , 16))
                        n += 3
                    cec.transmit(int("0x" + ms[4], 16), int("0x" + ms[6:8], 16), bytes(array))
                #except ValueError:
                #    greeting += "Invalid Expression!\n"
               
            elif(ms[0:5] == 'clear') :
                greeting = ''
        elif webpage == 2 :
            if(start_flag == 1) :
                start_flag = 0
            #await websocket.send(str(greeting))
            #ms = await websocket.recv()
            #print(exitThread)
            cec.remove_callback(cb, cec.EVENT_ALL & ~cec.EVENT_LOG)
            cec.remove_callback(log_cb, cec.EVENT_ALL)
            if(ms == 'stop') : exitThread = 0
            if(ms[0:5] == 'start') :
                exitThread = 1
                ser = serial.Serial(port = "/dev/serial0")
                if ms[6] == '0' : ser.baudrate = 9600
                elif ms[6] == '1' : ser.baudrate = 14400
                elif ms[6] == '2' : ser.baudrate = 19200
                elif ms[6] == '3' : ser.baudrate = 38400
                elif ms[6] == '4' : ser.baudrate = 57600
                elif ms[6] == '5' : ser.baudrate = 115200
                elif ms[6] == '6' : ser.baudrate = 230400
                elif ms[6] == '7' : ser.baudrate = 460800
                elif ms[6] == '8' : ser.baudrate = 921600
                
                if ms[7] == '0' : ser.bytesize = serial.SEVENBITS
                elif ms[7] == '1' : ser.bytesize = serial.EIGHTBITS
                
                if ms[8] == '0' : ser.parity = serial.PARITY_NONE 
                elif ms[8] == '1' : ser.parity = serial.PARITY_ODD
                elif ms[8] == '2' : ser.parity = serial.PARITY_EVEN
                elif ms[8] == '3' : ser.parity = serial.PARITY_MARK
                elif ms[8] == '4' : ser.parity = serial.PARITY_SPACE
                
                if ms[9] == '0' : ser.stopbits = serial.STOPBITS_ONE
                elif ms[9] == '1' : ser.stopbits = serial.STOPBITS_ONE_POINT_FIVE
                elif ms[9] == '2' : ser.stopbits = serial.STOPBITS_TWO
                
                greeting = 'opened\n'
                try :
                    ser.flushInput()
                    ser.flushOutput()
                    if(ms == 'stop') : break
                    t=threading.Thread(target=serial_Receive,args=(ser,))
                    t.start()
                    
                except :
                    continue
def serial_Receive(ser) :
    global greeting
    global exitThread
    while exitThread == 1:
        try :
            greeting += str(ser.read_until(b'\n').strip().decode('utf-8')) + "\n"#ser.inWaiting()
            print(greeting)
        except :
            continue
    ser.close()
#data = ser.read_until(b'\n').strip().decode()#ser.inWaiting()
    #greeting += str(data) + '\n'
    
def cb(event, *args):
    print("Got event", event, "with data", args)

def log_cb(event, level, time, message):
    global greeting, cec_translate, now
    present_Time = now.now()
    
    send_Time = str(str("{:02d}".format(int(present_Time.hour))) + ':' + str("{:02d}".format(int(present_Time.minute)))
                    + ':' + str("{:02d}".format(int(present_Time.second))) + ':' + str("{:03d}".format(int(present_Time.microsecond/1000))))
    print("CEC Log message:", message, "time:", time, "level:", level, "event:", event)
    
    if(level == 8) :
        greeting += send_Time + ' '
        if(len(message) < 6) : 
            greeting += cec_translate.translate_cec_poll(message[3], message[4])
        elif(len(message) < 9) : 
            greeting += cec_translate.translate_cec(message[3], message[4], message[6:8])
        else :
            greeting += cec_translate.translate_cec_parameter(message[3], message[4], message[6:8], message[9:]) 
 
print("ready")
cec_translate = cec_translate()
print(type(cec_translate))
asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, '172.30.1.27', 8080)  #192.168.100.36
)

asyncio.get_event_loop().run_forever()