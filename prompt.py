#! /usr/bin/python2.6


"""
prompt.py is to completely replace $PS1 and $PROMPT_COMMAND
"""

import sys
from os import environ
sys.path.append(environ['PY_LIBS_DIR'])
import subprocess26 as subprocess
import tput # TODO make tput know the state of the colors by using the env vars FG_COLOR and BG_COLOR

# CONSTANTS

N_COLORS = 8
DEFAULT_FG_COLOR = 7
# default bg_color is SHLVL, to distinguish away terminals

# DETERMINE bg_color

bg_color = int(environ['SHLVL']) # fall-back default

if 'BG_COLOR' in environ:
    bg_color = int(environ['BG_COLOR'])

bg_color = bg_color % N_COLORS


# DETERMINE fg_color

fg_color = DEFAULT_FG_COLOR

if 'FG_COLOR' in environ:
    fg_color = int(environ['FG_COLOR'])

fg_color = fg_color % N_COLORS


# DETERMINE fg_color_of_prompt (itself)





# STRINGS THAT CONSIST THE PROMPT TEXT

print bg_color, fg_color

