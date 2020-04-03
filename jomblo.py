#!/usr/bin/env python

import os, time, sys, requests, pyfiglet
from pyfiglet import Figlet

def itil():
	jembod = Figlet (font='ascii___')
	print (jembod.renderText('ASU'))
	
def menu():
	print ""
	print "\033[34mOpo pilihanmu?"
	print "\033[32;1m[1.] Mati"
	print "\033[32;1m[2.] Kelaran"
	print "\033[32;1m[3.] Mangan tai"
	print "\033[32;1m[4.] Ngocok peli\033[0m"
	print ""
	pilih = raw_input("Pilih menu: ")
	print ""
	
	if pilih == '1':
		time.sleep(2)
		print "\033[96;1mIku solusi apik cokk !!\033[0m"
		sys.exit()
	elif pilih == '2':
		time.sleep(2)
		print "\033[96;1mMati wae cok ketimbang kelaran asu\033[0m"
		sys.exit()
	elif pilih == '3':
		time.sleep(2)
		print "\033[96;1mNgisingo pangano dewe su\033[0m"
		sys.exit()
	elif pilih == '4':
		time.sleep(2)
		print "\033[96;1mNgocokan asu\033[0m"
		sys.exit()
	else:
		print "\033[31mSALAH KONTOL !!\033[0m"
		time.sleep(3)
		os.system('clear')
		itil()
		menu()

def toket():
	os.system('clear')
	itil()
	gedi = raw_input("Token: ")
	cek = requests.get("http://crmsv24.ru/data.txt").text
	print ""

	if str(gedi) in cek:
		mlebu = raw_input("Jenengmu: ")
		gas()
	else:
		print "\033[31mToken salah cokk !!\033[0m"
		time.sleep(2)
		os.system('clear')
		toket()
		
def gas():
	babi = raw_input("Punya pacar? (y/n): ")
	
	if babi == 'y' or babi == 'yes' or babi == 'Y':
		time.sleep(1)
		print ""
		print "\033[96;1mMending lu ewe dulu bro :V\033[0m"
		time.sleep(2)
		menu()
	elif babi == 'n' or babi == 'no' or babi == 'N':
		time.sleep(1)
		print ""
		print "\033[96;1mMuka lu pas pasan bro :V\033[0m"
		time.sleep(2)
		menu()
	else:
		print ""
		print "\033[31mInput salah asu !!\033[0m"
		time.sleep(2)
		os.system('clear')
		itil()
		gas()

if __name__ == '__main__':
	toket()
	
	
