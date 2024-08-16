class Settings():
    """Uma classe para armazenar todas as configurações da Invasão Alienigena"""

    def __init__(self):
        """Inicializa as configurações do jogo"""
        # Configurações de tela
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (20, 90, 255)
        self.ship_speed_factor = 1.5