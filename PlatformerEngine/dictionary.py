from PlatformerEngine.sprites.tiles import Grass, Sand, Dirt, Castle, Snow

GROUND_TILES_DIRECTORY = "../images/tiles/ground"

dictionary = {
    "0": {
        "class": None,
        "args": (),
        "kwargs": {},
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
}
