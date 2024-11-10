import yaml

from prompt import PROMPT_TEMPLATE
import ollama


# Function to generate the node sequence using Llama model
def generate_node_sequence(user_prompt, client, model):
    # Create the full prompt for the LLM
    prompt = PROMPT_TEMPLATE.format(user_prompt)

    # Use Llama client to generate a response with streaming
    response = client.generate(
        model=model,
        prompt=prompt,
        stream=False
    )

    # Collect the response as a single text string
    generated_text = response['response']

    return generated_text


# Main function to run the application
def main():
    # Load configuration from YAML file
    with open('../config.yaml', 'r') as config_file:
        config = yaml.safe_load(config_file)

    model = config['model']

    # Start the service before creating the client
    client = ollama.Client()
    # Take user input or use a predefined prompt for testing
    while True:
        user_prompt = input("Enter a prompt: ")
        if user_prompt == "exit":
            break

        # Generate the node sequence
        node_sequence = generate_node_sequence(user_prompt, client, model)

        # Display the generated node sequence
        print("Generated Node Sequence:", node_sequence)


if __name__ == "__main__":
    main()
