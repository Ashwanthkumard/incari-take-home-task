from nltk.translate.bleu_score import sentence_bleu


def calculate_metrics(pred_seq, refer_seq):
    exact_matches = 0
    precisions, recalls, f1_scores, bleu_scores = [], [], [], []

    for generated, reference in zip(pred_seq, refer_seq):
        # Exact Match
        if generated == reference:
            exact_matches += 1

        # Precision, Recall, F1 (treating nodes as unordered)
        true_positive = len(set(generated) & set(reference))
        precision = true_positive / len(generated) if generated else 0
        recall = true_positive / len(reference) if reference else 0
        f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

        # BLEU Score (N-gram Precision)
        bleu_score = sentence_bleu([reference], generated, weights=(0.5, 0.5))  # weights for 1-gram, 2-gram

        # Append to lists
        precisions.append(precision)
        recalls.append(recall)
        f1_scores.append(f1)
        bleu_scores.append(bleu_score)

    # Overall Metrics
    exact_match_accuracy = (exact_matches / len(refer_seq)) * 100
    avg_precision = sum(precisions) / len(precisions) * 100
    avg_recall = sum(recalls) / len(recalls) * 100
    avg_f1_score = sum(f1_scores) / len(f1_scores) * 100
    avg_bleu_score = sum(bleu_scores) / len(bleu_scores) * 100

    return {
        "Exact Match Accuracy": exact_match_accuracy,
        "Average Precision": avg_precision,
        "Average Recall": avg_recall,
        "Average F1 Score": avg_f1_score,
        "Average BLEU Score": avg_bleu_score
    }


# Example usage
generated_sequences = [["OnClick", "FetchData", "DisplayModal"], ["Log", "Display"]]
reference_sequences = [["OnClick", "FetchData", "DisplayModal"], ["Log", "Show"]]

metrics = calculate_metrics(generated_sequences, reference_sequences)
print(metrics)
