#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 07:12:31 2018

@author: phansson
"""

import argparse
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import Reader
import pandas as pd

def get_args():
    """Command line options."""
    parser = argparse.ArgumentParser('Read full log file.')
    parser.add_argument('file', type=str, help='Single log file to read.')
    a = parser.parse_args()
    print(a)
    return a

args = get_args()

if args.file is not None:
    filename = args.file
else:
    filename = "/Users/phansson/work/climeon/logging/data/Datalog_2018_05_03_01_00_02.csv"


print("Reading log file: " + filename)

# open and process
logfile = Reader.LogFileType1(filename)

# Example selecting a row (first one) by integer: print headers to std output
print(logfile.df.iloc[0])


# examples plotting

# raw vs time
logfile.df['T33 [deg C]'].plot()

plt.figure()

# only positive readings
logfile.df['T33 [deg C]'][logfile.df['T33 [deg C]']>0].plot()

plt.figure()

# simple correlations  
logfile.df.plot(x='T33 [deg C]', y='T31 [deg C]')

plt.figure()

#two simple plots on the same axis
ax = logfile.df["T33 [deg C]"][logfile.df['T33 [deg C]']>0].plot(label="T33 [deg C]", legend=True)
logfile.df["T31 [deg C]"][logfile.df['T33 [deg C]']>0].plot(ax=ax, label="T31 [deg C]", legend=True)
# change date formatting on plots
ax.set_label("Temperatures")
ax.set_ylabel("Temperature [deg C]")
ax.xaxis.set_minor_locator(dates.HourLocator(interval=2))   # every two hours
ax.xaxis.set_minor_formatter(dates.DateFormatter('%H:%M'))  # hours and minutes
ax.xaxis.set_major_locator(dates.DayLocator(interval=1))    # every day
ax.xaxis.set_major_formatter(dates.DateFormatter('\n%d-%m-%Y')) 


plt.figure()
# slice in time
ax = logfile.df.between_time('10:00','13:00')["T33 [deg C]"].plot()
ax.xaxis.set_major_formatter(dates.DateFormatter('%H:%M'))

# adjacent plots
fig, (ax1, ax2) = plt.subplots(2,1)
ax1.plot(logfile.df["NetOutEnergy [kWh]"])
ax2.plot(logfile.df["TurbSpeed [rpm]"])

plt.show()



