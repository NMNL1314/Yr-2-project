import pygame


class Indicator:
        def __init__(self, x, y, letter):
            # Initializes variables such as color, size, position, and letter.
            self.x = x
            self.y = y
            self.text = letter
            self.rect = (self.x, self.y, 57, 75)
            self.bg_color = OUTLINE

        def draw(self):
            # Puts the indicator and its text on the screen at the desired position.
            pygame.draw.rect(SCREEN, self.bg_color, self.rect)
            self.text_surface = AVAILABLE_LETTER_FONT.render(self.text, True, "white")
            self.text_rect = self.text_surface.get_rect(center=(self.x+27, self.y+30))
            SCREEN.blit(self.text_surface, self.text_rect)
            pygame.display.update()