#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 07:18:32 2018

Read log files.

@author: phansson
"""

import os
import sys
import argparse
import csv
import numpy as np
import pandas as pd

def get_args():
    parser = argparse.ArgumentParser('Read log file.')
    parser.add_argument('--file', nargs=1, help='Log files to read.')
    a = parser.parse_args()
    print(a)
    return a






class LogFile(object):
    def __init__(self, log_file=None):
        self.log_file = log_file

    def process(self):
        """Process the data"""
        

class LogFileType1(LogFile):
    def __init__(self, log_file=None):
        super(LogFileType1,self).__init__(log_file)
        self.header_line = 4
        self.data_line = 5
        self.headers = []
        self.raw_data = None
        self.raw_time = None
        self.df = None
    
    def __get_headers(self):
        # open file for reading
        f = open(self.log_file,'r')
        # find header row
        for i in range(self.header_line):
            next(f)
        self.headers = next(f).split(",")
        del self.headers[-1]
        del self.headers[0]
        print("got {:n} headers".format(len(self.headers)))
        print(self.headers)
        
    def __get_data(self):
        # open file for reading
        f = open(self.log_file,'r')
        # find data row
        for i in range(self.data_line):
            next(f)
        self.raw_data = np.loadtxt(f,delimiter=",",skiprows=0,usecols=range(1,len(self.headers)+1))
        print("got data " + str(self.raw_data.shape))
        
    def __get_time(self):
        # open file for reading
        f = open(self.log_file,'r')
        # find data row
        for i in range(self.data_line):
            next(f)
        reader = csv.reader(f)
        #invert and get first row
        self.raw_time = list(zip(*reader))[0]
        print("got {:d} times ".format(len(self.raw_time)))
        self.pd_time = pd.to_datetime(self.raw_time)
        
    
    def process(self):
        self.__get_headers()
        self.__get_data()
        self.__get_time()
        self.df = pd.DataFrame(self.raw_data, columns=self.headers)
        self.df = self.df.assign(TimeStamp = self.pd_time)


if __name__ == '__main__':
    
    args = get_args()
    
    logfile = None
    
    if args.file is not None:
        logfile = LogFileType1(args.file)
    else:
        # try to read local test file
        logfile = LogFileType1("/Users/phansson/work/climeon/logging/data/Datalog_2018_05_03_01_00_02.csv")
    
    logfile.process()
    
    print(logfile.raw_data)

    logfile.df['T31 [deg C]'][logfile.df['T33 [deg C]'] > 0].plot()
    
