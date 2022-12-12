#Подключение библиотек
import time
import picamera


#Объявление переменных
experiment_number = 0
lamps = ["mercury", "tungsten", "tungsten", "tungsten", "tungsten", "tungsten"]
paper = ["white", "white", "red", "yellow", "green", "blue"]


#Функция подготовки камеры
def prepare_camera():
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.start_preview()
        time.sleep(10)


#Сделать снимоr
def photo(experiment_name):
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.capture(experiment_name + ".png")

#Main part
print("-----To start experiment type y-----")
a = input()

if a == "y":
    print("Preparing the camera...")
    prepare_camera()
    print("Camera is ready")

for i in range(6):
    print("-----Type y to take a photo-----")
    a = input()
    if a == 'y':
        print("Taking a photo for  + paper[i] +  paper +  and  + lamps[i] +  lamp")
        photo(paper[i] + "-" + lamps[i])
    else:
        break
print("-----End of experiment-----")