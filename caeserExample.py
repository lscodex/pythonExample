# -*- coding: utf-8 -*-
import sys

# there is max alphabet
MAX_KEY_SIZE = 26


# quit programs 
def quit():
	choice = raw_input('Press "q" to quit: ')
	if choice == 'q':
		sys.exit(0)
	else:
		setVariable()


# define to question fo user that encrypt or decrypt
def getMode():
	print('Do you wish to encrypt or decrypt a message')
	mode = raw_input().lower()
	if mode in 'encrypt e decrypt d'.split():
		print('OK!')
		return mode
	else:
		print('Either enter "encrypt" or "e" or "decrpyt" "d"')

# so, we get a message later to decide type 
def getMessage():
	print('Enter your message')
	return raw_input()

# later we get key from user that encrypt or decrypt to messages
def getKey():
	key = 0
	print('Enter the key number (1-%s)' % MAX_KEY_SIZE)
	key=int(raw_input())
	if (key >= 1 and key <= MAX_KEY_SIZE):
		return key

# finaly, translate to the message 

def getTranslatedMessage(mode,message,key):
	if mode[0] == 'd':
		key = -key
	translated = ''
	for symbol in message:
		if symbol.isalpha():
			num = ord(symbol)
			num += key
			if num > ord('z'):
				num -= 26
			elif num < ord('a'):
				num += 26
			translated += chr(num)
		else:
			translated += symbol
	return translated
#set to variable 
def setVariable():
	# get all variables from three function 
	mode = getMode()
	message = getMessage()
	key = getKey()

	# set the translate messeage for user
	print('Your translate text is:')
	print(getTranslatedMessage(mode,message,key))
	quit()


setVariable()
