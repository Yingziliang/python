import re
import os
import subprocess as sp

def getTouchDevice():

    device=os.popen("adb shell getevent -pl")
    device_ln=0
    str=[0,0,0,0,0,0,0,0,0,0]
    for line in device.readlines():
        if line[0]=='a':
            str[device_ln]=line
            device_ln=device_ln+1
        else:
            str[device_ln-1]=str[device_ln-1]+line.strip()
        
    print "The device are total %d input events ." %device_ln

    Dev='ABS_MT_TOUCH'
    for i in range(device_ln):
        m=re.search(Dev,str[i])
        if m:
            return str[i].strip('\r\n').split()[3]
    
if __name__ == '__main__':
    Touchdev=getTouchDevice()
    print "The touch device is :%s." %Touchdev
    
    
    try:
        print "--recorder start now:"
        file = "D:\\Personal\\Desktop\\learn\\record_stuff.txt"
        print "****please press Ctrl + C to stop the record.****** "
        opt=sp.Popen('adb shell getevent -t ' + Touchdev + ' >' + file, stdin=sp.PIPE, stdout=sp.PIPE, shell=True)
        opt.stdout.readlines()
                   
    except KeyboardInterrupt:
        print "--recorder stopped."
