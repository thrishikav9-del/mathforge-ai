# MathForge AI

**Deterministic Natural Language to Algorithm Generation Framework**

MathForge AI is a deterministic framework that transforms natural-language mathematical problem statements into structured algorithmic representations, pseudocode, executable Python code, and computational complexity analysis.

Inspired by compiler design principles, the framework uses a rule-based processing pipeline to make the transformation process reproducible, interpretable, and traceable.

---

## Overview

Mathematical problems are often expressed in natural language, while computational systems require structured algorithmic representations.

MathForge AI addresses this gap by systematically processing problem descriptions and transforming them into formal algorithmic representations, executable Python implementations, and complexity estimates through a deterministic pipeline.

Unlike probabilistic large language model-based approaches, MathForge AI relies on predefined rules and algorithm templates for supported problem patterns. This provides predictable and interpretable processing for the supported inputs.

---

## Key Capabilities

- Natural-language mathematical problem interpretation
- Deterministic algorithm identification
- Intermediate Representation (IR) generation
- Pseudocode generation
- Python code synthesis
- Time and space complexity estimation
- Confidence scoring based on interpretation and validation signals

---

## Motivation

Translating a mathematical problem from natural language into executable code requires several stages of interpretation.

MathForge AI organizes this process into a structured pipeline:

1. Problem interpretation
2. Algorithm identification
3. Intermediate representation
4. Pseudocode generation
5. Python code generation
6. Complexity analysis

The goal is to make this transformation process explicit, reproducible, and easier to inspect than an opaque code-generation workflow.

---

## System Architecture

```text
Natural-Language Problem
          |
          v
  Text Preprocessing
          |
          v
  Semantic Analysis
   (Rule-Based NLP)
          |
          v
Intermediate Representation
          |
          v
 Pseudocode Generation
          |
          v
   Code Synthesis
      (Python)
          |
          v
 Complexity Analysis
          |
          v
  Confidence Scoring
          |
          v
     Final Output
```

### Processing Pipeline

1. **Text Preprocessing**  
   Normalizes and prepares the input problem statement.

2. **Semantic Analysis**  
   Uses rule-based NLP techniques to identify patterns, keywords, parameters, and problem characteristics.

3. **Intermediate Representation**  
   Converts the interpreted problem into a structured representation containing algorithmic information.

4. **Pseudocode Generation**  
   Produces structured pseudocode based on the identified algorithm pattern.

5. **Code Synthesis**  
   Generates Python code using predefined algorithm templates.

6. **Complexity Analysis**  
   Estimates time and space complexity based on the structural properties of the generated algorithm.

7. **Confidence Scoring**  
   Provides a score based on interpretation, parameter extraction, and validation signals.

---

## Core Components

### 1. Natural Language Processing Engine

The NLP component performs deterministic processing of mathematical problem statements using:

- Tokenization and normalization
- Keyword-based pattern matching
- Parameter extraction
- Rule-based semantic classification

---

### 2. Intermediate Representation

The Intermediate Representation (IR) provides a structured abstraction between natural-language input and generated code.

It can encode information such as:

- Algorithm type
- Control structures
- Loops and recursion
- Data structures
- Computational properties
- Extracted parameters

---

### 3. Algorithm Template Engine

The template engine maps supported problem patterns to predefined algorithm implementations.

Key characteristics include:

- Predefined algorithm templates
- Deterministic template selection
- Structured algorithm mapping
- Consistent code-generation patterns

### Supported Algorithm Patterns

The project currently supports algorithm patterns including:

- Bubble Sort
- Selection Sort
- Merge Sort
- Binary Search
- Factorial
- Newton-Raphson

---

### 4. Code Generation

The code-generation component produces Python implementations from the selected algorithm templates.

The generated output includes:

- Python source code
- Algorithm-specific structure
- Implementable logic
- Complexity information

---

### 5. Complexity Analysis

MathForge AI performs rule-based estimation of computational complexity using structural characteristics of algorithms.

Examples include:

```text
Nested loops       → O(n²)
Divide and conquer → O(n log n)
Linear traversal   → O(n)
```

The analysis is intended for the supported algorithm patterns and generated structures.

---

### 6. Confidence Scoring

The framework provides confidence information based on signals such as:

- Keyword matching
- Parameter extraction
- Validation consistency
- Interpretation results

The confidence score provides additional context about the generated interpretation.

---

## Technology Stack

- **Python**
- **FastAPI**
- **HTML**
- **CSS**
- **JavaScript**
- **Rule-based NLP**

---

## Project Structure

```text
mathforge-ai/
│
├── backend/              # Backend API and processing pipeline
├── frontend/             # Frontend interface
├── data/                 # Sample inputs and project data
├── evaluation/           # Evaluation and testing scripts
├── docs/                 # Project documentation
├── README.md
├── LICENSE
└── .gitignore
```

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/thrishikav9-del/mathforge-ai.git
cd mathforge-ai
```

### 2. Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

### 3. Frontend Setup

Open the frontend entry point:

```text
frontend/index.html
```

The frontend can be opened directly in a browser or served through a local development server.

---

## Example Workflow

A typical MathForge AI workflow is:

```text
Input
  ↓
Natural-language mathematical problem
  ↓
Text preprocessing
  ↓
Pattern and parameter extraction
  ↓
Algorithm identification
  ↓
Intermediate Representation
  ↓
Pseudocode generation
  ↓
Python code generation
  ↓
Complexity analysis
  ↓
Confidence scoring
  ↓
Final structured output
```

---

## Example

### Input

```text
Find factorial of a number
```

### Generated Algorithm

```text
Algorithm: Recursion
```

### Generated Pseudocode

```text
function factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

### Generated Python

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

### Complexity

```text
Time Complexity: O(n)
Space Complexity: O(n)
```

---

## Evaluation

The repository includes an `evaluation/` directory containing testing and evaluation resources for the supported algorithm patterns.

The evaluation component can be used to examine:

- Algorithm identification
- Parameter extraction
- Generated Python code
- Complexity estimation
- Confidence scoring

Evaluation results should be interpreted within the scope of the predefined algorithm templates and supported problem patterns.

---

## Advantages

- Deterministic processing for supported problem patterns
- Rule-based and interpretable pipeline
- Reproducible processing for supported inputs
- Explicit intermediate representation
- Structured code-generation workflow
- Transparent complexity-analysis stage
- Suitable for educational and research-oriented experimentation

---

## Limitations

- Currently limited to predefined algorithm templates
- Rule-based NLP may have difficulty with ambiguous problem statements
- Limited support for advanced mathematical domains
- No general-purpose symbolic algebra engine
- Generated results depend on supported problem patterns and templates

---

## Future Work

Potential extensions include:

- Expanding the algorithm template library
- Improving handling of ambiguous natural-language inputs
- Supporting more advanced mathematical problem types
- Adding algorithm execution visualization
- Exploring multilingual input support
- Investigating neural or hybrid NLP approaches
- Extending evaluation coverage across broader problem types

---

## Applications

MathForge AI can serve as a foundation for:

- Educational tools for learning algorithms
- Algorithm learning and visualization systems
- Automated code-generation experiments
- AI-assisted programming environments
- Computational mathematics applications
- Research into interpretable AI-based code generation

---

## Why MathForge AI?

MathForge AI explores an alternative approach to natural-language-to-code generation by using a deterministic, rule-based pipeline rather than relying entirely on probabilistic language models.

The project focuses on making the transformation from a natural-language problem to an executable algorithmic solution more explicit and inspectable.

Its compiler-inspired structure separates interpretation, representation, generation, and analysis into distinct stages.

---

## Academic and Research Context

MathForge AI was developed as an academic and research-oriented project exploring:

- Deterministic AI system design
- Natural-language problem interpretation
- Algorithm generation
- Explainable computational workflows
- Natural-language-to-code transformation

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

**Vullasa Thrishika**

B.Tech Artificial Intelligence  
Amrita Vishwa Vidyapeetham

GitHub: [@thrishikav9-del](https://github.com/thrishikav9-del)
