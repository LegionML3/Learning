class Player:
    def __init__(self, username, score, token):
        self.username = username
        self.score = score
        self.token = token

    def level_up(self):
        self.token += 10
        print(f"{self.username} leveled up!")

player1 = Player("josh234", 100, 10)
player2 = Player("narin40", 80, 30)
player3 = Player("didt204", 100, 10)

player3.level_up()
player2.level_up()

player_list = [player1, player2, player3]

def get_mvp_player(list) -> str:
    username = ""
    current = -1
    current_tokens = 999
    for player in list:
        if player.score > current:
            username = player.username
            current = player.score
            current_tokens = player.token
        elif player.score == current:
            if player.token < current_tokens:
                username = player.username
                current = player.score
                current_tokens = player.token
    return username

print(f"{get_mvp_player(player_list)} got the highest score!")

