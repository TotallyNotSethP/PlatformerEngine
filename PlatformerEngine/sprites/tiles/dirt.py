from PlatformerEngine.sprites import Tile


class Dirt(Tile):
    def __init__(self, *args, **kwargs):
        super().__init__("dirt", *args, **kwargs)
