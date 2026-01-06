import telebot
from telebot import types
import random

TOKEN = "8524255428:AAEACvagw2jQ-LQsna_oLxPvBfuin-uG3sw"
bot = telebot.TeleBot(TOKEN)

reaction_emojis = ["👍","😂","❤️","🔥","😢","👏","😍","😮","😡","🎉"]

@bot.message_handler(func=lambda m: True)
def auto_random_reaction(message):
    if message.chat.type not in ["group", "supergroup", "channel"]:
        return

    markup = types.InlineKeyboardMarkup(row_width=5)
    buttons = []

    for emoji in reaction_emojis:
        count = random.randint(1, 5)
        buttons.append(
            types.InlineKeyboardButton(f"{emoji} {count}", callback_data=emoji)
        )

    markup.add(*buttons)

    bot.send_message(
        message.chat.id,
        "Reactions 👇",
        reply_to_message_id=message.message_id,
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: True)
def reaction_click(call):
    bot.answer_callback_query(call.id, "Reaction added ✅")

bot.infinity_polling()
