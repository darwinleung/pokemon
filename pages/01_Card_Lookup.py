import streamlit as st

from pokemontcgsdk import Card, RestClient

st.set_page_config(page_title="Card Lookup", page_icon="img/favicon.ico")

# Configure the API key
RestClient.configure("f6461fa4-0eb0-4b9b-a404-e846742da4e5")

st.title("Pokémon TCG Card Lookup")
st.write("Here you can look up any card and check the market price in USD.")

# Search input
search_query = st.text_input("Enter card name or ID:")

if search_query:
    # Search for cards
    cards = Card.where(q=f'name:*{search_query}*')
    
    if cards:
        for card in cards:
            st.subheader(card.name)
            
            # Display card image
            if card.images.small:
                st.image(card.images.small, width=250)
            
            # Display card details
            st.write(f"**Set:** {card.set.name}")
            st.write(f"**Number:** {card.number}")
            st.write(f"**Rarity:** {card.rarity}")
            
            # Display type and HP for Pokémon cards
            if card.supertype == "Pokémon":
                st.write(f"**Type:** {', '.join(card.types)}")
                st.write(f"**HP:** {card.hp}")
            
            # Display market prices if available
            if hasattr(card, 'tcgplayer') and hasattr(card.tcgplayer, 'prices'):
                st.subheader("Market Prices")
                prices = card.tcgplayer.prices
                if hasattr(prices, 'normal') and prices.normal and prices.normal.market:
                    st.write(f"**Normal:** ${prices.normal.market:.2f}")
                if hasattr(prices, 'holofoil') and prices.holofoil and prices.holofoil.market:
                    st.write(f"**Holofoil:** ${prices.holofoil.market:.2f}")
                if hasattr(prices, 'reverseHolofoil') and prices.reverseHolofoil and prices.reverseHolofoil.market:
                    st.write(f"**Reverse Holofoil:** ${prices.reverseHolofoil.market:.2f}")
                if hasattr(prices, 'firstEditionHolofoil') and prices.firstEditionHolofoil and prices.firstEditionHolofoil.market:
                    st.write(f"**1st Edition Holofoil:** ${prices.firstEditionHolofoil.market:.2f}")
                if hasattr(prices, 'firstEditionNormal') and prices.firstEditionNormal and prices.firstEditionNormal.market:
                    st.write(f"**1st Edition Normal:** ${prices.firstEditionNormal.market:.2f}")
            
            st.markdown("---")
    else:
        st.warning("No cards found matching your search.")


