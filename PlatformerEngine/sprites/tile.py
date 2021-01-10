from PlatformerEngine import Sprite


class Tile(Sprite):
    def __init__(self, name="grass", file_ext="png", directory="images/tiles/ground"):
        super().__init__(name, file_ext, directory)
        self._add_pose("Center", "")
        self._add_pose("Center_rounded", "")
        self._add_pose("CliffLeft", "")
        self._add_pose("CliffLeftAlt", "")
        self._add_pose("CliffRight", "")
        self._add_pose("CliffRightAlt", "")
        self._add_pose("Half", "")
        self._add_pose("HalfLeft", "")
        self._add_pose("HalfMid", "")
        self._add_pose("HalfRight", "")
        self._add_pose("HillLeft", "")
        self._add_pose("HillLeft2", "")
        self._add_pose("HillRight", "")
        self._add_pose("HillRight2", "")
        self._add_pose("LedgeLeft", "")
        self._add_pose("LedgeRight", "")
        self._add_pose("Left", "")
        self._add_pose("Mid", "")
        self._add_pose("Right", "")

    def calculate_pose(self, above, below, left, right):
        prev_pose = self.pose
        if above:
            if above.pose == "HillLeft":
                self.change_pose("HillLeft2")
            elif above.pose == "HillRight":
                self.change_pose("HillRight2")
            else:
                self.change_pose("Center")
        else:
            if (not right) and left and below:
                self.change_pose("HillLeft")
            elif right and (not left) and below:
                self.change_pose("HillRight")
            elif (not left) and (not right) and (not below):
                self.change_pose()
            elif (not left) and (not below):
                self.change_pose("CliffLeft")
            elif (not right) and (not below):
                self.change_pose("CliffRight")
            else:
                self.change_pose("Mid")

        return self.pose != prev_pose

    def __bool__(self):
        return True
