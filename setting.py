class Settings():
    """Class for saving everything games settings"""
    def __init__(self):
        """initialization game settings"""
        # Screen settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
