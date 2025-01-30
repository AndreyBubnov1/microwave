import random
from lexicon.lexicon import lexicon

def get_bot_choice():
    return random.choice((lexicon.rock, lexicon.paper, lexicon.scissors))

def get_winner(bot, player):
    if bot == lexicon.paper and player == lexicon.rock:
        return lexicon.bot_winner
    elif bot == lexicon.scissors and player == lexicon.paper:
        return lexicon.bot_winner
    elif bot == lexicon.rock and player == lexicon.scissors:
        return lexicon.bot_winner
    
    elif player == lexicon.paper and bot == lexicon.rock:
        return lexicon.player_winner
    elif player == lexicon.scissors and bot == lexicon.paper:
        return lexicon.player_winner
    elif player == lexicon.rock and bot == lexicon.scissors:
        return lexicon.player_winner
    
    else:
        return lexicon.nobody_winner