from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Посмотреть товары", callback_data='view_products')],
        [InlineKeyboardButton("Контакты", callback_data='contact')],
        [InlineKeyboardButton("О нас", callback_data='about')],
        [InlineKeyboardButton("Наше Местоположение", callback_data='place')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Добро пожаловать в магазин одежды! Выберите действие:", reply_markup=reply_markup)


async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()  

    if query.data == 'view_products':
        await query.edit_message_text(text="Доступные товары:\n- Футболка: 500 сом\n- Джинсы: 1200 сом\n-Куртка:2300сом")
    elif query.data == 'contact':
        await query.edit_message_text(text="Контакты: akmatbekovc1@gmail.com")
    elif query.data == 'about':
        await query.edit_message_text(text="Мы - лучший магазин одежды в вашем городе!")
        
    elif query.data == 'place':
        await query.edit_message_text(text="Наше Местоположение: Бишкек")

if __name__ == '__main__':
    TOKEN = "7599548322:AAG9qFM0kC1UYu2x3CB0uig3LvVWqNZlW4Q"  

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_callback))

    
    app.run_polling()
