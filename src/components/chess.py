class Chess:
    def __init__(self):
        self.position = self.papan()

    def papan(self):
        # ceritanya nanti jadi papan catur
        return [
            [None, None, None, None, None, None, None, None,],
            [None, None, None, None, None, None, None, None,],
            [None, None, None, None, None, None, None, None,],
            [None, None, None, None, None, None, None, None,],
            [None, None, None, None, None, None, None, None,],
            [None, None, None, None, None, None, None, None,],
            [None, None, None, None, None, None, None, None,],
            [None, None, None, None, None, None, None, None,],
        ]

    def move(self, playing_side, starting_code, destination_code):
        pass

    def __is_obstructed(self, start_pos, target_pos):
        return False

    def __is_killing(self, target_pos, playing_side):
        return False

    def __is_backward(self, current_pos, target_pos, playing_side):
        return False

