
import streamlit as st
from typing import List, Tuple
from app.modules.app_logic import Card, HeroCard, ItemCard, Location, User


def display_cards(cards: List[Card]) -> None:
    for card in cards:
        st.image(card.image, width=100)
        st.write(card.name)
        st.write(card.description)


def display_user_info(user: User) -> None:
    st.write(f"Username: {user.username}")
    st.write(f"Email: {user.email}")


def display_locations(locations: List[Location]) -> None:
    for location in locations:
        st.image(location.image, width=100)
        st.write(location.name)
        st.write(location.description)


def select_cards_for_trade(user: User) -> List[int]:
    card_ids = st.multiselect("Select cards to trade:", list(range(1, len(user.cards) + 1)))
    return card_ids


def select_cards_for_exploration(user: User) -> Tuple[List[int], List[int]]:
    hero_card_ids = st.multiselect("Select hero cards for exploration:", list(range(1, len(user.hero_cards) + 1)))
    item_card_ids = st.multiselect("Select item cards for exploration:", list(range(1, len(user.item_cards) + 1)))
    return hero_card_ids, item_card_ids


def select_cards_for_battle(user: User) -> Tuple[List[int], List[int]]:
    hero_card_ids = st.multiselect("Select hero cards for battle:", list(range(1, len(user.hero_cards) + 1)))
    item_card_ids = st.multiselect("Select item cards for battle:", list(range(1, len(user.item_cards) + 1)))
    return hero_card_ids, item_card_ids


def select_location(locations: List[Location]) -> Location:
    location_names = [location.name for location in locations]
    selected_location_name = st.selectbox("Select a location:", location_names)
    return next(location for location in locations if location.name == selected_location_name)


def show_event_description(event_description: str) -> None:
    st.write("Event Description:")
    st.write(event_description)


def show_loot(loot: List[ItemCard]) -> None:
    st.write("Loot:")
    display_cards(loot)


def show_trade_result(success: bool) -> None:
    if success:
        st.success("Trade completed successfully!")
    else:
        st.error("Trade failed. Please try again.")


def show_exploration_result(success: bool) -> None:
    if success:
        st.success("Exploration completed successfully!")
    else:
        st.error("Exploration failed. Please try again.")


def show_battle_result(success: bool) -> None:
    if success:
        st.success("Battle completed successfully!")
    else:
        st.error("Battle failed. Please try again.")

