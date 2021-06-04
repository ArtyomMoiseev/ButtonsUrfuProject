import smbus2
import bme280
import time
from datetime import datetime

port = 1
address = 0x76
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)
weather_db = open('weatherData', 'a')
data = bme280.sample(bus, address, calibration_params)

while True:
	data = bme280.sample(bus, address, calibration_params)
	weather_db.write(str(str(data.timestamp) + ';' + str(round(data.temperature,2)) + ';' + str(round(data.humidity,2)) + ';' + str(round(data.pressure,2))))
	time.sleep(30)