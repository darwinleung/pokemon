import streamlit as st

import math
from math import comb

st.set_page_config(page_title="Starting Hand", page_icon="img/favicon.ico")

st.markdown("# Starting Hand Card Count")
st.markdown("Sometimes you might wonder how many cards should you put in the deck.\
            Here you can see the probability of drawing a specific card in your starting hand.") 

n = st.slider("Number of specific cards in deck:", 0, 4, 1)

# prompt: write a function to calculate the probability of drawing 7 cards with k number of a certain card in a 60 cards deck

def prob_k_cards(k, num_specific_card=n, total_cards=60, hand_size=7):
  """
  Calculates the probability of drawing exactly k specific cards in a hand.

  Args:
    k: The number of specific cards to draw.
    total_cards: The total number of cards in the deck.
    hand_size: The size of the hand being drawn.
    num_specific_card: The number of specific cards in the deck.

  Returns:
    The probability of drawing exactly k specific cards.
  """
  return (comb(num_specific_card, k) * comb(total_cards - num_specific_card, hand_size - k)) / comb(total_cards, hand_size)

st.write(f"If you put {n} specific cards in your deck. \
         There is a {100-prob_k_cards(0,n)*100:.02f}% chance that you will draw at least 1 of them in your starting hand.")

for i in range(n+1):
  st.write(f"Probability of having {i} cards in starting hand: {prob_k_cards(i,n)*100:.02f}%")