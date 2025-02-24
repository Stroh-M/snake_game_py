# Snake Game (Terminal-Based)

This is a simple **snake game** implemented in Python using the `curses` library. The game runs in the terminal and features a moving snake that grows when it eats food (`*`). The goal is to grow the snake as long as possible without hitting the walls or itself.

## Features
- Snake moves continuously in one direction.
- Collect food (`*`) to grow the snake.
- Game over if the snake **hits a wall** or **collides with itself**.
- Displays the **score** (number of food collected) when the game ends.
- Automatically restarts if a key is pressed after game over.
- Press `END` key after game over to **exit the program**.

## Controls
- **Arrow keys** → Move the snake
- **END key** → Quit the game
- **Any other key after game over** → Restart the game

## How to Play
1. Run the script in a terminal.
2. Use the arrow keys to move the snake.
3. Eat food (`*`) to increase the snake's length.
4. Avoid crashing into the walls or yourself.
5. If you lose, the game displays "Game Over" and your score.
6. Press any key to restart or press `END` to exit.

## Requirements
- Python 3
- `curses` module (comes pre-installed with Python on Linux/macOS, for Windows, use `windows-curses`)

## Installation (Windows)
Since `curses` is not included by default in Windows, install it with:

```sh
pip install windows-curses
```

Then, run the game:

```sh
python snake.py
```

## Notes
- The food **never spawns inside the snake's body**.
- If the terminal window is too small, the game may not work correctly.
- Works best in **Linux/macOS terminals** but can run on Windows with the necessary package.

Enjoy the game! 🐍