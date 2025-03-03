# PyBrawl
A simple API wrapper made in python built around the official Supercell Brawl Stars API.

## Initialization
In order to start using pybrawl, you must first create a new `Brawl` class with your API token as a parameter:
```py
brawl = Brawl("YOUR_API_KEY_HERE")
```

## Methods
### Player
The `player()` method can be used to get all information pertaining to a player as an object, given a proper player tag.
```py
my_player = brawl.player("#PLAYER_TAG")

print(my_player.name) # Returns the player's name or errors if provided with an invalid tag.
```
