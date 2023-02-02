import RPi.GPIO as GPIO
import time

# Define o modo de numeração da GPIO
GPIO.setmode(GPIO.BCM)

# Define o pino do LED como saída
led_pin = 18
GPIO.setup(led_pin, GPIO.OUT)

# Desliga o LED
GPIO.output(led_pin, GPIO.LOW)

# Limpa as configurações da GPIO
GPIO.cleanup()