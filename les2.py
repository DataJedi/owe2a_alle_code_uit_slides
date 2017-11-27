import matplotlib.pyplot as plt
from random import randint
import numpy as np
from scipy.interpolate import spline
from scipy import ndimage

# Scatterplot
scatx = []
scaty = []    
for i in range(0,100):
    scatx.append(randint(10,20))
    scaty.append(randint(0,50))

plt.scatter(scatx,scaty)
plt.show()
######################################

# Staafdiagram
barx = [1,2,3,4]
bary = [10,20,10,15]
plt.bar(barx,bary)
plt.show()
######################################

# Lijndiagram
linex = [1,2,3,4]
liney = [10,20,10,15]
plt.plot(linex,liney)
plt.show()
######################################

# smooth lijn
x = np.array([1,2,3,4,5,6])
y = np.array([2**0,2**1,2**2,2**3,2**4,2**5]) #machten van 2, want redenen

# getal bepaald hoeveel datapunten tussen x.min en x.max te genereren
x_smooth = np.linspace(x.min(),x.max(),50) 
#smoothen de curve van x en y mbv de nieuwe datapunten
y_smooth = spline(x,y,x_smooth) 

plt.plot(x_smooth,y_smooth)
plt.show()
######################################

# Opdracht 2
x_data = [1,2,3,4,5,6,7,8,9,10]
y_data = []
for i in range(len(x_data)):
    y_data.append(randint(10,20))
    
plt.bar(x_data,y_data)
plt.show()
######################################

# Taart diagram
labels = ['Studenten', 'Docenten', 'Secretariaat','Overig']
percentages = [45, 30, 20, 5]
plt.pie(percentages, labels=labels, autopct='%1.1f%%')
plt.title("Percentage beroep ondervraagden")
plt.show()
######################################

# Opdracht 3
x_data = [1,2,3,4,5,6,7,8,9,10]
y_data = [randint(10,20) for i in range(0,10)]

x_np = np.array(x_data)
y_np = np.array(y_data)

plt.plot(x_np,y_np)
plt.show()
######################################

# Plaatjes
from scipy import ndimage
from scipy import misc
kitten = ndimage.imread("kitten.jpg")
kitten_new = ndimage.imread("kitten_new.jpg")
fig, axs = plt.subplots(nrows=1, ncols=2)
axs[0].imshow(kitten)
axs[1].imshow(kitten_new)
plt.show()
######################################

# subplots: meerdere grafieken
x_data = [1,2,3,4,5]
y_data = [4,5,6,7,8]
x_test = [1,2,3,4,5]
y_test = [7,8,9,10,11]

fig, axs = plt.subplots(ncols=2,nrows=1)

axs[1].plot(x_data,y_data)
axs[0].scatter(x_test,y_test)

plt.show()
######################################

#subplots: meerdere lijnen
x_data = [1,2,3,4,5]
y_data = [4,5,6,7,8]
x_test = [1,2,3,4,5]
y_test = [7,8,9,10,11]

plt.plot(x_data,y_data, color="blue")
plt.scatter(x_test,y_test, color="red")

plt.show()
######################################

# Opdracht 4
x_data = [1,2,3,4,5,6,7,8,9,10]
y1_data = [randint(10,20) for i in range(0,10)]
y2_data = [randint(10,20) for i in range(0,10)]

plt.plot(x_data,y1_data, color='blue')
plt.plot(x_data,y2_data, color='red')

plt.show()
######################################

# Grafiek eigenschappen
x_data = [1,2,3,4,5,6,7,8,9,10]
y1_data = [randint(10,20) for i in range(0,10)]
y2_data = [randint(10,20) for i in range(0,10)]

plt.plot(x_data,y1_data, color='blue', label="Rode lijn")
plt.plot(x_data,y2_data, color='red', label="Blauwe lijn")

plt.title("Twee random lijnen")
plt.legend()
plt.xlabel("xlabel")
plt.ylabel("ylabel")
plt.show()
######################################

# Opdracht 5
x1_data = [randint(10,20) for i in range(0,100)]
y1_data = [randint(10,20) for i in range(0,100)]

x2_data = [randint(15,30) for i in range(0,100)]
y2_data = [randint(15,30) for i in range(0,100)]

plt.scatter(x1_data,y1_data, color='blue', label="Dataset 1")
plt.scatter(x2_data,y2_data, color='red', label="Dataset 2")

plt.title("Twee random datasets")
plt.legend()
plt.xlabel("xlabel")
plt.ylabel("ylabel")
plt.show()
######################################

# Extra opdracht 1
from scipy import ndimage

# Data
#kitten = ndimage.imread("kitten.jpg")
x1_data = [randint(10,20) for i in range(0,100)]
y1_data = [randint(10,20) for i in range(0,100)]

x2_data = [i for i in range(0,100)]
y2_data = [randint(15,30) for i in range(0,100)]

x3_data = [i for i in range(0,20)]
y3_data = [randint(0,50) for i in range(len(x3_data))]

x4_data = [45, 30, 20, 5]
y4_data = ['Studenten', 'Docenten', 'Secretariaat','Overig']

# Make subplots
fig, axs = plt.subplots(nrows=2, ncols=2)
axs[0][0].pie(x4_data, labels=y4_data, autopct='%1.1f%%')
axs[0][1].scatter(x1_data,y1_data, color='blue', label="Dataset 1")
axs[1][0].plot(x2_data,y2_data, color='red', label="Dataset 2")
axs[1][1].bar(x3_data,y3_data, color='yellow',label="Dataset 3")
plt.show()
######################################

# Extra opdracht 2
fig = plt.figure()
# add_subplot(ncols,nrows,plot_number)
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 2, 3)
ax3 = fig.add_subplot(2, 2, 4)
ax1.plot(x2_data,y2_data, color='blue', label="Dataset 2")
ax2.pie(x4_data, labels=y4_data, autopct='%1.1f%%')
ax3.bar(x3_data,y3_data, color='yellow',label="Dataset 3")
plt.show()

