class Logic:
    def __init__(self, values):
        self.values = values

    def check_game_state(self):
        r = [1 for x in self.values if x.id != 0]
        if len(r) == 0:
            print('someone win')
