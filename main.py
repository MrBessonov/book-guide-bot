import books_dict
import books_soup
import logging
import os
import telebot
from books_buttons import *
from flask import Flask, request
from jinja2 import Template

b_token = os.getenv('BOT_TOKEN')
b_url = os.getenv('BOT_URL')
bot = telebot.TeleBot(token=b_token)

server = Flask(__name__)

msg = Template("Рекомендую {{p['title']}}. Автор {{p['author']}}.\nСредняя оценка на fantlab.ru: {{p['mark']}}.\nАннотация: {{p['annotation']}}")


def recomendation(message):
    return msg.render(p=books_soup.book_info)


def bot_mess_com(message):
    books_soup.soup_func(message, book_type="e-graph")
    bot.send_message(message.chat.id, recomendation(message))
    bot.send_photo(message.chat.id, photo=books_soup.book_info['cover'])


def bot_mess_book(message):
    books_soup.soup_func(message)
    bot.send_message(message.chat.id, recomendation(message))
    bot.send_photo(message.chat.id, photo=books_soup.book_info['cover'])


@bot.message_handler(commands=['start'])
def start(message):
    username = message.from_user.username
    send_mess = f"Привет, {username}! Я помогу тебе выбрать книгу!"
    bot.send_message(message.chat.id, send_mess, reply_markup=start_markup)


@bot.message_handler(func=lambda message: message.text == 'Начать с начала')
def start2(message):
    final_message = 'Давай заново.'
    bot.send_message(message.chat.id, final_message, reply_markup=start_markup)


@bot.message_handler(func=lambda message: message.text == "Комикс")
def comic(message):
    final_message = "Выбери направление."
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=comic_markup)


@bot.message_handler(func=lambda message: message.text == "Обратно к выбору направления")
def comic(message):
    final_message = "Выбери направление."
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=comic_markup)


@bot.message_handler(func=lambda message: message.text == "Постмодернизм")
def comic1(message):
    final_message = "Постмодернизм о..."
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=comic_post_markup)


@bot.message_handler(func=lambda message: message.text == "Мистика")
def comic2(message):
    final_message = "Есть отличные варианты:"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=comic_mist_markup)


@bot.message_handler(func=lambda message: message.text == "Странное будущее")
def comic3(message):
    final_message = "Есть отличные варианты:"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=comic_fut_markup)


@bot.message_handler(func=lambda message: message.text == "Хоррор")
def horror(message):
    final_message = "Кого будешь бояться?"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=horror_markup)


@bot.message_handler(func=lambda message: message.text == "Обратно к выбору существ")
def horror(message):
    final_message = "Кого будешь бояться?"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=horror_markup)


@bot.message_handler(func=lambda message: message.text == "Вампиры")
def horror1(message):
    final_message = "Какую историю предпочтёшь?"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=horror_1_markup)


@bot.message_handler(func=lambda message: message.text == "Зомби и что-то вроде")
def horror2(message):
    final_message = "Хочешь масштабную историю? Или отдашь предпочтение одинокому выживанию? Или может лучше драму?"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=horror_2_markup)


@bot.message_handler(func=lambda message: message.text == "Оборотни")
def horror3(message):
    final_message = "Оборотни в..."
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=horror_3_markup)


@bot.message_handler(func=lambda message: message.text == "Призраки")
def horror4(message):
    final_message = "На что обратишь внимание?"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=horror_4_markup)


@bot.message_handler(func=lambda message: message.text == "Боги и демоны")
def horror5(message):
    final_message = "Какой поджанр больше нравится?"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=horror_5_markup)


@bot.message_handler(func=lambda message: message.text == "Смесь жанров")
def fanscifi(message):
    final_message = "Действие должно развиваться в прошлом или будущем?"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=fanscifi_markup)


@bot.message_handler(func=lambda message: message.text == "Прошлое")
def fanscifi_1(message):
    final_message = "Нравятся монстры?"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=fanscifi_1_markup)


@bot.message_handler(func=lambda message: message.text == "Будущее")
def fanscifi_2(message):
    final_message = "Нравится математика?"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=fanscifi_2_markup)


@bot.message_handler(func=lambda message: message.text == "Неа")
def fanscifi_2_2(message):
    final_message = "Тогда, что интереснее: умирающее Солнце или демон из шипов и лезвий?"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=fanscifi_2_2_markup)


@bot.message_handler(func=lambda message: message.text == "Другое")
def other(message):
    final_message = "Как насчёт трагедии?"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=other_markup)


@bot.message_handler(func=lambda message: message.text == "Можно")
def other_1(message):
    final_message = "Любовь или преодоление несправедливости?"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=other_love_markup)


@bot.message_handler(func=lambda message: message.text == "Да ну")
def other_2(message):
    final_message = "Как насчёт мозговыноса?"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=other_postmodern_markup)


@bot.message_handler(func=lambda message: message.text == "Мозговынос")
def other_brain(message):
    final_message = "А путешествия во времени надо?"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=other_brain_markup)


@bot.message_handler(func=lambda message: message.text == "Что-то попроще")
def other_easier(message):
    final_message = "Антиутопию хочешь?"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=other_easier_markup)


@bot.message_handler(func=lambda message: message.text == "Антиутопия")
def other_dys(message):
    final_message = "Выбери направление:"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=other_dys_markup)


@bot.message_handler(func=lambda message: message.text == "Фэнтези")
def fantasy(message):
    final_message = "Хочешь что-то похожее на 'Гарри Поттера?'"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=fantasy_markup)


@bot.message_handler(func=lambda message: message.text == "Непохожее")
def fantasy_new(message):
    final_message = "Вы новичок в фэнтези?"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=fantasy_new_markup)


@bot.message_handler(func=lambda message: message.text == "Нет, конечно")
def fantasy_artur(message):
    final_message = "Кто твой любимый персонаж из историй о короле Артуре?"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=fantasy_artur_markup)


@bot.message_handler(func=lambda message: message.text == "Не люблю Артуриану")
def fantasy_modset(message):
    final_message = "Современный сеттинг подойдёт?"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=fantasy_modset_markup)


@bot.message_handler(func=lambda message: message.text == "Да, конечно")
def fantasy_gods(message):
    final_message = "Сделай выбор:"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=fantasy_gods_markup)


@bot.message_handler(func=lambda message: message.text == "Только не вестерны")
def fantasy_dark(message):
    final_message = 'А как насчёт фэнтези про животных?'
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=fantasy_animals_markup)


@bot.message_handler(func=lambda message: message.text == "Не надо животных")
def fantasy_althis(message):
    final_message = 'Может хочешь альтернативную историю?'
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=fantasy_althis_markup)


@bot.message_handler(func=lambda message: message.text == "Не хочу")
def fantasy_series(message):
    final_message = 'Хорошо, подумай над этим:'
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=fantasy_series_markup)


@bot.message_handler(func=lambda message: message.text == "Не интересно")
def fantasy_withend(message):
    final_message = 'Ладно, переходим к циклам. Тебе важно, чтоб цикл был закончен?'
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=fantasy_withend_markup)


@bot.message_handler(func=lambda message: message.text == "Важно")
def fantasy_withend1(message):
    final_message = 'Начнем со стандартного:'
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=fantasy_standart_markup)


@bot.message_handler(func=lambda message: message.text == "Не важно")
def fantasy_withend2(message):
    final_message = 'Что-то возвышенное или более приземлённое?'
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=fantasy_pops_markup)


@bot.message_handler(func=lambda message: message.text == "Что-то нетривиальное")
def fantasy_trilogy(message):
    final_message = 'Давай поговорим о трилогиях. Могу посоветовать, например, трилогию...'
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=fantasy_trilogy_markup)


@bot.message_handler(func=lambda message: message.text == "Не надо трилогии")
def fantasy_more(message):
    final_message = 'Пять-шесть книг подойдёт?'
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=fantasy_more_markup)


@bot.message_handler(func=lambda message: message.text == "Мало")
def fantasy_greatevil(message):
    final_message = 'Есть шикарные многотомники. Выбери, что интереснее:'
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=fantasy_greatevil_markup)


@bot.message_handler(func=lambda message: message.text == "Научная фантастика")
def scifi(message):
    final_message = 'Сперва определимся с направлением:'
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=scifi_markup)


@bot.message_handler(func=lambda message: message.text == "Нырнём в киберпанк")
def scifi_cyber(message):
    final_message = 'Киберпанк с чем?'
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=scifi_cyber_markup)


@bot.message_handler(func=lambda message: message.text == "Останемся на Земле")
def scifi_earth(message):
    final_message = 'В глубь не хочешь?'
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=scifi_earth_markup)


@bot.message_handler(func=lambda message: message.text == "Поверхность лучше")
def scifi_science(message):
    final_message = 'Что тебя интересует?'
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=scifi_science_markup)


@bot.message_handler(func=lambda message: message.text == "Полетим в космос")
def scifi_space(message):
    final_message = 'Очень далеко?'
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=scifi_space_markup)


@bot.message_handler(func=lambda message: message.text == "Марс и чуть дальше")
def scifi_mars(message):
    final_message = 'Смотри, что больше нравится:'
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=scifi_mars_markup)


@bot.message_handler(func=lambda message: message.text == "Иные направления")
def scifi_dif(message):
    final_message = 'Тогда подумай над этим:'
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=scifi_dif_markup)


@bot.message_handler(func=lambda message: message.text == "Далеко-далеко")
def scifi_war(message):
    final_message = 'А там война?'
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=scifi_war_markup)


@bot.message_handler(func=lambda message: message.text == "Война!")
def scifi_enemy(message):
    final_message = 'А кого с кем?'
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=scifi_enemy_markup)


@bot.message_handler(func=lambda message: message.text == "Не надо войны")
def scifi_humor(message):
    final_message = 'Тогда что-то с юмором?'
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=scifi_humor_markup)


@bot.message_handler(func=lambda message: message.text == "Без юмора")
def scifi_contact(message):
    final_message = 'С упором на первый контакт с инопланетянами?'
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=scifi_contact_markup)


@bot.message_handler(func=lambda message: message.text == "С упором")
def scifi_alien(message):
    final_message = 'А какими инопланетянами?'
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=scifi_alien_markup)


@bot.message_handler(func=lambda message: message.text == "Без упора")
def scifi_last(message):
    final_message = 'Тогда выберете, что больше нравится?'
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=scifi_last_markup)


@bot.message_handler()
def book_rec(message):
    if message.text in books_dict.books_list[:6]:
        bot_mess_com(message)
    elif message.text == "Совсем нет":
        books_soup.soup_func(message)
        bot.send_message(message.chat.id, recomendation(message))
        bot.send_photo(message.chat.id, photo=books_soup.book_info['cover'], reply_markup=fantasy_dark_markup)
    else:
        bot_mess_book(message)


@server.route('/' + b_token, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=b_url + b_token)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
