import PlatformerEngine
import pygame


class GroundTileManager:
    def __init__(self, file, dictionary=PlatformerEngine.dictionary):
        self.sprite_map = []
        self.sprite_group = pygame.sprite.Group()
        self._interpret_file(file, dictionary)
        self.x_offset = 0

    def _interpret_file(self, file, dictionary):
        for i, line in enumerate(file.readlines()):
            self.sprite_map.append([])
            for char in line.split(","):
                char = char.strip()
                if dictionary[char]["class"]:
                    sprite = dictionary[char]["class"](*dictionary[char]["args"], **dictionary[char]["kwargs"])
                    self.sprite_map[i].append(sprite)
                    self.sprite_group.add(sprite)
                else:
                    self.sprite_map[i].append(None)

    def calculate_sprite_poses(self):
        for x, line in enumerate(self.sprite_map):
            for y, sprite in enumerate(line):
                try:
                    if sprite:
                        sprite.calculate_pose(self.get_sprite((x - 1, y)),
                                              self.get_sprite((x + 1, y)),
                                              self.get_sprite((x, y + 1)),
                                              self.get_sprite((x, y - 1)))
                except IndexError:
                    pass

    def get_sprite(self, pos):
        return self.sprite_map[pos[0]][pos[1]]

    def move_sprites(self, screen_height):
        x, y = self.x_offset, screen_height
        for line in self.sprite_map[::-1]:
            y -= line[0].image.get_height()
            for sprite in line:
                sprite.rect.x, sprite.rect.y = x, y
                x += sprite.image.get_width()
            x = self.x_offset

    def move_screen(self, amount):
        self.x_offset += amount

    def update_sprites(self, screen_size):
        self.sprite_group.update()
        self.move_sprites(screen_size[0])
        self.resize_sprites(screen_size[1])

    def resize_sprites(self, screen_width):
        for line in self.sprite_map:
            for sprite in line:
                aspect_ratio = sprite.image.get_width() / sprite.image.get_height()
                width = screen_width / len(self.sprite_map)
                height = width * aspect_ratio
                sprite.resize((int(width), int(height)))

    def draw_sprites(self, screen):
        self.move_sprites(screen.get_height())
        self.sprite_group.draw(screen)

    def update(self, screen): #, color=PlatformerEngine.constants.BLACK):
        #screen.fill(color)
        self.update_sprites(screen.get_size())
        self.draw_sprites(screen)
