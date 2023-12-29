from flask import Flask, render_template, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

app = Flask(__name__)

# Use SQLite and point to the database file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sensor_data.db'
db = SQLAlchemy(app)

class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sensor_id = db.Column(db.Integer)
    normal_light_state = db.Column(db.Integer)
    light_out_event = db.Column(db.Boolean)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/get_sensor_history/<int:sensor_id>')
def get_sensor_history(sensor_id):
    # Fetch historical data for the selected sensor from the last 24 hours
    history_data = SensorData.query.filter(
        SensorData.sensor_id == sensor_id,
        SensorData.timestamp >= datetime.utcnow() - timedelta(hours=24)
    ).order_by(SensorData.timestamp).all()

    if history_data:
        # Format the historical data with 24-hour time format
        formatted_history = [{
            'normal_light_state': entry.normal_light_state,
            'timestamp': entry.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        } for entry in history_data]

        return jsonify({'history': formatted_history})

    response_data = {'error': 'No historical data found'}
    return make_response(jsonify(response_data), 404)

@app.route('/get_sensor_ids')
def get_sensor_ids():
    # Retrieve distinct sensor IDs from the database
    sensor_ids = db.session.query(SensorData.sensor_id).distinct().all()
    sensor_ids = [id[0] for id in sensor_ids]
    
    return jsonify(sensor_ids)

@app.route('/get_sensor_data/<int:sensor_id>')
def get_sensor_data(sensor_id):
    # Fetch most recent data for the selected sensor from the database
    sensor_data = SensorData.query.filter_by(sensor_id=sensor_id).order_by(SensorData.timestamp.desc()).first()

    if sensor_data:
        # Format the data as needed
        formatted_data = {
            'sensor_id': sensor_data.sensor_id,
            'normal_light_state': sensor_data.normal_light_state,
            'light_out_event': sensor_data.light_out_event,
            'timestamp': sensor_data.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        }
        return jsonify({'data': formatted_data})

    response_data = {'error': 'Sensor data not found'}
    return make_response(jsonify(response_data), 404)

def store_sensor_data(sensor_id, normal_light_state):
    new_data = SensorData(sensor_id=sensor_id, normal_light_state=normal_light_state)
    db.session.add(new_data)
    db.session.commit()
    print("Sensor data stored successfully")

def store_light_out_event(sensor_id, light_out_event):
    recent_data = SensorData.query.filter_by(sensor_id=sensor_id).order_by(SensorData.timestamp.desc()).first()

    if recent_data:
        recent_data.light_out_event = light_out_event
        db.session.commit()
        print("Light out event stored successfully")
    else:
        print(f"No sensor data found for sensor_id: {sensor_id}")

@app.route('/')
def home():
    latest_data = {}
    sensor_ids = db.session.query(SensorData.sensor_id).distinct().all()
    sensor_ids = [id[0] for id in sensor_ids]

    for sensor_id in sensor_ids:
        recent_data = SensorData.query.filter_by(sensor_id=sensor_id).order_by(SensorData.timestamp.desc()).first()
        if recent_data:
            latest_data[sensor_id] = {
                'sensor_id': recent_data.sensor_id,
                'normal_light_state': recent_data.normal_light_state,
                'light_out_event': recent_data.light_out_event,
                'timestamp': recent_data.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            }

    return render_template("index.html", latest_data=latest_data)

@app.route('/store_data', methods=['POST'])
def store_data():
    data = request.get_json()

    if 'normal_light_state' in data:
        store_sensor_data(data.get('sensor_id'), data.get('normal_light_state'))
    elif 'light_out_event' in data:
        store_light_out_event(data.get('sensor_id'), data.get('light_out_event'))

    print("Received data:", data)
    return jsonify({"message": "Data received and stored successfully"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', port=5000)