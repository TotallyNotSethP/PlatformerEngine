import time

import pygame

from PlatformerEngine import GroundTileManager, constants
from PlatformerEngine.sprites import Player, Coin


PLAYER_HEIGHT = 50

MIN_MOVEMENT_SPEED = 1
MAX_MOVEMENT_SPEED = 5

VERSION = "Release v1.1.0 - GNU General Public License"


def setup():
    global last_pos, score, running, screen, clock, player, player_group, game_over, score_font, help_font, help_text
    global aspect_ratio, width, w_down, a_down, s_down, d_down, movement_speed, start_time, ground_tile_manager
    global bg_image, version_text, coin_sound, you_win_sound
    last_pos = []
    score = 0

    pygame.display.set_mode((1, 1))

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

    game_over = False

    score_font = pygame.font.SysFont("Comic Sans MS", 24)
    help_font = pygame.font.SysFont("Calibri", 15)
    help_text = help_font.render("Gold: $1.50, Silver: $1.25, Bronze: $1.00, Get $50 to win!", True, constants.WHITE)

    version_font = pygame.font.SysFont("Calibri", 10)
    version_text = version_font.render(VERSION, True, constants.WHITE)

    aspect_ratio = player.image.get_width() / player.image.get_height()
    width = int(PLAYER_HEIGHT * aspect_ratio)
    player.size = (width, PLAYER_HEIGHT)

    w_down, a_down, s_down, d_down = False, False, False, False
    movement_speed = MAX_MOVEMENT_SPEED

    player.move((0, 0))
    player.change_pose("swim")

    bg_image = pygame.image.load("images/background.jpg")
    aspect_ratio = bg_image.get_height() / bg_image.get_width()
    width = screen.get_width()
    height = int(width * aspect_ratio)
    new_size = (width, height)
    bg_image = pygame.transform.scale(bg_image, new_size)

    coin_sound = pygame.mixer.Sound("sfx/coin_sound.ogg")
    coin_sound.set_volume(0.1)

    you_win_sound = pygame.mixer.Sound("sfx/you_win_sound.ogg")


def text_screen(line1="Astro's", line2="Speedrun", line3="Challenge", subtitle_text="Press Q To Continue",
                line1_font_size=50, e_callback=None, no_sidebars=False):
    global last_pos, score, running, screen, clock, player, player_group, game_over, score_font, help_font, help_text
    global aspect_ratio, width, w_down, a_down, s_down, d_down, movement_speed, start_time, ground_tile_manager
    global bg_image, version_text
    
    title_font = pygame.font.SysFont("Segoe Print", 50)
    title1_font = pygame.font.SysFont("Segoe Print", line1_font_size)
    title1 = title1_font.render(line1, True, constants.WHITE)
    title2 = title_font.render(line2, True, constants.WHITE)
    title3 = title_font.render(line3, True, constants.WHITE)

    font = pygame.font.SysFont("Calibri", 20)

    if not no_sidebars:
        sidebar_title_font = pygame.font.SysFont("Segoe Print", 30, True)
        left_sidebar_title = sidebar_title_font.render("Story", True, constants.WHITE)
        right_sidebar_title = sidebar_title_font.render("Controls", True, constants.WHITE)
        left_sidebar_content1 = font.render("*gasp* The PS5 is on sale for only $50!", True, constants.WHITE)
        left_sidebar_content2 = font.render("But you need to act fast.", True,
                                            constants.WHITE)
        left_sidebar_content3 = font.render("The sale expires in 20 seconds!", True, constants.WHITE)
        left_sidebar_content4 = font.render("You rush to the money planet at the speed of light.", True, constants.WHITE)
        left_sidebar_content5 = font.render("Can you collect enough money to buy it?!?!", True, constants.WHITE)
        right_sidebar_content1 = font.render("WASD: Movement", True, constants.WHITE)
        right_sidebar_content2 = font.render("Shift: Hold to go slower", True, constants.WHITE)

    subtitle = font.render(subtitle_text, True, constants.WHITE)

    titlescreenrunning = True
    
    while titlescreenrunning:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    titlescreenrunning = False
                elif event.key == pygame.K_e and e_callback:
                    e_callback()
                    titlescreenrunning = False
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(bg_image, (0, 0))
        screen.blit(title1, (int((screen.get_width() / 2) - (title1.get_width() / 2)),
                             int((screen.get_height() / 2) - (title1.get_height() / 2)) - 60))
        screen.blit(title2, (int((screen.get_width() / 2) - (title2.get_width() / 2)),
                             int((screen.get_height() / 2) - (title2.get_height() / 2))))
        screen.blit(title3, (int((screen.get_width() / 2) - (title3.get_width() / 2)),
                             int((screen.get_height() / 2) - (title3.get_height() / 2)) + 60))
        screen.blit(subtitle, (int((screen.get_width() / 2) - (subtitle.get_width() / 2)),
                               int((screen.get_height() / 2) - (subtitle.get_height() / 2)) + 110))
        screen.blit(version_text, (5, screen.get_height() - 15))

        if not no_sidebars:
            screen.blit(right_sidebar_title, (int((screen.get_width() / 4 * 3) - (right_sidebar_title.get_width() / 2) + 50),
                                              int((screen.get_height() / 2) - (right_sidebar_title.get_height() / 2)) - 30))
            screen.blit(right_sidebar_content1,
                        (int((screen.get_width() / 4 * 3) - (right_sidebar_content1.get_width() / 2) + 50),
                         int((screen.get_height() / 2) - (right_sidebar_content1.get_height() / 2))))
            screen.blit(right_sidebar_content2,
                        (int((screen.get_width() / 4 * 3) - (right_sidebar_content2.get_width() / 2) + 50),
                         int((screen.get_height() / 2) - (right_sidebar_content2.get_height() / 2)) + 20))
            screen.blit(left_sidebar_title, (int((screen.get_width() / 4) - (left_sidebar_title.get_width() / 2) - 50),
                                              int((screen.get_height() / 2) - (left_sidebar_title.get_height() / 2)) - 50))
            screen.blit(left_sidebar_content1,
                        (int((screen.get_width() / 4) - (left_sidebar_content1.get_width() / 2) - 50),
                         int((screen.get_height() / 2) - (left_sidebar_content1.get_height() / 2)) - 20))
            screen.blit(left_sidebar_content2,
                        (int((screen.get_width() / 4) - (left_sidebar_content2.get_width() / 2) - 50),
                         int((screen.get_height() / 2) - (left_sidebar_content2.get_height() / 2))))
            screen.blit(left_sidebar_content3,
                        (int((screen.get_width() / 4) - (left_sidebar_content3.get_width() / 2) - 50),
                         int((screen.get_height() / 2) - (left_sidebar_content3.get_height() / 2)) + 20))
            screen.blit(left_sidebar_content4,
                        (int((screen.get_width() / 4) - (left_sidebar_content4.get_width() / 2) - 50),
                         int((screen.get_height() / 2) - (left_sidebar_content4.get_height() / 2)) + 40))
            screen.blit(left_sidebar_content5,
                        (int((screen.get_width() / 4) - (left_sidebar_content5.get_width() / 2) - 50),
                         int((screen.get_height() / 2) - (left_sidebar_content5.get_height() / 2)) + 60))
        pygame.display.flip()
        clock.tick(60)


def main():
    global last_pos, score, running, screen, clock, player, player_group, game_over, score_font, help_font, help_text
    global aspect_ratio, width, w_down, a_down, s_down, d_down, movement_speed, start_time, ground_tile_manager
    global bg_image, coin_sound, version_text, you_win_sound

    pygame.init()
    pygame.mixer.music.load('music/bg_music.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)

    setup()

    text_screen()

    start_time = time.time()

    ground_tile_manager.update(screen)
    player_group.update()

    while running:
        player_relative_movement = [0, 0]
        time_remaining = 0.0
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
                elif event.key == pygame.K_SPACE and game_over:
                    setup()
                    game_over = False
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
            if sprite:
                player.pos = last_pos[0][:]
            if type(sprite) == Coin:
                coin_sound.play()
                if sprite.pose == "Gold":
                    score += 1.5
                elif sprite.pose == "Silver":
                    score += 1.25
                else:
                    score += 1
                sprite.kill()

        time_remaining = -(time.time() - start_time - 20)

        screen.blit(bg_image, (0, 0))

        ground_tile_manager.update(screen)
        player_group.update()
        player_group.draw(screen)

        score_text = score_font.render(f"Money: ${score:.2f}, Time Left: {time_remaining:.2f}", True, constants.WHITE)
        screen.blit(score_text, (5, 5))
        screen.blit(help_text, (5, 40))
        screen.blit(version_text, (5, screen.get_height() - 15))

        pygame.display.flip()

        def main_menu():
            pygame.mixer.music.set_volume(0.5)
            text_screen()

        if score == 50:
            pygame.mixer.music.set_volume(0)
            time.sleep(0.1)
            you_win_sound.play()
            text_screen("You win!",
                        "You got $50 in",
                        f"just {20 - time_remaining:.2f} seconds!",
                        "Press Q To Play Again; Press E To Go To The Main Menu", 100, main_menu, True)
            pygame.mixer.music.set_volume(0.5)
            setup()
            start_time = time.time()

            ground_tile_manager.update(screen)
            player_group.update()

        elif score >= 50:
            pygame.mixer.music.set_volume(0)
            time.sleep(0.1)
            you_win_sound.play()
            text_screen("You win!",
                        "You got over $50 in",
                        f"just {20 - time_remaining:.2f} seconds!",
                        "Press Q To Play Again; Press E To Go To The Main Menu", 100, main_menu, True)
            pygame.mixer.music.set_volume(0.5)
            setup()
            start_time = time.time()

            ground_tile_manager.update(screen)
            player_group.update()

        elif time.time() - start_time >= 20:
            text_screen("So close!",
                        f"You got ${score:.2f} in",
                        "20 seconds.",
                        "Press Q To Try Again; Press E To Go To The Main Menu", 100, text_screen, True)
            setup()
            start_time = time.time()

            ground_tile_manager.update(screen)
            player_group.update()

    clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()
