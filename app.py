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

# User choice
user_choice = st.selectbox("Choose your move:", options=list(
    RPS), format_func=lambda x: x.name.capitalize())

# Play button with loading animation, only displayed if round <= 3
if st.session_state.round <= 3 and st.button("Play"):
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

    # Display result
    st.write(st.session_state.game.final_winner_message())

    # Update round
    st.session_state.round += 1

# Check if the series is complete
if st.session_state.round > 3:
    st.write("Best of 3 series complete!")

    # Automatically reset scores after the final round
    st.session_state.game = RockPaperScissorsGame()
    st.session_state.round = 1

    if st.button("Play Again"):
        st.rerun()

with st.sidebar:
    st.write("Made with ❤️ by [Adaeze](https://github.com/Adaezeeke1)")
