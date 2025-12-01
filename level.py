import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from csv_map import *
from random import choice
from weapon import Weapon
from UserInterface import UserInterface
from enemy import Enemy
from particles import AnimationPlayer
from power import PlayerPower
from upgrade import Upgrade

class Level:
    def __init__(self):

        self.display_surface = pygame.display.get_surface()
        self.game_paused = False

        # sprite group
        self.visible_sprites = CameraGroup()

        self.obstacle_sprites = pygame.sprite.Group()

        # attack
        self.current_attack = None

        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

        # Sprite Setup
        self.create_map()

        # User Interface
        self.UI = UserInterface(self.player)
        self.upgrade = Upgrade(self.player)

        # particle effects
        self.animation_player = AnimationPlayer()
        self.playerpower = PlayerPower(self.animation_player)
        self.weapon_player = AnimationPlayer()




    def create_map(self):
        layouts = {
            'boundary': import_csv_layout("map/FloorBlock.csv"),
            'rocks': import_csv_layout('map/Rocks.csv'),
            'object': import_csv_layout('map/Objects copy.csv'),
            'tree': import_csv_layout('map/nus_trees.csv'),
            'entities': import_csv_layout('map/latest_enemy.csv'),

        }
        graphics = {
            'rocks': import_folder("graphics/Rocks"),
            'objects': import_folder("graphics/Objects"),
            'trees': import_folder("graphics/tree"),
        }

        for style,layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '0':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        # Create tiles
                        if style == 'boundary':
                            Tile((x,y),[self.obstacle_sprites],'invisible')
                        if style == 'rocks':
                            surf = graphics['rocks'][int(col)]
                            Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'rocks', surf)
                        if style == 'object':
                            surf = graphics['objects'][int(col)]
                            Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'object', surf)
                        if style == 'tree':
                            surf = graphics['trees'][int(col)]
                            Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'tree', surf)

                        if style == 'entities':
                            if col == '17':
                                self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites,self.attack_weapon,self.remove_weapon_graphics,self.create_power)
                            else:
                                if col == '1': enemy_name = 'wintermushroom'
                                elif col == '2': enemy_name = 'snake'
                                elif col == '3': enemy_name = 'slime'
                                elif col == '4': enemy_name = 'skull'
                                elif col == '5': enemy_name = 'redEye'
                                elif col == '6': enemy_name = 'reptile'
                                elif col == '7': enemy_name = 'racoon'
                                elif col == '8': enemy_name = 'mushroom'
                                elif col == '9': enemy_name = 'lizard'
                                elif col == '10': enemy_name = 'goldenRacoon'
                                elif col == '11': enemy_name = 'cyclope'
                                elif col == '12': enemy_name = 'spirit boss'
                                elif col == '13': enemy_name = 'racoon boss'
                                elif col == '14': enemy_name = 'cyclope boss'
                                elif col == '15': enemy_name = 'winterreptile'
                                else: enemy_name = 'wintereye'
                                Enemy(enemy_name,(x,y),[self.visible_sprites,self.attackable_sprites],self.obstacle_sprites,self.damage_player,self.death_particle,self.add_exp)
   

    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite,self.attackable_sprites,False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        target_sprite.get_damage(self.player,attack_sprite.sprite_type)

    def remove_weapon_graphics(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def damage_player(self,amount,attack_type):
        if self.player.vulnerable:
            self.player.health -= amount
            self.player.vulnerable = False
            self.player.hurt_time = pygame.time.get_ticks()
            self.animation_player.create_particles(attack_type,self.player.rect.center,[self.visible_sprites])

    def toggle_menu(self):
        self.game_paused = not self.game_paused
        

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.UI.display(self.player)
        self.player.update_health()
        self.UI.display_hearts(self.display_surface, self.player)

        if self.game_paused:
            self.upgrade.display()
        else:
            self.visible_sprites.update()
            self.visible_sprites.enemy_update(self.player)
            self.player_attack_logic()

    def attack_weapon(self):
        self.current_attack = Weapon(self.player,[self.visible_sprites,self.attack_sprites])
    
    def create_power(self,style,strength,cost):
        if style =='flame':
            self.playerpower.flame(self.player,cost,[self.visible_sprites,self.attack_sprites])

        if style =='heal':
            self.playerpower.heal(self.player,strength,cost,[self.visible_sprites])

        if style =='blue projectile':
            self.playerpower.blue_projectile(self.player, cost, [self.visible_sprites, self.attack_sprites])

        if style =='red projectile':
            self.playerpower.red_projectile(self.player, cost, [self.visible_sprites, self.attack_sprites])

    def add_exp(self,amount):
        self.player.exp += amount

    def death_particle(self,pos,particle_type):
        self.animation_player.create_particles(particle_type,pos,[self.visible_sprites])

class CameraGroup(pygame.sprite.Group):
  def __init__(self):
    super().__init__()
    self.display_surface = pygame.display.get_surface()
    self.half_width = self.display_surface.get_size()[0] // 2 
    self.half_height = self.display_surface.get_size()[1] // 2
    self.offset = pygame.math.Vector2()

    # Camera view
    self.zoom_width = self.half_width // 1.65
    self.zoom_height = self.half_height // 1.65

    # New surface for zooming
    self.zoom_surface = pygame.Surface((self.zoom_width, self.zoom_height))

    # getting floor
    self.floor_surf = pygame.image.load("graphics/tilemap/ground1.png").convert()
    self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

  def custom_draw(self,player):
    # get offset
    self.offset.x = player.rect.centerx - self.zoom_width // 2
    self.offset.y = player.rect.centery - self.zoom_height // 2

    # drawing floor
    floor_offset_pos = self.floor_rect.topleft - self.offset
    self.zoom_surface.blit(self.floor_surf,floor_offset_pos)

    for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
        offset_pos = sprite.rect.topleft - self.offset
        self.zoom_surface.blit(sprite.image,offset_pos)

    # Scale up the zoom surface and blit it onto the display surface
    zoomed_surface = pygame.transform.scale(self.zoom_surface, self.display_surface.get_size())
    self.display_surface.blit(zoomed_surface, (0, 0))

  def enemy_update(self, player):
    enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
    for enemy in enemy_sprites:
        enemy.enemy_update(player)