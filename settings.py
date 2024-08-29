class Settings():
    """Uma classe para armazenar todas as configurações da Invasão Alienigena"""

    def __init__(self):
        """Inicializa as configurações do jogo"""
        # Configurações de tela
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (20, 90, 255)
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60