# -*- coding: utf-8 -*-
import os
import time
import tgdraws
import rrdtool
import buttonsrrd
import telebot
from telebot import types

rrd_path = "weather.rrd"

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('⛅ Погода сейчас')
    itembtn2 = types.KeyboardButton('🕖 Погода за сегодня')
    itembtn3 = types.KeyboardButton('📅 Погода за неделю')
    markup.add(itembtn1,itembtn2,itembtn3)
    bot.send_message(message.from_user.id, "Чем вам помочь?", reply_markup=markup)

@bot.message_handler(regexp="Погода сейчас")
def handle_message(message):
    (time,temp,hum,pressure) = buttonsrrd.parse_rrd_record(rrdtool.lastupdate(rrd_path))
    bot.send_message(message.from_user.id, tgdraws.print_day_weather(time,temp,hum,pressure))

@bot.message_handler(regexp="Погода за сегодня")
def handle_message(message):
    f_name_temp = str(message.from_user.id) + "_day_graph_temp.png"
    f_name_hum = str(message.from_user.id) + "_day_graph_hum.png"
    f_name_pressure = str(message.from_user.id) + "_day_graph_pressure.png"
    buttonsrrd.draw_day_graph_temp(rrd_path,f_name_temp)
    buttonsrrd.draw_day_graph_hum(rrd_path,f_name_hum)
    buttonsrrd.draw_day_graph_pressure(rrd_path,f_name_pressure)
    graph_temp = open(f_name_temp,'rb')
    graph_hum = open(f_name_hum,'rb')
    graph_pressure = open(f_name_pressure,'rb')
    bot.send_photo(message.from_user.id, graph_temp)
    bot.send_photo(message.from_user.id, graph_hum)
    bot.send_photo(message.from_user.id, graph_pressure)
    os.remove(f_name_temp)
    os.remove(f_name_pressure)
    os.remove(f_name_hum)
    pass

@bot.message_handler(regexp="Погода за неделю")
def handle_message(message):
    f_name_temp = str(message.from_user.id) + "_week_graph_temp.png"
    f_name_hum = str(message.from_user.id) + "_week_graph_hum.png"
    f_name_pressure = str(message.from_user.id) + "_week_graph_pressure.png"
    buttonsrrd.draw_week_graph_temp(rrd_path,f_name_temp)
    buttonsrrd.draw_week_graph_hum(rrd_path,f_name_hum)
    buttonsrrd.draw_week_graph_pressure(rrd_path,f_name_pressure)
    graph_temp = open(f_name_temp,'rb')
    graph_hum = open(f_name_hum,'rb')
    graph_pressure = open(f_name_pressure,'rb')
    bot.send_photo(message.from_user.id, graph_temp)
    bot.send_photo(message.from_user.id, graph_hum)
    bot.send_photo(message.from_user.id, graph_pressure)
    os.remove(f_name_temp)
    os.remove(f_name_pressure)
    os.remove(f_name_hum)
    pass

bot.polling(none_stop=True, interval=0)
