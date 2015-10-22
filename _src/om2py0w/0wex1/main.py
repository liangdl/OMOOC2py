#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

# display journal.txt
def display_journal():
    # display journal.txt content
    print "之前输入的日志："
    print open("journal.txt").read()


def new_journal():
    # display journal.txt content
    display_journal()
    #append new message to journal.txt
    target = open("journal.txt", 'a')
    line = raw_input(">")
    target.write(line)
    target.write("\n")
    target.close()


display_journal()
