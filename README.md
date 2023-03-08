# Monopoly
Constructing a classic Monopoly game in Python with the intent of measuring the frequencies of location visits.

My code was successfully able to run 1,000,000 turns of Monopoly, and by appending each visited location to a list and using the Counter() method from the Collections module, I was able to calculate the number of visits to each location. Attached is a bar graph which shows that jail is by far the most frequently visited location, which is to be expected given the rules of the game.

## Limitations
The plot() method within the Player class does not work if not every location is visited (a ValueError is raised since the number of labels/colors does not match the number of x values). This should not be a very difficult fix but for the purpose of this project I decided to just leave an error message if not every location was visited. It makes more sense in this context to run many trials and consequently increase the likelihood of all locations being visited.