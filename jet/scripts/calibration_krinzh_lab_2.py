import numpy as np
import matplotlib.pyplot as plt
def read(filename):
    with open(filename) as f:
        lines = f.readlines()

    steps = int(lines[2].split()[2])
    measures = np.asarray(lines[4:], dtype=int)

    return measures
measures_00 = read("calibration_00.txt")
print(np.mean(measures_00), " - 0па")
measures_70 = read("calibration_70.txt")
print(np.mean(measures_70), " - 70Па")
print(round(70 /(np.mean(measures_70) - np.mean(measures_00)), 4), " - паскалей в одной условной единице измерения")

approx = np.polyfit(np.array([np.mean(measures_00), np.mean(measures_70)]), np.array([0, 70]), 1)
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.set_title("Калибровочный график зависимости показаний АЦП от давления")
ax1.plot(np.array([0, 70]), np.array([np.mean(measures_00), np.mean(measures_70)]), c = 'black', linewidth = 1, label = f"P = {round(approx[0], 4)}*N {round(approx[1], 3)}")
ax1.scatter(np.array([0, 70]), np.array([np.mean(measures_00), np.mean(measures_70)]), marker = 'o', c = 'blue', s = 100, label = "Измерения")
ax1.grid(which = 'major', color = 'b')
ax1.minorticks_on()
ax1.grid(which = 'minor', color = 'g', linestyle = ':')
ax1.set_xlabel('Давление, Па')
ax1.set_ylabel('Показания АЦП, у.е.')
ax1.legend(shadow = False, fontsize = 10)

approx2 = np.polyfit(np.array([0, 900]),np.array([0, 5]), 1)
ax2.set_title("Калибровочный график зависимости перемещения от шага двигателя")
ax2.plot(np.array([0, 900]), np.array([0, 5]), c = 'black', linewidth = 1, label = f"P = {round(approx2[0], 4)}*N + {round(approx2[1], 3)}")
ax2.scatter(np.array([0, 900]), np.array([0, 5]), marker = 'o', c = 'blue', s = 100, label = "Измерения")
ax2.grid(which = 'major', color = 'b')
ax2.minorticks_on()
ax2.grid(which = 'minor', color = 'g', linestyle = ':')
ax2.set_xlabel('Перемещение, y.e.')
ax2.set_ylabel('Перемещение, см')
ax2.legend(shadow = False, fontsize = 10)
plt.show()