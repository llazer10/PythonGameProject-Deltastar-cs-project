from typing import Any
import pygame
from csv_map import import_folder

class AnimationPlayer:
    def __init__(self):
        self.frames = {
            # power
            'flame': import_folder('graphics/particles/flame/frames'),
            'heal': import_folder('graphics/particles/heal/frames'),
            'blue projectile': import_folder('graphics/particles/blue projectile/frames'),
            'red projectile': import_folder('graphics/particles/red projectile/frames'),

            # attacks
            'slash': import_folder('graphics/particles/slash'),
            'slash curved': import_folder('graphics/particles/slash curved'),
            'bossthunder': import_folder('graphics/particles/bossthunder'),
            'bossice': import_folder('graphics/particles/bossice'),
            'cyclopebossflam': import_folder('graphics/particles/cyclopebossflam'),

            # enemy deaths
            'slime': import_folder('graphics/particles/death'),
            'snake': import_folder('graphics/particles/death'),
            'racoon': import_folder('graphics/particles/death'),
            'reptile': import_folder('graphics/particles/death'),
            'mushroom': import_folder('graphics/particles/death'),
            'wintereye': import_folder('graphics/particles/death'),
            'wintermushroom': import_folder('graphics/particles/death'),
            'winterreptile': import_folder('graphics/particles/death'),
            'lizard': import_folder('graphics/particles/death'),
            'goldenRacoon': import_folder('graphics/particles/death'),
            'redEye': import_folder('graphics/particles/death'),
            'skull': import_folder('graphics/particles/death'),
            'cyclope': import_folder('graphics/particles/death'),
            'cyclope boss': import_folder('graphics/particles/death'),
            'racoon boss': import_folder('graphics/particles/death'),
            'spirit boss': import_folder('graphics/particles/death'),
        }

    def create_particles(self,animation_type,pos,groups):
        animation_frames = self.frames[animation_type]
        ParticleEffect(pos,animation_frames,groups)

class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self,pos,animation_frames,groups):
        super().__init__(groups)
        self.sprite_type = 'power'
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()
