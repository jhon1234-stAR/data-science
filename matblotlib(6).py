import matplotlib.pyplot as plt
"""
x = [1,2,3,4,5]
y = [1,2,3,4,5]

plt.plot(x,y)
plt.show()


plt.plot(x,y,'r^')
plt.show()











plt.plot(x,y)
plt.axis([0,6,0,6])
plt.show()




plt.plot(x,y,'r--',label = "Y=X",linewidth = 4)
plt.axis([0,10,0,50])
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line plot")
plt.legend()
plt.show()





plt.plot([1,2,3,4,5],[1,4,9,16,25],'r--',label = "Y=X**2",linewidth = 4)
plt.plot([1,2,3,4,5],[1,8,27,64,125],'b--',label = "Y=X**3",linewidth = 4)
plt.axis([0,10,0,50])
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("sapmple graph")
plt.legend()
plt.show()



import numpy as np

x = np.arange(0,10,0.2
              )
print(x)

y1 = x**2
y2=x**3

plt.plot(x,x**2,'g--',x,x**3,'b--')
plt.show()


## task ask the user for input m ans c ans plot the line y =mx + c usinf matplotlib


m = float(input("Enter the slope m "))
c = float(input("Enter the y intercept c "))

x = np.arange(0, 10, 0.1)
y = m * x + c

plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line plot: y = mx + c")
plt.show()

"""








### how to put a bar plot

plt.bar([1,3,5,7],[2,6,4,9], color = "b")
plt.show()


plt.bar([1,3,5,7],[2,6,4,9], color = "b")
plt.bar([2,4,6,8],[3,7,5,10], color = "g")
plt.show()
