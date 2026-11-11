#Monte-carlo-blackjac

#Overview
-A Python based Monte Carlo simulation that runs multiple randomised games of Blackjack under common Las Vegas rules to analyse how different player decisions and behaviors affect game outcomes.
-The simulation records the results of each game and exports the data into an Excel spreadsheet and file for further analysis.
-This program could be able to help someone learn the most logical moves of a game of blackjack.

#How it works
-Randomly selects one player to act as dealer.
-Deals 2 cards to every player.
-Non-dealer players randomly deal provided they haven't gone bust (over 21).
-The dealer follows predefined rules: must draw when their total is below 16, cannot draw if their total is above 17. If their total is 17 they have a random chance of dealing like a regular player.
-Once player 1 and 2 have finished dealing, the winner is caculated.
-Results are written to a txt file and .xlsx spreadsheet.

#Running it
-The simulation can run multiple games in succession. The number of games can be adjusted by editing the for loop on line 224.
-Running more simulations provides a larger dataset improving the acuracy.
-See requirements folder to run this program yourself.

#Technologies used
-Python
-Object-Oriented Programming
-Random module
-XlsxWriter library

#What I learned and developed
-Understand and implemented classes more effectively.
-Learn how to use the XlsxWriter library to generate Excel spreadsheets.
-Developed problem-solving and logical thinking skills.
-Worked with randomisation and repeated simulations.
-Structured a Python program to create and process large numbers of results.
-Developed my skills in making re-usable code.

#Future improvements
-Have the user choose how many players there are.
-Allow the user to visualize the results.
-Utilize modularization better.
