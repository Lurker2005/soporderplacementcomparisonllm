# SOP Order Placement – LLM Comparison

This project focuses on **comparing Large Language Models (LLMs)** for automating and evaluating **SOP (Standard Operating Procedure) order placement workflows**.  
The goal is to analyze how different LLMs interpret instructions, follow structured steps, and generate consistent, reliable outputs for order placement scenarios.

---

## 📌 Project Overview

Manual SOP-based order placement can be:
- Time-consuming  
- Error-prone  
- Inconsistent across operators  

This project explores how LLMs can assist or automate parts of this process by:
- Understanding structured SOP instructions  
- Extracting key entities (order details, quantities, conditions)  
- Producing standardized outputs  

---

## 🧠 What This Project Does

- Compares responses from different LLMs
- Evaluates:
  - Instruction-following accuracy
  - Consistency of outputs
  - Hallucination or deviation from SOP
- Uses prompt-based experiments and analysis notebooks

---

## 🛠 Tech Stack

- **Python 3.x**
- **Jupyter Notebook**
- **Hugging Face Transformers**
- **PyTorch**
- Supporting libraries listed in `requirements.txt`

---

## 📂 Project Structure

```text
.
├── main.ipynb            # Core notebook for LLM comparison & experiments
├── requirements.txt      # Python dependencies
├── .gitignore            # Ignored files (venv, .env, cache, etc.)
├── .env.example          # Environment variable template (no secrets)
└── README.md             # Project documentation
