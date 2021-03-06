import os
import sys
import operator
import time
import logging

import enso.config
from enso.messages import displayMessage


def cmd_enso(ensoapi, cmd):
    """ Enso system command """
    if cmd == 'quit':
        enso.stop()
    elif cmd == 'about':
        displayMessage(enso.config.ABOUT_BOX_XML)
    elif cmd == "commands":
        ensoapi.display_message("Enso commands", "enso")

cmd_enso.valid_args = ['about', 'help', 'quit', 'commands']

# vim:set tabstop=4 shiftwidth=4 expandtab:
