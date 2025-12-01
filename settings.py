# Game Setup
W = 1700
H = 1100
FPS = 60
TILESIZE = 16

# User Interface
BAR_HEIGHT = 20
ENERGY_BAR_WIDTH = 180
ITEM_BOX_SIZE = 80
UI_Font = 'graphics/font/joystix.ttf'


# colours
ENERGY_COLOUR = 'BLUE'
UI_BORDER_COLOUR_ACTIVE = 'GOLD'
TEXT_COLOUR = '#EEEEEE'
UI_BORDER_COLOUR = '#111111'
UI_BG_COLOUR = '#222222'
HIGHLIGHT_COLOR = (255, 255, 255, 0.5)


# upgrade menu colours

TEXT_COLOUR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

# Weapon Data
weapon_data = {
    'sword': {'cooldown': 100, 'damage': 40, 'graphic':'graphics/weapons/sword/full.png'},
    'rapier': {'cooldown': 350, 'damage': 60, 'graphic':'graphics/weapons/rapier/full.png'},
    'war axe': {'cooldown': 400, 'damage': 70, 'graphic':'graphics/weapons/war axe/full.png'},
    'sai': {'cooldown': 10, 'damage': 60, 'graphic':'graphics/weapons/sai/full.png'},
    'katana': {'cooldown': 120, 'damage': 50, 'graphic':'graphics/weapons/katana/full.png'}}

# power data
power_data = {
    'flame': {'strength': 10, 'cost': 30, 'graphic':'graphics/particles/flame/fire.png'},
    'heal': {'strength': 50, 'cost': 30, 'graphic':'graphics/particles/heal/heal.png'},
    'blue projectile': {'strength': 250, 'cost': 50, 'graphic':'graphics/particles/blue projectile/blue projectile.png'},
    'red projectile': {'strength': 600, 'cost': 70, 'graphic':'graphics/particles/red projectile/red projectile.png'}}

# enemy data
enemy_data = {
        'slime': {'health': 120,'exp':150,'damage':20,'attack_type': 'slash','attack_sound': 'audio/attack/slash.wav','speed': 1.5, 'resistance': 2, 'attack_radius': 12, 'notice_radius': 90},
        'snake': {'health': 100,'exp':80,'damage':25,'attack_type': 'slash','attack_sound': 'audio/attack/slash.wav','speed': 2, 'resistance': 2, 'attack_radius': 12, 'notice_radius': 90},
        'racoon': {'health': 200,'exp':200,'damage':15,'attack_type': 'slash curved','attack_sound': 'audio/attack/slash.wav','speed': 1.5, 'resistance': 2, 'attack_radius': 12, 'notice_radius': 90},
        'reptile': {'health': 300,'exp':300,'damage':30,'attack_type': 'slash curved','attack_sound': 'audio/attack/slash.wav','speed': 1, 'resistance': 2, 'attack_radius': 13, 'notice_radius': 90},
        'mushroom': {'health': 60,'exp':60,'damage':10,'attack_type': 'slash','attack_sound': 'audio/attack/slash.wav','speed': 2, 'resistance': 2, 'attack_radius': 9, 'notice_radius': 90},
        'wintereye': {'health': 400,'exp':300,'damage':40,'attack_type': 'slash','attack_sound': 'audio/attack/slash.wav','speed': 1.5, 'resistance': 2, 'attack_radius': 12, 'notice_radius': 90},
        'wintermushroom': {'health': 250,'exp':180,'damage':30,'attack_type': 'slash','attack_sound': 'audio/attack/slash.wav','speed': 2, 'resistance': 2, 'attack_radius': 9, 'notice_radius': 90},
        'winterreptile': {'health': 800,'exp':500,'damage':70,'attack_type': 'slash curved','attack_sound': 'audio/attack/slash.wav','speed': 1, 'resistance': 2, 'attack_radius': 13, 'notice_radius': 90},
        'lizard': {'health': 200,'exp':800,'damage':60,'attack_type': 'slash','attack_sound': 'audio/attack/slash.wav','speed': 2.5, 'resistance': 2, 'attack_radius': 11, 'notice_radius': 90},
        'goldenRacoon': {'health': 1500,'exp':400,'damage':50,'attack_type': 'slash','attack_sound': 'audio/attack/slash.wav','speed': 1.5, 'resistance': 2, 'attack_radius': 12, 'notice_radius': 90},
        'redEye': {'health': 2000,'exp':200,'damage':70,'attack_type': 'slash','attack_sound': 'audio/attack/slash.wav','speed': 1.5, 'resistance': 2, 'attack_radius': 12, 'notice_radius': 90},
        'skull': {'health': 2500,'exp':1000,'damage':80,'attack_type': 'slash','attack_sound': 'audio/attack/slash.wav','speed': 1.5, 'resistance': 2, 'attack_radius': 11, 'notice_radius': 90},
        'cyclope': {'health': 4000,'exp':1500,'damage':100,'attack_type': 'slash curved','attack_sound': 'audio/attack/slash.wav','speed': 2, 'resistance': 1, 'attack_radius': 13, 'notice_radius': 90},
        'cyclope boss': {'health': 20000,'exp':9000,'damage':200,'attack_type': 'cyclopebossflam','attack_sound': 'audio/attack/claw.wav','speed': 2, 'resistance': 0.5, 'attack_radius': 33, 'notice_radius': 150},
        'racoon boss': {'health': 10000,'exp':4000,'damage':150,'attack_type': 'bossthunder','attack_sound': 'audio/attack/thunder.wav','speed': 2, 'resistance': 0.5, 'attack_radius': 33, 'notice_radius': 150},
        'spirit boss': {'health': 5000,'exp':2000,'damage':100,'attack_type': 'bossice','attack_sound': 'audio/attack/ice explosion.wav','speed': 2, 'resistance': 0.5, 'attack_radius': 33, 'notice_radius': 150},
}