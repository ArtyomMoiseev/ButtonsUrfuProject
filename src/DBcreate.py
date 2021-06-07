# -*- coding: utf-8 -*-
from rrdtool import *
fname = 'database.rrd'
#rrd = RoundRobinDatabase(fname)

rrdtool.create(
   DataSource("temperature", type=GaugeDST, heartbeat=60, min=0, max=12500000),
   DataSource("humidity", type=GaugeDST, heartbeat=60, min=0, max=12500000),
   DataSource("pressure", type=GaugeDST, heartbeat=60, min=0, max=12500000),
   RoundRobinArchive(cf=AverageCF, xff=0.5, steps=6, rows=48),
   RoundRobinArchive(cf=AverageCF, xff=0.5, steps=24, rows=84),
   RoundRobinArchive(cf=AverageCF, xff=0.5, steps=96, rows=90),
   step=300
   )