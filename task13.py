import random

def simulate_game(strategy_func, n_rounds=10000):
    """
    Simulate multiple rounds to evaluate a strategy.
    strategy_func: function deciding whether to draw or pass
    """
    wins = 0
    for _ in range(n_rounds):
        deck = list(range(1, 14))  # Cards 1 to 13
        random.shuffle(deck)

        player_card = deck.pop()
        opponent_card = deck.pop()

        # Strategy decides whether to draw a new card
        if strategy_func(player_card):
            player_card = deck.pop()  # Draw new card

        if player_card > opponent_card:
            wins += 1
    return wins / n_rounds


# Strategy examples
def always_draw(card):
    return True

def never_draw(card):
    return False

def smart_strategy(card):
    """Draw if card is 7 or lower"""
    return card <= 7


# Test the strategies
for name, strat in [("Always Draw", always_draw),
                    ("Never Draw", never_draw),
                    ("Smart (<=7)", smart_strategy)]:
    win_rate = simulate_game(strat)
    print(f"{name:15s} -> Win rate: {win_rate:.2%}")
