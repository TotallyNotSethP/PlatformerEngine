from PlatformerEngine.sprite import Sprite


class Player(Sprite):
    def __init__(self, name="alienGreen", file_ext="png", directory="images/players", fps=5):
        super().__init__(name, file_ext, directory)
        self._add_animation("climb", fps=fps)
        self._add_animation("swim", fps=fps)
        self._add_animation("walk", fps=fps)
        self._add_pose("duck")
        self._add_pose("hurt")
        self._add_pose("jump")
        self._add_pose("stand")
