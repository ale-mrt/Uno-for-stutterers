from random import randint
import pygame
import os

# this dictionary contains the key->color pairs used by the Card constructor
colors = {"0": "r", "1": "b", "2": "g", "3": "y"}
# this dictionary contains the key->color pairs used for the stringification of instances of Card in italian, used for debugging purposes
colorsIT = {"0": "rosso", "1": "blu", "2": "verde", "3": "giallo"}
# this tuple contains the values for the cards' numbers in italian, used for debugging purposes
numbers = ("zero", "uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove")


class Card():
    """
    A class used to represent a card

    ...

    Attributes
    ----------
    value : int
        the value on the card used to locate the correct image file for the card
    color : str
        the color of the card used to locate the correct image file for the card
    image_path : str
        the formatted string used to locate the correct image file for the card
    image : Surface
        the image that will be rendered, obtained using image_path

    Methods
    -------
    blitme(screen)
        renders the image file onto the pygame window
    """
    def __init__(self, value, color):
        """
        Parameters
        ----------
        value : int
            the value of the card
        color : str
            the color of the card
        """
        self.value = value
        self.color = color
        self.image_path = "{}\\img\\{}{}.bmp".format(os.getcwd(), colors[str(self.color)], self.value)
        self.image = pygame.image.load(self.image_path)
    
    def __str__(self) -> str:
        return "{} {}".format(numbers[self.value], colorsIT[str(self.color)])

    def blitme(self, screen):
        """It renders the card image onto the Surface instance screen

        Parameters
        ----------
        screen : Surface
            the surface where the image will render itself
        """

        # gets the size data of the screen passed as a parameter
        screen_rect = screen.get_rect()
        # scales the image by an arbitrary factor, so that every screen can visualize it, and updates the image rectangle
        self.image = pygame.transform.smoothscale(self.image, (int(screen_rect.w/8), int(screen_rect.h/3)))
        self_rect = self.image.get_rect()

        # centers the image
        self_rect.centerx = screen_rect.centerx
        self_rect.centery = screen_rect.centery

        screen.blit(self.image, self_rect)

class Start_button():
    """
    A class used to represent the start button

    ...

    Attributes
    ----------
    image_path : str
        the string used to locate the correct image file for the start button
    image : Surface
        the image that will be rendered, obtained using image_path

    Methods
    -------
    blitme(screen)
        renders the image file onto the pygame window
    """
    def __init__(self):
        image_path = "{}\\img\\start.bmp".format(os.getcwd())
        self.image = pygame.image.load(image_path)

    def blitme(self, screen):
        """It renders the start button onto the Surface instance of the main screen

        Parameters
        ----------
        screen : Surface
            the surface where the image will render itself
        """

        # gets the size data of the screen passed as a parameter
        screen_rect = screen.get_rect()
        # scales the image by an arbitrary factor, so that every screen can visualize it, and updates the image rectangle
        self.image = pygame.transform.smoothscale(self.image, (int(screen_rect.w/4), int(screen_rect.h/4)))
        self_rect = self.image.get_rect()

        # centers the image
        self_rect.centerx = screen_rect.centerx
        self_rect.centery = screen_rect.centery

        screen.blit(self.image, self_rect)

class Text_box():
    """
    A class used to represent the text box in the main menu

    ...

    Attributes
    ----------
    font : Surface
        the Surface instance used for rendering the textbox and its text onto the main screen Surface
    font_color : tuple
        the color of the text expressed in RGB
    text : Surface
        the rendered text that will be put onto the textbox

    Methods
    -------
    blitme(value, mode, screen)
        renders the textbox with something written on it onto the main screen
    """
    def __init__(self, font):
        """
        Parameters
        ----------
        font : str
            the string used for the instantiation of the font Surface
        """
        if(font in pygame.font.get_fonts()):
            self.font = pygame.font.SysFont(font, 20)
        else:
            self.font = pygame.font.SysFont("Arial", 20)
        self.font_color = (255, 255, 255)
        
    def blitme(self, value, mode, screen):
        """It renders the textbox onto the Surface instance of the main screen

        Parameters
        ----------
        value : float
            the time of the previous run will be held in this variable and it will be formatted into the text Surface

        mode : bool
            if the user never had a run, then the mode will be set in False mode and won't display a time

        screen : Surface
            the surface where the image will render itself

        """

        # if mode is True then the user already had a run, and text will hold the instruction to start the program and the time of the previous run
        # if mode is False then the user never had a run, and the text will only hold the instruction to start the program
        if(mode == True):
            self.text = self.font.render("Premere invio per iniziare e la barra spaziatrice per mostrare la carta successiva. Tempo precedente = {:.2f}".format(value), True, self.font_color)
        else:
            self.text = self.font.render("Premere invio per iniziare e la barra spaziatrice per mostrare la carta successiva.", True, self.font_color)

        # getting the data of the rectangles containing the screen and the text
        self_rect = self.text.get_rect()
        screen_rect = screen.get_rect()

        # centering the textbox
        self_rect.centerx = screen_rect.centerx
        self_rect.centery = 0 + 20
        
        screen.blit(self.text, self_rect)

class Settings():
    """
    A class used to represent the global settings of the game

    ...

    Attributes
    ----------
    width : int
        the initial width of the window
    height : int
        the initial height of the window
    bg_color : tuple
        the background color expressed in RGB
    window_name : str
        the name of the pygame window
    """
    def __init__(self, width, height, bg_color, window_name):
        """
        Parameters
        ----------
        width : int
            the initial width of the window
        height : int
            the initial height of the window
        bg_color : tuple
            the background color expressed in RGB
        window_name : str
            the name of the pygame window
        """
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.window_name = window_name

def create_deck():
    """A simple function that randomizes a deck of cards"""
    init_deck = []
    deck = []
    max_index = 39
    i = 0

    # creating the deck in order
    for i in range(0, 10):
        for j in range(0, 4):
            init_deck.append(Card(i, j))

    # randomizing the deck, appending the objects popped from init_deck in a random fashion
    while(max_index != -1):
        deck.append(init_deck.pop(randint(0, max_index)))
        max_index -= 1

    return deck