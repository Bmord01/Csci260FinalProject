import quandl as qd
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st

ATT = qd.get("WIKI/T",trim_start = "2000-1-1", trim_end="2018-1-1",collumn_index=1)
VERIZON = qd.get("WIKI/VZ",trim_start = "2000-1-1", trim_end="2018-1-1",collumn_index=1)
SPRINT = qd.get("WIKI/S",trim_start = "2000-1-1", trim_end="2018-1-1",collumn_index=1)

'''print(ATT)
print(VERISON)
print(SPRINT)
'''
plt.plot(ATT['Open'],label="AT&T")
plt.plot(VERIZON['Open'],label="Verizon")
plt.plot(SPRINT['Open'],label = "Sprint")
plt.title('Opening Stock Price for Phone Companies')
plt.xlabel("Date")
plt.ylabel("Open Price")
plt.legend()
plt.savefig("SPRINT.png")


