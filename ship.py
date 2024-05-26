import pygame


class Ship():
    """class for ship"""

    def __init__(self, ai_game):
        """init ship and his start position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # download ship-image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        # flag moving
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)

    def update(self):
        """refresh position ship if a flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

    def blitme(self):
        self.screen.bilt(self.image, self.rect)
