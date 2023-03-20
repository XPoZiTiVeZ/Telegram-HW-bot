import keep_alive
import os
import json
import datetime
import time
import telebot
from telebot import types
from telebot.types import ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from tg_calendar import Calendar, CallbackData, RUSSIAN_LANGUAGE

token = os.environ['token']
writers = ['1139762823', '1349175494', '1173088677', '869710019', '919919639']
Date = []

subject = ['Русский',
			'Литература',
			'Французский',
			'Немецкий',
			'Английский(Слипухина)',
		    'Английский(Соколова)',
			'Физика',
			'ОБЖ',
			'Биология',
			'Информатика',
			'История',
			'Алгебра',
			'Геометрия',
			'Обществознание',
			'География',
			'Химия',
			'Классный час',
		   	'Дополнительно']

subject_keys = ['rus1',
				'lit1',
				'fre1',
				'deu1',
				'eng1',
				'phy1',
				'lsf1',
				'bio1',
				'inf1',
				'sto1',
				'alg1',
				'geo1',
				'soc1',
				'geog1',
				'che1',
				'cla1',
				'addi1',
				'eng21',
			   	'rus2',
				'lit2',
				'fre2',
				'deu2',
				'eng2',
				'phy2',
				'lsf2',
				'bio2',
				'inf2',
				'sto2',
				'alg2',
				'geo2',
				'soc2',
				'geog2',
				'che2',
				'cla2',
				'addi2',
				'eng22',
			   	'rus3',
				'lit3',
				'fre3',
				'deu3',
				'eng3',
				'phy3',
				'lsf3',
				'bio3',
				'inf3',
				'sto3',
				'alg3',
				'geo3',
				'soc3',
				'geog3',
				'che3',
				'cla3',
				'addi3',
				'eng23',
			   	'rus4',
				'lit4',
				'fre4',
				'deu4',
				'eng4',
				'phy4',
				'lsf4',
				'bio4',
				'inf4',
				'sto4',
				'alg4',
				'geo4',
				'soc4',
				'geog4',
				'che4',
				'cla4',
				'addi4',
				'eng24',
			   	'rus5',
				'lit5',
				'fre5',
				'deu5',
				'eng5',
				'phy5',
				'lsf5',
				'bio5',
				'inf5',
				'sto5',
				'alg5',
				'geo5',
				'soc5',
				'geog5',
				'che5',
				'cla5',
				'addi5',
			   	'eng25']

def write(data, file):
    with open(file, "w", encoding='utf-8') as write_file:
        json.dump(data, write_file, indent=4, sort_keys=True, ensure_ascii=False)

def read(file):
    with open(file, "r", encoding='utf-8') as read_file:
        data = json.load(read_file)
        return data

def add(message):
	global Date
	try:
		hw = read('homework.json')
		if Date[0] not in list(hw.get('date').keys()):
			hw.get('date').update({Date[0]:{}})
		if Date[1] not in list(hw.get('date').get(Date[0]).keys()):
			hw.get('date').get(Date[0]).update({Date[1]:[]})
		hw2 = hw.get('date').get(Date[0]).get(Date[1])
		if not message.text.find(';') == -1:
			hw1 = message.text.split(';')
			for i in range(len(hw1)):
				hw2.append(hw1[i])
		else:
			hw2.append(message.text)
		hw.get('date').get(Date[0]).update({Date[1]: hw2})
		write(hw, 'homework.json')
	except:
		bot.send_message(chat_id=message.chat.id,
							text="Что-то сработало неправильно")
		Date = []

def remove(message):
	global Date
	try:
		hw = read('homework.json')
		if Date[0] not in list(hw.get('date').keys()):
			bot.send_message(chat_id=message.chat.id,
								 text="На этот день нет домашнего задания")
			pass
		if Date[1] not in list(hw.get('date').get(Date[0]).keys()):
			bot.send_message(chat_id=message.chat.id,
								 text="На этот урок нет домашнего задания")
			pass
		hw.get('date').get(Date[0]).pop(Date[1])
		if len(list(hw.get('date').get(Date[0]).keys())) == 0:
			hw.get('date').pop(Date[0])
		write(hw, 'homework.json')
	except:

		Date = []
		
def removed(message):
	global Date
	try:
		hw = read('homework.json')
		if Date[0] not in list(hw.get('date').keys()):
			bot.send_message(chat_id=message.chat.id,
								 text="На этот день нет домашнего задания")

			pass
		hw.get('date').pop(Date[0])
		write(hw, 'homework.json')
	except:

		Date = []

def change(message):
	global Date
	try:
		hw = read('homework.json')
		if Date[0] not in list(hw.get('date').keys()):
			hw.get('date').update({Date[0]:{}})
		if Date[1] not in list(hw.get('date').get(Date[0]).keys()):
			hw.get('date').get(Date[0]).update({Date[1]:[]})
		hw2 = []
		if not message.text.find(';') == -1:
			hw1 = message.text.split(';')
			for i in range(len(hw1)):
				hw2.append(hw1[i])
		else:		
			hw2.append(message.text)
		hw.get('date').get(Date[0]).update({Date[1]: hw2})
		write(hw, 'homework.json')
	except:
		bot.send_message(chat_id=message.chat.id,
							 text="Что-то сработало неправильно")
		Date = []

def printhw(date1, date2, call):
	hw = read('homework.json')
	homework = ""
	for i in range(len(hw.get('date').get(date1).keys())):
		hw1 = list(hw.get('date').get(date1))
		homework += hw1[i] + ' :\n'
		for j in range(len(hw.get('date').get(date1).get(list(hw.get('date').get(date1).keys())[i]))):
			hw1 = list(hw.get('date').get(date1).get(list(hw.get('date').get(date1).keys())[i]))
			homework += str(hw1[j]) + '\n'
		homework += '\n'
	bot.send_message(
			chat_id=call.from_user.id,
			text=homework
        )

def actions():
	actions = types.InlineKeyboardMarkup()
	btn_add = types.InlineKeyboardButton(text="Добавить ДЗ", callback_data="add")
	actions.add(btn_add)
	btn_remove = types.InlineKeyboardButton(text="Удалить ДЗ(урок)", callback_data="remove")
	actions.add(btn_remove)
	btn_removed = types.InlineKeyboardButton(text="удалить ДЗ(день)", callback_data="removed")
	actions.add(btn_removed)
	btn_change = types.InlineKeyboardButton(text="Изменить ДЗ", callback_data="change")
	actions.add(btn_change)
	close = InlineKeyboardButton(text='Отмена',
						  	callback_data='cancel')
	actions.add(close)
	return actions

def subject1():
	subjects = InlineKeyboardMarkup()
	rus = InlineKeyboardButton(text=subject[0],
						  callback_data=subject_keys[0])
	lit = InlineKeyboardButton(text=subject[1],
						  callback_data=subject_keys[1])
	fre = InlineKeyboardButton(text=subject[2],
						  callback_data=subject_keys[2])
	deu = InlineKeyboardButton(text=subject[3],
						  callback_data=subject_keys[3])
	eng = InlineKeyboardButton(text=subject[4],
						  callback_data=subject_keys[4])
	phy = InlineKeyboardButton(text=subject[5],
						  callback_data=subject_keys[5])
	lsf = InlineKeyboardButton(text=subject[6],
						  callback_data=subject_keys[6])
	bio = InlineKeyboardButton(text=subject[7],
						  callback_data=subject_keys[7])
	inf = InlineKeyboardButton(text=subject[8],
						  callback_data=subject_keys[8])
	sto = InlineKeyboardButton(text=subject[9],
						  callback_data=subject_keys[9])
	alg = InlineKeyboardButton(text=subject[10],
						  callback_data=subject_keys[10])
	geo = InlineKeyboardButton(text=subject[11],
						  callback_data=subject_keys[11])
	soc = InlineKeyboardButton(text=subject[12],
						  callback_data=subject_keys[12])
	geog = InlineKeyboardButton(text=subject[13],
						  callback_data=subject_keys[13])
	che = InlineKeyboardButton(text=subject[14],
						  callback_data=subject_keys[14])
	cla = InlineKeyboardButton(text=subject[15],
						  callback_data=subject_keys[15])
	addi = InlineKeyboardButton(text=subject[16],
						  callback_data=subject_keys[16])
	eng2 = InlineKeyboardButton(text=subject[17],
						  callback_data=subject_keys[17])
	close = InlineKeyboardButton(text='Отмена',
						  	callback_data='cancel')
	subjects.add(rus)
	subjects.add(lit)
	subjects.add(fre)
	subjects.add(deu)
	subjects.add(eng)
	subjects.add(phy)
	subjects.add(lsf)
	subjects.add(bio)
	subjects.add(inf)
	subjects.add(sto)
	subjects.add(alg)
	subjects.add(geo)
	subjects.add(soc)
	subjects.add(geog)
	subjects.add(che)
	subjects.add(cla)
	subjects.add(addi)
	subjects.add(eng2)
	subjects.add(close)
	return subjects

def subject2():
	subjects = InlineKeyboardMarkup()
	rus = InlineKeyboardButton(text=subject[0],
						  callback_data=subject_keys[17])
	lit = InlineKeyboardButton(text=subject[1],
						  callback_data=subject_keys[18])
	fre = InlineKeyboardButton(text=subject[2],
						  callback_data=subject_keys[19])
	deu = InlineKeyboardButton(text=subject[3],
						  callback_data=subject_keys[20])
	eng = InlineKeyboardButton(text=subject[4],
						  callback_data=subject_keys[21])
	phy = InlineKeyboardButton(text=subject[5],
						  callback_data=subject_keys[22])
	lsf = InlineKeyboardButton(text=subject[6],
						  callback_data=subject_keys[23])
	bio = InlineKeyboardButton(text=subject[7],
						  callback_data=subject_keys[24])
	inf = InlineKeyboardButton(text=subject[8],
						  callback_data=subject_keys[25])
	sto = InlineKeyboardButton(text=subject[9],
						  callback_data=subject_keys[26])
	alg = InlineKeyboardButton(text=subject[10],
						  callback_data=subject_keys[27])
	geo = InlineKeyboardButton(text=subject[11],
						  callback_data=subject_keys[28])
	soc = InlineKeyboardButton(text=subject[12],
						  callback_data=subject_keys[29])
	geog = InlineKeyboardButton(text=subject[13],
						  callback_data=subject_keys[30])
	che = InlineKeyboardButton(text=subject[14],
						  callback_data=subject_keys[31])
	cla = InlineKeyboardButton(text=subject[15],
						  callback_data=subject_keys[32])
	addi = InlineKeyboardButton(text=subject[16],
						  callback_data=subject_keys[33])
	eng2 = InlineKeyboardButton(text=subject[17],
						  callback_data=subject_keys[34])
	close = InlineKeyboardButton(text='Отмена',
						  	callback_data='cancel')
	subjects.add(rus)
	subjects.add(lit)
	subjects.add(fre)
	subjects.add(deu)
	subjects.add(eng)
	subjects.add(phy)
	subjects.add(lsf)
	subjects.add(bio)
	subjects.add(inf)
	subjects.add(sto)
	subjects.add(alg)
	subjects.add(geo)
	subjects.add(soc)
	subjects.add(geog)
	subjects.add(che)
	subjects.add(cla)
	subjects.add(addi)
	subjects.add(eng2)
	subjects.add(close)
	return subjects

def subject3(message):
	subjects = InlineKeyboardMarkup()
	rus = InlineKeyboardButton(text=subject[0],
						  callback_data=subject_keys[34])
	lit = InlineKeyboardButton(text=subject[1],
						  callback_data=subject_keys[35])
	fre = InlineKeyboardButton(text=subject[2],
						  callback_data=subject_keys[36])
	deu = InlineKeyboardButton(text=subject[3],
						  callback_data=subject_keys[37])
	eng = InlineKeyboardButton(text=subject[4],
						  callback_data=subject_keys[38])
	phy = InlineKeyboardButton(text=subject[5],
						  callback_data=subject_keys[39])
	lsf = InlineKeyboardButton(text=subject[6],
						  callback_data=subject_keys[40])
	bio = InlineKeyboardButton(text=subject[7],
						  callback_data=subject_keys[41])
	inf = InlineKeyboardButton(text=subject[8],
						  callback_data=subject_keys[42])
	sto = InlineKeyboardButton(text=subject[9],
						  callback_data=subject_keys[43])
	alg = InlineKeyboardButton(text=subject[10],
						  callback_data=subject_keys[44])
	geo = InlineKeyboardButton(text=subject[11],
						  callback_data=subject_keys[45])
	soc = InlineKeyboardButton(text=subject[12],
						  callback_data=subject_keys[46])
	geog = InlineKeyboardButton(text=subject[13],
						  callback_data=subject_keys[47])
	che = InlineKeyboardButton(text=subject[14],
						  callback_data=subject_keys[48])
	cla = InlineKeyboardButton(text=subject[15],
						  callback_data=subject_keys[49])
	addi = InlineKeyboardButton(text=subject[16],
						  callback_data=subject_keys[50])
	eng2 = InlineKeyboardButton(text=subject[17],
						  callback_data=subject_keys[51])
	close = InlineKeyboardButton(text='Отмена',
						  	callback_data='cancel')
	subjects.add(rus)
	subjects.add(lit)
	subjects.add(fre)
	subjects.add(deu)
	subjects.add(eng)
	subjects.add(phy)
	subjects.add(lsf)
	subjects.add(bio)
	subjects.add(inf)
	subjects.add(sto)
	subjects.add(alg)
	subjects.add(geo)
	subjects.add(soc)
	subjects.add(geog)
	subjects.add(che)
	subjects.add(cla)
	subjects.add(addi)
	subjects.add(eng2)
	subjects.add(close)
	return subjects

def subject4():
	subjects = InlineKeyboardMarkup()
	rus = InlineKeyboardButton(text=subject[0],
						  callback_data=subject_keys[51])
	lit = InlineKeyboardButton(text=subject[1],
						  callback_data=subject_keys[52])
	fre = InlineKeyboardButton(text=subject[2],
						  callback_data=subject_keys[53])
	deu = InlineKeyboardButton(text=subject[3],
						  callback_data=subject_keys[54])
	eng = InlineKeyboardButton(text=subject[4],
						  callback_data=subject_keys[55])
	phy = InlineKeyboardButton(text=subject[5],
						  callback_data=subject_keys[56])
	lsf = InlineKeyboardButton(text=subject[6],
						  callback_data=subject_keys[57])
	bio = InlineKeyboardButton(text=subject[7],
						  callback_data=subject_keys[58])
	inf = InlineKeyboardButton(text=subject[8],
						  callback_data=subject_keys[59])
	sto = InlineKeyboardButton(text=subject[9],
						  callback_data=subject_keys[60])
	alg = InlineKeyboardButton(text=subject[10],
						  callback_data=subject_keys[61])
	geo = InlineKeyboardButton(text=subject[11],
						  callback_data=subject_keys[62])
	soc = InlineKeyboardButton(text=subject[12],
						  callback_data=subject_keys[63])
	geog = InlineKeyboardButton(text=subject[13],
						  callback_data=subject_keys[64])
	che = InlineKeyboardButton(text=subject[14],
						  callback_data=subject_keys[65])
	cla = InlineKeyboardButton(text=subject[15],
						  callback_data=subject_keys[66])
	addi = InlineKeyboardButton(text=subject[16],
						  callback_data=subject_keys[67])
	eng2 = InlineKeyboardButton(text=subject[17],
						  callback_data=subject_keys[68])
	close = InlineKeyboardButton(text='Отмена',
						  	callback_data='cancel')
	subjects.add(rus)
	subjects.add(lit)
	subjects.add(fre)
	subjects.add(deu)
	subjects.add(eng)
	subjects.add(phy)
	subjects.add(lsf)
	subjects.add(bio)
	subjects.add(inf)
	subjects.add(sto)
	subjects.add(alg)
	subjects.add(geo)
	subjects.add(soc)
	subjects.add(geog)
	subjects.add(che)
	subjects.add(cla)
	subjects.add(addi)
	subjects.add(eng2)
	subjects.add(close)
	return subjects

def subject5():
	subjects = InlineKeyboardMarkup()
	rus = InlineKeyboardButton(text=subject[0],
						  callback_data=subject_keys[68])
	lit = InlineKeyboardButton(text=subject[1],
						  callback_data=subject_keys[69])
	fre = InlineKeyboardButton(text=subject[2],
						  callback_data=subject_keys[70])
	deu = InlineKeyboardButton(text=subject[3],
						  callback_data=subject_keys[71])
	eng = InlineKeyboardButton(text=subject[4],
						  callback_data=subject_keys[72])
	phy = InlineKeyboardButton(text=subject[5],
						  callback_data=subject_keys[73])
	lsf = InlineKeyboardButton(text=subject[6],
						  callback_data=subject_keys[74])
	bio = InlineKeyboardButton(text=subject[7],
						  callback_data=subject_keys[75])
	inf = InlineKeyboardButton(text=subject[8],
						  callback_data=subject_keys[76])
	sto = InlineKeyboardButton(text=subject[9],
						  callback_data=subject_keys[77])
	alg = InlineKeyboardButton(text=subject[10],
						  callback_data=subject_keys[78])
	geo = InlineKeyboardButton(text=subject[11],
						  callback_data=subject_keys[79])
	soc = InlineKeyboardButton(text=subject[12],
						  callback_data=subject_keys[80])
	geog = InlineKeyboardButton(text=subject[13],
						  callback_data=subject_keys[81])
	che = InlineKeyboardButton(text=subject[14],
						  callback_data=subject_keys[82])
	cla = InlineKeyboardButton(text=subject[15],
						  callback_data=subject_keys[83])
	addi = InlineKeyboardButton(text=subject[16],
						  callback_data=subject_keys[84])
	eng2 = InlineKeyboardButton(text=subject[17],
						  callback_data=subject_keys[85])
	close = InlineKeyboardButton(text='Отмена',
						  	callback_data='cancel')
	subjects.add(rus)
	subjects.add(lit)
	subjects.add(fre)
	subjects.add(deu)
	subjects.add(eng)
	subjects.add(phy)
	subjects.add(lsf)
	subjects.add(bio)
	subjects.add(inf)
	subjects.add(sto)
	subjects.add(alg)
	subjects.add(geo)
	subjects.add(soc)
	subjects.add(geog)
	subjects.add(che)
	subjects.add(cla)
	subjects.add(addi)
	subjects.add(eng2)
	subjects.add(close)
	return subjects

def cancel():
	global Date
	cancel = InlineKeyboardMarkup()
	close = InlineKeyboardButton(text='Отмена',
						  	callback_data='cancel')
	cancel.add(close)
	return cancel

bot = telebot.TeleBot(token)
print('bot is online!')
calendar = Calendar(language=RUSSIAN_LANGUAGE)
calendar_1_callback = CallbackData("calendar_1", "action", "year", "month",
                                   "day")
calendar_2_callback = CallbackData("calendar_2", "action", "year", "month",
                                   "day")


@bot.callback_query_handler(
    func=lambda call: call.data.startswith(calendar_1_callback.prefix))
def callback_inline(call: CallbackQuery):
	name, action, year, month, day = call.data.split(calendar_1_callback.sep)
	date = calendar.calendar_query_handler(bot=bot,
                                           call=call,
                                           name=name,
                                           action=action,
                                           year=year,
                                           month=month,
                                           day=day)
	if action == "DAY":
		bot.send_message(
		    chat_id=call.from_user.id,
		    text=f"Домашнее задание на {date.strftime('%d.%m.%Y')}")
		date1=date.strftime('%d.%m.%y')
		date2=date.strftime('%A')
		try:
			printhw(date1, date2, call)
		except: 
			bot.send_message(
		    chat_id=call.from_user.id,
		    text=f"Домашнего задания нет",
		)


	elif action == "CANCEL":
		bot.send_message(
			chat_id=call.from_user.id,
			text="Вы отменили выбор"
        )

@bot.callback_query_handler(
    func=lambda call: call.data.startswith(calendar_2_callback.prefix))
def callback_inline(call: CallbackQuery):
	name, action, year, month, day = call.data.split(calendar_2_callback.sep)
	date = calendar.calendar_query_handler(bot=bot,
                                           call=call,
                                           name=name,
                                           action=action,
                                           year=year,
                                           month=month,
                                           day=day)
	if action == "DAY":
		global Date
		bot.send_message(
		    chat_id=call.from_user.id,
		    text="Выберите предмет:",
		    reply_markup=actions(),
		)
		date1=date.strftime('%d.%m.%y')
		Date = []
		Date.append(date1)
		# print(Date)

		
	elif action == "CANCEL":
		bot.send_message(
			chat_id=call.from_user.id,
			text="Вы отменили выбор")

		
@bot.message_handler(commands=['help', 'start'])
def check_other_messages(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn1 = types.KeyboardButton("Получить дз")
	btn2 = types.KeyboardButton("Записать дз")
	markup.add(btn1, btn2)
	bot.send_message(
		message.from_user.id,
		text="""Я умею записывать, присылать и редактировать домашние задания. 
  Для просмотра задания напишите /дз, /hw или нажмите(или напишите) "Получить дз".
  Для записи задания напишите /writer или нажмите(или напишите) "Записать дз".
""", 	reply_markup=markup)


@bot.message_handler(commands=['btn'])
def check_other_messages(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn1 = types.KeyboardButton("Получить дз")
	btn2 = types.KeyboardButton("Записать дз")
	markup.add(btn1, btn2)
	bot.send_message(
		message.from_user.id,
		text="Кнопки появились", 	
		reply_markup=markup)
	

@bot.message_handler(commands=['id'])
def print_id(message):
	print(message.chat.id, ' ', message.from_user.id, ' ', message.from_user.username)


@bot.message_handler(commands=['дз', 'hw'])
def check_other_messages(message):
	now = datetime.datetime.now()
	bot.send_message(
	        message.from_user.id,
	        "Выберите день, на который вам нужно домашнее задание",
	        reply_markup=calendar.create_calendar(
	            name=calendar_1_callback.prefix,
	            year=now.year,
	            month=now.month,
	        )
	    )


@bot.message_handler(commands=['writer'])
def check_other_messages(message):
	global writers
	if str(message.from_user.id) in writers:
		now = datetime.datetime.now()
		bot.send_message(chat_id=message.from_user.id,
					 	text='Выберите дату:',
					 	reply_markup=calendar.create_calendar(
	            	name=calendar_2_callback.prefix,
	            	year=now.year,
	            	month=now.month,
					 	)
					 	)
	else:
		bot.send_message(chat_id=message.from_user.id,
					 	text="Вы не являетесь writer'ом")


@bot.message_handler(content_types=['text'])
def check_other_messages(message):
	if message.text == 'Получить дз':
		now = datetime.datetime.now()
		bot.send_message(
	        	message.from_user.id,
	        	"Выберите день, на который вам нужно домашнее задание",
	        	reply_markup=calendar.create_calendar(
	            	name=calendar_1_callback.prefix,
	            	year=now.year,
	            	month=now.month,
	        	)
	    	)
	if message.text == 'Записать дз':
		global writers
		if str(message.from_user.id) in writers:
			now = datetime.datetime.now()
			bot.send_message(chat_id=message.from_user.id,
					 		text='Выберите дату:',
					 		reply_markup=calendar.create_calendar(
	            		name=calendar_2_callback.prefix,
	            		year=now.year,
	            		month=now.month,
					 		)
					 		)
		else:
			bot.send_message(chat_id=message.from_user.id,
					 		text="Вы не являетесь writer'ом")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	if call.message:
		if call.data == "add":
			now = datetime.datetime.now()
			bot.edit_message_text(chat_id=call.message.chat.id,
							 message_id=call.message.message_id,
							 text="Выберите предмет:",
							 reply_markup=subject1())
			# print(Date)
		# if call.data == "addc":
		# 	now = datetime.datetime.now()
		# 	bot.edit_message_text(chat_id=call.message.chat.id,
		# 					 message_id=call.message.message_id,
		# 					 text="Выберите предмет:",
		# 					 reply_markup=subject2())
		if call.data == "remove":
			now = datetime.datetime.now()
			bot.edit_message_text(chat_id=call.message.chat.id,
							 message_id=call.message.message_id,
							 text="Выберите предмет:",
							 reply_markup=subject3(call.message))
		if call.data == "removed":
			now = datetime.datetime.now()
			bot.edit_message_text(chat_id=call.message.chat.id,
							 message_id=call.message.message_id,
							 text="Всё домашнее задание на этот день будет удалено",
								 )
			removed(call.message)
		if call.data == "change":
			now = datetime.datetime.now()
			bot.edit_message_text(chat_id=call.message.chat.id,
							 message_id=call.message.message_id,
							 text="Выберите предмет:",
							 reply_markup=subject5())
			
		if call.data == "rus1":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="Напишите задание:",
							 		reply_markup=cancel())
			Date.append(subject[0])
			bot.register_next_step_handler(call.message, add)
		if call.data == "lit1":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="Напишите задание:",
							 		reply_markup=cancel())
			Date.append(subject[1])
			bot.register_next_step_handler(call.message, add)
		if call.data == "fre1":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="Напишите задание:",
							 		reply_markup=cancel())
			Date.append(subject[2])
			bot.register_next_step_handler(call.message, add)
		if call.data == "deu1":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="Напишите задание:",
							 		reply_markup=cancel())
			Date.append(subject[3])
			bot.register_next_step_handler(call.message, add)
		if call.data == "eng1":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="Напишите задание:",
							 		reply_markup=cancel())
			Date.append(subject[4])
			bot.register_next_step_handler(call.message, add)
		if call.data == "eng21":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="Напишите задание:",
							 		reply_markup=cancel())
			Date.append(subject[17])
			bot.register_next_step_handler(call.message, add)
		if call.data == "phy1":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="Напишите задание:",
							 		reply_markup=cancel())
			Date.append(subject[5])
			bot.register_next_step_handler(call.message, add)
		if call.data == "lsf1":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="Напишите задание:",
							 		reply_markup=cancel())
			Date.append(subject[6])
			bot.register_next_step_handler(call.message, add)
		if call.data == "bio1":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="Напишите задание:",
							 		reply_markup=cancel())
			Date.append(subject[7])
			bot.register_next_step_handler(call.message, add)
		if call.data == "inf1":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="Напишите задание:",
							 		reply_markup=cancel())
			Date.append(subject[8])
			bot.register_next_step_handler(call.message, add)
		if call.data == "sto1":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="Напишите задание:",
							 		reply_markup=cancel())
			Date.append(subject[9])
			bot.register_next_step_handler(call.message, add)
		if call.data == "alg1":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="Напишите задание:",
							 		reply_markup=cancel())
			Date.append(subject[10])
			bot.register_next_step_handler(call.message, add)
		if call.data == "geo1":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="Напишите задание:",
							 		reply_markup=cancel())
			Date.append(subject[11])
			bot.register_next_step_handler(call.message, add)
		if call.data == "soc1":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="Напишите задание:",
							 		reply_markup=cancel())
			Date.append(subject[12])
			bot.register_next_step_handler(call.message, add)
		if call.data == "geog1":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="Напишите задание:",
							 		reply_markup=cancel())
			Date.append(subject[13])
			bot.register_next_step_handler(call.message, add)

		if call.data == "che1":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="Напишите задание:",
							 		reply_markup=cancel())
			Date.append(subject[14])
			bot.register_next_step_handler(call.message, add)
		if call.data == "cla1":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="Напишите задание:",
							 		reply_markup=cancel())
			Date.append(subject[15])
			bot.register_next_step_handler(call.message, add)
		if call.data == "addi1":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="Напишите задание:",
							 		reply_markup=cancel())
			Date.append(subject[16])
			bot.register_next_step_handler(call.message, add)
			
		if call.data == "rus3":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="урок будет удалён.")
			Date.append(subject[0])
			remove(call.message)
		if call.data == "lit3":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="урок будет удалён.")
			Date.append(subject[1])
			remove(call.message)
		if call.data == "fre3":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="урок будет удалён.")
			Date.append(subject[2])
			remove(call.message)
		if call.data == "deu3":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="урок будет удалён.")
			Date.append(subject[3])
			remove(call.message)
		if call.data == "eng3":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="урок будет удалён.")
			Date.append(subject[4])
			remove(call.message)
		if call.data == "eng23":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="Напишите задание:",
							 		reply_markup=cancel())
			Date.append(subject[17])
			remove(call.message)
		if call.data == "phy3":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="урок будет удалён.")
			Date.append(subject[5])
			remove(call.message)
		if call.data == "lsf3":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="урок будет удалён.")
			Date.append(subject[6])
			remove(call.message)
		if call.data == "bio3":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="урок будет удалён.")
			Date.append(subject[7])
			remove(call.message)
		if call.data == "inf3":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="урок будет удалён.")
			Date.append(subject[8])
			remove(call.message)
		if call.data == "sto3":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="урок будет удалён.")
			Date.append(subject[9])
			remove(call.message)
		if call.data == "alg3":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="урок будет удалён.")
			Date.append(subject[10])
			remove(call.message)
		if call.data == "geo3":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="урок будет удалён.")
			Date.append(subject[11])
			remove(call.message)
		if call.data == "soc3":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="урок будет удалён.")
			Date.append(subject[12])
			remove(call.message)
		if call.data == "geog3":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="урок будет удалён.")
			Date.append(subject[13])
			remove(call.message)
		if call.data == "che3":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="урок будет удалён.")
			Date.append(subject[14])
			remove(call.message)
		if call.data == "cla3":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="урок будет удалён.")
			Date.append(subject[15])
			remove(call.message)
		if	 call.data == "addi3":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="урок будет удалён.")
			Date.append(subject[16])
			remove(call.message)

		if call.data == "rus5":
			bot.edit_message_text(chat_id=call.message.chat.id,
									message_id=call.message.message_id,
									text="Напишите задание:",
									reply_markup=cancel())
			Date.append(subject[0])
			bot.register_next_step_handler(call.message, change)
		if call.data == "lit5":
			bot.edit_message_text(chat_id=call.message.chat.id,
									message_id=call.message.message_id,
									text="Напишите задание:",
									reply_markup=cancel())
			Date.append(subject[1])
			bot.register_next_step_handler(call.message, change)
		if call.data == "fre5":
			bot.edit_message_text(chat_id=call.message.chat.id,
									message_id=call.message.message_id,
									text="Напишите задание:",
									reply_markup=cancel())
			Date.append(subject[2])
			bot.register_next_step_handler(call.message, change)
		if call.data == "deu5":
			bot.edit_message_text(chat_id=call.message.chat.id,
									message_id=call.message.message_id,
									text="Напишите задание:",
									reply_markup=cancel())
			Date.append(subject[3])
			bot.register_next_step_handler(call.message, change)
		if call.data == "eng5":
			bot.edit_message_text(chat_id=call.message.chat.id,
									message_id=call.message.message_id,
									text="Напишите задание:",
									reply_markup=cancel())
			Date.append(subject[4])
			bot.register_next_step_handler(call.message, change)
		if call.data == "eng25":
			bot.edit_message_text(chat_id=call.message.chat.id,
							 		message_id=call.message.message_id,
							 		text="Напишите задание:",
							 		reply_markup=cancel())
			Date.append(subject[17])
			bot.register_next_step_handler(call.message, change)
		if call.data == "phy5":
			bot.edit_message_text(chat_id=call.message.chat.id,
									message_id=call.message.message_id,
									text="Напишите задание:",
									reply_markup=cancel())
			Date.append(subject[5])
			bot.register_next_step_handler(call.message, change)
		if call.data == "lsf5":
			bot.edit_message_text(chat_id=call.message.chat.id,
									message_id=call.message.message_id,
									text="Напишите задание:",
									reply_markup=cancel())
			Date.append(subject[3])
			bot.register_next_step_handler(call.message, change)
		if call.data == "bio5":
			bot.edit_message_text(chat_id=call.message.chat.id,
									message_id=call.message.message_id,
									text="Напишите задание:",
									reply_markup=cancel())
			Date.append(subject[7])
			bot.register_next_step_handler(call.message, change)
		if call.data == "inf5":
			bot.edit_message_text(chat_id=call.message.chat.id,
									message_id=call.message.message_id,
									text="Напишите задание:",
									reply_markup=cancel())
			Date.append(subject[8])
			bot.register_next_step_handler(call.message, change)
		if call.data == "sto5":
			bot.edit_message_text(chat_id=call.message.chat.id,
									message_id=call.message.message_id,
									text="Напишите задание:",
									reply_markup=cancel())
			Date.append(subject[9])
			bot.register_next_step_handler(call.message, change)
		if call.data == "alg5":
			bot.edit_message_text(chat_id=call.message.chat.id,
									message_id=call.message.message_id,
									text="Напишите задание:",
									reply_markup=cancel())
			Date.append(subject[10])
			bot.register_next_step_handler(call.message, change)
		if call.data == "geo5":
			bot.edit_message_text(chat_id=call.message.chat.id,
									message_id=call.message.message_id,
									text="Напишите задание:",
									reply_markup=cancel())
			Date.append(subject[11])
			bot.register_next_step_handler(call.message, change)
		if call.data == "soc5":
			bot.edit_message_text(chat_id=call.message.chat.id,
									message_id=call.message.message_id,
									text="Напишите задание:",
									reply_markup=cancel())
			Date.append(subject[12])
			bot.register_next_step_handler(call.message, cnahge)
		if call.data == "geog5":
			bot.edit_message_text(chat_id=call.message.chat.id,
								  	message_id=call.message.message_id,
								  	text="Напишите задание:",
								  	reply_markup=cancel())
			Date.append(subject[13])
			bot.register_next_step_handler(call.message, change)

		if call.data == "che5":
			bot.edit_message_text(chat_id=call.message.chat.id,
									message_id=call.message.message_id,
									text="Напишите задание:",
									reply_markup=cancel())
			Date.append(subject[14])
			bot.register_next_step_handler(call.message, change)
		if call.data == "cla5":
			bot.edit_message_text(chat_id=call.message.chat.id,
									message_id=call.message.message_id,
									text="Напишите задание:",
									reply_markup=cancel())
			Date.append(subject[15])
			bot.register_next_step_handler(call.message, change)
		if call.data == "addi5":
			bot.edit_message_text(chat_id=call.message.chat.id,
									message_id=call.message.message_id,
								  	text="Напишите задание:",
								  	reply_markup=cancel())
			Date.append(subject[16])
			bot.register_next_step_handler(call.message, change)
			
		if call.data == "cancel":
			bot.edit_message_text(chat_id=call.message.chat.id, 
								  message_id=call.message.message_id, 			
								  text='Вы отменили выбор.')
			bot.clear_step_handler_by_chat_id(chat_id=call.message.chat.id)

keep_alive.keep_alive()
bot.infinity_polling()
