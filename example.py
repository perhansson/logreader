#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 07:12:31 2018

@author: phansson
"""

import matplotlib.pyplot as plt
import matplotlib.dates as dates
import Reader

    
logfile = Reader.LogFileType1("/Users/phansson/work/climeon/logging/data/Datalog_2018_05_03_01_00_02.csv")


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

# adjacent plots
fig, (ax1, ax2) = plt.subplots(2,1)
ax1.plot(logfile.df["NetOutEnergy [kWh]"])
ax2.plot(logfile.df["TurbSpeed [rpm]"])

plt.show()



