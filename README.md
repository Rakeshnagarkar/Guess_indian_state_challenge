
# Guess_indian_state_challenge

This project is a fun game that helps you learn the names and locations of the Indian states and union territories. The game works by showing you a map of India and asking you to guess the name of a state. If you get the answer right, the game will add the state's name to the map. The game ends when you have guessed all the states or when you decide to stop. 
If you press "Exit" during the game, the program will end and show you a list of the Indian states and union territories that you did not guess correctly. It does this by comparing the list of all the states with the list of states you correctly guessed and then creating a new list of the states that you did not guess. The program saves this new list to a file called "states_to_learn_in_india.csv".

## Requirements:

-Python 3 installed on your system
-The CSV file "36_states.csv" and the GIF image "temp_image.gif" in the same folder as the game code

## How to run the game:

1.Download or clone the game code, CSV file, and GIF image from the GitHub repository to a folder on your computer.

2.Open a terminal or command prompt and navigate to the folder where you downloaded the game code.

3.Run the game using the command "python3 indian_states_game.py" (or the appropriate command for your Python 3 installation).

## How to play the game:

The game will look something like this:

![indianmap git](https://user-images.githubusercontent.com/114185766/229351006-12230542-0e75-4e00-aeb6-e7e8513179e5.png)

1.A map of India will be displayed on the screen with some states and union territories highlighted.

2.The input screen will show the number of states you have correctly guessed out of 35, in the format "guessed state/35".

3.You will be prompted to enter the name of an Indian state or union territory.

4.If you guess correctly, the name of the state or union territory will be displayed on the map and your score will be updated.

5.If you guess incorrectly, you can keep guessing until you get it right or choose to exit the game by typing "exit" (without quotes) instead of a state name.

6.If you exit the game early, a CSV file called "states_to_learn_in_india.csv" will be created in the same folder as the game code, which will contain the names of the states and union territories that you did not guess correctly.

7.If you correctly guess all 35 states and union territories, a congratulations message will be displayed.

## Design
"I got the idea for this project from Angelena Yu's U.S. States Game project, which displays a map of the United States and challenges users to guess the names of the states. I decided to create my own version of the game, called Guess Indian State Challenge, which displays a map of India and challenges users to guess the names and locations of the states and union territories. The project uses Python and the turtle graphics library to create the map and enable users to input their guesses. I hope this game helps people learn more about the geography of India!"

## Libraries:
-Turtle: used for creating graphics and drawing the map of the United States in the game.
-Pandas: used for reading and manipulating data from the "36_states.csv" file, which contains information about the states.

## Note:
India has a total of 28 states and 9 union territories. In this project, you will see that I have mentioned 35 locations which include some states and some territories. The reason for this is that it is difficult to see the territories inside a map because two named collide with nearly the same location, making it difficult to read and understand the location. Therefore, I have only mentioned 35 states and territories which are clearly readable and understandable.
