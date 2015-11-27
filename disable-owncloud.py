#!/usr/bin/python

import re
import shutil
from subprocess import call
from sys import exit

TESTEDWITH = '0.14'

NGINX_PATH = '/etc/nginx/conf.d/local.conf'
NGINX_PATH_BACKUP = NGINX_PATH + '.bak'
OWNCLOUD_PATH = '/home/user-data/owncloud/'

start = re.compile('^\s# ownCloud configuration\.$') # dropped
stop = re.compile('^# ssl files sha1.*$') # kept


# user warning & confirmation
print 'This might mess up your mailinabox config. Tested only with version %s of mailinabox. Use at own risk. In case something goes wrong, re-install mailinabox.' % TESTEDWITH
if str(raw_input("Type 'yes' to continue: ")).lower() != 'yes':
	print 'Aborted'
	exit()


# backup nginx config file
print 'Backing up %s to %s' % (NGINX_PATH, NGINX_PATH_BACKUP)
shutil.copyfile(NGINX_PATH, NGINX_PATH_BACKUP)

# read file and iterate over lines, write lines into variable
# drop all lines between 'start' (inclusive) and 'end' (exclusive)
print 'Removing owncloud from nginx configuration'
with open(NGINX_PATH, 'r') as inFile:
	out	= ''
	on = True
	for line in inFile:
		if start.match(line):
			on = False
		elif stop.match(line):
			on = True
		
		if on:
			out += line

# overwrite file with "filtered" string
with open(NGINX_PATH, 'w') as outFile:
	outFile.write(out)


# Remove owncloud folder
print 'Removing owncloud directory under %s' % OWNCLOUD_PATH
shutil.rmtree(OWNCLOUD_PATH)


# Reload nginx config
print 'Reloading nginx'
call(['service', 'nginx', 'reload'])