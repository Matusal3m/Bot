import telebot


codbot="6028892799:AAFiKNAdqTzqcRHXcqdoPlykDx1k255fTaU"

bot= telebot.TeleBot(codbot)

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def chat():
    bot.reply_backend(mensagem, "não")
    
bot.polling()