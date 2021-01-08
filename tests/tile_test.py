from PlatformerEngine import constants
from PlatformerEngine.sprites import Tile
import pygame
from random import choice

all_players = ["castle", "grass", "dirt", "sand", "snow"]
all_poses = ["", "Center", "Center_rounded", "CliffLeft", "CliffLeftAlt", "CliffRight", "CliffRightAlt", "Half",
             "HalfLeft", "HalfMid", "HalfRight", "HillLeft", "HillLeft2", "HillRight", "HillRight2", "LedgeLeft",
             "LedgeRight", "Left", "Mid", "Right"]


def main():
    pygame.init()

    size = (700, 500)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("PlatformerEngine Tileset Test")

    done = False

    player = Tile(choice(all_players), directory="../images/tiles/ground")
    current_pose = choice(all_poses)
    player.change_pose(current_pose)
    sprites = pygame.sprite.Group()
    sprites.add(player)

    clock = pygame.time.Clock()

    big_font = pygame.font.SysFont("Calibri", 25, True, False)
    small_font = pygame.font.SysFont("Calibri", 10, True, False)

    controls = big_font.render("T: Change Theme | S: Change Shape", True, constants.WHITE)
    notice = small_font.render(""""T" and "S" generate stuff randomly. This means that it is possible things may not """
                               """change when a key is pressed. Just keep mashing it until it does something :D""",
                               True, constants.WHITE)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_t:
                    player.kill()
                    player = Tile(choice(all_players), directory="../images/tiles/ground")
                    player.change_pose(current_pose)
                    sprites = pygame.sprite.Group()
                    sprites.add(player)
                elif event.key == pygame.K_s:
                    current_pose = choice(all_poses)
                    player.change_pose(current_pose)

        # TODO: Game logic

        screen.fill(constants.BLACK)

        sprites.update()
        player.rect.center = (int(size[0] / 2), int(size[1] / 2))

        sprites.draw(screen)
        screen.blit(controls, [10, 10])
        screen.blit(notice, [10, 40])

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()
