# -*- coding: utf-8 -*-
def print_day_weather(time,temp,hum,pres):
	return '🕛Время:' + str(time) + "\n" + '🌡Температура:' + str(round(temp, 2)) + ' °C' + "\n" + '💦Влажность:' + str(round(hum, 2)) + ' %' + "\n" + 'Давление:' +str(round(pres, 2)) + 'ГПа'
