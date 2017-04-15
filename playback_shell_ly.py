from  __future__ import unicode_literals
import re
import os
import linecache
from decimal import *
import math

'''
file = "C:\\Users\\ly\\Desktop\\LOG\\android_tap_record-master\\python\\record_stuff.txt"
afile = "C:\\Users\\ly\\Desktop\\LOG\\android_tap_record-master\\python\\tmp_a.txt"
ofile = "C:\\Users\\ly\\Desktop\\LOG\\android_tap_record-master\\python\\tmp_o.txt"
tfile = "C:\\Users\\ly\\Desktop\\LOG\\android_tap_record-master\\python\\tmp_t.txt"
tlfile = "C:\\Users\\ly\\Desktop\\LOG\\android_tap_record-master\\python\\tmp_tl.txt"
send = "C:\\Users\\ly\\Desktop\\LOG\\android_tap_record-master\\python\\send.sh"
tcfile = "C:\\Users\\ly\\Desktop\\LOG\\android_tap_record-master\\python\\tmp_c.c"
modelcfile = "C:\\Users\\ly\\Desktop\\LOG\\android_tap_record-master\\python\\model_send.c"
targetcfile="C:\\Users\\ly\\Desktop\\LOG\\android_tap_record-master\\python\\send.c"
'''
file = "D:\\Personal\\Desktop\\learn\\record_stuff.txt"
afile = "D:\\Personal\\Desktop\\learn\\python\\tmp_a.txt"
ofile = "D:\\Personal\\Desktop\\learn\\python\\tmp_o.txt"
tfile = "D:\\Personal\\Desktop\\learn\\python\\tmp_t.txt"
tlfile = "D:\\Personal\\Desktop\\learn\\python\\tmp_tl.txt"
send = "D:\\Personal\\Desktop\\learn\\python\\send.sh"
tcfile = "D:\\Personal\\Desktop\\learn\\python\\tmp_c.c"
modelcfile = "D:\\Personal\\Desktop\\learn\\python\\model_send.c"
targetcfile="D:\\Personal\\Desktop\\learn\\python\\send.c"




sleep_arry_line=[]                          
sleep_arry_time=[] 

#delete the '[' and ']' in the record_stuff.txt file  to get tmp_a.txt file.

af=open(afile,'w')
f=open(file,'r')
for i in f.readlines():
    ri=re.sub(r'[\[\]]','',i)
    af.write(ri)   
f.close()
af.close()

#define the input dev and compose the command

touchD='/dev/input/event5'
touchdev='sendevent /dev/input/event5'
of=open(ofile,'w')
af=open(afile,'r')
#delete the time list and hex converted to decimal
for j in af.readlines():

    o=re.sub(r' ',touchdev,j,1)
    oj=re.sub(r'4294967295','-1',o)
    ojj=oj.split()[0]+' '+ oj.split()[1]+' ' +str(int(oj.split()[3],16))+' '+str(int(oj.split()[4],16))+' '+str(int(oj.split()[5],16))    #del time list
    of.write(ojj)
    of.write('\n')
af.close()
of.close()    


#get the time list in tmp_a.txt(afile) and write in tmp_tl.txt(tlfile)
tlf=open(tlfile,'w')
af=open(afile,'r')
for i in af.readlines():
    tlf.write(i.split()[0])
    tlf.write('\n')
tlf.close()
af.close()


with open(tlfile,'r') as f:
    lines=f.readlines()
    tstart=lines[0]
    tend=lines[-1]
    

#if the mindiff greater than the tdiff,return True(don't sleep), else return False(sleeping)

def compare_float(m,t):
    a=m
    b=t
    if a > b:
        return True
    else:
        return False

#        
def containsElement(a,b):
    len_list=len(b)
    for i in range(len_list):
        if int(b[i])==a:
            return 1
        
    return 0

 
mindiff=0.1 #define the min difference,if greater than it, it is sleep
tdiff=0 #the time difference between two adjacent operations
index=1 

#
tf=open(tfile,'w')
tlf=open(tlfile,'r')

for i in tlf.readlines():
    #the first and last time don't sleep.
    if (i == tstart or i == tend):
        tdiff=0
    #
    else:
        #Compare the time difference between two adjacent operations
        prev=linecache.getlines(tlfile)[index-2]
        tdiff=float(i)-float(prev)
    #if don't sleep, write the \n to the tmp_t.txt(tfile)   
    if compare_float(mindiff,tdiff):
        tf.write('\n')
        
    else:
#        print "sleep %s; %s" %(tdiff, i)
    #write the sleep time and operations write to the tmp_t.txt(tfile)  
    
#        it='sleep'+' ' +str(tdiff)+';'+' '+' '.join(sleep_arry_line)   
        it='sleep'+' ' +str(tdiff)+';'+' '
        tf.write(it)
        tf.write('\n')
        sleep_arry_line.append(str(index))
        sleep_arry_time.append(tdiff*1000000)
    index=index+1
#print "the sleep_arry_line = " , sleep_arry_line
#print "the sleep_arry_time =" , sleep_arry_time    
tlf.close()
tf.close()

#compose the executable shell script 

sf=open(send,'w')
tf=open(tfile,'r')
of=open(ofile,'r')
len_of=len(of.readlines())
print 'the ofile is %d' %len_of
len_tf=len(tf.readlines())
print 'the tfile is %d' %len_tf
for i in range(len_of):
    ii=linecache.getlines(tfile)[i].strip('\n') + '    '+linecache.getlines(ofile)[i].strip('\n')
#    print ii
    sf.write(ii)
    sf.write('\n')
sf.close()
tf.close()
of.close()
with open(send,'a') as sf:
    sf.write('exit')
    
#delete the unwanted documents
os.remove(afile)
os.remove(ofile)
os.remove(tfile)
os.remove(tlfile)

'''
os.popen('adb push D:\\Personal\\Desktop\\learn\\python\\send.sh /data')
os.popen('adb shell chmod 777 /data/send.sh')
Cricle=50
i=1
while Cricle!=0:

    os.popen('adb shell sh /data/send.sh')
    print 'this is the %d cricle.' %i
    i=i+1
    Cricle=Cricle-1
print 'the total cricle is %d.' %i
# compose the executable c 
'''  



'''  
index_0=1
sleep_arry_time_index=0

of=open(ofile,'r')
tcf=open(tcfile,'w')
for i in of.readlines():
    type=i.split()[2]
    code=i.split()[3]
    value=i.split()[4]
    if containsElement(index_0,sleep_arry_line):

        us='usleep'+'('+str(int(round(Decimal(sleep_arry_time[sleep_arry_time_index]))))+')'+';'
        print us
        
        tcf.write('    '+us)
        tcf.write('\n')
    
    tcf.write('    '+"memset(&event,0,sizeof(event));")
    tcf.write('\n')
    tcf.write('    '+"event.type ="+type+";")
    tcf.write('\n')
    tcf.write('    '+"event.code ="+code+";")
    tcf.write('\n')
    tcf.write('    '+"event.value ="+value+";")
    tcf.write('\n')
    tcf.write('    '+"ret=write(fd,&event,sizeof(event));")
    tcf.write('\n')
    tcf.write('    '+"if(ret<sizeof(event)){")
    tcf.write('\n')
    tcf.write('    '+"    fprintf(stderr,\"write event failed, %s\\n\",streeror(errno));")
    tcf.write('\n')
    tcf.write('    '+"   return -1;")
    tcf.write('\n')
    tcf.write('    '+"   }")
    tcf.write('\n')
    index_0=index_0+1

of.close()
tcf.close()

append_line=67
modelcf=open(modelcfile,'r')
tcf=open(tcfile,'r')
targetcf=open(targetcfile,'a')
mcf_len=len(modelcf.readlines())

for i in linecache.getlines(modelcfile)[0:append_line]:
    ii=re.sub('_REPLACE_DEVICE_',touchD,i)
    targetcf.write(ii)



for j in tcf.readlines():
    targetcf.write(j)

for q in  linecache.getlines(modelcfile)[append_line:mcf_len]:
    targetcf.write(q)
    
tcf.close()
targetcf.close()
modelcf.close()
'''






























































