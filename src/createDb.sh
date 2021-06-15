 rrdtool create weather.rrd \
   --step 1m \
   DS:temperature:GAUGE:1m:0:150 \
   DS:humidity:GAUGE:1m:0:110 \
   DS:pressure:GAUGE:1m:0:1000 \
   RRA:AVERAGE:0.5:1m:24h \
   RRA:AVERAGE:0.5:30m:30d \
   RRA:AVERAGE:0.5:4h:30d \
   RRA:AVERAGE:0.5:8h:120d