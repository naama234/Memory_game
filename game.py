from tkinter import PhotoImage
from tkinter import Button
from functools import partial
import random
from card import Card
from PIL import Image, ImageTk


class Game:
    def __init__(self, root):
        self.root = root

        self.root.title('Memory game')

        #The buttons are the cards
        self.buttons = {}

        #The images of the cards
        self.images = {}

        #The cards of the game
        self.cards = []

        #The moves
        self.count_clicks = 0

        #The open cards, the size of this list is up to two
        self.current_pair = []


        #Set the default borad
        for r in range(3):
            for c in range(3):
                self.images[(r, c)] = PhotoImage\
                    (file = r"back.png")

        #Set the cards in borad
        for r in range(3):
            for c in range(3):
                button = Button(self.root, image = self.images[r, c],
                                            command = partial(self.make_move, r , c))

                new_card = Card(button, self.images[r, c], r, c)
                self.cards.append(new_card)
                button.grid(row=r, column=c)
                self.buttons[(r, c)] = button

        #Put the pairs in random order
        self.set_pair_ids()

    #Search a card by his indrx
    def get_card_by_index(self, r, c):
        for card in self.cards:
            if(card.index[0] == r and card.index[1] == c):
                return card

    #Set an image after the card chosen
    def set_image(self, r, c, card):
        if(card.pair_id == 0):
            path = r"micky.png"
        elif(card.pair_id == 1):
            path = r"donald.png"
        elif(card.pair_id == 2):
            path = r"daisy.png"
        elif(card.pair_id == 3):
            path = r"mini.png"
        else:
            path = r"pluto.png"
        self.change_card_picture(r, c, path)

    #Set pair id to each card in the game
    def set_pair_ids(self):
        pair_ids = [0,0,1,1,2,2,3,3,4]
        for card in self.cards:
            rand_pair_id = random.choice(pair_ids)
            card.pair_id = rand_pair_id
            pair_ids.remove(rand_pair_id)

    #Change card picture
    def change_card_picture(self, r, c, path):
        self.images[(r, c)] = \
                PhotoImage(file = path)
        self.buttons[(r, c)].config(image = self.images[r, c])

    #If two cards face up, flip them back
    def upside_down_pair(self):
        self.change_card_picture(self.current_pair[0]['index'][0],
                                 self.current_pair[0]['index'][1],
                                 r"back.png")
        self.change_card_picture(self.current_pair[1]['index'][0],
                                 self.current_pair[1]['index'][1],
                                 r"back.png")
        #No cards faceup right now
        self.current_pair = []

    #How the move work
    def make_move(self, r, c):
        card = self.get_card_by_index(r, c)
        if(card.facedown and len(self.current_pair) < 2):
            self.count_clicks = self.count_clicks + 1

            self.set_image(r, c, card)

            new_pair_item = {'pair_id' : card.pair_id, 'index' : [r,c]}
            self.current_pair.append(new_pair_item)

            if(self.count_clicks % 2 == 0):
                if(self.check_pair()):
                    self.current_pair = []
                else:
                    self.root.after(3000, self.upside_down_pair)


    def check_pair(self):
        if(self.current_pair[0]['pair_id'] == self.current_pair[1]['pair_id']):
            return True

        return False