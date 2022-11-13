# -*- coding: utf-8 -*-
import csv
import pandas as pd
from datetime import datetime, timedelta

nbval=0
sat=[]
def compread(filepath):
    file = open(filepath, "r")
    line = file.readline()
    i=1
    time=0
    cellsat=[]
    value=[]
    output=[['TIME', 'PRN', 'misure']]
    while line:
        if "GPS_START_TIME" in line:
            celldata=line.split()
            year=int(celldata[1])
            month=int(celldata[2])
            day=int(celldata[3])
            hour=int(celldata[4])
            minute=int(celldata[5])
            second=int(float(celldata[6]))
            dt=datetime(year, month, day, hour, minute, second)
        if (i % 2) != 0 and i>2:
            cellsat=line.split()
            time=int(float(cellsat[0]))
            if int(cellsat[1]) != -1:
                nbval=int(cellsat[1])
                sat=[cellsat[e] for e in range(2,nbval+2)]
        if (i % 2) == 0 and i>2:
            cellval=line.split()
            value=[]
            for f in range(nbval):
                if "S" in cellval[f]:
                    value.append("NaN")
                else:
                    value.append(float(cellval[f]))
                output.append([(dt+timedelta(seconds=time)),sat[f],value[f]])
        
        i=i+1
        line = file.readline()
    file.close()   
    return pd.DataFrame(output[1:], columns=output[0])