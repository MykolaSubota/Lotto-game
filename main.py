import random


class Card:
    def __init__(self, numbers: list):
        self.numbers = numbers

    def __str__(self):
        str_numbers = ''
        i = 1
        for numeric in self.numbers:
            str_numbers += f'{numeric} '.zfill(3)
            if i % 9 == 0:
                str_numbers += '\n'
            i += 1
        return str_numbers


class Player:
    def __init__(self, name: str, player_card: Card, is_computer: bool = True, plays: bool = True, points: int = 0):
        self.name = name
        self.player_card = player_card
        self.is_computer = is_computer
        self.plays = plays
        self.points = points

    def __str__(self):
        return self.name


class Barrel:
    def __init__(self, numbers=None):
        if numbers is None:
            numbers = list(range(1, 91))
        self.numbers = numbers


def print_cards(items: list[Player]):
    for item in items:
        print(f'{f"{item}".center(26, "-")}\n{item.player_card}{"".center(26, "-")}')


players, number_of_players, switch = [], 0, False
while not switch:
    number_of_players = int(input('Number of players (more than one): '))
    if int(number_of_players) > 1:
        switch = True
computers = 0
for number in range(number_of_players):
    switch, computer, player_name = False, True, ''
    while not switch:
        user_response = input(f'{number + 1}st computer player (Y/n)? ').strip().lower()
        if user_response == 'y' or user_response == 'n':
            if user_response == 'n':
                computer = False
            switch = True
    if not computer:
        switch = False
        while not switch:
            unique_name = True
            player_name = input(f'Name of {number + 1}st player: ').strip()
            for p in players:
                if p.name == player_name:
                    print('A player with that name already exists!')
                    unique_name = False
                    break
            if unique_name:
                switch = True
    else:
        computers += 1
        player_name = f'Computer {computers}'
    card = random.sample(range(1, 91), 27)
    if not computer:
        players.append(Player(player_name, Card(card), False))
    else:
        players.append(Player(player_name, Card(card)))
print('Players cards:')
print_cards(players)
print('Start!'.center(26, ' '))
barrel = Barrel()
end_of_the_game = False
while not end_of_the_game:
    number = random.choice(barrel.numbers)
    print(f'New barrel {f"{number}".zfill(2)} (lost: {len(barrel.numbers)})')
    for player in players:
        if player.plays:
            if player.is_computer:
                print(f'{f"{player}".center(26, "-")}\n{player.player_card}{"".center(26, "-")}')
                if number in player.player_card.numbers:
                    player.player_card.numbers[player.player_card.numbers.index(number)] = '--'
                if player.player_card.numbers.count('--') != 27:
                    player.points += 1
            else:
                print(f'{f"{player}".center(26, "-")}\n{player.player_card}{"".center(26, "-")}')
                switch, player_response = False, ''
                while not switch:
                    player_response = input('Cross out a number (Y/n)? ').strip().lower()
                    if player_response == 'y' or player_response == 'n':
                        switch = True
                if player_response == 'y' and (number in player.player_card.numbers):
                    player.player_card.numbers[player.player_card.numbers.index(number)] = '--'
                    player.points += 1
                elif player_response == 'n' and (number not in player.player_card.numbers):
                    player.points += 1
                else:
                    player.plays = False
    barrel.numbers.remove(number)
    playing_players = 0
    for player in players:
        if len(barrel.numbers) == 0:
            end_of_the_game = True
            break
        if player.plays:
            playing_players += 1
    if playing_players == 1:
        end_of_the_game = True
print(f'{"End of the  game".center(26, " ")}\n{"Game result:".center(26, "-")}')
print_cards(players)
players.sort(key=lambda x: x.points, reverse=False)
for player in players:
    print(f'{player}: {player.points}')
