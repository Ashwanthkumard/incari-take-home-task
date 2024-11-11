import streamlit as st
from main import initialize_client_and_model, generate_node_sequence
import sys

# Initialize Ollama client and model only once when the app starts
if 'initialized' not in st.session_state:
    initialize_client_and_model()
    st.session_state['initialized'] = True

st.title("Node Sequence Generator")

# Streamlit input for the user prompt
user_prompt = st.text_input("Enter a prompt:")

if st.button("Generate Node Sequence"):
    if user_prompt:
        # Generate and display the node sequence
        node_sequence = generate_node_sequence(user_prompt)
        st.write("Generated Node Sequence:", node_sequence)
    else:
        st.write("Please enter a prompt.")
