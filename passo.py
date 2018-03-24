from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

#EasyDriveBase
pino_passo = 5
pino_direcao = 13
passo_foto = 0

#EasyDriveCamera
pino_direcaoC = 29
pino_passoC = 21

#Quantidade maxima de passo
qtd_passo = 19

#Melhor distancia para nao perder espaco
passo_motor = 150
t
oque = 33

camera = PiCamera()
#width = 260
#height = 320
width = 480
height = 800

camera.resolution = (width, height)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(width, height))

# tempo para inicializar a camera
time.sleep(0.1)

GPIO.setup(pino_passo, GPIO.OUT)
GPIO.setup(pino_direcao, GPIO.OUT)
GPIO.setup(pino_passoC, GPIO.OUT)
GPIO.setup(pino_direcaoC, GPIO.OUT)

GPIO.setup(toque, GPIO.IN)

#Verificacao da posicao inicial do carrinhos (Testar)

GPIO.output(pino_direcao, GPIO.HIGH)

while (GPIO.input(33) == GPIO.HIGH):
    for i in range (0,1):
        for i in range(0,1):
            GPIO.output(pino_passo, GPIO.HIGH)
            time.sleep(0.001)
            GPIO.output(pino_passo, GPIO.LOW)
            time.sleep(0.001)

j = 1

time.sleep(1)

GPIO.output(pino_direcao, GPIO.LOW)

for i in range (0,qtd_passo):

    passo_foto = passo_foto +1
    print passo_foto
    if passo_foto >6:
        camera.capture('foto' + str(j) + '.jpg')
        j = j + 2
        time.sleep(1)

    for i in range(0,passo_motor):
        GPIO.output(pino_passo, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(pino_passo, GPIO.LOW)
        time.sleep(0.001)
    time.sleep(1)

#Movimentar motor da camera
GPIO.output(pino_direcaoC, GPIO.HIGH)

for i in range (0,31):
    for i in range (0,31):
        GPIO.output(pino_passoC, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(pino_passoC, GPIO.LOW)
        time.sleep(0.001)

time.sleep(1)


z =j-1

print '--------------------'

GPIO.output(pino_direcao, GPIO.HIGH)
for i in range (0,qtd_passo):
    print passo_foto
    passo_foto = passo_foto -1

    if passo_foto > 5:
        camera.capture('foto' + str(z) + '.jpg')
        z = z-2
        time.sleep(1)
    for i in range(0,passo_motor):
        GPIO.output(pino_passo, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(pino_passo, GPIO.LOW)
        time.sleep(0.001)
    time.sleep(1)


#Volta a camera para a posicao inicial
GPIO.output(pino_direcaoC, GPIO.LOW)

for i in range (0,31):
    for i in range (0,31):
        GPIO.output(pino_passoC, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(pino_passoC, GPIO.LOW)
        time.sleep(0.001)

time.sleep(1)
