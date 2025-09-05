# Classic Pong Game
---
### Overview

This project is a classic **Pong game** implemented in **Python** using the **Pygame** library. It’s a 1 vs 1 version where two players can compete against each other on the same computer. The gameplay mirrors the original arcade-style Pong game, with each player controlling a paddle and trying to score by getting the ball past their opponent.

To start playing, simply run the ```Pong.py``` file, and you’re ready to challenge a friend in this timeless two-player game.


<img width="812" height="640" alt="Screenshot 2025-09-05 at 17 44 11" src="https://github.com/user-attachments/assets/bc284174-05d8-4674-bf44-6557546b6ede" />

### Features

- **1 vs 1 Gameplay:** Two players can play against each other locally on the same computer.
- **Simple Controls:** Each player uses separate keys to control their paddle:
  - **Player 1:** Uses the W and S keys to move their paddle up and down.
  - **Player 2:** Uses the Up Arrow and Down Arrow keys for their paddle.
- **Classic Pong Mechanics:** The ball bounces off the paddles and walls, and points are scored when the ball passes the opponent’s paddle.
- **Score Tracking:** The game keeps track of each player’s score, displayed at the top of the screen.
- **Restartable Game:** Players can restart the game after one player wins.

### How It Works

The game follows the traditional Pong mechanics:

- **Ball Movement:** The ball starts in the center and moves diagonally. It bounces off the paddles and walls, but if it passes a paddle, the opposing player scores.
- **Paddle Movement:** Players control their paddles to block the ball, using separate controls for Player 1 and Player 2.
- **Scoring:** Each time a player misses the ball, the opposing player earns a point. The game continues until a player reaches a predetermined winning score (or can be modified to keep playing endlessly).
