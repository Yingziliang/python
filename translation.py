#_*_encoding_*_='unicode'
#!/usr/bin/env python

import os
import sys
import time
import re
import string
import linecache
import csv

#send = "D:\\Personal\\Desktop\\learn\\python\\send.sh"
send = "C:\\Users\\ly\\Desktop\\LOG\\android_tap_record-master\\python\\send.sh"

#rfile="D:\\Personal\\Desktop\\learn\\window_dump.xml"
#csvfile="D:\\Personal\\Desktop\\learn\\csv_file.csv"

#Gets the text value of the current page
def getPageText(pageNum): 
    xml = os.popen('adb shell uiautomator dump').read().split(":")[1]
    tran00 = os.popen('adb shell cat' +xml).read().split('text="')
    wf.write('*********** This is the %dth page\'s texts. *************\n' %pageNum)

    for i in range(1,len(tran00)):
        tran_d=tran00[i].split('"')[0]
        if tran_d != "":
            wf.write(tran_d)
            wf.write('\n')

    wf.write('*************the %dth page end.*****************\n' %pageNum)
    
    
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
    pageNum=1
    try:
        print " start now get translation:"
        wfile="C:\\Users\\ly\\Desktop\\LOG\\tran.txt"
        wf=open(wfile,'a')
        print "******please press Ctrl + C to stoped.******** "
        while True:
            time00=time.time()
            getPageText(pageNum)
            pageNum=pageNum+1
            time01=time.time()
            getPageTextsTime=time01-time00
            wf.write('****** The getpagetext use time is %lfs. ****** \n' %getPageTextsTime) 
            
            print "Please turn to the %dth page." %pageNum
            time.sleep(3)
    except KeyboardInterrupt:
        print "get texts stopped."
    wf.close() 
    wf=open(wfile,'r')
    dfile="C:\\Users\\ly\\Desktop\\LOG\\Dtran.txt"
    df=open(dfile,'w')
    len_wf=len(wf.readlines())-1

    for i in range(len_wf):
        ff = linecache.getlines(wfile)[i].split()[0][0]
        if ff != '*' :
            df.write(linecache.getlines(wfile)[i])
       
    df.close()
    wf.close()    
    