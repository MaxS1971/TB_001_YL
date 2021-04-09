from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler

from wiki import search_wiki

TOKEN = "1709676171:AAEzL1wnNTazuSeGCVv1Tu0IkfGLs5Q46dI"

def start(update, context):
    update.message.reply_text(
        "Привет! Я эхо-бот. Напишите мне что-нибудь, и я пришлю это назад!")


def help(update, context):
    update.message.reply_text(
        "/start  -  начало работы\n/help - вызов помощи")

def wikip(update, context):
    print(update.message['chat']['first_name']," запросил: ", context.args)

    poisk = ' '.join(context.args).strip()
    result = "Проверьте введенное слово"
    if poisk:
        result = search_wiki(poisk)
        if not result:
            result = "Проверьте введенное слово"
    update.message.reply_text(result)


# Определяем функцию-обработчик сообщений.
# У неё два параметра, сам бот и класс updater, принявший сообщение.
def echo(update, context):
    # У объекта класса Updater есть поле message,
    # являющееся объектом сообщения.
    # У message есть поле text, содержащее текст полученного сообщения,
    # а также метод reply_text(str),
    # отсылающий ответ пользователю, от которого получено сообщение.
    print(update.message['chat']['first_name'])
    name = update.message['chat']['first_name']
    txt = update.message.text
    if txt.lower() in ['привет', 'здравствуй']:
        txt = f"И тебе привет {name}!"
    update.message.reply_text(txt)


def main():
    print("Бот запущен ...")
    # Создаём объект updater.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен
    updater = Updater(TOKEN, use_context=True)

    # Получаем из него диспетчер сообщений.
    dp = updater.dispatcher


    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("wiki", wikip))
    # Регистрируем обработчик в диспетчере.
    dp.add_handler(MessageHandler(Filters.text, echo))
    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()

    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()