# incari-take-home-task

## Instructions to Run the Streamlit App standalone
## Setup the server by running the following commands:

```bash
chmod +x start_llama.sh
```

Run the script before starting your Python code:

```bash
./start_llama.sh
```

Start Your Python Script: Once the Ollama service is confirmed to be running, you can start your Python script as usual.

```bash
streamlit run app/streamlit_app.py
```

And then open the URL provided in the terminal: http://localhost:8501


### clean up port 8501 after testing
```bash
kill -9 $(lsof -t -i :8501)
```

# Instructions to Run the Streamlit App in Docker

Make sure you have ollama installed and running on host machine

```bash
ollama run llama3.2
```

### clean up port 8501 if already in use
```bash
kill -9 $(lsof -t -i :8501)
```

### Build the Docker Image:
```bash
docker build -t my-streamlit-app .
```

### Run the Docker Container:
```bash
docker run -p 8501:8501 --name streamlit-app -e OLLAMA_HOST="http://host.docker.internal:11434" my-streamlit-app
```

### Stop the Docker Container:
```bash
docker stop streamlit-app
```

With this setup, Docker will start Streamlit in the same way you currently run it, ensuring consistency across environments.


## Evaluation Metrics

To evaluate the performance of the node sequence generation model, the following metrics are used:

### 1. Exact Match Accuracy
This metric calculates the percentage of sequences that perfectly match the reference sequences.

**Formula:**
```
Exact Seq Match Accuracy = (Number of exact seq matches / Total number of sequences) * 100
```

### 2. Precision and Recall
For cases where generated sequences don’t match the reference exactly, Precision and Recall provide insight into how well individual nodes in the generated sequences overlap with the reference.

**Precision:**
Measures the proportion of nodes in the generated sequence that are correct.
```
Precision = True Positives / (True Positives + False Positives)
```

**Recall:**
Measures the proportion of reference nodes that were correctly generated.
```
Recall = True Positives / (True Positives + False Negatives)
```

**F1 Score:**
Combines Precision and Recall to balance the two.
```
F1 Score = 2 * (Precision * Recall) / (Precision + Recall)
```

### 3. N-gram Precision (BLEU Score)
BLEU measures n-gram overlap between generated and reference sequences to evaluate sequence similarity more granularly.

- **1-gram Precision:** Checks individual node overlap.
- **2-gram Precision:** Checks pairs of consecutive nodes, and so on.

The BLEU score combines different n-gram precisions, typically up to 4-grams, with weights applied to each. For node sequences, you might prioritize 1-gram and 2-gram precisions if node order is flexible.

**Formula:**
```
BLEU Score = BP * exp(sum(w_n * log(p_n)))
```
where:
- `BP` is the brevity penalty.
- `w_n` is the weight for n-gram precision.
- `p_n` is the n-gram precision.

