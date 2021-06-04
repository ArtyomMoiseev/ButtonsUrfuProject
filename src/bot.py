# -*- coding: utf-8 -*-
import smbus2
import bme280
import time
import tgdraws

port = 1
address = 0x76
bus = smbus2.SMBus(port)
f = open('data.txt', 'w')
calibration_params = bme280.load_calibration_params(bus, address)

import readbme
import telebot
from telebot import types
bot = telebot.TeleBot("key")

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
        data = bme280.sample(bus, address, calibration_params)
        #messageOut = str(data.timestamp) + "\n" + str(round(data.temperature, 2)) + "\n"  + str(round(data.humidity, 2)) + "\n" +str(round(data.pressure, 2))
        bot.send_message(message.from_user.id, print_day_weather(data.timestamp,data.temperature,data.humidity,data.pressure))

@bot.message_handler(regexp="Погода за сегодня")
def handle_message(message):
    pass

@bot.message_handler(regexp="Погода за неделю")
def handle_message(message):
    pass

bot.polling(none_stop=True, interval=0)
