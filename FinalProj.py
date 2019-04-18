import quandl as qd
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np

ATT = qd.get("WIKI/T",trim_start = "2000-1-1", trim_end="2018-1-1",collumn_index=1)
VERIZON = qd.get("WIKI/VZ",trim_start = "2000-1-1", trim_end="2018-1-1",collumn_index=1)
SPRINT = qd.get("WIKI/S",trim_start = "2000-1-1", trim_end="2018-1-1",collumn_index=1)

'''print(ATT)
print(VERISON)
print(SPRINT)
'''
plt.plot(ATT.index,ATT['Open'],label="AT&T")
plt.plot(VERIZON.index,VERIZON['Open'],label="Verizon")
plt.plot(SPRINT.index,SPRINT['Open'],label = "Sprint")
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
    if(ATT[item]["Open"]==minA):
        minADate = int(item)
print(minADate)

plt.plot(xA[0:2],yA[0:2]);
plt.plot(xA[0:2],yV[0:2]);
plt.plot(xA[0:2],yS[0:2]);
plt.savefig("TRENT.png")



