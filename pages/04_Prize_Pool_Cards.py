import streamlit as st

import math
from math import comb

st.set_page_config(page_title="Prize Pool", page_icon="img/favicon.ico")

st.markdown("# Prize Pool Card Count")
st.markdown("Sometimes you might wonder how many cards being trapped in the prize pool.\
            Here you can see the probability of having a specific card(s) in your prize pool.") 

n = st.slider("Number of specific cards in deck:", 0, 4, 1)

# prompt: write a function to calculate the probability of drawing 7 cards with k number of a certain card in a 60 cards deck

def prob_specific_cards_in_prize_pool(num_specific_card, cards_trapped, total_cards=59, prize_pool_size=6):
    """
    Calculate the probability of a specific number of cards being trapped in the Prize pool.

    Args:
        num_specific_card: The number of specific cards in the deck.
        cards_trapped: The number of specific cards to be trapped in the Prize pool.
        total_cards: The total number of cards in the deck (default is 59).
        prize_pool_size: The size of the Prize pool (default is 6).
    
    Returns:
        Probability of 'cards_trapped' specific cards being in the Prize pool.
    """
    # Check for valid input
    if cards_trapped > num_specific_card:
        return 0  # Cannot trap more specific cards than available

    # Calculate combinations
    specific_combinations = comb(num_specific_card, cards_trapped)
    non_specific_combinations = comb(total_cards - num_specific_card, prize_pool_size - cards_trapped)
    total_combinations = comb(total_cards, prize_pool_size)

    # Calculate probability
    probability = (specific_combinations * non_specific_combinations) / total_combinations
    return probability

st.write(f"If you put {n} specific cards in your deck. \
         There is a {100-prob_specific_cards_in_prize_pool(n,0)*100:.02f}% chance that you will have at least 1 of them in your prize pool.")

for i in range(n+1):
  st.write(f"Probability of having {i} specific cards in prize pool: {prob_specific_cards_in_prize_pool(n,i)*100:.03f}%")