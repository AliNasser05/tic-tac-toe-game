# Tic Tac Toe Game

This is a two-player Tic Tac Toe game that runs in the terminal. Players take turns placing their chosen symbols on a 3x3 grid, aiming to get three in a row horizontally, vertically, or diagonally.

## Features

- **Two-Player Gameplay**: Play against a friend locally
- **Custom Symbols**: Each player can choose their own single-character symbol
- **Input Validation**: 
  - Validates coordinate ranges (1-3)
  - Prevents placing symbols in occupied cells
  - Ensures symbols are single characters and not whitespace
  - Handles non-numeric input gracefully
- **Visual Board Display**: Clear grid with row and column numbers for easy navigation
- **Win Detection**: Automatically detects wins across rows, columns, and diagonals
- **Draw Detection**: Recognizes when the board is full with no winner
- **Replay Option**: Play multiple rounds without restarting the program
- **Clean OOP Design**: Organized with `Player` and `Board` classes

## How to Play

1. Run the program:
```bash
   python tic_tac_toe.py
```

2. Enter player names and choose symbols for both players

3. Players take turns entering coordinates:
   - **Row**: Enter a number from 1 to 3
   - **Column**: Enter a number from 1 to 3

4. The first player to get three symbols in a row wins!

5. After each game, choose whether to play again

## Code Structure

- **`Player` class**: Manages player information and move input
- **`Board` class**: Handles board display and win condition checking
- **`get_symbol()` function**: Validates and retrieves player symbols
- **`start_game()` function**: Main game loop and flow control

## Example Gameplay
```
    1   2   3 
  -------------
1 | X |   |   |
  -------------
2 |   | O |   |
  -------------
3 |   |   | X |
  -------------
```

## Future Enhancements

Potential features for future versions:
- Score tracking across multiple games
- AI opponent with difficulty levels
- Larger board sizes (4x4, 5x5)

## Author

[Ali Nasser]
