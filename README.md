<div align="center">

  <h1>⚔️ Deltastar ⚔️</h1>
  
  <p>
    <b>A 2D Top-Down Action RPG built in Python & Pygame</b>
  </p>

<p>
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Pygame-2.0+-green.svg" alt="Pygame Version">
  <img src="https://img.shields.io/badge/Architecture-OOP-orange.svg" alt="OOP">
</p>

</div>

<br/>

## 📖 About The Project

Inspired by the challenging combat of Souls-like games and the classic exploration of retro Zelda titles, this project is a fully functional 2D action RPG. It features modular object-oriented architecture, dynamic level generation driven by Excel spreadsheets, and a custom progression system.

### ✨ Key Features
* **Souls-like Combat:** Real-time, challenging combat mechanics with various weapons, magic powers, and distinct enemy entities.
* **Data-Driven Tile Maps:** Levels are dynamically rendered by parsing exported Excel layouts (`csv_map.py`), allowing for scalable game environments.
* **Progression System:** Players earn experience points from defeated enemies to spend in a dedicated upgrade menu (`upgrade.py`) to increase attributes (health, mana, attack power).
* **Object-Oriented Architecture:** Highly modular codebase separating entities, players, enemies, weapons, and user interfaces.
* **Custom VFX & Audio:** Integrated particle systems (`particles.py`) and sound effects to enhance game feel.

## 📁 Project Structure 

| File / Folder | Description |
| :--- | :--- |
| **`audio/`** | Directory containing all game music and sound effects. |
| **`graphics/`** | Directory containing all game sprites, tilesets, and visual assets. |
| **`map/`** | Directory containing the level layouts and map data. |
| **`.gitattributes`**| Git configuration file. |
| **`UserInterface.py`**| Handles the on-screen display (HUD) for player health, mana, and experience. |
| **`csv_map.py`** | Logic for the data-driven tile map system, parsing exported Excel/CSV layouts. |
| **`debug.py`** | Utility script for displaying real-time debugging information on screen. |
| **`enemy.py`** | Contains the logic, AI behaviors, and stats for enemy entities. |
| **`entity.py`** | The base class handling shared movement and collision logic for all moving objects. |
| **`level.py`** | Manages map rendering, camera updates, and entity generation within the game world. |
| **`main.py`** | The entry point of the game containing the main game loop and state management. |
| **`particles.py`** | Handles custom VFX and particle systems used for magic and combat feedback. |
| **`player.py`** | Core class governing player input, movement, and combat interactions. |
| **`power.py`** | Logic, animation, and attributes for magical abilities. |
| **`settings.py`** | Global configuration file storing game constants (screen size, FPS, control bindings, etc.). |
| **`tile.py`** | Defines the stationary objects, walls, and obstacles in the game environment. |
| **`upgrade.py`** | The interactive UI menu for the player stat progression system. |
| **`weapon.py`** | Logic, positioning, and attributes for physical weapons and attacks. |

<hr/>

## 🛠️ Prerequisites & Installation

Since this game does not have a standalone .exe file, you will need to run it directly through Python. Make sure you have the following installed on your system:

Python 3.x (preferably 3.8 or higher)

Pygame library

**1. Clone the repository:**
```bash
git clone [https://github.com/llazer10/PythonGameProject-Deltastar-cs-project.git](https://github.com/llazer10/PythonGameProject-Deltastar-cs-project.git)
cd PythonGameProject-Deltastar-cs-project
```
**2. Install the required dependencies:**
```bash
pip install pygame
```
**3. Run the game:**
```bash
python main.py
```
(Note: If you are using a code editor like VS Code or PyCharm, you can simply open the project folder and run main.py directly from your editor.)
