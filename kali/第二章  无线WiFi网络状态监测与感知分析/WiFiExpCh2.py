#coding:utf-8
import os
import sys
import subprocess
from scapy.all import *

AP = {'signal': [],'ESSID':[],'TYPE':[],'BSSID':[],'CHANNEL':[]}
def scan(num):
    global j,i
    j = 0
    while num>0:
        proc = subprocess.Popen("iwlist wlan0 scanning", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        lines = proc.communicate()[0].split('\n')
        for line in lines:
            if 'Address' in line:
                print '-'*30
                print '[+]AP的BSSID：'+line[29:]
                AP['BSSID'].append(line[9:])
            if 'Channel:' in line:
                print '[+]AP的信道：'+line[28:]
                AP['CHANNEL'].append(line[28:])
            if 'Signal' in line:
                print '[+]AP的信号强度：'+line[48:54]
                AP['signal'].append(line[48:54])
            if 'Encryption key:off' in line:
                print '[+]AP的认证方式：'+'OPEN'
                AP['TYPE'].append('OPEN')
            if 'ESSID' in line:
                line2 = line[27:]
                line3 = line2.split('"',1)[0]
                line4 = eval("'"+line3+"'")
                print '[+]AP的ESSID：'+line4
                AP['ESSID'].append(line4)
                j+=1
            if 'IEEE' in line:
                print '[+]AP的认证方式：'+line[37:41]
                AP['TYPE'].append(line[37:41])
                print '-'*30
        num-=1
    return j

def main():
    scan(1)
    print "AP个数为："
    print j
if __name__ == '__main__':
    main()
