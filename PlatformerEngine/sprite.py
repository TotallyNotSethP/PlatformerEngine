import pygame
from PlatformerEngine.constants import BLACK
from time import time


class Sprite(pygame.sprite.Sprite):
    class AnimationManager:
        def __init__(self, frames, fps=5):
            self.frames = frames
            self.frame_index = -1
            self.max_frame_index = len(frames) - 1
            self.last_update = time()
            self.fps = fps

        def get_next_frame(self):
            if time() - self.last_update >= 1 / self.fps:
                self.frame_index += 1
                if self.frame_index > self.max_frame_index:
                    self.frame_index = 0
                self.last_update = time()

            return self.frames[self.frame_index]

    def __init__(self, name, file_ext="png", directory="images"):
        """Loads image {name}.{file_ext}"""
        super().__init__()
        self.name = name
        self.file_ext = file_ext
        self.directory = directory
        try:
            self.poses
        except AttributeError:
            self.poses = {}
        self.pose = None
        self.animation_manager = None
        self._add_pose("", "")
        self.change_pose()
        self.velocity: tuple[int, int] = (0, 0)
        self.auto_reset_velocity = True

    def _set_image(self, image, colorkey=BLACK):
        if type(image) == str:
            self.image = pygame.image.load(image)
        elif type(image) == pygame.Surface:
            self.image = image
        if colorkey:
            self.image.set_colorkey(colorkey)
        self.rect = self.image.get_rect()

    def _add_animation(self, name, separator="_", frame_names=None, fps=5):
        if frame_names is None:
            frame_names = ["1", "2"]

        frames = []
        for frame in frame_names:
            frames.append(pygame.image.load(self.directory + "/" + self.name + separator +
                                            name + frame + "." + self.file_ext))

        self.poses[name] = self.AnimationManager(frames, fps)

    def _add_pose(self, name, separator="_"):
        self.poses[name] = pygame.image.load(self.directory + "/" + self.name + separator + name + "." + self.file_ext)

    def change_pose(self, name=""):
        pose = self.poses[name]
        self.pose = name
        if type(pose) == pygame.Surface:
            self.animation_manager = None
            self._set_image(pose)
        elif type(pose) == self.AnimationManager:
            self.animation_manager = pose

    def update(self):
        if self.animation_manager:
            self._set_image(self.animation_manager.get_next_frame())
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if self.auto_reset_velocity:
            self.velocity = (0, 0)

    def get_pose(self):
        if self.pose:
            return self.pose
        return f"Default Pose"
