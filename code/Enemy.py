from Sprite import Sprite

class Enemy(Sprite):
    def __init__(self):
        super().__init__()
        self.vida = None
        self.tipo = None

    def seguir_jogador(self):
        pass

    def atacar(self):
        pass

    def morrer(self):
        pass
