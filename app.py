"""
WARGAMER

This is the main script to run the wargamer Streamlit tool.

TODO:
- Switch button functionality utilize the on click parameter.

Author: Anthony Baum
"""

from app_logic import data, actions
import streamlit as st


st.title('Wargamer')

# Create deck for each phase of play
action_decks = {
    'command': actions.CardDeck('command'),
    'movement': actions.CardDeck('movement'),
    'psychic': actions.CardDeck('psychic'),
    'shooting': actions.CardDeck('shooting'),
    'charge': actions.CardDeck('charge'),
    'fight': actions.CardDeck('fight'),
    'morale': actions.CardDeck('morale')
    }

# Create buttons for generating cards
cmd_move_psych_shoot_container = st.container()
charge_fight_morale_reset_container = st.container()
output_container = st.container(border=True)

# Create a global variable for the currently selected card
current_card = None
current_action = None

# Display buttons
with cmd_move_psych_shoot_container:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        command_button = st.button('Command')
        if command_button:
            action_card = action_decks['command'].pull_card()
            current_card = action_card
            current_action = 'Command'

    with col2:
        movement_button = st.button('Movement')
        if movement_button:
            action_card = action_decks['movement'].pull_card()
            current_card = action_card
            current_action = 'Movement'

    with col3:
        psychic_button = st.button('Pyschic')
        if psychic_button:
            action_card = action_decks['psychic'].pull_card()
            current_card = action_card
            current_action = 'Psychic'

    with col4:
        shooting_button = st.button('Shooting')
        if shooting_button:
            action_card = action_decks['shooting'].pull_card()
            current_card = action_card
            current_action = 'Shooting'

with charge_fight_morale_reset_container:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        charge_button = st.button('Charge')
        if charge_button:
            action_card = action_decks['charge'].pull_card()
            current_card = action_card
            current_action = 'Charge'

    with col2:
        fight_button = st.button('Fight')
        if fight_button:
            action_card = action_decks['fight'].pull_card()
            current_card = action_card
            current_action = 'Fight'

    with col3:
        morale_button = st.button('Morale')
        if morale_button:
            action_card = action_decks['morale'].pull_card()
            current_card = action_card
            current_action = 'Morale'

    with col4:
        pass

# Display new card on button click
with output_container:
    if isinstance(current_card, actions.ActionCard):
        st.header(f'{current_action} Action Card')
        st.subheader('Preferred Action')
        st.text(current_card.action1)
        st.subheader('Backup Action')
        st.text(current_card.action2)
        st.subheader('Secondary Backup Action')
        st.text(current_card.action3)
    else:
        st.header('Select an Action')
        pass



