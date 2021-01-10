from PlatformerEngine.sprites import Tile
import pygame


class Empty(Tile):
    def __init__(self, directory="images/tiles/ground", *args, **kwargs):
        self.poses = {"": pygame.image.load(directory + "/empty.png")}
        super().__init__("empty", *args, **kwargs)

    def _add_pose(self, *args, **kwargs):
        pass

    def change_pose(self, *args, **kwargs):
        super().change_pose()

    def __bool__(self):
        return False
