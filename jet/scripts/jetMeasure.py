import jetFunctions as j
import matplotlib.pyplot as plt

j.initSpiAdc()
j.initStepMotorGpio()
try:
    samples = []
    j.stepBackward(200)
    for i in range(40):
        samples.append(j.getMeanAdc(1000))
        j.stepForward(10)
    j.stepBackward(200)
    j.save(samples, 10)
    plt.plot(samples)
    plt.show()

finally:
    j.deinitSpiAdc()
