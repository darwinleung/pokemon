import streamlit as st

st.set_page_config(page_title="Card Lookup", page_icon="img/favicon.ico")

st.markdown("# Card Lookup")
st.markdown("WIP") 


import streamlit as st
from pokemontcgsdk import Card, RestClient

# Configure the API key
RestClient.configure("YOUR_API_KEY_HERE")

st.title("Pokémon TCG Card Lookup")
st.write("Here you can look up any card and check the market price")

# Search input
search_query = st.text_input("Enter card name or ID:")

# if search_query:
#     # Search for cards
#     cards = Card.where(q=f"name:{search_query}")
    
#     if cards:
#         for card in cards:
#             st.subheader(card.name)
            
#             # Display card image
#             if card.images.small:
#                 st.image(card.images.small, width=250)
            
#             # Display card details
#             st.write(f"**Set:** {card.set.name}")
#             st.write(f"**Number:** {card.number}")
#             st.write(f"**Rarity:** {card.rarity}")
            
#             # Display type and HP for Pokémon cards
#             if card.supertype == "Pokémon":
#                 st.write(f"**Type:** {', '.join(card.types)}")
#                 st.write(f"**HP:** {card.hp}")
            
#             # Display market prices if available
#             if hasattr(card, 'tcgplayer') and hasattr(card.tcgplayer, 'prices'):
#                 st.subheader("Market Prices")
#                 for price_type, price_data in card.tcgplayer.prices.items():
#                     if price_data:
#                         st.write(f"**{price_type.capitalize()}:** ${price_data.market:.2f}")
            
#             st.markdown("---")
#     else:
#         st.warning("No cards found matching your search.")