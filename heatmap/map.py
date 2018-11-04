import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import time
import random


# def createMap(x, y):
#     heatmap, xedges, yedges = np.histogram2d(x, y, bins=(40,40))
#     extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
 
#     # Plot heatmap
#     plt.clf()
#     plt.title('Pythonspot.com heatmap example')
#     plt.ylabel('y')
#     plt.xlabel('x')
#     plt.imshow(heatmap, extent=extent)
#     plt.show()

nullQ = []
for i in range(0,60):
    nullQ.append(None)
xQ = deque(nullQ)
yQ = deque(nullQ)
xlist = [0,
-4,
-8,
-12,
-16,
-20,
-24,
-28,
-32,
-36,
-40,
-44,
-48,
-52,
-56,
-60,
-56,
-52,
-48,
-44,
-40,
-36,
-32,
-28,
-24,
-20,
-16,
-12,
-8,
-4,
0,
4,
8,
12,
16,
20,
24,
28,
32,
28,
24,
20,
16,
12,
8,
4,
0,
-4,
-8,
-12,
-16,
-20,
-24,
-28,
-32,
-28,
-24,
-20,
-16,
-12,
-8,
-4,
0,
4,
2,
-2,
0,
-2,
-4,
0,
0,
4,
2,
-2,
0,
-2,
-4,
0,
0,
4,
2,
-2,
0,
-2,
-4,
0,
0,
-4,
-8,
-12,
-16,
-20,
-24,
-28,
-32,
-36,
-40,
-44,
-48,
-52,
-56,
-60,
-56,
-52,
-48,
-44,
-40,
-36,
-32,
-28,
-24,
-20,
-16,
-12,
-8,
-4,
0,
4,
8,
12,
16,
20,
24,
28,
32,
28,
24,
20,
16,
12,
8,
4,
0,
-4,
-8,
-12,
-16,
-20,
-24,
-28,
-32,
-28,
-24,
-20,
-16,
-12,
-8,
-4,
0,
4,
2,
-2,
0,
-2,
-4,
0,
0,
4,
2,
-2,
0,
-2,
-4,
0,
0,
4,
2,
-2,
0,
-2,
-4,
0]
ylist = [0,
0,
0,
0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
12,
13,
14,
10,
16,
18,
20,
17,
28,
30,
33,
29,
38,
41,
43,
46,
48,
51,
54,
57,
59,
62,
66,
70,
74,
78,
80,
81,
84,
87,
90,
94,
100,
105,
110,
118,
107,
99,
88,
83,
78,
71,
69,
62,
56,
50,
42,
40,
36,
31,
27,
22,
18,
13,
10,
7,
2,
5,
6,
15,
22,
30,
34,
39,
44,
51,
60,
54,
47,
38,
32,
29,
23,
0,
0,
0,
0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
12,
13,
14,
14,
16,
18,
20,
25,
28,
30,
33,
36,
38,
41,
43,
46,
48,
51,
54,
57,
59,
62,
66,
70,
74,
78,
80,
81,
84,
87,
90,
94,
100,
105,
110,
118,
107,
99,
88,
83,
78,
71,
69,
62,
56,
50,
42,
40,
36,
31,
27,
22,
18,
13,
10,
7,
2,
5,
6,
15,
22,
30,
34,
39,
44,
51,
60,
54,
47,
38,
32,
29,
23]
def updateQueue(x, y):
    xQ.appendleft(x)
    yQ.appendleft(y)
    xQ.pop()
    yQ.pop()
    xVals = list(xQ)
    yVals = list(yQ)
    return xVals, yVals

def createMap():
    fig = plt.figure()
    plt.title('Distance (in inches) from Front Center of Mic Array')
    ax1 = fig.add_subplot(1,1,1)
    ax1.set_xbound(lower=-60, upper=60)
    ax1.set_ybound(lower=0, upper=120)
    ax1.set_autoscale_on(b=False)
    ax1.set_xlabel('Horizontal Distance')
    ax1.set_ylabel('Vertical Distance')


    def animate(i):
        # x = random.randint(-25,25)
        # y = random.randint(0,120)
        x = xlist.pop()
        y = ylist.pop()
        xVals, yVals = updateQueue(x, y)
        ax1.clear()
        plt.title('Distance (in inches) from Front Center of Mic Array')
        ax1.set_xbound(lower=-60, upper=60)
        ax1.set_ybound(lower=0, upper=120)
        ax1.set_xlabel('Horizontal Distance')
        ax1.set_ylabel('Vertical Distance')
        plt.xlim((-60,60))
        plt.ylim((1,120))
        ax1.scatter(xVals, yVals, c='red')


    ani = animation.FuncAnimation(fig,animate, interval=1000)
    plt.xlim((1,120))
    plt.ylim((1,120))
    plt.show()
