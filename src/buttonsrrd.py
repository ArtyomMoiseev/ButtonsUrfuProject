import rrdtool
from datetime import datetime

def parse_rrd_record(record):
	time = record["date"]
	temp = record["ds"]["temperature"]
	hum = record["ds"]["humidity"]
	pres = record["ds"]["pressure"]
	return (time,temp,hum,pres)

def draw_day_graph_temp(rrd_path,file_name):
	rrdtool.graph(file_name,
	"-w 785 -h 240 -a PNG",
	'--start', "-1d",
    '--end', 'now',
	"--slope-mode",
	"--vertical-label", "temperature (°C)",
	"DEF:temp1=weather.rrd:temperature:MAX",
	"LINE1:temp1#ff0000:\"temperature\" "
	)
	pass

def draw_week_graph_temp(rrd_path,file_name):
	rrdtool.graph(file_name,
	"-w 785 -h 480 -a PNG",
	'--start', "-7d",
    '--end', 'now',
	"--slope-mode",
	"--vertical-label", "temperature (°C)",
	"DEF:temp1=weather.rrd:temperature:MAX",
	"LINE1:temp1#ff0000:\"temperature\" "
	)
	pass

def draw_day_graph_hum(rrd_path,file_name):
	rrdtool.graph(file_name,
	"-w 785 -h 480 -a PNG",
	'--start', "-1d",
    '--end', 'now',
	"--slope-mode",
	"--vertical-label", "humidity (%)",
	"DEF:temp1=weather.rrd:humidity:MAX",
	"LINE1:temp1#00dcff:\"humidity\" "
	)
	pass

def draw_week_graph_hum(rrd_path,file_name):
	rrdtool.graph(file_name,
	"-w 785 -h 480 -a PNG",
	'--start', "-7d",
    '--end', 'now',
	"--slope-mode",
	"--vertical-label", "humidity (%)",
	"DEF:temp1=weather.rrd:humidity:MAX",
	"LINE1:temp1#00dcff:\"humidity\" "
	)
	pass

def draw_day_graph_pressure(rrd_path,file_name):
	rrdtool.graph(file_name,
	"-w 785 -h 480 -a PNG",
	'--start', "-1d",
    '--end', 'now',
	"--slope-mode",
	"--vertical-label", "pressure (Hpa)",
	"DEF:temp1=weather.rrd:pressure:MAX",
	"LINE1:temp1#c900ff:\"pressure\" "
	)
	pass

def draw_week_graph_pressure(rrd_path,file_name):
	rrdtool.graph(file_name,
	"-w 785 -h 480 -a PNG",
	'--start', "-7d",
    '--end', 'now',
	"--slope-mode",
	"--vertical-label", "pressure (Hpa)",
	"DEF:temp1=weather.rrd:pressure:MAX",
	"LINE1:temp1#c900ff:\"pressure\" "
	)
	pass

def export_data(rrd_path,start,step):
	data = rrdtool.fetch(rrd_path, 'AVERAGE', '-r', str(step), '-s', str(start))
	with open('WeatherData', 'w') as f:
		for item in data:
			f.write("%s\n" % str(item))
	f = open('WeatherData')
	return f