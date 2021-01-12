from PlatformerEngine import GroundTileManager
import pygame


def main():
    with open("testmap.pemap") as f:
        ground_tile_manager = GroundTileManager(f)
    ground_tile_manager.calculate_sprite_poses()

    running = True
    screen = pygame.display.set_mode((ground_tile_manager.get_sprite((0, 0)).image.get_width() *
                                      len(ground_tile_manager.sprite_map[0]),
                                      ground_tile_manager.get_sprite((0, 0)).image.get_height() *
                                      len(ground_tile_manager.sprite_map)))
    clock = pygame.time.Clock()
    l_key_down, r_key_down = False, False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    l_key_down = True
                elif event.key == pygame.K_RIGHT:
                    r_key_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    l_key_down = False
                elif event.key == pygame.K_RIGHT:
                    r_key_down = False

        if l_key_down:
            ground_tile_manager.move_screen(5)
        if r_key_down:
            ground_tile_manager.move_screen(-5)

        ground_tile_manager.update(screen)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
