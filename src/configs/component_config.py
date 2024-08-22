from src.gui.components.game_component import *

component_mapper = {
    0: None,
    1: create_wall,
    2: create_dot,
    3: create_power,
    7: create_enemy_wall,
    10: DebugDot
}
