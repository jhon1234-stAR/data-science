import matplotlib.pyplot as plt


"""
## histograms
x = [25,24,26,27,28,25,26,28,30,20,20,24,23,227]
bins = [ 0,10,20,30,40,50,60,70,80,90,100]


plt.hist(x, bins=bins, histtype='bar', edgecolor='black')
plt.xlabel("age")
plt.ylabel("Number of People")
plt.title("Histogram of Ages")
plt.show()











##pycharts 

slices = [6,1,12,1,3]
activities = ["sleeping","running","watching tv","playing football","eating"]

cols = ["c","m","r","g","b"]

plt.pie(slices, labels=activities, colors=cols, startangle=90)
plt.title("Pie Chart of Activities")
plt.show()

















# scatter plot - task 

x = [1,2,3,4,5,6,7,8,9]
y = [0,1,0,1,0,1,0,1,0]

plt.scatter(x,y , label = "cheese", color = "b")

plt.title("cheese burger")
plt.ylabel("cheese")
plt.xlabel("chez")
plt.show()






### stacked plots 
"""

import numpy as np


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1=np.arange(0.5,0.1)
t2=np.arange(0.5,0.02)
plt.figure()

plt.subplot(221)
plt.plot(t1,f(t1),"bo")

plt.subplot(224)
plt.plot(t2,np.cos(2*np.pi*t2))
plt.show()
