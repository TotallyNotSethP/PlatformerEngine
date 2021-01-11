from PlatformerEngine import Screen
import pygame


def main():
    with open("testmap.pmap") as f:
        screen_cls = Screen(f)
    for x in range(11):
        for y in range(12):
            sprite = screen_cls.get_sprite((x, y))
            try:
                if sprite:
                    sprite.calculate_pose(screen_cls.get_sprite((x-1, y)),
                                          screen_cls.get_sprite((x+1, y)),
                                          screen_cls.get_sprite((x, y+1)),
                                          screen_cls.get_sprite((x, y-1)))
            except IndexError:
                pass

            if sprite:
                print(f"{sprite.get_pose():^12}", end=" ")
            else:
                print("    None    ", end=" ")
        print()

    running = True
    screen = pygame.display.set_mode((1000, 1000))
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen_cls.update_screen(screen)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
