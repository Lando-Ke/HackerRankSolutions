import sys
from time import localtime, strftime


time = '07:05:45PM'

#x=raw_input()
t =time.split(':')
if(t[2][2]=='P' or t[2][2]=='p'):
    if(t[0]!='12'):
        t[0]=str(12+int(t[0]))
elif (t[0]=='12'):
    t[0]='00'
t=':'.join(t)
print t[:-2:]

#Converting it from 24hr to 12 hr

ttime = strftime("%H:%M:%S", localtime())
tt= ttime.split(':')

if (int(tt[0])>12):
	tt[0] = str(int(tt[0])-12)
elif (tt[0]=='00'):
	tt[0]='12'
tt= ':'.join(tt)

print "The local time in 24hrs is %s" %(ttime)
print "The local time in 12hrs is %s" %(tt)