# AI Response Validation System with Hallucination Detection Assistance

A lightweight prototype that validates AI-generated responses against trusted reference information and identifies sentences that may require hallucination review.

## Project Overview

Large Language Models can generate responses that sound correct but contain unsupported or fabricated information. This project provides an assistance layer for response validation.

The prototype:
- Accepts an AI-generated response.
- Accepts trusted reference/context information.
- Splits the response into sentences.
- Measures lexical overlap and text similarity.
- Produces a sentence-level support confidence.
- Flags potentially hallucinated content.
- Gives an overall validation score.

## Features

- Simple web interface using Streamlit
- Sentence-level analysis
- Validation score
- Likely Supported / Partially Supported / Potential Hallucination labels
- No API key required for the prototype
- Easy to run locally and deploy

## Technology Stack

- Python
- Streamlit
- Regular Expressions
- Python difflib
- Basic NLP/text similarity techniques

## Project Structure

```text
AI_Response_Validation_System/
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
└── docs/
    ├── AGILE_DOCUMENTATION.md
    ├── PROJECT_REPORT.md
    └── ARCHITECTURE.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Response-Validation-System.git
cd AI-Response-Validation-System
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## Example

Reference:

> The Earth revolves around the Sun. One complete revolution takes approximately 365 days.

AI Response:

> The Earth revolves around the Sun. One complete revolution takes approximately 365 days. The Earth has two moons.

The system should identify the first statements as supported and flag the unsupported moon claim for review.

## Limitations

This is an academic prototype. It uses similarity and lexical-overlap heuristics rather than a complete factual verification engine. A production system could add retrieval-augmented generation, external knowledge sources, semantic embeddings, NLI models, source citation checks, and LLM-based verification.

## Future Enhancements

- Embedding-based semantic similarity
- Retrieval-Augmented Generation (RAG)
- Source citation verification
- Knowledge-base integration
- Transformer/NLI-based contradiction detection
- Confidence calibration
- Batch CSV validation
- Authentication and user history
- Cloud deployment

## Academic Project

**Project:** Development of AI Response Validation System with Hallucination Detection Assistance  
**Batch:** 2026–27  
**Group:** 1
