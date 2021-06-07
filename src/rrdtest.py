import rrdtool

print(rrdtool.lastupdate("weather.rrd")["date"])
