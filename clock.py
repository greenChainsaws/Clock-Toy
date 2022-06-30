import time
from datetime import datetime
import colorama
from colorama import Fore, Back, Style
import sys
import os

os.system("clear")
while True:
	now=datetime.now()
	s=int(now.strftime("%S"))
	m=int(now.strftime("%M"))
	h=int(now.strftime("%H"))

	sbar=Style.BRIGHT+Fore.WHITE+"\033[0;0H\033[K["+Style.RESET_ALL+Style.BRIGHT+Fore.GREEN+"#"*s
	sbar+=Style.RESET_ALL+Style.BRIGHT+Fore.WHITE+"-"*(60-s)
	sbar+="]"

	mbar="\033[2;0H\033[K["+Style.RESET_ALL+Style.BRIGHT+Fore.GREEN+"#"*m
	mbar+=Style.RESET_ALL+Style.BRIGHT+Fore.WHITE+"-"*(60-m)
	mbar+="]"

	hbar="\033[3;0H\033[K["+Style.RESET_ALL+Style.BRIGHT+Fore.GREEN+"#"*h
	hbar+=Style.RESET_ALL+Style.BRIGHT+Fore.WHITE+"-"*(24-h)
	hbar+="]"

	print(sbar)
	print(mbar)
	print(hbar)
	print(now.strftime("Current time: %H:%M:%S"))
	time.sleep(.01)
