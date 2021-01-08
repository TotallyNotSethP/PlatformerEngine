from PlatformerEngine.sprites import Tile
from typing import Optional

positions = ["above", "below", "to the left", "to the right"]


def main():
    tiles: list[Optional[Tile]] = [Tile(directory="../images/tiles/ground") for _ in range(5)]

    for i, tile in enumerate(tiles[1:]):
        pose = input(f"Pose for tile {positions[i]}? ")
        if pose == "None":
            tiles[i+1] = None
        else:
            tile.change_pose(pose)

    tiles[0].calculate_pose(*tiles[1:])
    print(tiles[0].pose)


if __name__ == "__main__":
    main()
