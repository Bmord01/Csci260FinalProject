import quandl as qd
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np

qd.ApiConfig.api_key = "ix7crpf3zvtxR66RyR55"

ATT = qd.get("WIKI/T",trim_start = "2000-1-1", trim_end="2018-1-1",collumn_index=1)
VERIZON = qd.get("WIKI/VZ",trim_start = "2000-1-1", trim_end="2018-1-1",collumn_index=1)
SPRINT = qd.get("WIKI/S",trim_start = "2000-1-1", trim_end="2018-1-1",collumn_index=1)

'''print(ATT)
print(VERISON)
print(SPRINT)
'''
plt.plot(ATT.index,ATT['Open'],label="AT&T")
plt.plot(VERIZON.index,VERIZON['Open'],'m',label="Verizon")
plt.plot(SPRINT.index,SPRINT['Open'],'g',label = "Sprint")
plt.title('Opening Stock Price for Phone Companies')
plt.xlabel("Date")
plt.ylabel("Open Price")
plt.legend()
plt.ylim([0,70])
plt.savefig("STOCKS.png")

plt.clf()

plt.ylim([0,70])
x = 0
x2 = 4527
xA = [x,x2]
yA = [ATT.iloc[0]["Open"],ATT.iloc[4526]["Open"]]
yV = [VERIZON.iloc[0]["Open"],VERIZON.iloc[4526]["Open"]]
yS = [SPRINT.iloc[0]["Open"],SPRINT.iloc[4526]["Open"]]
minA = ATT["Open"].min()
minV = VERIZON["Open"].min()
minS = SPRINT["Open"].min()
print(minA,minV,minS)
for item in range(1,4527):
    if(ATT["Open"][item]==minA):
        minADate = int(item)
    if(VERIZON["Open"][item]==minV):
        minVDate = int(item)
    if(SPRINT["Open"][item]==minS):
        minSDate = int(item)
print(minADate,minVDate,minSDate)
#print(ATT.iloc[minADate])
#print(VERIZON.iloc[minVDate])
#print(SPRINT.iloc[minSDate])
yALow = [ATT.iloc[0]["Open"],ATT.iloc[minADate]["Open"]]
yVLow = [VERIZON.iloc[0]["Open"],VERIZON.iloc[minVDate]["Open"]]
ySLow = [SPRINT.iloc[0]["Open"],SPRINT.iloc[minSDate]["Open"]]

yAAfter = [ATT.iloc[minADate]["Open"],ATT.iloc[4526]["Open"]]
yVAfter = [VERIZON.iloc[minVDate]["Open"],VERIZON.iloc[4526]["Open"]]
ySAfter = [SPRINT.iloc[minSDate]["Open"],SPRINT.iloc[4526]["Open"]]

xATTLow = [0,minADate]
xVLow = [0,minVDate]
xSLow = [0,minSDate]

xATTAfter = [minADate,4526]
xVAfter = [minVDate,4526]
xSAfter = [ minSDate,4526]

plt.plot(xA[0:2],yA[0:2],'b')
plt.plot(xA[0:2],yV[0:2],'m')
plt.plot(xA[0:2],yS[0:2],'g')
plt.savefig("OverallTrend.png")
plt.clf()
plt.ylim([0,70])
plt.plot(xATTLow[0:2],yALow[0:2],'b')
plt.plot(xATTAfter[0:2],yAAfter[:2],'b')
plt.plot(xVLow[:2],yVLow[:2],'m')
plt.plot(xVAfter[:2],yVAfter[:2],'m')
plt.plot(xSLow[:2],ySLow[:2],'g')
plt.plot(xSAfter[:2],ySAfter[:2],'g')
plt.savefig("TREND.png")



