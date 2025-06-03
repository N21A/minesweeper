"""Individual cell logic / behaviour settings."""

import pygame
from typing import Tuple, Optional
from src.constants import COLORS, NUMBER_COLORS, CELL_SIZE, CELL_MARGIN

class Cell:
    """Represents a single cell on the Minesweeper grid."""

    def __init__(self, row: int, col: int):
        """
        Initialises a cell at a given position.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
        """
        self.row = row
        self.col = col
        self.is_mine = False
        self.is_revealed = False
        self.is_flagged: False
        self.adjacent_mines = 0

        # Visual properties
        self.rect = None
        self.animation_progress = 0.0
        self.hover_scale = 1.0

    
    def set_rect(self, x: int, y: int):
        """
        Sets the cell rectangle based on the distance from the top-left corner of the screen.

        Args:
            x (int): The x-coordinate of the top-left corner of the screen.
            y (int): The y-coordinate of the top-left corner on the screen.
        """
        self.rect = pygame.Rect(
            x + CELL_MARGIN,
            y + CELL_MARGIN,
            CELL_SIZE - 2 * CELL_MARGIN,
            CELL_SIZE - 2 * CELL_MARGIN
        )
    
    
    def reveal(self) -> bool:
        """
        Reveals the cell.

        Returns:
            True if the cell is a mine.
            False if the cell isn't a mine.
        """
        if self.is_revealed or self.is_flagged:
            return False
        
        self.is_revealed = True
        self.animation_progress = 0.0
        return self.is_mine
    

    def toggle_flag(self):
        """Toggles flag on/off for a given cell."""
        if not self.is_revealed:
            self.is_flagged = not self.is_flagged
    

    def update(self, dt: float):
        """
        Updates cell animations.
        
        Args:
            dt (float): The time delta (in seconds) since the last update call. Used to increment the animation.
        """
        if self.is_revealed and self.animation_progress < 1.0:
            self.animation_progress = min(1.0, self.animation_progress + dt * 5)
        
    
    def draw(self, screen: pygame.Surface, font: pygame.font.Font):
        """
        Draws the cell on the screen.
        
        Args:
            screen (pygame.Surface): The in-game window over which the cell is drawn.
            font (pygame.font.Font): The font used for rendering numbers on the cell when adjacent mines are present.
        """
        if not self.rect:
            return
        
        # Calculate rectangle with hover effect
        if self.hover_scale > 1.0:
            center = self.rect.center
            width = self.rect.width * self.hover_scale
            height = self.rect.height * self.hover_scale
            draw_rect = pygame.Rect(0, 0, width, height)
            draw_rect.center = center
        else:
            draw_rect = self.rect
        
        # Draw cell background
        if self.is_revealed:
            # Reveal cells with a fade animation
            if self.animation_progress < 1.0:
                color = self._interpolate_color(
                        COLORS['cell_hidden'],
                        COLORS['cell_revealed'],
                        self.animation_progress
                )
            else:
                color = COLORS['cell_revealed']
            pygame.draw.rect(screen, color, draw_rect, border_radius=4)

            # If the cell is a mine, draw a mine
            if self.is_mine:
                self._draw_mine(screen, draw_rect)
            # If the cell is not mined (but has a number), draw a number
            elif self.adjacent_mines > 0:
                self._draw_number(screen, draw_rect, font)
        # Otherwise, reveal the hidden cell(s)
        else:
            color = COLORS['cell_hover'] if self.hover_scale > 1.0 else COLORS['cell_hidden']
            pygame.draw.rect(screen, color, draw_rect, border_radius=4)

            # Draw a flag if the cell is flagged
            if self.is_flagged:
                self._draw_flag(screen, draw_rect)
    

    def _draw_mine(self, screen: pygame.Surface, rect: pygame.Rect):
        """
        Draws a mine in the cell.

        Args:
            screen (pygame.Surface): The in-game window over which the mine is drawn.
            rect (pygame.Rect): A rectangle defining the window's position and size. The mine is drawn and centred within this area.
        """
        center = rect.center
        radius = rect.width // 3

        # Create the mine body
        pygame.draw.circle(screen, COLORS['mine'], center, radius)

        # Create the mine spikes
        for angle in range(0, 360, 45):
            end_x = center[0] + radius * 1.5 * pygame.math.Vector2(1, 0).rotate(angle).x
            end_y = center[1] + radius * 1.5 * pygame.math.Vector2(1, 0).rotate(angle).y


    def _draw_number(self, screen: pygame.Surface, rect: pygame.Rect, font: pygame.font.Font):
        """
        Draws the adjacent mine indicator / number.

        Args:
            screen (pygame.Surface): The in-game window over which the number is drawn.
            rect (pygame.Rect): A rectangle defining the window's position and size. The number is drawn and centred within this area.
            font: (pygame.font.Font): The font which the number will be displayed in.
        """
        text = font.render(str(self.adjacent_mines), True, NUMBER_COLORS[self.adjacent_mines])
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)

    
    def _draw_flag(self, screen: pygame.Surface, rect = pygame.Rect):
        """
        Draws a flag in the cell.

        Args:
            screen (pygame.Surface): The in-game window over which the mine is drawn.
            rect (pygame.Rect): A rectangle defining the window's position and size. The flag is drawn and centred within this window.
        """
        # Create the flag pole
        pole_x = rect.centerx
        pole_top = rect.centery - rect.height // 4
        pole_bottom = rect.centery + rect.height // 4
        pygame.draw.line(screen, COLORS['flag'], (pole_x, pole_top), (pole_x, pole_bottom), 2)

        # Create the flag
        flag_points = [
            (pole_x, pole_top),
            (pole_x + rect.width // 3, pole_top + rect.height // 6),
            (pole_x, pole_top + rect.height // 3)
        ]
        pygame.draw.polygon(screen, COLORS['flag'], flag_points)


    def _interpolate_color(self,
                           color1: Tuple[int, int, int],
                           color2: Tuple[int, int, int],
                           progress: float) -> Tuple[int, int, int]:
        """
        Interpolates between two colors.
        
        Args:
            color1 (Tuple[int, int, int]): Start colour as an (R, G, B) tuple.
            color2 (Tuple[int, int, int]): End colour as an (R, G, B) tuple.
            progress (float): A float between 0.0 and 1.0 representing interpolation progress.

        Returns:
            Tuple[int, int, int]: The interpolated colour as an (R, G, B) tuple.
        """
        return tuple(
            int(c1 + (c2 - c1) * progress)
            for c1, c2 in zip(color1, color2)
        )
    