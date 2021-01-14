from PlatformerEngine import Sprite
import random


class Coin(Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__("coin", *args, set_default_img=False, **kwargs)
        self._add_pose("Gold", "")
        self._add_pose("Silver", "")
        self._add_pose("Bronze", "")
        self.change_pose(random.choice(["Gold", "Silver", "Silver", "Bronze", "Bronze", "Bronze", "Bronze", "Bronze"]))

    def calculate_pose(self, *args, **kwargs):
        pass

    def __bool__(self):
        return False
