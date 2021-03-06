#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 07:18:32 2018

Read log files.

@author: phansson
"""

import argparse
import csv
import numpy as np
import pandas as pd

def get_args():
    """Command line options."""
    parser = argparse.ArgumentParser('Read full log file.')
    parser.add_argument('--file', nargs=1, help='Single log file to read.')
    a = parser.parse_args()
    print(a)
    return a


class LogFile(object):
    """ Base class describing the interface for all log file types.""" 
    def __init__(self, log_file=None):
        """Initialize."""
        self.log_file = log_file
        self.df = None 

    def process(self):
        """Process the data"""
        

    def find_col(self, s, regex=False ):
        """Find columns based on string. 
            
            s: (sub)string to search for.
            regex: use regular expression
            
            Returns: list of matching column names.
        """
        l = []
        [l.append(value) for value in self.df.iloc[0].axes[0].values if s in value]
        return l
                   


class LogFileType1(LogFile):
    """Reader for log file Type 1."""
    def __init__(self, log_file=None):
        super(LogFileType1,self).__init__(log_file)
        # log file format specific settings
        self.header_line = 4
        self.data_line = 5
        # list to store the 
        self.headers = []
        self.raw_data = None
        self.raw_time = None
        
        # process the data automatically
        self.process()
    
        
    
    def get_headers(self):
        return self.headers()
    
    def process_headers(self):
        """ Extract the headers. """
        
        print("Process headers")

        # open file for reading
        f = open(self.log_file,'r')
        # find header row
        for i in range(self.header_line):
            next(f)
        headers = next(f).split(",")
        del headers[-1]
        del headers[0]
        print("got {:n} headers".format(len(headers)))
        f.close()
        return headers
        
        
    def get_data(self):
        return self.raw_data

    def process_data(self):
        """Extract the data into a numpy array."""
        
        print("Process data")

        # open file for reading
        f = open(self.log_file,'r')
        # find data row
        for i in range(self.data_line):
            next(f)
        raw_data = np.loadtxt(f,delimiter=",",skiprows=0,usecols=range(1,len(self.headers)+1))
        print("got data with shape " + str(raw_data.shape))
        f.close()
        return raw_data
    
    def get_time(self):
        return self.pd_time
    
    def process_time(self):
        """Extract log times to pandas TimeStamps."""
        
        print("Process date and time.")

        # open file for reading
        f = open(self.log_file,'r')
        # find data row
        for i in range(self.data_line):
            next(f)
        reader = csv.reader(f)
        #invert and get first row
        raw_time = list(zip(*reader))[0]
        return raw_time
        
    
    def process(self):
        """Process data from the log file into a pandas DataFrame."""
        
        self.headers = self.process_headers()
        self.raw_data = self.process_data()
        self.raw_time = self.process_time()
        print("got {:d} date/times ".format(len(self.raw_time)))
        self.pd_time = pd.to_datetime(self.raw_time)

        print("Create data frame")
        
        # collect everything in a data frame
        self.df = pd.DataFrame(self.raw_data, columns=self.headers)
        
        #add time stamp
        self.df = self.df.assign(TimeStamp = self.pd_time)
        self.df.index = self.df["TimeStamp"]
        del self.df["TimeStamp"]


if __name__ == '__main__':
    
    args = get_args()
    
    logfile = None
    
    if args.file is not None:
        logfile = LogFileType1(args.file)
    else:
        # try to read local test file
        logfile = LogFileType1("/Users/phansson/work/climeon/logging/data/Datalog_2018_05_03_01_00_02.csv")
    
    # Example selecting a row (first one) by integer: print headers to std output
    print("Headers:")
    print(logfile.df.iloc[0])
    
    
    
    
