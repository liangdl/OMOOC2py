# coding=utf-8
import socket
import sys
import time

PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print 'Socket created'

s.bind(('', PORT))
print 'Socket bind complete'

while 1:
    data, addr = s.recvfrom(1024)
    print data

