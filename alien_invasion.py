import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions

def run_game():
    # Inicializa o jogo.
    pygame.init()

    # Cria uma instância das configurações.
    ai_settings = Settings()

    # Cria a tela principal do jogo.
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    # Título do jogo.
    pygame.display.set_caption("Alien Invasion")

    # Cria o botão Play
    play_button = Button(ai_settings, screen, "Play")

    # Cria uma instância para armazenar dados estatísticos do jogo
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Cria a espaçonave.
    ship = Ship(ai_settings, screen)

    # Cria um grupo no qual serão armazenados os alienígenas.
    aliens = Group()

    # Cria uma frota de alienígenas.
    game_functions.create_fleet(ai_settings, screen, ship, aliens)

    # Cria um grupo no qual serão armazenados os projéteis.
    bullets = Group()

    # Inicia o laço principal do jogo.
    while True:
        # Observa eventos de teclado e de mouse.
        game_functions.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:

            # Atualiza os movimentos da espaçonave.
            ship.update()

            # Atualiza os projéteis e apaga os projéteis que desapareceram.
            game_functions.update_bullets(ai_settings, screen, stats, sb,  ship, aliens, bullets)

            # Atualiza a posição dos alienígensa.
            game_functions.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
                    
        # Faz o update da tela.
        game_functions.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()