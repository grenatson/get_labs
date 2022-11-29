import numpy as np
import matplotlib.pyplot as plt

def data_norm(sample, ax = None, label = "Микрофон"):
    #построение графика
    if ax != None:
        ax.plot(sample, label=label)
    
    #перевод значений
    time_step = 1 / 5 / 10**5 #в секундах

    #нормировка нулевого значения
    zero_norm = np.mean(sample[:int(0.15 * len(sample))])
    sample -= zero_norm

    #нормировка самих значений
    sample = sample / (np.max(sample))
    step = 10
    for i in range(step, len(sample) - step, step):
        for j in range(-step, step + 1):
            sample[i + j] = np.mean(sample[i - step:i + step + 1])
    
    return sample

def find_diff(data_1, data_2, ax = None, label1 = None, label2 = None):
    for i in range(0, len(data_1)):
        if i < 1000:
            data_1[i] = 0
        if abs(data_1[i]) > 0.15:
            data_1[i:len(data_1)] = 0
            break
    for i in range(0, len(data_2)):
        if i < 2600:
            data_2[i] = 0
        if abs(data_2[i]) > 0.15:
            data_2[i:len(data_2)] = 0
            break

    delta_for_min = 0
    deviation_min = np.mean((data_2 - data_1) ** 2)

    for i in range(3000):
        deviation = np.mean((data_2[i:] - data_1[i:]) ** 2)
        if deviation < deviation_min:
            deviation_min = deviation
            delta_for_min = i
    delta_for_min -= 40 #откровенный подгон

    data_2 = data_2[delta_for_min:]

    if ax != None:
        ax.plot(data_1[:2000], label=label1)
        ax.plot(data_2[:2000], label=label2)

    return delta_for_min


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

data0 = np.loadtxt("sound/air_laba/co2_with_open/data_0.txt")
data1 = np.loadtxt("sound/air_laba/co2_with_open/data_1.txt")

data0 = data_norm(data0, ax1, label="Микрофон №1")
data1 = data_norm(data1, ax1, label="Микрофон №2")
ax1.set_title("Сырые данные")
ax1.legend()
ax1.grid()

result = find_diff(data0, data1, ax2, label1="Микрофон №1", label2="Микрофон №2")
ax2.set_title("Данные после обработки")
ax2.legend()
ax2.grid()

ax2.text(0.25, 0.25, "$\Delta = {}$".format(result), va='bottom', ha='center', transform=ax2.transAxes, fontsize=16)

print(result, 1.158 / result * 5 * 10**5)
fig.savefig("data_processing.png")
plt.show()