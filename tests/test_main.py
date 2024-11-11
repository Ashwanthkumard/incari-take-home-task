import os
import sys
import unittest
from unittest.mock import patch

import yaml

from app.evaluation import calculate_metrics

# Ensure app directory is in the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))
from app.main import generate_node_sequence

with open('../config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

model = config['model']


class TestMain(unittest.TestCase):
    @patch('app.main.client')
    def test_generate_node_sequence(self, mock_client):
        # Mock the generate method on the Ollama client
        mock_client.generate.return_value = {'response': '[OnKeyPress, Log, Display]'}

        # Run the function with test input
        test_input = "Log a message when a key is pressed and display the key value on the screen."
        result = generate_node_sequence(test_input)

        # Assert the output is as expected
        self.assertEqual(result, ['OnKeyPress', 'Log', 'Display'])

class TestEvaluationMetrics(unittest.TestCase):
    def setUp(self):
        # Sample generated and reference sequences
        self.generated_sequences = [
            ["OnClick", "FetchData", "DisplayModal"],
            ["Log", "Display"],
            ["OnMouseEnter", "Highlight", "OnMouseLeave", "Show"]
        ]
        self.reference_sequences = [
            ["OnClick", "FetchData", "DisplayModal"],
            ["Log", "Show"],
            ["OnMouseEnter", "Highlight", "OnMouseLeave", "Highlight"]
        ]

    def test_calculate_metrics(self):
        # Expected metrics
        expected_metrics = {
            "Exact Match Accuracy": 33.33,  # Only 1 out of 2 is an exact match
            "Average Precision": 75.0,     # 3/4 nodes correct
            "Average Recall": 75.0,        # 3/4 nodes correct
            "Average F1 Score": 75.0,      # F1 Score for both sequences
            "Average BLEU Score": 56.09     # BLEU calculated with 1-gram and 2-gram overlap
        }

        # Calculate metrics
        metrics = calculate_metrics(self.generated_sequences, self.reference_sequences)
        # Assert each metric is as expected
        for metric_name, expected_value in expected_metrics.items():
            with self.subTest(metric=metric_name):
                self.assertAlmostEqual(metrics[metric_name], expected_value, delta=1.0,
                                       msg=f"{metric_name} is not as expected")
if __name__ == '__main__':
    unittest.main()
