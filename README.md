# Monte Carlo Blackjack Simulation

## Overview

A Python-based Monte Carlo simulation that runs multiple randomised games of Blackjack using a simplified set of Las Vegas-style rules. The aim is to analyse how different player decisions and behaviours affect game outcomes.
The simulation records the results of each game and exports the data into a text file and an Excel spreadsheet for further analysis.
The project could potentially help identify effective playing strategies by analysing the outcomes of a large number of simulated games.

## How It Works

- Randomly selects one player to act as the dealer.
- Deals two random cards to every player.
- Non-dealer players randomly decide whether to draw another card, provided they haven't gone bust (exceeded 21).
- The dealer follows predefined rules:
  - Must draw when their total is below 16.
  - Cannot draw when their total is above 17.
  - When their total is exactly 17, they have a random chance of drawing another card.
- Once all players have finished drawing cards, the winner is calculated.
- Results are written to a `.txt` file and an `.xlsx` spreadsheet.

## Running the Simulation

The simulation can run multiple games in succession. The number of games can be adjusted by editing the `for` loop on line 224.

Running more simulations produces a larger dataset, allowing for more extensive analysis of the results.

### Requirements

- Python 3
- XlsxWriter

Install the required library using:

```bash
pip install XlsxWriter
```

Run the program using:

```bash
python main.py
```

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- Random module
- XlsxWriter library

## What I Learned and Developed

- Improved my understanding and implementation of classes.
- Learned how to use the XlsxWriter library to generate Excel spreadsheets.
- Developed my problem-solving and logical thinking skills.
- Gained experience working with randomisation and repeated simulations.
- Learned how to structure a Python program to generate and process large amounts of data.
- Improved my ability to write reusable code.

## Future Improvements

- Allow users to choose the number of players.
- Introduce data visualisation to make simulation results easier to interpret.
- Improve modularisation by separating different parts of the program into individual Python files.

## Example output from .xlsx file

<img width="751" height="181" alt="Screenshot 2026-11-11 212710" src="https://github.com/user-attachments/assets/a6d8b498-2a07-4276-bf11-31ec0b108d1f" />
