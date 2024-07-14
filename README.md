# Uno Game Statistical Analysis

This project provides a statistical analysis of the popular card game Uno through simulation and data visualization.

## Overview

This Python script simulates multiple games of Uno and analyzes the results to provide insights into game dynamics, player advantages, and overall game statistics.

## Features

- Simulates thousands of Uno games with a configurable number of players
- Implements a simplified version of Uno game rules
- Tracks and analyzes game statistics, including:
  - Win distribution among players
  - Average number of turns per game
  - Average number of cards played per game
  - Longest winning streak
  - Most frequent winner
- Visualizes results with a bar chart showing the distribution of wins
- Provides detailed text output of game statistics

## Requirements

- Python 3.x
- pandas
- matplotlib

## Installation

1. Clone this repository:
git clone https://github.com/yourusername/uno-game-analysis.git
Copy2. Install the required packages:
pip install -r requirements.txt


## Usage

Run the script using Python:
python uno_analysis.py
Copy
The script will simulate the specified number of Uno games and output the results both in the console and as a saved PNG image.

## Customization

You can modify the following parameters in the script:

- `num_games`: Number of games to simulate
- `num_players`: Number of players in each game

## Output

The script generates:

1. A console output with detailed game statistics
2. A bar chart saved as 'uno_results.png' showing the distribution of wins among players

## Limitations

- This simulation uses simplified Uno rules and random play strategies
- Real-world results may vary due to player skill and strategy

## Future Improvements

- Implement more complex Uno rules (e.g., special cards, official scoring)
- Add different player strategies
- Extend analysis to include card usage statistics and game duration

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/uno-game-analysis/issues) if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Acknowledgements

- This project was inspired by the classic Uno card game
- Thanks to the Python community for providing excellent data analysis and visualization tools
