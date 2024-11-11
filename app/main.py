import os
import re
import subprocess

import yaml

from prompt import PROMPT_TEMPLATE
import ollama

client, model = None, None


# Function to initialize Ollama client and model
def initialize_client_and_model():
    global client, model
    # Load configuration from YAML file
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config.yaml')
    with open(config_path, 'r') as config_file:
        config = yaml.safe_load(config_file)
    model = config['model']

    # Start the client
    # Determine the host dynamically
    host = os.getenv("OLLAMA_HOST")  # Returns None if OLLAMA_HOST is not set

    # Initialize the client, using host only if it's explicitly set
    client = ollama.Client(host=host) if host else ollama.Client()


def filter_node_sequence(response_text):
    # Use regex to extract the first sequence enclosed in brackets
    match = re.search(r'\[.*?\]', response_text)
    if match:
        node_sequence = match.group(0)
        # Remove any extra whitespace and split the nodes into a list
        nodes = [node.strip() for node in node_sequence.strip("[]").split(",")]
        return nodes
    else:
        print("Invalid response format.")
        return []


# Function to generate the node sequence using the Llama model
def generate_node_sequence(user_prompt):
    global client, model
    # Create the full prompt for the LLM
    prompt = PROMPT_TEMPLATE.format(user_prompt)

    # Use Llama client to generate a response
    response = client.generate(
        model=model,
        prompt=prompt,
        stream=False
    )

    # Collect the response as a single text string
    generated_text = response['response']

    # Filter to get clean node sequence
    return filter_node_sequence(generated_text)


# CLI Main function
def main():
    initialize_client_and_model()
    # Take user input or use a predefined prompt for testing
    while True:
        user_prompt = input("Enter a prompt (or type 'exit' to quit): ")
        if user_prompt.lower() == "exit":
            break
        # Generate the node sequence
        node_sequence = generate_node_sequence(user_prompt)
        # Display the generated node sequence
        print("Generated Node Sequence:", node_sequence)


if __name__ == "__main__":
    main()
