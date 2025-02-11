from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, CallbackQueryHandler
import asyncio
from tortoise import Tortoise, run_async
from models import User, Order


TOKEN = '7287431498:AAEVkzhrn3xjTOj-Q-WFo1qBzDoNlZMgmaM'
cake_creator_id =  845963398


start_key = [['/start']]
reply_markup = ReplyKeyboardMarkup(start_key, resize_keyboard=True, one_time_keyboard=True)


first_level_keyboard = [
    [
        InlineKeyboardButton('Мои заказы', callback_data='user_orders')
    ],
    [
        InlineKeyboardButton("Хочу выбрать 🎂", callback_data='choose_cake'),
        InlineKeyboardButton("Собрать 🍰", callback_data='build_cake'),
    ],
]
first_level_reply_markup = InlineKeyboardMarkup(first_level_keyboard)


choose_cake_keyboard = [
    [
        InlineKeyboardButton("Шоколадный торт 🍫🍰", callback_data='chocolate_cake'),
        InlineKeyboardButton('Медовик 🍰🍯',callback_data='honey_cake')
    ],
    [
        InlineKeyboardButton('Красный бархат 🍒🍰', callback_data='red_cake'),
        InlineKeyboardButton('Абрикосовый 🍑🍰',callback_data='apricot_cake'),
    ],
    [
        InlineKeyboardButton('Ванильный торт 🎂',callback_data='vanilla_cake'),
        InlineKeyboardButton('Маковый торт⚫️🍋🍰',callback_data='poppy_sand_cake')
    ],
    [
    
         InlineKeyboardButton("Назад", callback_data='back_to_main')
    
    ]
]


choose_cake_reply_markup = InlineKeyboardMarkup(choose_cake_keyboard)
build_cake_keyboard = [
    [
        InlineKeyboardButton("Выбрать корж", callback_data='select_crust'),
        InlineKeyboardButton("Выбрать начинку", callback_data='select_filling'),
    ],
    [
        InlineKeyboardButton("Назад", callback_data='back_to_main'),
    ],
    [
        InlineKeyboardButton("Заказать ещё", callback_data='back_to_main'),
    ],
    [
        InlineKeyboardButton('Заказать',callback_data='weight_cake')
    ]
]


build_cake_base = [
    [
        InlineKeyboardButton('Ванильный',callback_data='vanilla_base')
    ],
    [
        InlineKeyboardButton('Шоколадный',callback_data='chocolate_base')
    ],
    [
        InlineKeyboardButton('Красный бархат',callback_data='red_velvet_base')
    ],
    [
        InlineKeyboardButton('Медовый',callback_data='honey_base')
    ],
    [
        InlineKeyboardButton('Маковый',callback_data='poppy_seed_base')
    ],
    [
        InlineKeyboardButton('Назад',callback_data='back_to_main')
    ],
]


cake_cream = [
    [
        InlineKeyboardButton('Сметанно-сливочный',callback_data='sour_cream')
    ],
    [
        InlineKeyboardButton('Творожно-сливочный(крем-чиз)',callback_data='cream_cheese')
    ],
    [
        InlineKeyboardButton('Ганаш с молочныйм шоколадом',callback_data='Milk_Chocolate_Ganache')
    ],
    [
        InlineKeyboardButton('Ганаш с белым шоколадом',callback_data='white_Chocolate_Ganache')
    ],
    [
        InlineKeyboardButton('Ганаш с темным шоколадом',callback_data='black_Chocolate_Ganache')
    ],
    [
        InlineKeyboardButton('Творожно-сливочный крем со сгущеным молоком',callback_data='sour_cream_2')
    ]
]


cake_filling = [
    [
        InlineKeyboardButton('Ягодная',callback_data='berry_filling')
    ],
     [
        InlineKeyboardButton('Муссовая',callback_data='mousse_filling')
    ],
    [
        InlineKeyboardButton('Ганаш',callback_data='ganache_filling')
    ],
    [
        InlineKeyboardButton('Карамель',callback_data='caramel_filling')
    ]
]
ccaramel_filling = [
    [
        InlineKeyboardButton('Карамель',callback_data='caramel_filling_ok')
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
berry_filling = [
    [
        InlineKeyboardButton('Малиновый конфитюр',callback_data='raspberry_jam')
    ],
    [
        InlineKeyboardButton('Клубничный конфитюр',callback_data='strawberry_jam')
    ],
    [
        InlineKeyboardButton('Вишневый конфитюр',callback_data='cherry_jam')
    ],
    [
        InlineKeyboardButton('Смородиновый конфитюр',callback_data='currant_Jam')
    ],
    [
        InlineKeyboardButton('Ягодный конфитюр(микс)',callback_data='mix_jam')
    ],
]

mousse_filling = [
    [
        InlineKeyboardButton('Шоколадный мусс',callback_data='chocolate_mousse')
    ],
    [
        InlineKeyboardButton('Карамельный мусс',callback_data='caramel_mousse')
    ],
    [
        InlineKeyboardButton('Ягодный мусс',callback_data='berry_mousse')
    ]
]


final_coating = [
    [
        InlineKeyboardButton('Ганаш на белом шоколаде',callback_data='final_coating_white_ganache')
    ],
    [
        InlineKeyboardButton('Ганаш на молочном шоколаде',callback_data='final_coating_milk_ganache')
    ],
    [
        InlineKeyboardButton('Крем-чиз',callback_data='final_cream_cheese')
    ],
]

chocolate_mousse = [
    [
        InlineKeyboardButton('Мусс на молочном шоколаде',callback_data='milk_chocolate_mousse')
    ],
    [
        InlineKeyboardButton('Мусс на белом шоколаде',callback_data='white_chocolate_mousse')
    ],
    [
        InlineKeyboardButton('Мусс на тёмном шоколаде',callback_data='black_chocolate_mousse')
    ],
]

berry_mousse = [
    [
        InlineKeyboardButton('Малина',callback_data='raspberry_mousse')
    ],
    [
        InlineKeyboardButton('Клубника',callback_data='strawberry_mousse')
    ],
    [
        InlineKeyboardButton('Вишня',callback_data='cerry_mousse')
    ],
    [
        InlineKeyboardButton('Cмородина',callback_data='currant_mousse')
    ],
    [
        InlineKeyboardButton('Cмесь ягод (микс)',callback_data='mix_mousse')
    ],
]

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
]
cake_build_final = [
    [
        InlineKeyboardButton('Да/Заказать',callback_data='YES')
    ],
    [
        InlineKeyboardButton('Нет/Главное меню',callback_data='back_to_main')
    ]
]
cake_final = [
    [
        InlineKeyboardButton('Да/Заказать',callback_data='yeap')
    ],
    [
        InlineKeyboardButton('Нет/Главное меню',callback_data='back_to_main')
    ]
]
cake_final_markup = InlineKeyboardMarkup(cake_final)
build_cake_reply_markup = InlineKeyboardMarkup(build_cake_keyboard)
mousse_filling_markup = InlineKeyboardMarkup(mousse_filling)
berry_filling_markup = InlineKeyboardMarkup(berry_filling)
cake_filling_markup = InlineKeyboardMarkup(cake_filling)
ganache_filling_markup = InlineKeyboardMarkup(ganache_filling)
caramel_filling_markup = InlineKeyboardMarkup(ccaramel_filling)
berry_mousse_markup = InlineKeyboardMarkup(berry_mousse)
chocolate_mousse_markup = InlineKeyboardMarkup(chocolate_mousse)
cake_cream_markup = InlineKeyboardMarkup(cake_cream)
build_cake_base_markup=InlineKeyboardMarkup(build_cake_base)
final_coating_markup = InlineKeyboardMarkup(final_coating)
cake_build_final_markup = InlineKeyboardMarkup(cake_build_final)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    try:
        user = await User.get(chat_id=chat_id)
        await update.message.reply_text(text=f'Привествуем вас, {user.name}!\nХодите выбрать торт или собрать?',reply_markup=first_level_reply_markup)
    except:
        await update.message.reply_text(text='Пожалуйста, введите ваше имя:')
        context.user_data['waiting_for_name']=True
        



async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    user = await User.get(chat_id=chat_id)
    query = update.callback_query
    await query.answer()

    if query.data == 'choose_cake':
        context.user_data['cake_name'] = {
            'торт': None,
            'вес': 0.0
        }
        await query.edit_message_text(text='Выберите торт:', reply_markup=choose_cake_reply_markup)
   
    elif query.data == "user_orders":
        user_orders = await Order.filter(user=user)
        
        await query.edit_message_text(text=f'{[str(order) for order in user_orders]}',reply_markup=InlineKeyboardMarkup([cake_final[-1]]))

    elif query.data == 'build_cake':
        context.user_data['cake_build'] = {
        'корж': None,
        'начинка': None,
        'крем': None,
        'покрытие': None,
        'вес': 0.0
        }
        await query.edit_message_text(text='Выберите корж:', reply_markup=build_cake_base_markup)
    
    elif query.data == 'vanilla_base':
        context.user_data['cake_build']['корж'] = "Ванильный"
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nВыберите крем:",reply_markup=cake_cream_markup)  
    elif query.data == 'red_velvet_base':
        context.user_data['cake_build']['корж'] = "Красный бархат"
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nВыберите крем:",reply_markup=cake_cream_markup)       
    elif query.data == 'honey_base':
        context.user_data['cake_build']['корж'] = "Медовый"
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nВыберите крем:",reply_markup=cake_cream_markup)         
    elif query.data == 'poppy_seed_base':
        context.user_data['cake_build']['корж'] = "Маковый"
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nВыберите крем:",reply_markup=cake_cream_markup) 
    elif query.data == 'chocolate_base':
        context.user_data['cake_build']['корж'] = "Шоколадный"
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nВыберите крем:",reply_markup=cake_cream_markup) 

    elif query.data == 'sour_cream':
        context.user_data['cake_build']['крем'] = 'Сметанно-сливочный'
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nВыберите начинку:",reply_markup=cake_filling_markup)           
    elif query.data == 'cream_cheese':
        context.user_data['cake_build']['крем'] = 'Творожно-сливочный(крем-чиз'
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nВыберите начинку:",reply_markup=cake_filling_markup)            
    elif query.data == 'Milk_Chocolate_Ganache':
        context.user_data['cake_build']['крем'] = 'Ганаш с молочныйм шоколадом'
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nВыберите начинку:",reply_markup=cake_filling_markup)             
    elif query.data == 'white_Chocolate_Ganache':
        context.user_data['cake_build']['крем'] = 'Ганаш с белым шоколадом'
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nВыберите начинку:",reply_markup=cake_filling_markup)     
    elif query.data == 'black_Chocolate_Ganache':
        context.user_data['cake_build']['крем'] = 'Ганаш с темным шоколадом'
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nВыберите начинку:",reply_markup=cake_filling_markup)          
    elif query.data == 'sour_cream_2':
        context.user_data['cake_build']['крем'] = 'Творожно-сливочный крем со сгущеным молоком'
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nВыберите начинку:",reply_markup=cake_filling_markup)
    
    elif query.data == 'mousse_filling':
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nВыберите начинку:",reply_markup=mousse_filling_markup)
    elif query.data == 'berry_filling':
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nВыберите начинку:",reply_markup=berry_filling_markup)
    elif query.data == 'chocolate_mousse':
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nВыберите начинку:", reply_markup=chocolate_mousse_markup)
    elif query.data == 'ganache_filling':
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nВыберите начинку:",reply_markup=ganache_filling_markup)
    elif query.data == 'caramel_filling':
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nВыберите начинку:",reply_markup=caramel_filling_markup)

    elif query.data == 'caramel_filling_ok':
        context.user_data['cake_build']['начинка'] = 'Карамель'
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nНачинка: {context.user_data['cake_build']['начинка']}\nВыберите финальное покрытие:",reply_markup=final_coating_markup)
    elif query.data == 'caramel_peanuts':
        context.user_data['cake_build']['начинка'] = 'Карамель-арахис'
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nНачинка: {context.user_data['cake_build']['начинка']}\nВыберите финальное покрытие:",reply_markup=final_coating_markup)
    elif query.data == 'caramel_walnut':
        context.user_data['cake_build']['начинка'] = 'Карамель-грецкий орех'
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nНачинка: {context.user_data['cake_build']['начинка']}\nВыберите финальное покрытие:",reply_markup=final_coating_markup)
    elif query.data == 'caramel_banana':
        context.user_data['cake_build']['начинка'] = 'Карамель-банан'
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nНачинка: {context.user_data['cake_build']['начинка']}\nВыберите финальное покрытие:",reply_markup=final_coating_markup)

    elif query.data == 'ganache_filling_white':
        context.user_data['cake_build']['начинка'] = 'Ганаш на белом шоколаде'
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nНачинка: {context.user_data['cake_build']['начинка']}\nВыберите финальное покрытие:",reply_markup=final_coating_markup)
    elif query.data == 'ganache_filling_milk':
        context.user_data['cake_build']['начинка'] = 'Ганаш на молочном шоколаде'
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nНачинка: {context.user_data['cake_build']['начинка']}\nВыберите финальное покрытие:",reply_markup=final_coating_markup)
    elif query.data == 'ganache_filling_black':
        context.user_data['cake_build']['начинка'] = 'Ганаш на тёмном шоколаде'
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nНачинка: {context.user_data['cake_build']['начинка']}\nВыберите финальное покрытие:",reply_markup=final_coating_markup)

    elif query.data == 'raspberry_jam':
        context.user_data['cake_build']['начинка'] = 'Малиновый конфитюр'
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nНачинка: {context.user_data['cake_build']['начинка']}\nВыберите финальное покрытие:",reply_markup=final_coating_markup)
    elif query.data == 'strawberry_jam':
        context.user_data['cake_build']['начинка'] = 'Клубничный конфитюр'
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nНачинка: {context.user_data['cake_build']['начинка']}\nВыберите финальное покрытие:",reply_markup=final_coating_markup)
    elif query.data == 'cherry_jam':
        context.user_data['cake_build']['начинка'] = 'Вишневый конфитюр'
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nНачинка: {context.user_data['cake_build']['начинка']}\nВыберите финальное покрытие:",reply_markup=final_coating_markup)
    elif query.data == 'currant_Jam':
        context.user_data['cake_build']['начинка'] = 'Смородиновый конфитюр'
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nНачинка: {context.user_data['cake_build']['начинка']}\nВыберите финальное покрытие:",reply_markup=final_coating_markup)
    elif query.data == 'mix_jam':
        context.user_data['cake_build']['начинка'] = 'Ягодный конфитюр(микс)'
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nНачинка: {context.user_data['cake_build']['начинка']}\nВыберите финальное покрытие:",reply_markup=final_coating_markup)    
    
    elif query.data == 'milk_chocolate_mousse':
        context.user_data['cake_build']['начинка'] = 'мусс на молочном шоколаде'
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nНачинка: {context.user_data['cake_build']['начинка']}\nВыберите финальное покрытие:",reply_markup=final_coating_markup)
    elif query.data == 'white_chocolate_mousse':
        context.user_data['cake_build']['начинка'] = 'мусс на белом шоколаде'
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nНачинка: {context.user_data['cake_build']['начинка']}\nВыберите финальное покрытие:",reply_markup=final_coating_markup)
    elif query.data == 'black_chocolate_mousse':
        context.user_data['cake_build']['начинка'] = 'мусс на тёмном шоколаде'
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nНачинка: {context.user_data['cake_build']['начинка']}\nВыберите финальное покрытие:",reply_markup=final_coating_markup)
    
    elif query.data == 'berry_mousse':
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nВыберите ягодный мусс:",reply_markup=berry_mousse_markup)
   
    elif query.data == 'raspberry_mousse':
        context.user_data['cake_build']['начинка'] = 'мусс: Малина'
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nНачинка: {context.user_data['cake_build']['начинка']}\nВыберите финальное покрытие:",reply_markup=final_coating_markup)
    elif query.data == 'strawberry_mousse':
        context.user_data['cake_build']['начинка'] = 'мусс: Клубника'
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nНачинка: {context.user_data['cake_build']['начинка']}\nВыберите финальное покрытие:",reply_markup=final_coating_markup)
    elif query.data == 'cerry_mousse':
        context.user_data['cake_build']['начинка'] = 'мусс: Вишня'
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nНачинка: {context.user_data['cake_build']['начинка']}\nВыберите финальное покрытие:",reply_markup=final_coating_markup)
    elif query.data == 'currant_mousse':
        context.user_data['cake_build']['начинка'] = 'мусс: Cмородина'
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nНачинка: {context.user_data['cake_build']['начинка']}\nВыберите финальное покрытие:",reply_markup=final_coating_markup)
    elif query.data == 'mix_mousse':
        context.user_data['cake_build']['начинка'] = 'мусс: Cмесь ягод (микс)'
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nНачинка: {context.user_data['cake_build']['начинка']}\nВыберите финальное покрытие:",reply_markup=final_coating_markup)

    elif query.data == 'caramel_mousse':
        context.user_data['cake_build']['начинка'] = 'мусс: Карамельный'
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nНачинка: {context.user_data['cake_build']['начинка']}\nВыберите финальное покрытие:",reply_markup=final_coating_markup)
    
    elif query.data == 'final_coating_white_ganache':
        context.user_data['cake_build']['покрытие'] = 'Ганаш на белом шоколаде'
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nНачинка: {context.user_data['cake_build']['начинка']}\nФинальное покрытие: {context.user_data['cake_build']['покрытие']}\nВведите вес торта в килограммах:")
        context.user_data['waiting_quantity_build_cake'] = True
    elif query.data == 'final_coating_milk_ganache':
        context.user_data['cake_build']['покрытие'] = 'Ганаш на молочном шоколаде'
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nНачинка: {context.user_data['cake_build']['начинка']}\nФинальное покрытие: {context.user_data['cake_build']['покрытие']}\nВведите вес торта в килограммах:")
        context.user_data['waiting_quantity_build_cake'] = True  
    elif query.data == 'final_cream_cheese':
        context.user_data['cake_build']['покрытие'] = 'Крем-чиз'
        await query.edit_message_text(f"Основа: {context.user_data['cake_build']['корж']}\nКрем: {context.user_data['cake_build']['крем']}\nНачинка: {context.user_data['cake_build']['начинка']}\nФинальное покрытие: {context.user_data['cake_build']['покрытие']}\nВведите вес торта в килограммах:")
        context.user_data['waiting_quantity_build_cake'] = True

    elif query.data == 'chocolate_cake':
        context.user_data['cake_name']['торт'] = 'Шоколадный'
        await query.edit_message_text(text='Шоколадный торт 🍫🍰\nДля любителей шоколада. Нежные насыщенные шоколадом коржи, прослоенные кремом с молочным шоколадом.\n—шоколадные коржи;\nШоколадный крем.',reply_markup=InlineKeyboardMarkup([build_cake_keyboard[-1],build_cake_keyboard[-3]]))            
    elif query.data == 'red_cake':
        context.user_data['cake_name']['торт'] = 'Красный бархат'
        await query.edit_message_text(text='Красный бархат 🍒🍰\nСамый необычный торт, поражает не только вкусом, но и видом. Насыщенные красные шоколадные коржи, с нежным сливочным кремом и прослойкой из вишни.\n— сливочно-шоколадные коржи;\nСливочно-творожный крем;\nВишневый конфитюр.',reply_markup=InlineKeyboardMarkup([build_cake_keyboard[-1],build_cake_keyboard[-3]]))
    elif query.data == 'apricot_cake':
        context.user_data['cake_name']['торт'] = 'Абрикосовый'
        await query.edit_message_text(text='Абрикосовый 🍑🍰\nСовременный торт, для любителей чего-то нового и необычного.  Достаточно одного кусочка, чтобы влюбиться 😱😻\n— классические ванильные коржи;\nСливочно-творожный крем;\nАбрикосовый мусс;\nАбрикосовый конфитюр;\nКлассическая соленая карамель.',reply_markup=InlineKeyboardMarkup([build_cake_keyboard[-1],build_cake_keyboard[-3]]))
    elif query.data == 'honey_cake':
        context.user_data['cake_name']['торт'] = 'Медовик'
        await query.edit_message_text(text='Медовик 🍰🍯\nТот самый, настоящий медовик. Песочные коржи со вкусом и ароматом меда, пропитанные сливочным кремом. Потрясающая классика для настоящих ценителей 🍯\n— медовые песочные коржи;,\nСметанно-сливочный крем;\nСливочно-творожный крем.',reply_markup=InlineKeyboardMarkup([build_cake_keyboard[-1],build_cake_keyboard[-3]]))
    elif query.data == 'vanilla_cake':
        context.user_data['cake_name']['торт'] = 'Ванильный'
        await query.edit_message_text(text='Ванильный торт 🎂 \nТорт на случай, когда нужен торт, и чтобы вкус не подвел.  Сочетание ванильного бисквита и сливочного крема, который погружает вас в детство. \n— классические ванильные коржи;\nСливочный крем с добавлением творожного сыра;\nФруктовая прослойка/джем по желанию.',reply_markup=InlineKeyboardMarkup([build_cake_keyboard[-1],build_cake_keyboard[-3]]))
    elif query.data == 'poppy_sand_cake':
        context.user_data['cake_name']['торт'] = 'Маковый'
        await query.edit_message_text(text='Маковый торт⚫️🍋🍰\nСовременный торт, для любителей чего-то нового и необычного.  Достаточно одного кусочка, чтобы влюбиться 😱😻\n— классические ванильные коржи с добавлением мака и лимонной цедры;\nСливочно-творожный крем с добавлением лимонной цедры;\nЛимонный джем;\nХрустящий маковый слой.',reply_markup=InlineKeyboardMarkup([build_cake_keyboard[-1],build_cake_keyboard[-3]]))
    elif query.data == 'weight_cake':
        await query.edit_message_text(text='Пожалуйста, введите количество килограммов торта:')
        context.user_data['waiting_for_quantity'] = True

    elif query.data == 'back_to_main':
        await query.edit_message_text(text='Хочешь выбрать конкретный торт или собрать самостоятельно?', reply_markup=first_level_reply_markup)

    elif query.data == 'yeap':
        weight_cake = context.user_data["cake_name"]["вес"]
        order = f'Торт: {context.user_data.get("cake_name")}\nВес: {weight_cake} кг.\nПользователь: {user.name}\nКонтактный номер: {user.phone_num}'
        await Order.create(user=user,order=order)
        await query.edit_message_text(text=f'{user.name}, спасибо за заказ!🤗\nВы выбрали торт {context.user_data["cake_name"]["торт"]}, весом {weight_cake} кг.🍰\nМы Вам перезвоним в течении получаса🕖📲',reply_markup=InlineKeyboardMarkup([build_cake_keyboard[-2]]))
        await send_message_creator(context,message=f'Пользователь {user.name} с номером: {user.phone_num} заказал торт: {context.user_data["cake_name"]["торт"]}, весом {weight_cake} кг')
    
    elif query.data == 'YES':        
        order_summary = (
                f"\n• Корж: {context.user_data['cake_build']['корж']}\n"
                f"• Крем: {context.user_data['cake_build']['крем']}\n"
                f"• Начинка: {context.user_data['cake_build']['начинка']}\n"
                f"• Покрытие: {context.user_data['cake_build']['покрытие']}\n"
                f"• Вес: {context.user_data['cake_build']['вес']} кг\n"
            )
        await Order.create(user=user,order=order_summary)
        await send_message_creator(context,f'Пользователь {user.name} с номером: {user.phone_num} заказал торт: {order_summary}')
        await query.edit_message_text(text=f'{user.name}, спасибо за заказ!🤗\nМы Вам перезвоним в течении получаса🕖📲',reply_markup=InlineKeyboardMarkup([build_cake_keyboard[-2]]))



async def send_message_creator(context:ContextTypes.DEFAULT_TYPE, message:str):
    await context.bot.send_message(chat_id=cake_creator_id, text=message)



async def echo(update: Update, context:ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    
    if context.user_data.get('waiting_for_name'):
        context.user_data['name'] = update.message.text
        await update.message.reply_text(text='Пожалуйста, введите ваш номер телефона:')
        context.user_data['waiting_for_name'] = False
        context.user_data['waiting_for_number'] = True

    elif context.user_data.get('waiting_for_number'):
        context.user_data['number_contact'] = update.message.text
        chat_id = update.effective_chat.id
        name = context.user_data['name']
        phone_num = context.user_data['number_contact']
        await User.create(chat_id=chat_id,name=name,phone_num=phone_num)
        await update.message.reply_text('Спасибо! Теперь вы можете выбрать торт или собрать его самостоятельно.', reply_markup=first_level_reply_markup)
        context.user_data['waiting_for_number'] = False

    elif context.user_data.get('waiting_for_quantity'):
            user = await User.get(chat_id=chat_id)
            context.user_data['cake_name']['вес'] = float(update.message.text)
            await update.message.reply_text(f'{user.name}, Вы выбрали торт {context.user_data["cake_name"]["торт"]}, весом {context.user_data["cake_name"]["вес"]} кг.',reply_markup=cake_final_markup)
            context.user_data['waiting_for_quantity'] = False

    elif context.user_data.get('waiting_quantity_build_cake'):
        user = await User.get(chat_id=chat_id)
        context.user_data['cake_build']['вес'] = float(update.message.text)
        order_summary = (
                f"Ваш заказ, {user.name}!\n\n"
                f"Вы выбрали торт:\n"
                f"• Корж: {context.user_data['cake_build']['корж']}\n"
                f"• Крем: {context.user_data['cake_build']['крем']}\n"
                f"• Начинка: {context.user_data['cake_build']['начинка']}\n"
                f"• Покрытие: {context.user_data['cake_build']['покрытие']}\n"
                f"• Вес: {context.user_data['cake_build']['вес']} кг.\n"
            )
        await update.message.reply_text(order_summary,reply_markup=cake_build_final_markup)
        context.user_data['waiting_quantity_build_cake'] = False

    else:
        await update.message.reply_text("юзай команды")


async def init():
    await Tortoise.init(
        db_url="sqlite://database.db",
        modules={"models": ["models"]}
    )
    await Tortoise.generate_schemas()


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init())

    application = ApplicationBuilder().token(TOKEN).build()
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(None, echo)
    button_handler = CallbackQueryHandler(button)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(button_handler)

    application.run_polling()

if __name__ == '__main__':
    main()