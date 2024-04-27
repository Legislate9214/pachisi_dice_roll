import numpy as np
import matplotlib.pyplot as plt


num_turn_per_game = 10
def play_one_game():
    player1, player2 = 0, 0
    for i in range(num_turn_per_game): # Each player rolls the dice 10 times (moving all their pieces)
        p1_roll = np.random.randint(1, 7) + np.random.randint(1, 7)
        p2_roll = np.random.randint(1, 7) + np.random.randint(1, 7)
        player1 += p1_roll
        player2 += p2_roll
    return player1, player2

def simulate_games(num_games):
    game_results = [play_one_game() for _ in range(num_games)]
    return game_results

# Number of games to simulate
num_games = 5

# Simulate games and store results in a list
game_results = simulate_games(num_games)

# Calculate the mean and standard deviation of player rolls
player1_rolls = [result[0] for result in game_results]
player2_rolls = [result[1] for result in game_results]
mean_player1, stddev_player1 = np.mean(player1_rolls), np.std(player1_rolls)
mean_player2, stddev_player2 = np.mean(player2_rolls), np.std(player2_rolls)

# Plot the histogram of player rolls
plt.hist(player1_rolls, bins=np.arange(min(player1_rolls), max(player1_rolls)+1), density=True, label='Joueur 1')
plt.hist(player2_rolls, bins=np.arange(min(player2_rolls), max(player2_rolls)+1), density=True, label='Joueur 2')

# Add a legend to the plot
plt.legend()

# Add the number of games played to the title
plt.title(f"""Nombre de pas avancés (somme des 2 dés du joueur)
 {num_turn_per_game} tours par partie avec 2 joueurs
 {num_games} parties""")

# Show the plot
plt.savefig(f"plot_diceroll_distribution_{num_games}_games.png")
