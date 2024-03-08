import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.animation import FuncAnimation
import shutup

shutup.please()

plt.style.use('dark_background')


def animate(i):
	data = pd.read_csv('test.csv')
	data2 = pd.read_csv('test_g.csv')
	data3 = pd.read_csv('test_b.csv')
	k = data['k']
	x = data['x_values']
	y = data['y_values']

	m = data2['m']
	x_g = data2['x_values']
	y_g = data2['y_values']

	n = data3['n']
	x_b = data3['x_values']
	y_b = data3['y_values']
	a = data3['angle']

	plt.cla()
	#plt.plot(k,y,color='red', label='red')
	plt.plot(k,x,color='red', label='red')
	#plt.plot(m,x_g,color='green', label='green')
	plt.plot(n,x_b,color='blue', label='blue')
	#plt.plot(n,a,color='blue', label='cyan')

	plt.legend(loc='upper left')
	#plt.tight_layout()

ani = FuncAnimation(plt.gcf(),animate,interval=100)

#plt.tight_layout()
plt.show()
