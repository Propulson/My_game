import pygame
import sys
from setting import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """class for resource and rule game"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Main game start"""
        while True:
            """checking mouse and keyboard"""
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """mouse and keyboard refresh"""
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                sys.exit()
            elif even.type == pygame.KEYDOWN:
                self._check_keydown_events(even)
            elif even.type == pygame.KEYUP:
                self._check_keyup_events(even)

    def _check_keydown_events(self, even):
        if even.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif even.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif even.key == pygame.K_q:
            sys.exit()
        elif even.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, even):
        if even.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif even.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new missile"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """refresh images on view"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

    pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
