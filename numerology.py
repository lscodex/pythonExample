#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
def main ():
 name = raw_input("Please, Enter your name: ").lower().strip() # wait for a name 
 alph = ["abcdefghijklmnopqrstuwxvyz"]      #alphabet list
 total = 0                                      #number of name
 for ch in name:
   total = ord(ch) + total - 96 # ord(all letters) equals to 96
 print("your name number: ", total)   # final return
 quit()

def quit():
	choice = raw_input('Press "q" to quit: ')
	if choice == 'q':
		sys.exit(0)
	else:
		main()
main()


