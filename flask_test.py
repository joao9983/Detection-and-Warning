from flask import Flask, request
import RPi.GPIO as GPIO

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

@app.route("/led", methods=["GET"])
def change_led_status():
    status = request.args.get("status")
    if status == "on":
        GPIO.output(18, True)
        return "LED ligado"
    elif status == "off":
        GPIO.output(18, False)
        return "LED desligado"
    else:
        return "Status inválido"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)