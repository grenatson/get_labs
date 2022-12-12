'''
TODO
    Подготовка - 0 баллов
        ###Импортировать файл с подготовленными функциями в пустой скрипт измерений import lightFunctions as j
        ###Подобрать координаты обрезки фотографии спектра в файле lightFunctions.py под исходные данные
    Калибровка - 4 балла
        ###Преобразовать фотографию спектра ртутной лампы в вектор интенсивностей
        ###Найти в википедии спектр ртутной лампы с указанием длин волн пиков
        ###Сопоставить номер столбца и длину волны через пики интенсивности ртутной лампы
            ###Найти пики интенсивности на спектре ртутной лампы "глазами и руками"
            ###Приветствуется автоматический поиск при помощи скрипта (необязательно, +1 балл)
        ###Получить калибровочную зависимость длины волны от относительного номера пикселя
    Обработка данных
        ###Построить общий график интенсивностей света лампы накаливания, отражённого от цветных поверхностей - 3 балла
        Построить общий график альбедо цветных поверхностей - 3 балла
'''
import numpy as np
import matplotlib.pyplot as plt
import lightFunctions as j

luma = j.readIntensity("light/white-mercury.png", "white-calibartion","mercury", "white")
calib_params = j.calibrate_mercury(luma)

#проверка, что приближение корректно
print(np.polyval(calib_params, np.array([np.argmax(luma[75:100])+75, np.argmax(luma[100:125])+100, np.argmax(luma[160:200])+160])))
print(calib_params)

# Создание листов значений яркости для каждой из ламп
wt = [j.readIntensity("light/white-tungsten.png", "white-tungsten", "Лампа накаливания", "Белый лист"), "Белый лист", "silver"]
yt = [j.readIntensity("light/yellow-tungsten.png", "yellow-tungsten", "Лампа накаливания", "Жёлтый лист"), "Жёлтый лист", "gold"]
bt = [j.readIntensity("light/blue-tungsten.png", "blue-tungsten", "Лампа накаливания", "Синий лист"), "Синий лист", "dodgerblue"]
rt = [j.readIntensity("light/red-tungsten.png", "red-tungsten", "Лампа накаливания", "Красный лист"), "Красный лист", "tomato"]
gt = [j.readIntensity("light/green-tungsten.png", "green-tungsten", "Лампа накаливания", "Зелёный лист"), "Зелёный лист", "lime"]
#wm = (j.readIntensity("light/white-mercury.png", "white-mercury", "Ртутная лампа", "Белый лист"), "Белый лист")

fig, ax1 = plt.subplots(figsize=(15, 5))
raw_intensities = np.array([wt, yt, bt, rt, gt])
for raw_i in raw_intensities:
    j.plot_intensities(ax1, raw_i[0], raw_i[1], raw_i[2], calib_params)

ax1.set_xlabel("Длина волны")
ax1.set_ylabel("Яркость")
ax1.set_facecolor("snow")
ax1.legend()
ax1.grid()

plt.savefig("intensities.png", dpi=600)

#ищем альбедо
fig, ax2 = plt.subplots(figsize=(15, 5))

for raw_i in raw_intensities:
    j.plot_intensities(ax2, raw_i[0] / raw_intensities[0][0], raw_i[1], raw_i[2], calib_params)
ax2.set_xlim((400, 725))
ax2.set_ylim((0, 1.25))

ax2.set_xlabel("Длина волны")
ax2.set_ylabel("Альбедо")
ax2.set_facecolor("snow")
ax2.legend(loc='upper right')

plt.savefig("albedos.png", dpi=600)