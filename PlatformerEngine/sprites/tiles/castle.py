from PlatformerEngine.sprites import Tile


class Castle(Tile):
    def __init__(self, *args, **kwargs):
        super().__init__("castle", *args, **kwargs)
