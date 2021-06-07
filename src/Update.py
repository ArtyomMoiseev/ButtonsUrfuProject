import smbus2
import bme280
import time
import rrdtool
from datetime import datetime

port = 1
address = 0x76
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)
weather_db = open('weatherData', 'a')
data = bme280.sample(bus, address, calibration_params)

rrd_path = "weather.rrd"

while True:
	data = bme280.sample(bus, address, calibration_params)
	rrd_record = "N:" + str(round(data.temperature,2)) + ':' + str(round(data.humidity,2)) + ':' + str(round(data.pressure,2))
	rrdtool.update(rrd_path, rrd_record)
	time.sleep(60)
