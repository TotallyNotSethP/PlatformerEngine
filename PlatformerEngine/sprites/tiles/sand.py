from PlatformerEngine.sprites import Tile


class Sand(Tile):
    def __init__(self, *args, **kwargs):
        super().__init__("sand", *args, **kwargs)
