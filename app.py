from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Mock data: safe perches and flying routes
safe_perches = [
    {"name": "Old Bell Tower", "lat": 40.7128, "lng": -74.0060},
    {"name": "Abandoned Mansion Roof", "lat": 40.7138, "lng": -74.0080},
    {"name": "Cave of Echoes", "lat": 40.7100, "lng": -74.0000},
]

# Simulated flying route
flight_path = [
    {"lat": 40.7105, "lng": -74.0045},
    {"lat": 40.7110, "lng": -74.0050},
    {"lat": 40.7120, "lng": -74.0060},
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/radar")
def radar():
    return render_template("radar.html")

@app.route("/api/perches")
def perches():
    return jsonify(safe_perches)

@app.route("/api/flight_path")
def path():
    return jsonify(flight_path)

@app.route("/api/radar")
def radar_data():
    # Randomly simulate threats on radar
    threats = [
        {"type": random.choice(["drone", "owl", "falcon"]),
         "distance": random.randint(100, 1000),
         "direction": random.randint(0, 359)}
        for _ in range(random.randint(1, 5))
    ]
    return jsonify(threats)

if __name__ == "__main__":
    app.run(debug=True)
