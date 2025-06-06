class GameStats():
    """Armazena dados statísticos da Invasão Alienígenas."""

    def __init__(self, ai_settings):
        """Inicializa os dados estatísticos."""
        # Inicia a Invasão Alienígena em um estado ativo
        self.game_active = True
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """Inicializa os dados estatísticos que podem mudar durante o jogo."""
        self.ships_left = self.ai_settings.ship_limit