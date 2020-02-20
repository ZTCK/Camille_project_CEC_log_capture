from __future__ import print_function
import asyncio
import os.path
import os
import websockets
import time  #delete
import cec
greeting = '\'contents of logcapture\''

async def echo(websocket,path):
    global greeting    
    print("\n",websocket)
    print(path)
    ms = '0'
    while 1:
##################contents of logcapture###################
        '''if ms == '11' :
        elif ms == '12' :
        elif ms == '13' :
        elif ms == '21' :
        elif ms == '22' :
        elif ms == '23' :
        elif len(ms) >= 3 : CecCommandTx(ms[3:])                #command tx 40:36...
        else :'''
#######################################################

#test code
        time.sleep(0.1)
        await websocket.send(str(greeting))
        #if greeting != '\'contents of logcapture\'':
            #greeting = '\'contents of logcapture\''
        ms = await websocket.recv()
        print(ms)
        if(ms[0:4] == 'save') :
            save_path = '/media/usb0/'
            if(os.access(save_path, os.W_OK)) :
                completeName = os.path.join(save_path, ms[4:ms.find(".txt") + 4]) 
                file = open(completeName, "w")
                file.write(ms[ms.find(".txt") + 5:])
                file.close()
            #else ignore
        elif(ms[0:5] == 'start') :
            greeting = 'st'

            
        elif(ms[0:4] == 'stop') :
            greeting = 'st1'
            
        if(greeting == 'start') :
            print("Start")
            
        elif(greeting == 'stop') :
            print("Stop")
            
#echo에 logcapture내용을 실어서 HTML로 보냄
#js에서 onmessage로 받아들여서 textarea로 띄우면 완료
#save, create file 중 websocket communication이 안됨 (save create중 auto stop)
def cb(event, *args):
    print("Got event", event, "with data", args)
    global greeting
    #greeting += args + '\n'
# arguments: iils
def log_cb(event, level, time, message):
    print("CEC Log message:", message, "time:", time, "level:", level, "event:", event)
    global greeting
    greeting += message + '\n'

cec.add_callback(cb, cec.EVENT_ALL & ~cec.EVENT_LOG)
cec.add_callback(log_cb, cec.EVENT_LOG)
print("Callback added")
time.sleep(2)

cec.init()

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, '192.168.100.36', 8080)
)

asyncio.get_event_loop().run_forever()