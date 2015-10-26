#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, os, time

running = True
# display_journalay journal.txt
def display_journal():
    # display journal.txt content
    if os.path.isfile('journal.txt'):
        print "大王，这是您之前的口谕："
        print open("journal.txt").read()

    else:
        print '''
        大王，您之前没留下话呢。
        '''

def input_journal():
    while running:
        line = raw_input("大王，有什么需要小人服务呢？>")
        if line == 'q':
            print "大王再见，大王慢走。"
            break
        elif line == '?' or line == 'h' or line == 'H' or line == 'help':
            print '''
                按q退出
                按 ?/h/H/help 显示帮助
                按s显示您之前的吩咐
            '''
        elif line == 's' or line == 'show':
            display_journal()
        elif line == '真主安拉':
            print "恭喜你答对了，奖你24个。。。葫芦娃。"
        else:
            target = open("journal.txt", 'a')
            target.write(time.strftime("%Y-%m-%d %X")+" : "+line+"\n")
            target.close()

def main():
    display_journal()
    input_journal()

if __name__ == '__main__':
    main()
