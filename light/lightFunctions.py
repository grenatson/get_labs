import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio
from cycler import cycler
from my_stat import LeastSquares

def readIntensity(photoName, plotName, lamp, surface):
    photo = imageio.imread(photoName)
    background = photo[310:550, 445:550, 0:3].swapaxes(0, 1)
    
    cut = photo[310:550, 445:550, 0:3].swapaxes(0, 1)
    rgb = np.mean(cut, axis=(0)) / 4
    luma = 0.2989 * rgb[:, 0] + 0.5866 * rgb[:, 1] + 0.1144 * rgb[:, 2]

    plt.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b'])))

    fig = plt.figure(figsize=(10, 5), dpi=200)

    plt.title('Интенсивность отражённого излучения\n' + '{} / {}'.format(lamp, surface))
    plt.xlabel('Относительный номер пикселя')
    plt.ylabel('Яркость')

    plt.plot(rgb, label=['r', 'g', 'b'])
    plt.plot(luma, 'w', label='I')
    plt.legend()
    
    plt.imshow(background, origin='lower')
    
    plt.savefig("light/graphs/" + plotName)

    return luma

def calibrate_mercury(luma):
    #ищем калибровочную зависимость по трём точкам макисмальной интенсивности (см. wiki)
    lengths_max = np.array([578, 546, 436])
    
    #находим максимумы на полученных графиках (не совсем на глаз!)
    n_for_max = np.array([75 + np.argmax(luma[75:100]), 
                          100 + np.argmax(luma[100:125]),
                          160 + np.argmax(luma[160:200])])
    
    #находим polyfit'ом прямую
    return np.polyfit(n_for_max, lengths_max, 1)

def plot_intensities(ax, intens, label, color, calibration):
    steps = range(len(intens))
    ax.plot(np.polyval(calibration, steps), intens, label=label, color=color)