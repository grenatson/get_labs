import numpy as np
import matplotlib.pyplot as plt
ro = 1.2 #кг на метр в кубе

def read(filename):
    with open(filename) as f:
        lines = f.readlines()

    steps = int(lines[2].split()[2])
    measures = np.asarray(lines[4:], dtype=int)
    return measures

fig, ax = plt.subplots(1)
colors = ['r', 'g', 'b', 'y', 'm', 'k', 'aquamarine', 'mediumseagreen', 'plum', 'indigo', 'lime']
for i in range(11):
    measure = read(f"{i*10}mm.txt")
    P = 0.1596*measure - 157.724
    R = []
    v = np.sqrt(abs(2 * P / ro))
    for j in range(len(v)):
        R.append(abs((0-10*0.0056*np.argmax(v) + j*10*0.0056))/100)
    sum = 0
    for j in range(len(v)-1):
        sum+=0.5*(R[j]*v[j] + R[j+1]*v[j+1])*abs(abs(R[j+1])-abs(R[j]))
    ax.plot([(0-10*0.0056*np.argmax(v) + j*10*0.0056) * 10 for j in range(0, len(v))],v, color = colors[i], linewidth = 1, label = f"Q({i*10}мм) = {round(2*np.pi*sum*1000, 2)} г/с")
ax.grid(which = 'major', color = 'b')
ax.minorticks_on()
ax.grid(which = 'minor', color = 'g', linestyle = ':')
ax.set_ylabel('Скорость воздуха, м/с')
ax.set_xlabel('Положение трубки Пито относительно центра струи, мм')
ax.legend(shadow = False, fontsize = 10)
plt.show()