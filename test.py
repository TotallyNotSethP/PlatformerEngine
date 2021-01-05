from PlatformerEngine import Player, constants
import pygame


def main():
    pygame.init()

    size = (700, 500)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("PlatformerEngine Test")

    done = False

    player = Player()
    player.change_pose("jump")
    sprites = pygame.sprite.Group()
    sprites.add(player)

    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # TODO: Game logic

        screen.fill(constants.BLACK)

        sprites.update()
        sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()
