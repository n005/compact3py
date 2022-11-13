# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from COMPACT3 import compread

val=compread('C:/Users/n005/Documents/TIPE/data/datatest/obs.m51')
val = val[val['PRN'] != 'G06']

plt.scatter(val['TIME'], val['misure'])
plt.title("Multipath error")
plt.xlabel("Time")
plt.ylabel("Error (m)")