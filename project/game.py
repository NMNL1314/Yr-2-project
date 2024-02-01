import pygame
import sys
import random
from words import WORDS

class WordleGame:
    def __init__(self):
        pygame.init()
        self.game_active = False

        self.clock = pygame.time.Clock()

        # Constants
        self.WIDTH, self.HEIGHT = 1200, 900

        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.BACKGROUND = pygame.image.load("assets/Starting Tiles.png")
        self.BACKGROUND_RECT = self.BACKGROUND.get_rect(center=(317, 300))
        self.ICON = pygame.image.load("assets/Icon.png")

        pygame.display.set_caption("Wordle!")
        pygame.display.set_icon(self.ICON)

        self.GREEN = "#6aaa64"
        self.YELLOW = "#c9b458"
        self.GREY = "#787c7e"
        self.OUTLINE = "#d3d6da"
        self.FILLED_OUTLINE = "#878a8c"

        self.CORRECT_WORD = "coder"

        self.ALPHABET = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

        self.GUESSED_LETTER_FONT = pygame.font.Font("assets/FreeSansBold.otf", 50)
        self.AVAILABLE_LETTER_FONT = pygame.font.Font("assets/FreeSansBold.otf", 25)

        self.SCREEN.fill("white")
        self.SCREEN.blit(self.BACKGROUND, self.BACKGROUND_RECT)

        self.LETTER_X_SPACING = 85
        self.LETTER_Y_SPACING = 12
        self.LETTER_SIZE = 75

        # Global variables
        self.guesses_count = 0

        # guesses is a 2D list that will store guesses. A guess will be a list of letters.
        # The list will be iterated through and each letter in each guess will be drawn on the screen.
        self.guesses = [[]] * 6

        self.current_guess = []
        self.current_guess_string = ""
        self.current_letter_bg_x = 110

        # Indicators is a list storing all the Indicator object. An indicator is that button thing with all the letters you see.
        self.indicators = []

        self.game_result = ""

        self.time = 0
        self.current_time = 0
        self.start_time = 0
        self.end_time = 0
        self.score = 0
        self.game_over = False

        self.text_font = pygame.font.Font("Pixeltype.ttf", 50)

    class Letter:
        def __init__(self, text, bg_position):
            # Initializes all the variables, including text, color, position, size, etc.
            self.bg_color = "white"
            self.text_color = "black"
            self.bg_position = bg_position
            self.bg_x = bg_position[0]
            self.bg_y = bg_position[1]
            self.bg_rect = (bg_position[0], self.bg_y, self.LETTER_SIZE, self.LETTER_SIZE)
            self.text = text
            self.text_position = (self.bg_x + 36, self.bg_position[1] + 34)
            self.text_surface = self.GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
            self.text_rect = self.text_surface.get_rect(center=self.text_position)

        def draw(self):
            # Puts the letter and text on the screen at the desired positions.
            pygame.draw.rect(self.SCREEN, self.bg_color, self.bg_rect)
            if self.bg_color == "white":
                pygame.draw.rect(self.SCREEN, self.FILLED_OUTLINE, self.bg_rect, 3)
            self.text_surface = self.GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
            self.SCREEN.blit(self.text_surface, self.text_rect)
            pygame.display.update()

        def delete(self):
            # Fills the letter's spot with the default square, emptying it.
            pygame.draw.rect(self.SCREEN, "white", self.bg_rect)
            pygame.draw.rect(self.SCREEN, self.OUTLINE, self.bg_rect, 3)
            pygame.display.update()

    class Indicator:
        def __init__(self, x, y, letter):
            # Initializes variables such as color, size, position, and letter.
            self.x = x
            self.y = y
            self.text = letter
            self.rect = (self.x, self.y, 57, 75)
            self.bg_color = self.OUTLINE

        def draw(self):
            # Puts the indicator and its text on the screen at the desired position.
            pygame.draw.rect(self.SCREEN, self.bg_color, self.rect)
            self.text_surface = self.AVAILABLE_LETTER_FONT.render(self.text, True, "white")
            self.text_rect = self.text_surface.get_rect(center=(self.x + 27, self.y + 30))
            self.SCREEN.blit(self.text_surface, self.text_rect)
            pygame.display.update()

    # Drawing the indicators on the screen.

if __name__ == "__main__":
    wordle_game = WordleGame()

    indicator_x, indicator_y = 20, 600

    for i in range(3):
        for letter in wordle_game.ALPHABET[i]:
            new_indicator = wordle_game.Indicator(indicator_x, indicator_y, letter)
            wordle_game.indicators.append(new_indicator)
            new_indicator.draw()
            indicator_x += 60
        indicator_y += 100
        if i == 0:
            indicator_x = 50
        elif i == 1:
            indicator_x = 105

    while True:
        wordle_game.display_time()

        if wordle_game.game_result != "":
            wordle_game.play_again()
            if wordle_game.game_result == "W":  # Player won
                wordle_game.end_time = wordle_game.current_time
                # Calculate the score, subtracting a penalty for each incorrect guess
                penalty = (6 - wordle_game.guesses_count) * 5  # Adjust penalty as needed
                wordle_game.score = max(0, 500 - wordle_game.end_time + penalty + 100)
                wordle_game.game_over = True
                print(f"End Time: {wordle_game.end_time} seconds")
                print(f"Score: {wordle_game.score}")
                wordle_game.display_score()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if wordle_game.game_result != "":
                        wordle_game.reset()
                        wordle_game.game_over = False
                        wordle_game.start_time = pygame.time.get_ticks()
                    else:
                        if len(wordle_game.current_guess_string) == 5 and wordle_game.current_guess_string.lower() in WORDS:
                            wordle_game.check_guess(wordle_game.current_guess)
                elif event.key == pygame.K_BACKSPACE:
                    if len(wordle_game.current_guess_string) > 0:
                        wordle_game.delete_letter()
                else:
                    key_pressed = event.unicode.upper()
                    if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "" and not wordle_game.game_over:
                        wordle_game.game_active = True
                        if len(wordle_game.current_guess_string) < 5:
                            wordle_game.create_new_letter()

        pygame.display.update()
        wordle_game.clock.tick(60)
