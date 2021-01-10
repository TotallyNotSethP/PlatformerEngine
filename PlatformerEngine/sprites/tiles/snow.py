from PlatformerEngine.sprites import Tile


class Snow(Tile):
    def __init__(self, *args, **kwargs):
        super().__init__("snow", *args, **kwargs)
