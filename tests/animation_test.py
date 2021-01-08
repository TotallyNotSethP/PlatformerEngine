from PlatformerEngine import constants
from PlatformerEngine.sprites import Player
from random import choice
import pygame

all_players = ["alienYellow", "alienBeige", "alienBlue", "alienGreen", "alienPink"]
all_poses = ["", "climb", "duck", "hurt", "jump", "stand", "swim", "walk"]


def main():
    pygame.init()

    size = (700, 500)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("PlatformerEngine Animation Test")

    done = False

    player = Player(choice(all_players))
    current_pose = choice(all_poses)
    player.change_pose(current_pose)
    sprites = pygame.sprite.Group()
    sprites.add(player)

    clock = pygame.time.Clock()

    big_font = pygame.font.SysFont('Calibri', 25, True, False)
    small_font = pygame.font.SysFont('Calibri', 10, True, False)

    controls = big_font.render("C: Change Characters | P: Change Pose/Animation", True, constants.WHITE)
    notice = small_font.render(""""C" and "P" generate stuff randomly. This means that it is possible things may not """
                               """change when a key is pressed. Just keep mashing it until it does something :D""",
                               True, constants.WHITE)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_c:
                    player.kill()
                    player = Player(choice(all_players))
                    player.change_pose(current_pose)
                    sprites = pygame.sprite.Group()
                    sprites.add(player)
                elif event.key == pygame.K_p:
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
