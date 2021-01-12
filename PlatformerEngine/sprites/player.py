from PlatformerEngine.sprite import Sprite
from typing import Optional, Union


class Player(Sprite):
    def __init__(self, starting_pos, name="alienGreen", file_ext="png", directory="images/players", fps=5):
        super().__init__(name, file_ext, directory)
        self._add_animation("climb", fps=fps)
        self._add_animation("swim", fps=fps)
        self._add_animation("walk", fps=fps)
        self._add_pose("duck")
        self._add_pose("hurt")
        self._add_pose("jump")
        self._add_pose("stand")
        self.pos = starting_pos
        self.size: tuple[Optional[Union[int, float]], Optional[Union[int, float]]] = (None, None)

    def move(self, relative_pos):
        self.pos[0] += relative_pos[0]
        self.pos[1] += relative_pos[1]

    def update(self):
        if self.size[0] and self.size[1]:
            self.resize(tuple(map(int, self.size)))
        self.rect.center = self.pos
