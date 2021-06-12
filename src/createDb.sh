 rrdtool create weahter.rrd \
   --step 1m \
   DS:temperature:GAUGE:1m:0:150 \
   DS:humidity:GAUGE:1m:0:110 \
   DS:pressure:GAUGE:1m:0:1000 \
   RRA:AVERAGE:0.5:1m:15m \
   RRA:AVERAGE:0.5:30m:1d \
   RRA:AVERAGE:0.5:2h:7d \
   RRA:AVERAGE:0.5:8h:30d