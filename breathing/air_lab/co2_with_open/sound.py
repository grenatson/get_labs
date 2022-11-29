import numpy as np
import matplotlib.pyplot as plt
from useful_functions import data_norm, find_diff

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

data0 = np.loadtxt("breathing/air_lab/co2_with_open/data_0.txt")
data1 = np.loadtxt("breathing/air_lab/co2_with_open/data_1.txt")

data0 = data_norm(data0, ax1, label="Микрофон №1")
data1 = data_norm(data1, ax1, label="Микрофон №2")
ax1.set_title("Сырые данные")
ax1.legend()
ax1.grid()

result = find_diff(data0, data1, ax2, label1="Микрофон №1", label2="Микрофон №2", tick=40)
ax2.set_title("Данные после обработки")
ax2.legend()
ax2.grid()

ax2.text(0.25, 0.25, "$\Delta = {}$".format(result), va='bottom', ha='center', transform=ax2.transAxes, fontsize=16)

print(result, 1.158 / result * 5 * 10**5)
fig.savefig("breathing/air_lab/co2_with_open/data_processing.png")
plt.show()