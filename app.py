import streamlit as st

import math
from math import comb
from math import perm

import matplotlib.pyplot as plt
import seaborn as sns

st.markdown("# Pokemon TCG Mulligan Calculator")

st.image("img/Iron Thorns Tyranitar.webp", width = 100)

basic_pkm_count = st.number_input("Basic Pokemon Count:", value = 4, step = 1)
st.write("You have ", basic_pkm_count, " basic pokemon")

def prob_of_mulligan(num_specific_card=4, total_cards=60, hand_size=7):
    """
    Calculate the probability of not drawing a specific card in an initial hand of a card game.
    
    :param num_specific_card: Number of specific cards in the deck.
    :param total_cards: Total number of cards in the deck.
    :param hand_size: Number of cards drawn in the initial hand.
    :return: Probability of not drawing the specific card in the initial hand.
    """
    return math.perm(total_cards - num_specific_card, hand_size) / math.perm(total_cards, hand_size)

def expected_mulligans(prob):
    """
    Calculate the expected number of mulligans based on the probability of a mulligan.
    
    :param prob: Probability of not drawing a specific card in the initial hand.
    :return: Expected number of mulligans.
    """
    return 1 / (1 - prob) - 1

def n_mulligan_prob(num_specific_card=4, mulligan_count=0):
    """
    Calculate the probability of needing a specific number of mulligans before drawing a specific card.

    :param num_specific_card: Number of specific cards in the deck.
    :param mulligan_count: Number of mulligans taken.
    :return: Probability of needing the specified number of mulligans.
    """
    p = 1 - prob_of_mulligan(num_specific_card)
    return ((1 - p) ** mulligan_count) * p

# prompt: build a bar chart to show the probability distribution above

def mulligan_count_prob_chart(num_specific_card=4, n=10):
    prob = prob_of_mulligan(num_specific_card)
    st.write("You are expected to have {:.02f} mulligans.".format(expected_mulligans(prob)))
    
    x_axis = []
    y_axis = []
    
    for i in range(n + 1):
        x_axis.append(i)
        y = n_mulligan_prob(num_specific_card, i) * 100
        y_axis.append(y)
        st.write("Probability of having {} mulligans: {:.02f}%".format(i, y))
    
    plt.figure(figsize=(8, 4))
    plt.bar(x_axis, y_axis, color='skyblue')
    plt.xlabel("Number of Mulligans")
    plt.ylabel("Probability (%)")
    plt.title("Probability Distribution of Mulligans")
    st.pyplot(plt)  # Display the plot in Streamlit

mulligan_count_prob_chart(basic_pkm_count)