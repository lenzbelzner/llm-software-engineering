
import streamlit as st
from app.modules.user_management import create_user, authenticate_user, get_user_by_username
from app.modules.app_logic import get_heroes, get_items, get_locations
from app.modules.user_interface import (
    display_user_info,
    display_cards,
    display_locations,
    select_cards_for_trade,
    select_cards_for_exploration,
    select_cards_for_battle,
    select_location,
    show_event_description,
    show_loot,
    show_trade_result,
    show_exploration_result,
    show_battle_result,
)

def create_account():
    username = st.text_input("Enter a username")
    password = st.text_input("Enter a password", type="password")
    email = st.text_input("Enter your email")
    if st.button("Create Account"):
        user = create_user(username, password, email)
        return user
    return None

def login():
    username = st.text_input("Enter your username")
    password = st.text_input("Enter your password", type="password")
    if st.button("Login"):
        if authenticate_user(username, password):
            user = get_user_by_username(username)
            return user
    return None

def display_main_menu(user):
    st.header("Main Menu")
    display_user_info(user)
    options = ["Trade Cards", "Explore Location", "Battle at Location"]
    choice = st.selectbox("Choose an action", options)

    if choice == "Trade Cards":
        trade_cards(user)
    elif choice == "Explore Location":
        explore_location(user)
    elif choice == "Battle at Location":
        battle_at_location(user)

def trade_cards(user):
    st.header("Trade Cards")
    display_cards(get_heroes())
    display_cards(get_items())
    card_ids = select_cards_for_trade(user)
    if card_ids:
        success = trade_cards(user, card_ids)
        show_trade_result(success)

def explore_location(user):
    st.header("Explore Location")
    display_locations(get_locations())
    location = select_location(get_locations())
    hero_card_ids, item_card_ids = select_cards_for_exploration(user)
    if location and hero_card_ids and item_card_ids:
        event_description, loot = start_exploration(user, location, hero_card_ids, item_card_ids)
        show_event_description(event_description)
        show_loot(loot)
        show_exploration_result(True)

def battle_at_location(user):
    st.header("Battle at Location")
    display_locations(get_locations())
    location = select_location(get_locations())
    hero_card_ids, item_card_ids = select_cards_for_battle(user)
    if location and hero_card_ids and item_card_ids:
        event_description, loot = start_battle(user, location, hero_card_ids, item_card_ids)
        show_event_description(event_description)
        show_loot(loot)
        show_battle_result(True)

if __name__ == "__main__":
    st.title("Trading Card Game")
    logged_in_user = None

    while not logged_in_user:
        if st.button("Create Account"):
            logged_in_user = create_account()
        elif st.button("Login"):
            logged_in_user = login()

    display_main_menu(logged_in_user)

