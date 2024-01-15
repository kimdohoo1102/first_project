import random

def monty_hall_simulation(num_trials):

    stay_wins = 0 
    switch_wins = 0

    for_ in range(num_trials):
        doors = ['goat', 'goat', 'car']
        random.shuffle(doors)
