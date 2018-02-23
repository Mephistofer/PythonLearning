#!/usr/bin/env python 
# -*- coding: utf-8 -*
'''
Created on 2017年9月15日

@author: Saya
'''

import subprocess
import re

begin=253
end=255    

while begin<end:
    p=subprocess.Popen("cmd.exe", shell=True, 
                       stdin=subprocess.PIPE, 
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
    dataIn = "ping 10.32.6." + str(begin) + '\n';
    print("==> "+"ping 10.32.6." + str(begin)) 
    p.stdin.write(dataIn.encode('gbk')) 
    p.stdin.close()
    begin+=1
    p.wait()
 
    out = p.stdout.read().decode("gbk")   
    regex = re.compile("数据包: 已发送 = \d，已接收 = \d，丢失 = \d \(\d% 丢失\)", re.IGNORECASE)
    print (regex.findall(out))                       
    regex = re.compile("最短 = \dms，最长 = \dms，平均 = \dms", re.IGNORECASE)
    print (regex.findall(out))
      
#     if subprocess.Popen.poll(p)==0:
#         break
   
# p = subprocess.Popen("notepad.exe test.txt", shell=True, stdin=subprocess.PIPE, 
#                         stdout=subprocess.PIPE,
#                         stderr=subprocess.PIPE)
# dataIn = "ping www.baidu.com"
# p.stdin.write(dataIn.encode(sys.stdout.encoding)) 
# p.stdin.close()
# p.wait()
# print ("execution result: %s"%p.stdout.read())


# while begin<end:  
#     dataIn = "ping.exe 10.32.6." + str(begin);
#     print("==> "+dataIn)
#     p = subprocess.Popen(dataIn,
#       stdin = subprocess.PIPE,
#       stdout = subprocess.PIPE,
#       stderr = subprocess.PIPE,
#       shell = True)   
#     begin+=1
#     p.wait()
#     out = p.stdout.read().decode("gbk")   
#     regex = re.compile("数据包: 已发送 = \d，已接收 = \d，丢失 = \d \(\d% 丢失\)", re.IGNORECASE)
#     print (regex.findall(out))                       
#     regex = re.compile("最短 = \dms，最长 = \dms，平均 = \dms", re.IGNORECASE)
#     print (regex.findall(out))