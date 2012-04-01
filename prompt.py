#! /usr/bin/python2.6


"""
prompt.py is to completely replace $PS1 and $PROMPT_COMMAND
"""

import hashlib # .sha256
from os import system as sy

from os import environ
sys.path.append(environ['PY_LIBS_DIR'])
import tput # .colorize, .decolorize

###
# CONSTANTS
###

USERNAME_HOSTNAME_COLOR = "GREEN"
USERNAME_HOSTNAME_BOLD = True

PWD_COLOR_MODULO = 8 # hash pwd.basename into 0 thru 7 inclusive
PWD_BOLD = True

LS_DIRS_COLOR = "WHITE"
LS_DIRS_BOLD = False

DOLLAR_SIGN_COLOR = "GREEN"
DOLLAR_SIGN_BOLD = True

###
# CODE
###

##
# initial decolorization
##

tput.decolorize()

##
# username
##

username = environ['USER']

tput.colorize(fg=USERNAME_HOSTNAME_COLOR, bold=USERNAME_HOSTNAME_BOLD)
print username, '@',

##
# pseudo-hostname (abbreviated via if-then rules)
##

hostname = environ['HOSTNAME']

if hostname == 'Jon-Rodriguezs-MacBook-Air.local':
    hostname = "jrodair"

# String trailing ".stanford.edu"
#
DOT_STANFORD_DOT_EDU = ".stanford.edu"
#
if hostname[-len(DOT_STANFORD_DOT_EDU):] == DOT_STANFORD_DOT_EDU:
    hostname = hostname[0:-len(DOT_STANFORD_DOT_EDU)]

tput.colorize(fg=USERNAME_HOSTNAME_COLOR, bold=USERNAME_HOSTNAME_BOLD)
print hostname, ':',

##
# pwd. color based on the basename
##

pwd = os.getcwd()
basename = os.path.basename(pwd)

digest_hex_string = hashlib.sha256(basename).hexdigest()
digest_int = int(digest_hex_string, 16)

pwd_color = digest_int % PWD_COLOR_MODULO

tput.colorize(fg=pwd_color, bold=PWD_BOLD)
print pwd

##
# list of subdirs of the pwd
##

tput.colorize(fg=LS_DIRS_COLOR, bold=LS_DIRS_BOLD)

for elem in os.listdir(pwd):
    full_path_elem = os.path.join(pwd, elem)

    if os.path.isdir(full_path_elem):
        print elem + '/',

print ""

##
# dollar sign and space
##

tput.colorize(fg=DOLLAR_SIGN_COLOR, bold=DOLLAR_SIGN_BOLD)
print '$',

##
# finish by decolorizing
##

tput.decolorize()


