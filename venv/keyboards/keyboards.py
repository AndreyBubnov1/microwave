from telebot import types
from lexicon.lexicon import lexicon
button_yes = types.KeyboardButton(text=lexicon.yes_button)
button_no = types.KeyboardButton(text=lexicon.no_button)
yes_no_kb = types.ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True 
)
yes_no_kb.add(button_yes, button_no)


button_rock = types.KeyboardButton(text=lexicon.rock)
button_paper= types.KeyboardButton(text=lexicon.paper)
button_scissors = types.KeyboardButton(text=lexicon.scissors)
game_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
game_kb.add(button_rock)
game_kb.add(button_paper)
game_kb.add(button_scissors)