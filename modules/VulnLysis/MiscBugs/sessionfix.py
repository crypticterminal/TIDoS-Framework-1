#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author: @_tID
#This module requires TIDoS Framework
#https://github.com/the-Infected-Drake/TIDoS-Framework

import time
import requests
from colors import *

def sessionfix(url):

	print R+'\n   ================================='
	print R+'    S E S S I O N   F I X A T I O N'
	print R+'   =================================\n'
	print GR+' [*] Making the request...'
	req = requests.get(url, allow_redirects=False, verify=True, timeout=7)
	if req.cookies:
		print G+' [+] Found cookie reflecting in headers...'
		print B+' [+] Initial cookie state:'+C, req.cookies+'\n'
		user = raw_input(O+' [#] Enter authentication username :> '+C)
		upass = raw_input(O+' [#] Enter password :> '+C) 
		print GR+' [*] Trying POST request with authentication...'
		cookie_req = requests.post(url, cookies=req.cookies, auth=(user, upass), timeout=7)
		print B+' [+] Authenticated cookie state:'+C, cookie_req.cookies
		if req.cookies == cookie_req.cookies:
			print G+' [+] Site seems to be vulnerable...'
			print G+' [+] Site is vulnerable to session fixation vulnerability!'
		else:
			print O+' [!] Cookie values do not match...'
			print R+' [-] Nope... no vulnerability...'
	else:
		print R+' [-] No basic cookie support!'
		print R+' [-] Target not vulnerable to session fixation!'
