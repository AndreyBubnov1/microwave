class Lexicon:
    def __init__(self):
        self.start = "Приветствую!\n\n Давай сыграем в игру 'Камень, ножницы, бумага'?"
        self.yes_button = "Давай"
        self.no_button = "Не хочу"
        self.yes = "Хорошо, сделай свой выбор"
        self.rock = "Камень"
        self.paper = "Бумага"
        self.scissors = "Ножницы"
        
        self.bot_winner = "Я победил\n\nСыграем еще?"
        self.player_winner = "Ты победил\n\nСыграем еще?"
        self.nobody_winner = "Ничья\n\nСыграем еще?"
lexicon = Lexicon()