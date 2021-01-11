import PlatformerEngine
import pygame


class Screen:
    def __init__(self, file, dictionary=PlatformerEngine.dictionary):
        self.sprite_map = []
        self.sprite_group = pygame.sprite.Group()
        self._interpret_file(file, dictionary)

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

    def get_sprite(self, pos):
        return self.sprite_map[pos[0]][pos[1]]

    def move_sprites(self, screen_height):
        x, y = 0, screen_height
        for line in self.sprite_map[::-1]:
            y -= line[0].image.get_height()
            for sprite in line:
                sprite.rect.x, sprite.rect.y = x, y
                x += sprite.image.get_width()
            x = 0

    def update_sprites(self):
        self.sprite_group.update()

    def draw_sprites(self, screen):
        self.move_sprites(screen.get_height())
        self.sprite_group.draw(screen)

    def update_screen(self, screen):
        self.update_sprites()
        self.draw_sprites(screen)
