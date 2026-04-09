# MathForge: Natural Language to Algorithm Generation Framework

## Overview

MathForge is a deterministic AI framework that transforms natural language mathematical problem descriptions into formal algorithmic representations, executable Python code, and computational complexity analysis.

The system bridges the gap between human-readable problem statements and machine-executable logic by converting unstructured input into structured, interpretable, and reproducible computational outputs.

---

## 📄 Documentation

* Research Paper / Report (to be added)

---

## Key Contributions

* End-to-end transformation from natural language to executable code
* Deterministic pipeline ensuring reproducibility and consistency
* Intermediate Representation (IR) for structured abstraction
* Automated pseudocode and Python code generation
* Time and space complexity estimation
* Confidence scoring for output reliability

---

## Motivation

Mathematical problems are typically expressed in natural language, while computational systems require formal syntax. This mismatch introduces complexity in translating human reasoning into executable solutions.

MathForge addresses this challenge by automating the complete pipeline:

* Problem interpretation
* Algorithm identification
* Code generation
* Complexity analysis

---

## System Architecture

The system follows a compiler-inspired deterministic pipeline:

1. Text Preprocessing
2. Semantic Analysis (rule-based NLP)
3. Intermediate Representation (IR) generation
4. Pseudocode generation
5. Code synthesis (Python)
6. Complexity analysis (time & space)
7. Output generation with confidence score

This architecture ensures transparency, traceability, and reproducibility across all stages.

---

## Core Components

### 1. Natural Language Processing Engine

* Tokenization and normalization
* Keyword-based pattern matching
* Parameter extraction
* Deterministic semantic classification

### 2. Intermediate Representation (IR)

A structured abstraction layer encoding:

* Algorithm type
* Control structures (loops, recursion)
* Data structures
* Computational properties

### 3. Algorithm Template Engine

* Predefined algorithm templates
* Deterministic template selection
* Ensures correctness and avoids hallucination

**Supported algorithms:**

* Sorting (Bubble, Selection, Merge Sort)
* Searching (Binary Search)
* Recursive patterns (Factorial)
* Numerical methods (Newton-Raphson)

### 4. Code Generation

* Template-based Python code generation
* Ensures syntactic correctness
* Produces executable implementations

### 5. Complexity Analysis

* Rule-based inference of time and space complexity
* Based on structural properties of algorithms

**Examples:**

* Nested loops → O(n²)
* Divide & conquer → O(n log n)

### 6. Confidence Scoring

* Quantifies reliability of interpretation
* Based on:

  * Keyword matching
  * Parameter extraction
  * Validation consistency

---

## Technology Stack

* Python
* FastAPI (Backend API)
* HTML, CSS, JavaScript (Frontend)
* Rule-based NLP techniques

---

## Project Structure

mathforge/
│── backend/           # API and processing pipeline
│── frontend/          # User interface
│── data/              # Sample inputs / datasets
│── evaluation/        # Testing and evaluation scripts
│── README.md

---

## Installation and Setup

### 1. Clone the Repository

git clone https://github.com/your-username/mathforge.git
cd mathforge

### 2. Backend Setup

cd backend
pip install -r requirements.txt
uvicorn main:app --reload

### 3. Frontend Setup

Open frontend/index.html in browser
(or run via local server)

---

## Example Workflow

1. Input: Natural language mathematical problem
2. System extracts algorithm pattern
3. Generates:

   * Intermediate Representation
   * Pseudocode
   * Python implementation
   * Complexity analysis
   * Confidence score

---

## Example Output

**Input:**
"Find factorial of a number"

**Output:**

* Algorithm: Recursion

**Pseudocode:**

```
function factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
```

**Python Code:**

```
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
```

**Time Complexity:** O(n)
**Space Complexity:** O(n)

---

## Results

Experimental evaluation (50 test cases):

* Algorithm detection accuracy: ~92%
* Code generation accuracy: ~90%
* Complexity estimation accuracy: ~95%
* Average confidence score: 0.88

---

## Advantages

* Deterministic and reproducible outputs
* No reliance on probabilistic LLMs
* High interpretability and transparency
* Suitable for educational and research applications

---

## Limitations

* Limited to predefined algorithm templates
* No symbolic algebra support
* Rule-based NLP may struggle with ambiguous inputs

---

## Future Work

* Integration of transformer-based NLP models
* Expansion of algorithm template library
* Support for advanced mathematical domains
* Visualization of algorithm execution
* Multi-language input support

---

## Applications

* Educational tools for learning algorithms
* Automated code generation systems
* AI-assisted programming environments
* Computational mathematics platforms

---

## Why This Project Matters

Unlike LLM-based systems, MathForge uses a deterministic pipeline, ensuring reproducibility, interpretability, and reliability in algorithm generation.

This makes it particularly valuable for:

* Education
* Research
* Verified and trustworthy code generation

---

## Disclaimer

This project is developed for academic and research purposes and demonstrates deterministic AI system design.

---

## Author

Thrishika
B.Tech in Computer Science and Engineering (AI)
