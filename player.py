import pygame 
from settings import *
from csv_map import import_folder
from entity import Entity


class Player(Entity):
  def __init__(self,pos,groups,obstacle_sprites,attack_weapon,remove_weapon_graphic,create_power):
    super().__init__(groups)
    self.image = pygame.image.load('graphics/test/player.png').convert_alpha()
    self.rect = self.image.get_rect(topleft = pos)
    self.hitbox = self.rect.inflate(0,-10)

    # animation setup
    self.import_player_sprites()
    self.status = 'down'


    # movement limiter
    self.attacking = False
    self.attack_cooldown = 200
    self.attack_time = None
    self.obstacle_sprites = obstacle_sprites

    # weapon direction grpahics
    self.attack_weapon = attack_weapon
    self.weapon_index = 0
    self.weapon = list(weapon_data.keys())[self.weapon_index]
    self.remove_weapon_graphic = remove_weapon_graphic
    self.WeaponSwitch = True
    self.switch_weapon_time = None
    self.switch_duration_cooldown = 150

    # power
    self.create_power = create_power
    self.power_index = 0
    self.power = list(power_data.keys())[self.power_index]
    self.PowerSwitch = True
    self.switch_power_time = None

    # player stats
    self.player_stats = {'health': 150,'energy':70, 'attack': 50, 'power': 5, 'speed': 2}
    self.max_stats = {'health': 700, 'energy': 400, 'attack': 500, 'power': 50, 'speed': 5}
    self.upgrade_cost = {'health': 500, 'energy': 500, 'attack': 500, 'power': 500, 'speed': 500}
    self.health_cost = 10
    self.health = self.player_stats['health']
    self.energy = self.player_stats['energy'] 
    self.exp = 0
    self.speed = self.player_stats['speed']

    # Add health tracking
    self.max_health = 3
    self.health = self.player_stats['health']  # Correctly initialize health to 100, not max_health

    # damage timer
    self.vulnerable = True
    self.hit_time = None
    self.invincibility_duration = 300

    # import sound
    self.weapon_attack_sound = pygame.mixer.Sound('audio/sword.wav')
    self.weapon_attack_sound.set_volume(0.4)

  def receive_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0  # Ensure health doesn't go below 0

    # Update player hearts

  def update_health(self):
        if self.health <= 0:
            pass

  def get_direction(self):
      if self.status.startswith('right'):
          return pygame.math.Vector2(1, 0)
      elif self.status.startswith('left'):
          return pygame.math.Vector2(-1, 0)
      elif self.status.startswith('up'):
          return pygame.math.Vector2(0, -1)
      elif self.status.startswith('down'):
          return pygame.math.Vector2(0, 1)
      return pygame.math.Vector2()

  def input(self):
    if not self.attacking:
      keys = pygame.key.get_pressed()

      # movement
      if keys[pygame.K_w]:
        self.direction.y = -1
        self.status = 'up'
      elif keys[pygame.K_s]:
        self.direction.y = 1
        self.status = 'down'
      else:
        self.direction.y = 0

      if keys[pygame.K_d]:
        self.direction.x = 1
        self.status = 'right'
      elif keys[pygame.K_a]:
        self.direction.x = -1
        self.status = 'left'
      else:
        self.direction.x = 0

      # attack input from the player
      if pygame.mouse.get_pressed()[0] == True:
        self.attacking = True
        self.attack_time = pygame.time.get_ticks()
        self.attack_weapon()
        self.weapon_attack_sound.play()

      # power input from the player
      if keys[pygame.K_q]:
        self.attacking = True
        self.attack_time = pygame.time.get_ticks()
        style = list(power_data.keys())[self.power_index]
        strength = list(power_data.values())[self.power_index]['strength'] + self.player_stats['power']
        cost = list(power_data.values())[self.power_index]['cost']

        self.create_power(style,strength,cost)

      # switch weapon
      if keys[pygame.K_1] and self.WeaponSwitch:
        self.WeaponSwitch = False
        self.switch_weapon_time = pygame.time.get_ticks()
        self.weapon_index = 0
        self.weapon = list(weapon_data.keys())[self.weapon_index]

      if keys[pygame.K_2] and self.WeaponSwitch:
        self.WeaponSwitch = False
        self.switch_weapon_time = pygame.time.get_ticks()
        self.weapon_index = 1
        self.weapon = list(weapon_data.keys())[self.weapon_index]

      if keys[pygame.K_3] and self.WeaponSwitch:
        self.WeaponSwitch = False
        self.switch_weapon_time = pygame.time.get_ticks()
        self.weapon_index = 2
        self.weapon = list(weapon_data.keys())[self.weapon_index]

      if keys[pygame.K_4] and self.WeaponSwitch:
        self.WeaponSwitch = False
        self.switch_weapon_time = pygame.time.get_ticks()
        self.weapon_index = 3
        self.weapon = list(weapon_data.keys())[self.weapon_index]

      if keys[pygame.K_5] and self.WeaponSwitch:
        self.WeaponSwitch = False
        self.switch_weapon_time = pygame.time.get_ticks()
        self.weapon_index = 4
        self.weapon = list(weapon_data.keys())[self.weapon_index]

      # switch power
      for event in pygame.event.get():
        if event.type == pygame.MOUSEWHEEL and self.PowerSwitch:
            self.PowerSwitch = False
            self.switch_power_time = pygame.time.get_ticks()

            if self.power_index < len(list(power_data.keys())) - 1:
                self.power_index += 1
            else:
                self.power_index = 0
            self.power = list(power_data.keys())[self.power_index]


  def get_status(self):

      # idle status
      if self.direction.x == 0 and self.direction.y == 0:
        if not 'idle' in self.status and not 'attack' in self.status:
          self.status = self.status + '_idle'

      if self.attacking:
        self.direction.x = 0
        self.direction.y = 0
        if not 'attack' in self.status:
          if 'idle' in self.status:
            self.status = self.status.replace('_idle','_attack')
          else:
            self.status = self.status + '_attack'
      else:
        if 'attack' in self.status:
          self.status = self.status.replace('_attack','')

  def import_player_sprites(self):
    player_path = 'graphics/player/'
    self.animations = {'up': [],'down': [],'left': [],'right': [],
                       'up_idle': [],'down_idle': [],'left_idle': [],'right_idle': [],
                       'up_attack': [],'down_attack': [],'left_attack': [],'right_attack': []}
    
    for animation in self.animations.keys():
      full_path = player_path + animation
      self.animations[animation] = import_folder(full_path)

  def cooldowns(self):
    current_time = pygame.time.get_ticks()

    if self.attacking:
      if current_time - self.attack_time >= self.attack_cooldown + weapon_data[self.weapon]['cooldown']:
        self.attacking = False
        self.remove_weapon_graphic()

    if not self.WeaponSwitch:
      if current_time - self.switch_weapon_time >= self.switch_duration_cooldown:
        self.WeaponSwitch = True

    if not self.PowerSwitch:
      if current_time - self.switch_power_time >= self.switch_duration_cooldown:
        self.PowerSwitch = True

    if not self.vulnerable:
      if current_time - self.hurt_time >= self.invincibility_duration:
        self.vulnerable = True

  def animate(self):
    animation = self.animations[self.status]

    # loop frame index
    self.frame_index += self.animation_speed
    if self.frame_index >= len(animation):
      self.frame_index = 0

    # print image
    self.image = animation[int(self.frame_index)]
    self.rect = self.image.get_rect(center = self.hitbox.center)

    # flicker
    if not self.vulnerable:
      alpha = self.wave_value()
      self.image.set_alpha(alpha)
    else:
      self.image.set_alpha(255)

  def get_full_weapon_damage(self):
    base_damage = self.player_stats['attack']
    weapon_damage = weapon_data[self.weapon]['damage']

    return base_damage + weapon_damage

  def get_full_power_damage(self):
    base_damage = self.player_stats['attack']
    power_damage = power_data[self.power]['strength']

    return base_damage + power_damage

  def get_value_by_index(self,index):
     return list(self.player_stats.values())[index]
     
  def get_cost_by_index(self,index):
     return list(self.upgrade_cost.values())[index]

  def energy_recovery(self):
    if self.energy < self.player_stats['energy']:
      self.energy += 0.03 * self.player_stats['power']
    else:
      self.energy = self.player_stats['energy']

  def update(self):
    self.input()
    self.cooldowns()
    self.get_status()
    self.animate()
    self.move(self.player_stats['speed'])
    self.energy_recovery()
  