import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 10)
pwm.start(0)
try:
    while True:
        value = input("Enter duty cycle: ")
        freq = input("Enter Frequency: ")
        value = float(value)
        pwm.ChangeDutyCycle(value)
        pwm.ChangeFrequency(float(freq))
        print(f"Duty, Freq cycle set: {value}, {freq} Hz")
except KeyboardInterrupt:
    pass

print("Stopping.")
pwm.stop()
GPIO.cleanup()


