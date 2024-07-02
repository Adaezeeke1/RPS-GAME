import streamlit as st
from game.game_logic import RockPaperScissorsGame
from game.rps import RPS
import time

# Helper function to get the image for the choice


def get_choice_image(choice):
    images = {
        RPS.ROCK: "images/RPS-rock1.png",
        RPS.PAPER: "images/RPS-paper1.png",
        RPS.SCISSORS: "images/RPS-scissors1.png"
    }
    return images[choice]


# Initialize the game and session state if not already initialized
if 'game' not in st.session_state:
    st.session_state.game = RockPaperScissorsGame()
    st.session_state.round = 1

# Streamlit UI
st.title("Rock Paper Scissors")
st.subheader("Choose your move and see who wins!", divider='rainbow')

# Display the current score
st.write("Score:")
st.write(f"You: {st.session_state.game.score['player']}")
st.write(f"Computer: {st.session_state.game.score['computer']}")

'''
'''

st.subheader(f"Round {st.session_state['round']} of 3")

'''
'''

# User choice buttons
col1, col2, col3 = st.columns(3)
user_choice = None

with col1:
    if st.button("Rock"):
        user_choice = RPS.ROCK
        # st.image(get_choice_image(RPS.ROCK))
with col2:
    if st.button("Paper"):
        user_choice = RPS.PAPER
        # st.image(get_choice_image(RPS.PAPER))
with col3:
    if st.button("Scissors"):
        user_choice = RPS.SCISSORS
        # st.image(get_choice_image(RPS.SCISSORS))


# Play button with loading animation, only displayed if a choice has been made
if user_choice and st.session_state.round <= 3:
    # Display loading spinner
    with st.spinner("Playing..."):
        time.sleep(2)  # Simulate a delay for animation effect

    # Get computer choice
    computer_choice = st.session_state.game.computer.get_choice()

    # Determine winner
    st.session_state.game.determine_winner(user_choice, computer_choice)

    # Display choices
    col1, col2 = st.columns(2)
    with col1:
        st.image(get_choice_image(user_choice),
                 caption="You", use_column_width=True)
    with col2:
        st.image(get_choice_image(computer_choice),
                 caption="Computer", use_column_width=True)

    # Update round
    st.session_state.round += 1

if st.session_state.round > 3:
    winner_message = st.session_state.game.final_winner_message()

    # Display final winner message with larger font size
    st.markdown(
        f"<h1 style='text-align: center; color: white;'>{winner_message}</h1>",
        unsafe_allow_html=True
    )

  # Only release balloons if the user wins
    if st.session_state.game.score['player'] > st.session_state.game.score['computer']:
        st.balloons()

    # Automatically reset scores after the final round
    st.session_state.game = RockPaperScissorsGame()
    st.session_state.round = 1

    if st.button("Play Again"):
        st.rerun()

with st.sidebar:
    st.write("Made with ❤️ by [Adaeze](https://github.com/Adaezeeke1)")
