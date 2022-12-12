import numpy as np
import matplotlib.pyplot as plt

def speedOfSound(temperature, h2oX, co2Max):
    temperature += 273.15

    cp_h2o = 1.863
    cv_h2o = 1.403
    mu_h2o = 18.01 * 10**-3
    x_h2o = h2oX

    cp_co2 = 0.838
    cv_co2 = 0.649
    mu_co2 = 44.01 * 10**-3
    x_co2 = co2Max * (1 - x_h2o)

    cp_n2 = 1.0036
    cv_n2 = 0.7166
    mu_n2 = 28.97 * 10**-3
    x_n2 = 0.78084 * (1 - x_h2o)

    cp_ar = 0.52
    cv_ar = 0.3118
    mu_ar = 40 * 10**-3
    x_ar = 0.934 / 100 * (1 - x_h2o)

    cp_o2 = 1.8188
    cv_o2 = 1.2991
    mu_o2 = 16 * 10**-3
    x_o2 = 20.976 / 100 * (1 - x_h2o) - co2Max

    '''
    cp_air = cp_n2 * x_n2 + cp_ar * x_ar + cp_o2 * x_o2
    cv_air = cv_n2 * x_n2 + cv_ar * x_ar + cv_o2 * x_o2
    mu_air = mu_n2 * x_n2 + mu_o2 * x_o2 + mu_ar * x_ar
    x_air = 1 - h2oX - co2Max
    '''

    cp_air = 3.5 * x_n2 + 2.5 * x_ar + 3.5 * x_o2
    cv_air = 2.5 * x_n2 + 1.5 * x_ar + 2.5 * x_o2
    mu_air = mu_n2 * x_n2 + mu_o2 * x_o2 + mu_ar * x_ar
    x_air = 1 - h2oX - co2Max

    gamma = (cp_air + 4 * x_h2o + 4 * x_co2) / (cv_air + 3 * x_h2o + 3 * x_co2)

    mu = 29 * 10**-3
    mu = mu_air + mu_h2o * x_h2o + mu_co2 * x_co2
    print(mu)

    co2X = x_co2
    soundSpeed = (gamma * 8.31 * temperature / mu) ** 0.5
    
    return co2X, soundSpeed

def process_speed(temperature, humidity, speed_check, ax):
    x_h2o = humidity / 100 * 3169 / 101325
    co2X, sound_speeds = speedOfSound(temperature, x_h2o, np.linspace(0, 0.05, 100))
    ax.plot(co2X, sound_speeds, label="Влажность $\\varphi$ = {}%".format(humidity))
    polynomial_fit = np.polyfit(sound_speeds, co2X, 1)
    
    co2_check = np.polyval(polynomial_fit, speed_check)
    ax.scatter(co2_check, speed_check)
    ax.text(co2_check, speed_check + 0.25, "{:.4f}\n {:.2f} м/с".format(co2_check, speed_check), ha='center', va='bottom', bbox={'pad': 2, 'alpha': 0.25})

fig, ax = plt.subplots()

process_speed(25.3, 37.2, 345.67, ax)
process_speed(25.3, 100, 343.21, ax)

ax.set_ylabel("Скорость звука, м/с")
ax.set_xlabel("Концентрация $CO_2$")
ax.grid()
ax.legend()

fig.savefig("breathing/air_lab/result.png")
plt.show()