# System Architecture

```text
+---------------------------+
|       User Interface      |
|       Streamlit Web UI    |
+-------------+-------------+
              |
              v
+---------------------------+
|      Input Processing     |
|  Cleaning + Sentence Split|
+-------------+-------------+
              |
              v
+---------------------------+
|     Validation Engine     |
|  Token Overlap + Similarity|
+-------------+-------------+
              |
              v
+---------------------------+
|  Hallucination Assistance |
| Supported / Partial /     |
| Potential Hallucination   |
+-------------+-------------+
              |
              v
+---------------------------+
|     Results & Score       |
| Sentence Analysis + Status|
+---------------------------+
```

## Processing Flow

1. User enters an AI response.
2. User provides trusted reference/context.
3. Text is cleaned and divided into sentences.
4. Each sentence is compared with reference text.
5. Support confidence is calculated.
6. Sentences are classified.
7. Overall validation score is displayed.
