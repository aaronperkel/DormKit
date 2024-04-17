'''
app.py
DORMKIT V1.0
'''

from flask import Flask, render_template
import HC_05

app = Flask(__name__)

@app.route("/lock_door", methods=["POST"])
def lock_door_url():
    print("Lock door")
    HC_05.lock_door()
    return "ok"

@app.route("/unlock_door", methods=["POST"])
def unlock_door_url():
    print("Unlock door")
    HC_05.unlock_door()
    return "ok"

@app.route("/light_on", methods=["POST"])
def light_on_url():
    print("Light on")
    HC_05.light_on()
    return "ok"

@app.route("/light_off", methods=["POST"])
def light_off_url():
    print("Light off")
    HC_05.light_off()
    return "ok"

@app.route("/", methods=["GET"])
def home():
    return render_template("buttons.html", title="DormKit")

app.run(host='0.0.0.0')
