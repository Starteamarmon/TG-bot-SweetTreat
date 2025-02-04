# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, CallbackQueryHandler
# import asyncio


# TOKEN = '8167854262:AAGbkPb2VRKPjScGKs-7B9TB_hVMmaEavGI'
# cake_creator_id = 845963398

# async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(update.message.text)


# def main():
#     application = ApplicationBuilder().token(TOKEN).build()
#     echo_handler = MessageHandler(None,echo)

#     application.add_handler(echo_handler)
#     application.run_polling()
# if __name__ == '__main__':
#     main()

ganache_filling = [
    [
        InlineKeyboardButton('Ганаш на белом шоколаде',callback_data='ganache_filling_white')
    ],
    [
        InlineKeyboardButton('Ганаш на молочном шоколаде',callback_data='ganache_filling_milk')
    ],
    [
        InlineKeyboardButton('Ганаш на тёмном шоколаде',callback_data='ganache_filling_black')
    ],