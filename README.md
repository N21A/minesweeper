# 💥 Minesweeper
A modern version of the classic game. Built with Python and Pygame.

## Features
- 🎨 Modern design with smooth animations
- 🎮 Classic Minesweeper gameplay
- 🎚️ Multiple difficulty levels
- 🏆 Win/loss tracking
- 🔊 Sound effects
- 💾 Save functionality

## Installation
1. Clone the repository:
```bash
git clone https://github.com/N21A/minesweeper.git
cd minesweeper
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## How to play
Launch the game using the command below:
```bash
python main.py
```

### Controls
- **Left click**: Reveal a cell
- **Right click**: Place / remove a flag
- **Middle click**: Reveal adjacent cells (if flags match mine count)

### Rules
- Find all mines without clicking on them
- Numbers show how many mines are adjacent to that cell
- Use flags to mark suspected mines

## Project structure
- `src/`: Core game modules
- `assets/`: Assets and resources
- `tests/`: Unit tests
- `main.py`: Program entry point

## Development
Run tests using the following command:
```bash
pytest tests/
```

## Licence
This project is licensed under the MIT Licence.