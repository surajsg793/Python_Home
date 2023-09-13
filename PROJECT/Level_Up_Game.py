class Character:
    def __init__(self, name, level=1, xp=0, inventory=[], strength=10, score=0):
        self.name = name
        self.level = level
        self.xp = xp
        self.inventory = inventory
        self.strength = strength
        self.score = score

    def level_up(self):
        self.level += 1
        # Implement logic for attribute improvements

    def earn_xp(self, amount):
        self.xp += amount
        # Check for level up based on XP thresholds

    def upgrade_strength(self):
        # Implement logic for upgrading character's strength
        self.strength += 1

    def increase_score(self, amount):
        self.score += amount

class Game:
    def __init__(self):
        self.locations = {"Town": {"unlocked": True}, "Dungeon": {"unlocked": False}}

    def unlock_location(self, location):
        self.locations[location]["unlocked"] = True

    # Implement saving/loading logic using file storage or blockchain

# Initialize the game
game = Game()

# Create a character
player_character = Character("Player")

# Simulate gameplay
player_character.earn_xp(100)
player_character.level_up()
game.unlock_location("Dungeon")

# Upgrade character's strength
player_character.upgrade_strength()

# Increase player's score
player_character.increase_score(50)

# Save the game state
# Implement save game functionality

# Load the game state
# Implement load game functionality
