from level import Level
import pygame
import sys
from settings import *


class Game:
    def __init__(self):
        self.state = 'menu'  # Start with the menu state
        pygame.init()
        self.screen = pygame.display.set_mode((W,H))
        pygame.display.set_caption("DeltaStar")
        self.clock = pygame.time.Clock()

        self.level = Level()

        # sound
        main_sound = pygame.mixer.Sound('audio/background music.ogg')
        main_sound.set_volume(0.5)
        main_sound.play(-1)


    def run(self):
        while True:
            if self.state == 'menu':
                self.menu_event_check()
                self.show_menu()
            elif self.state == 'running':
                self.game_loop()
            elif self.state == 'dead':
                self.handle_death()
            self.clock.tick(FPS)

    def menu_event_check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state = 'running'

    def show_menu(self):
        self.screen.fill((0,94,255))
        font = pygame.font.Font(UI_Font, 74)
        text = font.render("Press SPACE to start", 1, (255, 255, 255))
        text_rect = text.get_rect(center=(W/2, H/2))
        self.screen.blit(text, text_rect)
        font = pygame.font.Font(UI_Font, 74)
        text = font.render("DeltaStar", 1, (255, 255, 255))
        text_rect = text.get_rect(center=(W/2, H/3))
        self.screen.blit(text, text_rect)
        player_image = pygame.image.load('graphics/player/down/down_0.png')
        new_player_image = pygame.transform.scale(player_image, (300,300))
        self.screen.blit(new_player_image, (700,650))
        enemy_image = pygame.image.load('graphics/enemies/cyclope boss/idle/0.png')
        new_enemy_image = pygame.transform.scale(enemy_image, (400,400))
        self.screen.blit(new_enemy_image, (200,590))
        enemy_image = pygame.image.load('graphics/enemies/racoon boss/idle/0.png')
        new_enemy_image = pygame.transform.scale(enemy_image, (400,400))
        self.screen.blit(new_enemy_image, (1100,590))
        pygame.display.update()

    def game_loop(self):
        while self.state == 'running':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()
                if self.level.player.health <= 0:
                    self.state = 'dead'
                    self.handle_death()

            self.screen.fill("Black")
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


    def handle_death(self):
        # Display death message or screen
        self.screen.fill((0,94,255))
        font = pygame.font.Font(UI_Font, 74)
        text = font.render("Game Over", 1, (255, 255, 255))
        self.screen.blit(text, (570, 250))
        text = font.render("Press R to restart", 1, (255, 255, 255))
        self.screen.blit(text, (300, 800))
        player_image = pygame.image.load('graphics/player/down/down_0.png')
        new_player_image = pygame.transform.scale(player_image, (300,300))
        self.screen.blit(new_player_image, (700,400))

        pygame.display.update()

        # Wait for restart
        waiting_for_restart = True
        while waiting_for_restart:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r: 
                        waiting_for_restart = False

        # Restart game logic
        self.restart_game()

    def restart_game(self):
        self.level = Level() 
        self.state = 'running'  

if __name__ == "__main__":
    game = Game()
    game.run()