import RPi.GPIO as GPIO
from flask import Flask

app = Flask(__name__)

# Define o pino de saída para o LED
LED_PIN = 18

# Configura o modo de numeração dos pinos
GPIO.setmode(GPIO.BCM)

# Configura o pino do LED como saída
GPIO.setup(LED_PIN, GPIO.OUT)

@app.route('/')
def toggle_led():
    # Lê o estado atual do LED
    led_status = GPIO.input(LED_PIN)
    
    # Muda o estado do LED
    GPIO.output(LED_PIN, not led_status)
    
    return 'LED está agora ' + ('ligado' if not led_status else 'desligado')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
