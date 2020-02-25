from __future__ import print_function
import asyncio
import os.path
import os
import websockets
import time  #delete
import cec
greeting = ''
start_flag = 2
print(cec)
print(websockets)
async def echo(websocket,path):
    global greeting, start_flag
    
    array = []
    print("\n",websocket)
    print(path)
    ms = '0'
    while 1:
        time.sleep(0.1)
        await websocket.send(str(greeting))
        ms = await websocket.recv()
        print(ms)
        if(ms[0:4] == 'save') :
            save_path = '/media/usb0/'
            if(os.access(save_path, os.W_OK)) :
                completeName = os.path.join(save_path, ms[4:ms.find(".txt") + 4]) 
                file = open(completeName, "w")
                file.write(ms[ms.find(".txt") + 5:])
                file.close()
            cec.remove_callback(cb, cec.EVENT_ALL & ~cec.EVENT_LOG)
            cec.remove_callback(log_cb, cec.EVENT_ALL)
            start_flag = 0;
        elif(ms[0:5] == 'start') :
            greeting += 'start log capture\n'
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
            start_flag = 0
            
        elif(ms[0:2] == 'tx') :
            print(len(ms))
            if(len(ms) <= 8 and len(ms) >= 6) :
                cec.transmit(int(ms[4]), int("0x" + ms[6:8], 16))
            elif(len(ms) >= 9) :
                array = []
                n = 9
                while(n < len(ms)) :
                    array.append(int("0x" + ms[n:n+2] , 16))
                    n += 3
                cec.transmit(int(ms[4]), int("0x" + ms[6:8], 16), bytes(array))
        elif(ms[0:5] == 'clear') :
            greeting = ''
        else :
            print(str(ms))
#cb function 없어도 됨
def cb(event, *args):
    print("Got event", event, "with data", args)

def log_cb(event, level, time, message):
    print("CEC Log message:", message, "time:", time, "level:", level, "event:", event)
    global greeting
    if(greeting == '\'contents of logcapture\'') :
        greeting = ''
    if(level == 8) :
        greeting += "[time : " + '{:>16}'.format(str(time)) + "]   " + message + '\n'

#git update 
print("ready")
asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, '192.168.100.36', 8080)
)

asyncio.get_event_loop().run_forever()