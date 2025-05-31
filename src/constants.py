"""Game constants and configuration settings."""

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

COLORS = {
    'background': (42, 42, 46),     # Dark grey
    'cell_hidden': (72, 72, 76),    # Medium grey
    'cell_revealed': (92, 92, 96),  # Light grey
    'cell_hover': (82, 82, 86),     # Hover grey
    'mine': (231, 76, 60),          # Red
    'flag': (241, 196, 15),         # Yellow
    'text': (236, 240, 241),        # Off-white
    'grid': (52, 52, 56),           # Grid lines
    'win': (46, 204, 113),          # Green
    'lose': (231, 76, 60)          # Red
}

NUMBER_COLORS = {
    1: (52, 152, 219),              # Blue
    2: (46, 204, 113),              # Green
    3: (231, 76, 60),               # Red
    4: (155, 89, 182),              # Purple
    5: (241, 196, 15),              # Yellow
    6: (26, 188, 156),              # Turquoise
    7: (52, 73, 94),                # Dark blue
    8: (149, 165, 166)              # Grey
}

DIFFICULTY_SETTINGS = {
    'easy': {'rows': 9, 'cols': 9, 'mines': 10},
    'medium': {'rows': 16, 'cols': 16, 'mines': 40},
    'hard': {'rows': 16, 'cols': 30, 'mines': 99}
}

CELL_SIZE = 30
CELL_MARGIN = 2

REVEAL_ANIMATION_SPEED = 0.1
HOVER_SCALE = 1.05
