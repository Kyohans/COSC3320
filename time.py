import time
import sys
from heapMedianSelection import select as heapSelect
from bubbleSort import select as bubbleSelect
from random import randint
import matplotlib.pyplot as plt

hTimes = []     # Heap sort times
bTimes = []     # Bubble sort times

l = [randint(0, 1000) for i in range(10000)]    # Array of size 10000
hFig, hPlot = plt.subplots()                    # Heap sort plot
bFig, bPlot = plt.subplots()                    # Bubble plot
fig, plot = plt.subplots()                      # Plot comparing Heap sort and Bubble sort

# First run heapSelect and construct graph for it
for x in range(1,10000,50):
    start_time = time.time()
    heapSelect(l[:x],x)
    elapsed_time = time.time() - start_time
    hTimes.append(elapsed_time)

hInputs = [i for i in range(1,10000,50)]
hPlot.plot(hInputs,hTimes)
hPlot.set(xlabel='No. of elements', ylabel='Time elapsed (sec)', title = 'Heap Sort on Linear-Time Median Selection')
hPlot.grid()
hFig.savefig("heapSort.png")

# Next, run bubbleSelect and construct a graph for it
for x in range(1,10000,50):
    start_time = time.time()
    bubbleSelect(l[:x],x)
    elapsed_time = time.time() - start_time
    bTimes.append(elapsed_time)

bInputs = [i for i in range(1,10000,50)]
bPlot.plot(bInputs,bTimes)
bPlot.set(xlabel='No. of elements', ylabel = 'Time Elapsed (sec)', title = 'Bubble Sort On Linear-Time Median Selection')
bPlot.grid()
bFig.savefig("bubbleSort.png")


# Then construct a graph including both data
plot.plot(hInputs,hTimes, label='Heap Sort')
plot.plot(bInputs,bTimes, label='Bubble Sort')
plot.set(xlabel='No. of elements', ylabel='Time Elapsed (sec)', title='Heap Sort vs Bubble Sort')
plot.grid()
plt.legend()
fig.savefig("bubble&heapSort.png")
