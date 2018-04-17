import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """Ship init, default placement"""
        super().__init__()
        self.screen = screen
        self.ai_setting = ai_settings

        # Ship pic loading
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Every new ship apears on the bootom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Center of the ship is float number
        self.center = float(self.rect.centerx)

        # Options indicating ship movement
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Ship position update based on options indicating his movement"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_setting.ship_speed_factor

        # Rect object update
        self.rect.centerx = self.center

    def blitme(self):
        """Showing ship in his current position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Put ship at the center of the screen"""
        self.center = self.screen_rect.centerx
