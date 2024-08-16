import sys, pygame

def check_keydown_events(event, ship):
    '''Responde presionamentos de teclas'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    '''Responde soltura de teclas'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    '''Responde a eventos de presionamentos de teclas'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    '''Atualiza as imagens na tela e alterna para a nova tela.'''
    # Redesenha a tela a cada passagem do laço
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # Deixa a tela mais recente visível
    pygame.display.flip()