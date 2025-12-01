import pygame
from settings import *

class UserInterface:
    def __init__(self, player):
        self.player = player
        # Font
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_Font,18)

        # Hearts
        self.full_heart = pygame.image.load('graphics/hearts/full heart.png').convert_alpha()
        self.half_heart = pygame.image.load('graphics/hearts/half heart.png').convert_alpha()
        self.empty_heart = pygame.image.load('graphics/hearts/empty heart.png').convert_alpha()

        self.full_heart = pygame.transform.scale(pygame.image.load('graphics/hearts/full heart.png').convert_alpha(), (30, 30))
        self.half_heart = pygame.transform.scale(pygame.image.load('graphics/hearts/half heart.png').convert_alpha(), (30, 30))
        self.empty_heart = pygame.transform.scale(pygame.image.load('graphics/hearts/empty heart.png').convert_alpha(), (30, 30))
    
        # energy bar
        self.energy_bar_rect = pygame.Rect(10,50,ENERGY_BAR_WIDTH,BAR_HEIGHT)

        # import power graphics
        self.power_graphics = []
        new_power_size = (50, 50)  # New size for the power images
        for power in power_data.values():
            power_image = pygame.image.load(power['graphic']).convert_alpha()
            power_image = pygame.transform.scale(power_image, new_power_size)  # Scale the image
            self.power_graphics.append(power_image)
        

    def show_bar(self,current,max_amount,background_rect,colour):
         # draw background
         pygame.draw.rect(self.display_surface,UI_BG_COLOUR,background_rect)

         # convert stats
         ratio = current / max_amount
         current_width = background_rect.width * ratio
         current_rect = background_rect.copy()
         current_rect.width = current_width

         # draw energy bar
         pygame.draw.rect(self.display_surface,colour,current_rect)
         pygame.draw.rect(self.display_surface,UI_BORDER_COLOUR,background_rect,4)
         
    def display(self,player):
        self.show_bar(player.energy,player.player_stats['energy'],self.energy_bar_rect,ENERGY_COLOUR)

        self.show_exp(player.exp)

        self.weapon_overlay()
        self.power_overlay(player.power_index,not player.PowerSwitch)


    def show_exp(self,exp):
         text_surf = self.font.render(str(int(exp)),False,TEXT_COLOUR)
         text_rect = text_surf.get_rect(bottomleft = (10,H - 10))
         pygame.draw.rect(self.display_surface,UI_BG_COLOUR,text_rect.inflate(10,10))
         self.display_surface.blit(text_surf,text_rect)

    def select_box(self,left,top):
         background_rect = pygame.Rect(left,top,ITEM_BOX_SIZE,ITEM_BOX_SIZE)
         pygame.draw.rect(self.display_surface,UI_BG_COLOUR,background_rect)
         pygame.draw.rect(self.display_surface,UI_BORDER_COLOUR,background_rect,3)
         return background_rect
    
    def select_box2(self,left,top, has_switched):
        background_rect = pygame.Rect(left,top,ITEM_BOX_SIZE,ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface,UI_BG_COLOUR,background_rect)
        if has_switched:
            pygame.draw.rect(self.display_surface,UI_BORDER_COLOUR_ACTIVE,background_rect,3)
        else:
            pygame.draw.rect(self.display_surface,UI_BORDER_COLOUR,background_rect,3)
        return background_rect

    def weapon_overlay(self):
        weapon_positions = [620, 710, 800, 890, 980]  # Adjusted positions for correct order
        weapon_order = ['sword', 'rapier', 'war_axe', 'sai', 'katana']  # Correct order of weapons
        new_size = (30, 50)  # New size for the weapon images, adjust as needed

        for index, weapon_name in enumerate(weapon_order):
            pos = weapon_positions[index]
            box_rect = self.select_box(pos, 1010)
            
            weapon_image_path = f'graphics/weapons/{weapon_name}.png'
            try:
                weapon_image = pygame.image.load(weapon_image_path).convert_alpha()
                weapon_image = pygame.transform.scale(weapon_image, new_size)  # Scale the image
            except FileNotFoundError:
                print(f"File not found: {weapon_image_path}")
                continue
            
            weapon_image_rect = weapon_image.get_rect(center=box_rect.center)
            self.display_surface.blit(weapon_image, weapon_image_rect)
            
            if weapon_name == weapon_order[self.player.weapon_index]:
                pygame.draw.rect(self.display_surface, HIGHLIGHT_COLOR, box_rect, 3)
        # weapon graphic

    def power_overlay(self,power_index,has_switched):
        background_rect = self.select_box2(10,90,has_switched)
        power_surf = self.power_graphics[power_index]
        power_rect = power_surf.get_rect(center = background_rect.center)

        self.display_surface.blit(power_surf,power_rect)


    def display_hearts(self, screen, player):
        x = 10
        y = 10
        max_health = player.player_stats['health']  
        health_per_heart = max_health / player.max_health 

        # Calculate the health represented by a full, half, or empty heart
        for i in range(player.max_health):
            # Calculate the threshold for the current heart
            heart_health_threshold = ((i + 1) * health_per_heart)
            if player.health >= heart_health_threshold:
                heart_image = self.full_heart
            elif player.health > (i * health_per_heart):
                heart_image = self.half_heart
            else:
                heart_image = self.empty_heart

            screen.blit(heart_image, (x, y))
            x += 40 