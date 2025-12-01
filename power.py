import pygame
from settings import *
from random import randint

class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos, direction, projectile_type, groups):
        super().__init__(groups)
        self.original_image = pygame.image.load(f'graphics/particles/{projectile_type}/{projectile_type}.png').convert_alpha()
        self.image = self.original_image  # This will be the rotated image
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(pos)
        self.direction = direction.normalize()
        self.speed = 5
        self.distance = 1
        self.max_distance = 250
        self.sprite_type = 'projectile'

        # Rotate the sprite to match the direction
        self.rotate()

    def rotate(self):
        angle = self.direction.angle_to(pygame.math.Vector2(0, -1))
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        self.pos += self.direction * self.speed
        self.rect.center = self.pos
        self.distance += self.speed
        if self.distance >= self.max_distance:
            self.kill()


class PlayerPower:
    def __init__(self,animation_player):
        self.animation_player = animation_player
        self.sounds = {
            'heal': pygame.mixer.Sound('audio/heal.wav'),
            'flame': pygame.mixer.Sound('audio/Fire.wav'),
            'projectile': pygame.mixer.Sound('audio/projectile.wav')
            }
        

    def flame(self, player,cost,groups):
        if player.energy >= cost:
            player.energy -= cost
            self.sounds['flame'].play()

            if player.status.split('_')[0] == 'right':
                direction = pygame.math.Vector2(1,0)
            elif player.status.split('_')[0] == 'left':
                direction = pygame.math.Vector2(-1,0)
            elif player.status.split('_')[0] == 'up':
                direction = pygame.math.Vector2(0,-1)
            else:
                direction = pygame.math.Vector2(0,1)

            for i in range(1,6):
                if direction.x:
                    offset_x = (direction.x * i) * TILESIZE
                    x = player.rect.centerx + offset_x + randint(-TILESIZE // 3,TILESIZE // 3)
                    y = player.rect.centery + randint(-TILESIZE // 3,TILESIZE // 3)
                    self.animation_player.create_particles('flame',(x,y),groups)

                else:
                    offset_y = (direction.y * i) * TILESIZE
                    x = player.rect.centerx + randint(-TILESIZE // 3,TILESIZE // 3)
                    y = player.rect.centery + offset_y +randint(-TILESIZE // 3,TILESIZE // 3)
                    self.animation_player.create_particles('flame',(x,y),groups)


    def heal(self,player,strength,cost,groups):
        if player.energy >= cost:
            self.sounds['heal'].play()
            player.health += strength
            player.energy -= cost
            self.animation_player.create_particles('heal',player.rect.center,groups)
            if player.health >= player.player_stats['health']:
                player.health = player.player_stats['health']



    def blue_projectile(self, player, cost, groups):
        if player.energy >= cost:
            player.energy -= cost
            self.sounds['projectile'].play()
            direction = player.get_direction()
            Projectile(player.rect.center, direction, 'blue projectile', groups)

    def red_projectile(self, player, cost, groups):
        if player.energy >= cost:
            player.energy -= cost
            self.sounds['projectile'].play()
            direction = player.get_direction()
            Projectile(player.rect.center, direction, 'red projectile', groups)

