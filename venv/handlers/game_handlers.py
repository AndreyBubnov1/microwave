from lexicon.lexicon import lexicon
from keyboards.keyboards import game_kb
def register_game_handlers(bot):
    @bot.message_handler(func=lambda message: message.text == lexicon.yes_button)
    def yes_game_handler(message):
        bot.send_message(
            chat_id=message.chat.id,
            text=lexicon.yes,
            reply_markup=game_kb
        )