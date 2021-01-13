from PlatformerEngine import GroundTileManager
from PlatformerEngine.sprites import Player
from PlatformerEngine.sprites.tiles import Snow
import pygame

PLAYER_HEIGHT = 50

MIN_MOVEMENT_SPEED = 1
MAX_MOVEMENT_SPEED = 5
movement_speed = MAX_MOVEMENT_SPEED


def main():
    global movement_speed
    pygame.init()

    last_pos = []

    pygame.display.set_mode((700, 500))

    with open("gamemap.pemap") as f:
        ground_tile_manager = GroundTileManager(f)
    ground_tile_manager.calculate_sprite_poses()

    running = True
    screen = pygame.display.set_mode((ground_tile_manager.get_sprite((0, 0)).image.get_width() *
                                      len(ground_tile_manager.sprite_map[0]),
                                      ground_tile_manager.get_sprite((0, 0)).image.get_height() *
                                      len(ground_tile_manager.sprite_map)))
    clock = pygame.time.Clock()
    player = Player([int(screen.get_width() / 2), int(screen.get_height() / 2)])
    # player = Player([0, 0])
    player_group = pygame.sprite.Group(player)

    aspect_ratio = player.image.get_width() / player.image.get_height()
    width = int(PLAYER_HEIGHT * aspect_ratio)
    player.size = (width, PLAYER_HEIGHT)

    w_down, a_down, s_down, d_down = False, False, False, False

    player.move((0, 0))

    ground_tile_manager.update(screen)
    player_group.update()

    while running:
        player_relative_movement = [0, 0]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    w_down = True
                elif event.key == pygame.K_a:
                    a_down = True
                elif event.key == pygame.K_s:
                    s_down = True
                elif event.key == pygame.K_d:
                    d_down = True
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    movement_speed = MIN_MOVEMENT_SPEED
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    w_down = False
                elif event.key == pygame.K_a:
                    a_down = False
                elif event.key == pygame.K_s:
                    s_down = False
                elif event.key == pygame.K_d:
                    d_down = False
                if not (pygame.key.get_mods() & pygame.KMOD_SHIFT):
                    movement_speed = MAX_MOVEMENT_SPEED

        last_pos.append(player.pos[:])
        if len(last_pos) > 2:
            last_pos.pop(0)

        if w_down and player.rect.y > movement_speed - 1:
            player_relative_movement[1] -= movement_speed
        if a_down and player.rect.x > movement_speed - 1:
            player_relative_movement[0] -= movement_speed
        if s_down and player.rect.y < screen.get_height() - player.image.get_height() - movement_speed - 1:
            player_relative_movement[1] += movement_speed
        if d_down and player.rect.x < screen.get_width() - player.image.get_width() - movement_speed - 1:
            player_relative_movement[0] += movement_speed

        player.move(player_relative_movement)

        for sprite in pygame.sprite.spritecollide(player, ground_tile_manager.sprite_group, False,
                                                  pygame.sprite.collide_mask):
            if type(sprite) == Snow:
                player.pos = last_pos[0][:]

        ground_tile_manager.update(screen)
        player_group.update()
        player_group.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
