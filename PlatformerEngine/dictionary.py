from PlatformerEngine.sprites.tiles import Grass, Sand, Dirt, Castle, Snow, Empty
from PlatformerEngine.sprites import Coin, pickone

GROUND_TILES_DIRECTORY = "images/tiles/ground"

dictionary = {
    "0": {
        "class": Empty,
        "args": (),
        "kwargs": {"directory": GROUND_TILES_DIRECTORY},
    },
    "1": {
        "class": Grass,
        "args": (),
        "kwargs": {"directory": GROUND_TILES_DIRECTORY},
    },
    "2": {
        "class": Sand,
        "args": (),
        "kwargs": {"directory": GROUND_TILES_DIRECTORY},
    },
    "3": {
        "class": Dirt,
        "args": (),
        "kwargs": {"directory": GROUND_TILES_DIRECTORY},
    },
    "4": {
        "class": Castle,
        "args": (),
        "kwargs": {"directory": GROUND_TILES_DIRECTORY},
    },
    "5": {
        "class": Snow,
        "args": (),
        "kwargs": {"directory": GROUND_TILES_DIRECTORY},
    },
    "6": {
        "class": pickone,
        "args": ([
                     [Coin, (), {"directory": "images/items"}],
                     [Coin, (), {"directory": "images/items"}],
                     [Coin, (), {"directory": "images/items"}],
                     [Empty, (), {"directory": GROUND_TILES_DIRECTORY}],
                 ],),
        "kwargs": {}
    }
}
