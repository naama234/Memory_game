class Card:
    def __init__(self, button, image, r, c):
        self.button = button
        self.facedown = True
        self.pair_id = 0
        self.image = image
        self.index = [r, c]