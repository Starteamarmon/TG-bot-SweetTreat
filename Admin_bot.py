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

caramel_filling_markup = InlineKeyboardMarkup(ccaramel_filling)
ccaramel_filling = [
    [
        InlineKeyboardButton('Карамель',callback_data='cramel_filling_ok')
    ],
    [
        InlineKeyboardButton('Карамель-арахис',callback_data='caramel_peanuts')
    ],
    [
        InlineKeyboardButton('Карамель-грецкий орех',callback_data='caramel_walnut')
    ],
    [
        InlineKeyboardButton('Карамель-банан',callback_data='caramel_banana')
    ]
]