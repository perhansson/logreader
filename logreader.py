#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 08:12:14 2018

GUI for looking at log files.

@author: phansson
"""

import os
import sys
import argparse
from PyQt4.QtGui import QApplication
from MainWindow import MainWindow


def get_args():

    parser = argparse.ArgumentParser("Log file GUI")
    parser.add_argument("--debug", "-d", action="store_true", help="debug toggle")
    args = parser.parse_args()
    return args


def main():
    
    # create the Qapp
    app = QApplication(sys.argv)

    # create the reader thread
    #reader = LogReader

    #### create the main GUI window
    form = MainWindow(parent=None, debug=args.debug)

    # show the main window
    form.show()

    # run the app
    sys.exit( app.exec_() )


if __name__ == "__main__":

    args = get_args()
    
    main()
