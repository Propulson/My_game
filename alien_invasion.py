import sys, pygame


class AlienInvasion:
    """class for resource and rule game"""

    def __init__(self):
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Invasion')

    @staticmethod
    def run_game():
        """Main game start"""
        while True:
            """checking mouse and keyboard"""
            for even in pygame.event.get():
                if even.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
