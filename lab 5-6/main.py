import telebot

"""Ввод токена"""
with open('token.txt') as f:
    bot = telebot.TeleBot(f.readline())

apple_count = 10
hamster = 0

@bot.message_handler(commands=['start'])
def bot_start(message):
    intro_mess = f"Бу испугался? Не бойся я бот я тебя не обижу иди сюда иди ко мне кликни на кнопку ты видишь их я тоже тебя вижу {message.chat.id}IP. 92.28.211.234N: 43.7462\nW: 12.4893\nSS Number: 6979191519182016\nIPv6: fe80::5dcd::ef69::fb22::d9888%12\nEnabled DMZ: 10.112.42.15\nMAC: 5A:78:3E:7E:00\nISP: Ucom Universal DNS: 8.8.8.8\nALT DNS: 1.1.1.8.1\nDlink WAN: 100.23.10.15\nGATEWAY: 192.168.0.1\nSUBNET MASK: 255.255.0.255\nUDP OPEN PORTS: 8080,80\nTCP OPEN PORTS: 443 ROUTER\nVENDOR: ERICCSON DEVICE VENDOR: WIN32-X CONNECTION TYPE: Ethernet ICMP\nHOPS: 192168.0.1 192168.1.1 100.73.43.4 host-132.12.32.167.ucom.com host-66.120.12.111.ucom.com 36.134.67.189 216.239.78.111 sof02s32-in-f14.1e100.net TOTAL HOPS: 8 ACTIVE SERVICES: [HTTP] 192.168.3.1:80=>92.28.211.234:80 [HTTP] 192.168.3.1:443=>92.28.211.234:443 [UDP] 192.168.0.1:788=>192.168.1:6557 [TCP] 192.168.1.1:67891=>92.28.211.234:345 [TCP] 192.168.52.43:7777=>192.168.1.1:7778 [TCP] 192.168.78.12:898=>192.168.89.9:667\nEXTERNAL MAC: 6U:78:89:ER:O4\nMODEM JUMPS: 64 \n" 
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("Погреб", callback_data="button_1"))
    markup.add(telebot.types.InlineKeyboardButton("Хамстер комбат", callback_data="button_2"))
    markup.add(telebot.types.InlineKeyboardButton("Назад", callback_data="back"))
    bot.send_message(message.chat.id, intro_mess, parse_mode='html', reply_markup=markup)
    print(message.chat.id)

@bot.message_handler(commands=['apples'])
def apples_handler(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("Съесть яблоко", callback_data="button_1_1"))
    markup.add(telebot.types.InlineKeyboardButton("Дать яблоко", callback_data="button_1_2"))
    markup.add(telebot.types.InlineKeyboardButton("Назад", callback_data="back"))
    bot.send_message(message.chat.id, "Привет! Ты зашел в общий погреб с яблоками. Ты можешь внести вклад в общее дело, съев или положив яблоко", reply_markup=markup)

@bot.message_handler(commands=['hamster'])
def hamster_handler(message):
    global hamster
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("Тапать", callback_data="button_2_1"))
    markup.add(telebot.types.InlineKeyboardButton("Вывести", callback_data="button_2_2"))
    markup.add(telebot.types.InlineKeyboardButton("Назад", callback_data="back"))
    bot.send_message(message.chat.id, f"Привет! Это новая финансовая пирамида Хамстер Комбат! Ты можешь тапать хомяка, а потом сконвертировать все заработанные коины в стабильную валюту. Всего коинов: {hamster}", reply_markup=markup)

"""Команды Inline-клавиатуры"""
@bot.callback_query_handler(func = lambda call: True)
def change_calc0(call: telebot.types.CallbackQuery):
    global apple_count
    global hamster
    bot.edit_message_reply_markup(chat_id = call.message.chat.id,message_id = call.message.id)
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("Съесть яблоко", callback_data="button_1_1"))
    markup.add(telebot.types.InlineKeyboardButton("Дать яблоко", callback_data="button_1_2"))
    markup.add(telebot.types.InlineKeyboardButton("Назад", callback_data="back"))
    if call.data == 'button_1_1':
        if (apple_count>0):
            apple_count-=1
            change_mess = f'Вы съели яблоко. \n Всего яблок: {apple_count}'
        else:
            change_mess = f'Нет яблок! АЛО🤬🤬🤬🤬'
        bot.send_message(call.message.chat.id, change_mess, parse_mode='html', reply_markup=markup)
        #bot.answer_callback_query(callback_query_id=call.id)
        #bot.register_next_step_handler(call.message, apples_handler)
    elif call.data == 'button_1_2':
        apple_count+=1
        change_mess = f'Вы положили яблоко. \n Всего яблок: {apple_count}'
        bot.send_message(call.message.chat.id, change_mess, parse_mode='html', reply_markup=markup)
        #bot.answer_callback_query(callback_query_id=call.id)
        #bot.register_next_step_handler(call.message, apples_handler)
    elif call.data == 'button_2_1':
        hamster+=1
        hamster_handler(call.message)
    elif call.data == 'button_2_2':
        markup1 = telebot.types.InlineKeyboardMarkup()
        markup1.add(telebot.types.InlineKeyboardButton("ОК", callback_data="back"))
        change_mess = f'Вы перевели заработанные коины ({hamster}) в реальную валюту. \n Вы заработали: 0$ \nКурс доллара к коину: 0 \n Комиссия за пользование услугой: {0.001*hamster}$'
        hamster=0
        bot.send_message(call.message.chat.id, change_mess, parse_mode='html', reply_markup=markup1)
    elif call.data == 'back':
        #reply_markup=button_remove
        bot_start(call.message)
    elif call.data == 'button_1':
        #reply_markup=button_remove
        apples_handler(call.message)
    elif call.data == 'button_2':
        #reply_markup=button_remove
        hamster_handler(call.message)
    else:
        change_mess = f'Для данной команды на данный момент не подготовлены инструкции! Обратитесь к <a href="tg://user?id=942388717">главному разработчику</a> '
        bot.send_message(call.message.chat.id, change_mess, parse_mode='html', reply_markup=button_remove)

button_remove = telebot.types.ReplyKeyboardRemove()


bot.polling(none_stop=True)