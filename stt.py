import RPi.GPIO as GPIO
import gspeech
import time

gsp = gspeech.Gspeech()
print("준비완료")

led_pin = [2, 4, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

pinPiezo = 13
GPIO.setup(pinPiezo, GPIO.OUT)
piezo = GPIO.PWM(pinPiezo, 1)
piezo.start(99)
piezo.ChangeDutyCycle(60)
도 = 261.6256
레 = 293.6648
미 = 329.6276
파 = 349.2282
솔 = 391.9954
라 = 440
시 = 493.8833

melody = [도, 레, 미, 레, 도, 시, 도, 레, 도, 레, 미, 레, 도, 파, 미, 미, 레, 도, 미, 레, 미, 파, 레, 도]


while 1:
    stt = gsp.getText()
    if stt is None:
        break
    stt = stt.strip()
    print(stt)
    if(stt in "켜져라"):
        GPIO.output(led_pin[0], GPIO.HIGH)
        GPIO.output(led_pin[1], GPIO.HIGH)
        GPIO.output(led_pin[2], GPIO.HIGH)
    elif(stt in "끝"):
        GPIO.output(led_pin[0], GPIO.LOW)
        GPIO.output(led_pin[1], GPIO.LOW)
        GPIO.output(led_pin[2], GPIO.LOW)
    elif(stt in "빨강"):
        GPIO.output(led_pin[0], GPIO.HIGH)
    elif(stt in "노랑"):
        GPIO.output(led_pin[1], GPIO.HIGH)
    elif(stt in "초록"):
        GPIO.output(led_pin[2], GPIO.HIGH)
    elif(stt in "버튼"):
        piezo.ChangeFrequency(262)
        time.sleep(2)
    elif(stt in "노래"):
        for i in melody:
            piezo.ChangeFrequency(i)
            time.sleep(0.2)
    piezo.ChangeFrequency(1)
    
    time.sleep(0.1)

