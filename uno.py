import sys
import pygame
from pygame.constants import RESIZABLE, VIDEORESIZE
from uno_classes import Settings, Start_button, Text_box
from uno_classes import create_deck as create_deck
import time

def game_main():
    # setting the 16:9 ratio
    w_ratio = 16
    h_ratio = 9
    # multiplier for the resolution ratio
    mult_ratio = 100

    # initializing the game and font renderers
    pygame.init()
    pygame.font.init()
    # instantiating the Settings object
    game_data = Settings(w_ratio*mult_ratio, h_ratio*mult_ratio, (0, 0, 0), "Uno for stutterers")
    # setting the game window
    pygame.display.set_caption(game_data.window_name)
    # setting the main Surface
    screen = pygame.display.set_mode((game_data.width, game_data.height), pygame.RESIZABLE)
    
    # avoiding unbounded variables and providing a value to check if something goes wrong
    current_card = -1
    cards = [-1]
    start = False
    start_time = -1
    final_time = -1

    # main loop
    while(True):
        # if start is false then the user just opened the program or finished a run
        if(start == False):
            # instantiating and rendering the start button
            button = Start_button()
            button.blitme(screen)
            # instantiating the textbox with the consolas font
            text_box = Text_box("Consolas")
            
            # if final_time is the same as the initialization then it means that the user didn't use the program and thus the time of the previous run is not to be shown
            if(final_time != -1):
                text_box.blitme(final_time, True, screen)
            else:
                text_box.blitme(final_time, False, screen)

            # listening for events
            for event in pygame.event.get():
                # the user closed the pygame window
                if(event.type == pygame.QUIT):
                    sys.exit()
                # the user resized the window
                elif(event.type == VIDEORESIZE):
                    # the screen Surface changes in resolution
                    screen = pygame.display.set_mode((event.w, event.h), RESIZABLE)
                # the user presses a button
                elif(event.type == pygame.KEYDOWN):
                    # the user pressed the spacebar
                    if(event.key == pygame.K_RETURN):
                        # changes the start boolean to True and signals the program to commencing to show the randomized cards
                        start = True
                        # wipes the screen from the start button and the text above
                        screen.fill(game_data.bg_color)
                        # creates the deck
                        cards = create_deck()
                        # pops the first card from the deck
                        current_card = cards.pop()
                        # starts the time
                        start_time = time.time()
                        break
        # if start is true then the user is about to be shown the randomized cards
        else:
            # the card is shown to the user
            current_card.blitme(screen)
            # listening for events
            for event in pygame.event.get():
                # if the user closes the window
                if(event.type == pygame.QUIT):
                    sys.exit()
                # if the user resizes the window
                elif(event.type == VIDEORESIZE):
                    # the screen Surface changes in resolution
                    screen = pygame.display.set_mode((event.w, event.h), RESIZABLE)
                # if the user presses a key
                elif(event.type == pygame.KEYDOWN):
                    # if the user pressed the spacebar
                    if(event.key == pygame.K_SPACE):
                        # if the card list is not empty pops another card from the deck
                        if(cards):
                            current_card = cards.pop()
                        # if the card list is empty then the user has seen all the cards in the deck
                        else:
                            # the start boolean is set to false in order for the program to execute the instructions of the first branch of the if statement
                            start = False
                            # wipes the screen from the card image
                            screen.fill(game_data.bg_color)
                            # calculates the clock stops and the timing is saved
                            final_time = time.time() - start_time
                            break
        pygame.display.flip()
        

game_main()