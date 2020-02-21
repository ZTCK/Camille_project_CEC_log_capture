from __future__ import print_function
import asyncio
import os.path
import os
import websockets
import time  #delete
import cec
greeting = '\'contents of logcapture\''
print(cec)
print(websockets)
async def echo(websocket,path):
    global greeting
    start_flag = 0
    array = []
    print("\n",websocket)
    print(path)
    ms = '0'
    while 1:
#test code
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
            #else ignore
        elif(ms[0:5] == 'start') :
            if start_flag == 0 :
                greeting = ''
                cec.add_callback(cb, cec.EVENT_ALL & ~cec.EVENT_LOG)
                cec.add_callback(log_cb, cec.EVENT_LOG)
            start_flag = 1
            cec.volume_up()
            cec.volume_down()
            cec.toggle_mute()
            
        elif(ms[0:4] == 'stop') :
            cec.remove_callback(cb, cec.EVENT_ALL & ~cec.EVENT_LOG)
            cec.remove_callback(log_cb, cec.EVENT_ALL)
            start_flag = 0
        elif(ms[0:2] == 'tx') :
            print(len(ms))
            print(ms[4])
            print(ms[6:2])
            #if(len(ms) <= 5) :
            #    cec.transmit(int(ms[4]), a)
            if(len(ms) <= 8) :
                cec.transmit(int(ms[4]), int("0x" + ms[6:8], 16))
            else :
                array = []
                n = 9
                while(n < len(ms)) :
                    array.append(int("0x" + ms[n:n+2] , 16))
                    n += 3
                cec.transmit(int(ms[4]), int("0x" + ms[6:8], 16), bytes(array))
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
    if(greeting == '\'contents of logcapture\'') :
        greeting = ''
    if(level == 8) :
        greeting += message + "  [time : " + str(time) + ']\n'
cec.init()
print("ready")
asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, '192.168.100.36', 8080)
)

asyncio.get_event_loop().run_forever()