import os
from confluent_kafka import SerializingProducer #Producer
import simplejson as json
from datetime import datetime, timedelta

LONDON_COORDINATES = {"latitude": 51.5074,"longitude": -0.1278}
BIRMINGHAM_COORDINATES = {"latitude": 52.4862,"longitude": -1.8904}

# Increment values for latitude and longitude to create a grid of coordinates between London and Birmingham

LATITUDE_INCREMENT = (BIRMINGHAM_COORDINATES['latitude'] - LONDON_COORDINATES['latitude']) / 10000

LONGITUDE_INCREMENT = (BIRMINGHAM_COORDINATES['longitude'] - LONDON_COORDINATES['longitude']) / 10000

# Environment variables for Kafka configuration
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
VEHICLE_TOPIC = os.getenv('VEHICLE_TOPIC', 'vehicle_data')
GPS_TOPIC = os.getenv('GPS_TOPIC', 'gps_data')
TRAFFIC_TOPIC = os.getenv('TRAFFIC_TOPIC', 'traffic_data')
WEATHER_TOPIC = os.getenv('WEATHER_TOPIC', 'weather_data')
EMERGENCY_TOPIC = os.getenv('EMERGENCY_TOPIC', 'emergency_data')

start_time = datetime.now()
start_location = LONDON_COORDINATES.copy()

def generate_vehicle_data(vehicle_id):
    location = stimulate_vehicle_movement()
    
def stimulate_journey(producer, vehicle_id):
    while True:
        vehicle_data = generate_vehicle_data(vehicle_id)
        gps_data = generate_gps_data(vehicle_id)
if __name__ == "__main__":
    # Kafka producer configuration
    producer_config = {
        'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
        'error_cb': lambda err: print(f"Kafka error: {err}"),
    }
    
    producer = SerializingProducer(producer_config)
    
    try:
        simulate_journey(producer, 'Steve-123')

    except KeyboardInterrupt:
        print("Simulation interrupted.")
    except Exception as e:
        print(f"An error occurred: {e}")