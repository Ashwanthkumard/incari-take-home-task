import unittest
from unittest.mock import patch, MagicMock
import sys
import os

import yaml

# Ensure app directory is in the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from app.main import generate_node_sequence
from app.prompt import PROMPT_TEMPLATE

with open('../config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

model = config['model']

class TestMain(unittest.TestCase):

    def test_generate_node_sequence(self):
        # Mock the ollama.Client and its generate method
        mock_client = MagicMock()
        mock_client.generate.return_value = {'response': '[OnKeyPress, Log, Display]'}

        # Define a test input and expected prompt template
        test_input = "Log a message when a key is pressed and display the key value on the screen."
        mock_prompt = PROMPT_TEMPLATE.format(test_input)

        # Run the function with the test input and mocked client
        result = generate_node_sequence(test_input, mock_client, model)

        # Verify the function output matches the expected node sequence
        self.assertEqual(result, '[OnKeyPress, Log, Display]')

        # Confirm generate was called with the correct arguments
        mock_client.generate.assert_called_once_with(
            model='llama3.2:1b',
            prompt=mock_prompt,
            stream=False
        )


if __name__ == '__main__':
    unittest.main()
