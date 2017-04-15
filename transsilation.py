#_*_encoding_*_='unicode'
#!/usr/bin/env python

import os
import sys
import time
import re
import string
import linecache
import csv

send = "D:\\Personal\\Desktop\\learn\\python\\send.sh"
#rfile="D:\\Personal\\Desktop\\learn\\window_dump.xml"
#csvfile="D:\\Personal\\Desktop\\learn\\csv_file.csv"

#Gets the text value of the current page
def getPageText(): 
    xml = os.popen('adb shell uiautomator dump').read().split(":")[1]
    tran00 = os.popen('adb shell cat' +xml).read().split('text="')    
    for i in range(1,len(tran00)):
        tran_d=tran00[i].split('"')[0]
        if tran_d != "":
            wf.write(tran_d)
            wf.write('\n')

#get the activity of the current page            
def getActivity():
    activity = os.popen('adb shell dumpsys activity top |findstr ACTIVITY').readline().split()[1]
    print activity
    return activity

#get the screen size
def getScreensize():
    wm = os.popen('adb shell wm size').read().split()[2].split('x')
    x = int(wm[0])
    y = int(wm[1])

#go to the page
def goToPage00():
    os.popen('adb shell input keyevent 3')
    time.sleep(3)
    getPageText()
    
if __name__ == '__main__':
    wfile="D:\\Personal\\Desktop\\learn\\tran.txt"
    wf=open(wfile,'a')
#    activity = getActivity()
#    os.popen('adb shell am start -S -W -n ' + activity)
    sf=open(send,'r')
    for i in sf.readlines():
        os.popen('adb shell '+ i)
        getPageText()
    sf.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    wf.close()