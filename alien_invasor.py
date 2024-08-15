import pygame
import game_functions as gf
from settings import Settings
from ship import Ship

def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen) # Cria uma nave

    # Inicia o laço principal do jogo
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)

                
run_game()