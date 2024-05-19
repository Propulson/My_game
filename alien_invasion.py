import sys, pygame


class AlienInvasion:
    """class for resource and rule game"""

    def __init__(self):
        self.screen = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption('Alien Invasion')
        self.bg_color = (230, 230, 230)  # Color

    def run_game(self):
        """Main game start"""
        while True:
            """checking mouse and keyboard"""
            for even in pygame.event.get():
                if even.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
