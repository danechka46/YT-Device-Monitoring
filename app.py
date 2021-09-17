import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

figure = plt.figure()

ax1 = figure.add_subplot(2,3,1)
ax2 = figure.add_subplot(2,3,2)
ax3 = figure.add_subplot(2,3,3)
ax4 = figure.add_subplot(2,3,4)
ax5 = figure.add_subplot(2,3,5)
ax6 = figure.add_subplot(2,3,6)

x = np.array([-3, -2, -1, 0, 1, 2, 3])
y = np.array([9, 4, 1, 0, 1, 4, 9])

ax1.plot(x, y)
ax4.plot(x, np.sin(x), c = (1.0,0.2,0.3), ls='-',marker='*',alpha = 0.1,lw='5',label='sin(x)')
ax2.plot(x, x+5, c = 'blue', ls='dotted',marker = '^',lw='0.5')
ax3.plot(x, x+3, c = 'g', ls='dashdot',marker ='o',alpha =0.3)
ax5.plot(x, np.cos(x), c = '0.75', ls='dashed',label='cos(x)')
ax6.plot(x, x, c = '#FFDD44', ls='solid')

ax1.set_xlim(0,5)
ax1.set_ylim(0,3)

ax4.set_title('six(x)')
ax4.set_xlabel('OX')
ax4.set_ylabel('OY')

ax1.set_xticks(np.arange(-3,3.5,0.5))
ax2.set_yticks(np.arange(0,13,2))

ax1.spines['right'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax4.spines['right'].set_visible(False)
ax5.spines['right'].set_visible(False)

figure.savefig('C:/Users/arzha/Desktop/figure1.png')

ax1.grid()
ax2.grid(color='g',lw=0.5)
ax4.legend(loc='lower left')
plt.show()

