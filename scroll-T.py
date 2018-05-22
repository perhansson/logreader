#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 08:46:46 2018

@author: phansson
"""

import argparse
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import Reader
import pandas as pd



def plot_series_twoscales(y1, y2, l1="l1", l2="l2"):
    fig, ax1 = plt.subplots()
    y1.plot(color="b", ax=ax1 )
    ax1.set_ylabel(l1, color='b')
    ax12 = ax1.twinx()
    y2.plot(color="r", ax=ax12 )
    ax12.set_ylabel(l2, color='r')
    ax12.tick_params('y', colors='r')
    return (fig, ax1)



filename = "/Users/phansson/work/climeon/data/M6/MainLog/Datalog_2018_05_16_14_14_53.csv"

print("Reading log file: " + filename)

# open and process
f = Reader.LogFileType1(filename)


plot_series_twoscales(f.df['P_N [kW]'], f.df['TurbSpeed [rpm]'],
                      l1='P_N [kW]', l2='TurbSpeed [rpm]')


plot_series_twoscales(f.df['ScrollExtT [deg C]'], f.df['ScrollDrainT [deg C]'],
                      l1='ScrollExtT [deg C]', l2='ScrollDrainT [deg C]')


plot_series_twoscales(f.df['T33 [deg C]'], f.df['T51 [deg C]'],
                      l1='T33 [deg C]', l2='T51 [deg C]')



#ax1.legend()
#ax12.legend(loc=1)
#ax2.legend()
fig, ax1 = plt.subplots()
f.df['T51 [deg C]'].sub(f.df['T33 [deg C]']).plot(ax=ax1, color='b')
ax1.set_ylabel('T51-T33 [deg C]', color='b')

plot_series_twoscales(f.df['T51 [deg C]'].sub(f.df['T33 [deg C]']), f.df['T51 [deg C]'],
                      l1='T51-T33 [deg C]', l2='T51 [deg C]')

plot_series_twoscales(f.df['T51 [deg C]'].sub(f.df['T33 [deg C]']), f.df['P_N [kW]'],
                      l1='T51-T33 [deg C]', l2='P_N [kW]')


# select stable running
stable_power = f.df['P_N [kW]'] > 70.0
    

plot_series_twoscales(f.df[stable_power]['T33 [deg C]'], f.df[stable_power]['T51 [deg C]'],
                      l1='T33 [deg C]', l2='T51 [deg C]')


plot_series_twoscales(f.df[stable_power]['ScrollExtT [deg C]'], f.df[stable_power]['ScrollDrainT [deg C]'],
                      l1='ScrollExtT [deg C]', l2='ScrollDrainT [deg C]')



fig40, ax40 = plt.subplots()
f.df[stable_power]['T51 [deg C]'].plot(ax=ax40, color='b', label='T51')
ax402 = ax40.twinx()
f.df[stable_power]['ScrollExtT [deg C]'].plot(ax=ax402, color='g', label='ScrollExt')
f.df[stable_power]['ScrollDrainT [deg C]'].plot(ax=ax402, color='g', style='.', label='ScrollDrainT')
ax402.set_ylabel('T [deg C]', color='g')
ax402.tick_params('y', colors='g')
ax402.legend()
ax40.legend()




fig10, ax10 = plt.subplots()
f.df[stable_power]['T51 [deg C]'].sub(f.df[stable_power]['T33 [deg C]']).plot(ax=ax10, color='b')
ax10.set_ylabel('T51-T33 [deg C]', color='b')




plot_series_twoscales(f.df[stable_power]['T51 [deg C]'].sub(f.df[stable_power]['T33 [deg C]']), f.df[stable_power]['T51 [deg C]'],
                      l1='T51-T33 [deg C]', l2='T51 [deg C]')

plot_series_twoscales(f.df[stable_power]['T51 [deg C]'].sub(f.df[stable_power]['T33 [deg C]']), f.df[stable_power]['P_N [kW]'],
                      l1='T51-T33 [deg C]', l2='P_N [kW]')


plot_series_twoscales(f.df[stable_power]['T38 [deg C]'], f.df[stable_power]['P_N [kW]'],
                      l1='T38 [deg C]', l2='P_N [kW]')



fig30, ax30 = plt.subplots()
f.df[stable_power]['T38 [deg C]'].plot(ax=ax30, color='b', label='T38')
f.df[stable_power]['T39 [deg C]'].plot(ax=ax30, color='r', label='T39')
f.df[stable_power]['T36 [deg C]'].plot(ax=ax30, color='c', label='T36')
f.df[stable_power]['T37 [deg C]'].plot(ax=ax30, color='y', label='T37')
ax302 = ax30.twinx()
f.df[stable_power]['P_N [kW]'].plot(ax=ax302, color='g')
ax302.set_ylabel('P_N [kW]', color='g')
ax302.tick_params('y', colors='g')
ax30.legend()




fig2, ax2 = plt.subplots()
f.df['T51 [deg C]'].plot(ax=ax2, color='b', label='T51')
f.df['ScrollExtT [deg C]'].plot(ax=ax2, color='r', label='ScrollExtT')
f.df['ScrollDrainT [deg C]'].plot(ax=ax2, color='g', label='ScrollDrainT')
ax22 = ax2.twinx()
f.df['P_N [kW]'].plot(ax=ax22, color="c")
ax22.set_ylabel('P_N [kW]', color='c')
ax22.tick_params('y', colors='c')
ax2.legend()


fig3, ax3 = plt.subplots()
f.df['T38 [deg C]'].plot(ax=ax3, color='b', label='T38')
f.df['T39 [deg C]'].plot(ax=ax3, color='r', label='T39')
f.df['T36 [deg C]'].plot(ax=ax3, color='c', label='T36')
f.df['T37 [deg C]'].plot(ax=ax3, color='y', label='T37')
ax32 = ax3.twinx()
f.df['P_N [kW]'].plot(ax=ax32, color='g')
ax32.set_ylabel('P_N [kW]', color='g')
ax32.tick_params('y', colors='g')
ax3.legend()


fig4, ax4 = plt.subplots()
f.df['T38 [deg C]'].sub(f.df['T39 [deg C]']).plot(ax=ax4, color='b', label='T39-T38')
f.df['T37 [deg C]'].sub(f.df['T36 [deg C]']).plot(ax=ax4, color='r', label='T37-T36')
ax42 = ax4.twinx()
f.df['P_N [kW]'].plot(ax=ax42, color='g')
ax42.set_ylabel('P_N [kW]', color='g')
ax42.tick_params('y', colors='g')
ax4.legend()





plt.show()

