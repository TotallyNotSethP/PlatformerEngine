from PlatformerEngine.sprite import Sprite


class Player(Sprite):
    def __init__(self, name="alienGreen", file_ext="png", directory="images/players"):
        super().__init__(name, file_ext, directory)
        self._add_animation("climb")
        self._add_animation("swim")
        self._add_animation("walk")
        self._add_pose("duck")
        self._add_pose("hurt")
        self._add_pose("jump")
        self._add_pose("stand")
