# -*- coding: utf-8 -*-
from sys import argv

def new_journal():
    # display journal.txt content
    print "之前输入的日志："
    print open("journal.txt").read()

    #append new message to journal.txt
    target = open("journal.txt", 'a')
    line = raw_input(">")
    target.write(line)
    target.write("\n")
    target.close()
