#! /usr/bin/python2.6


"""
prompt.py is to completely replace $PS1 and $PROMPT_COMMAND
"""

import sys
from os import environ
sys.path.append(environ['PY_LIBS_DIR'])
import tput

# CONSTANTS

