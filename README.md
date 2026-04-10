# Rubric

Rubric is a tool for the automated strategic evaluation of professional certificate partnerships. It uses large language models to score potential opportunities against a standardized framework of brand recognition, domain authority, and career impact.

## Table of Contents
- [Quick Start](#quick-start)
- [Core Value Demonstration](#core-value-demonstration)
- [Evaluation Framework](#evaluation-framework)
- [Installation](#installation)
- [Basic Usage](#basic-usage)
- [Data Processing](#data-processing)

## Quick Start

### Installation
Install the package in editable mode using pip:

```bash
pip install -e .
```

Note: This project requires Python 3.12+ and expects sibling directories for `dbclients-project`, `conduit-project`, and `kramer-project` as defined in the `pyproject.toml`.

### Single Command Evaluation
Score a certificate title immediately via the CLI:

```bash
score "Google Data Analytics Professional Certificate"
```

## Core Value Demonstration

Rubric transforms a simple certificate title into a multi-dimensional strategic assessment. For a given input, the system generates a structured evaluation:

**Input:**
`score "Meta Marketing Analytics"`

**Output:**
```text
Meta's "Marketing Analytics" certificate scores 14/15 points (strategic priority (tier 1)).

The partnership features very high brand recognition among professionals, high domain expertise in this specific skill area, and very high career impact for learners' career advancement. This combination suggests immediate pursuit recommended.

Key strengths: strong brand recognition, established domain authority, high-value skill for career advancement
No significant concerns identified.
```

## Evaluation Framework

The system evaluates partnerships across three dimensions, scoring each from 1 to 5 for a maximum total of 15 points.

### Scoring Dimensions

| Dimension | Description |
|-----------|-------------|
| **General Recognition** | Global brand awareness among a general professional audience. |
| **Domain Authority** | Specific reputation and leadership within the certificate's technical niche. |
| **Career Impact** | The degree to which the skill drives employability or salary growth in North America. |

### Priority Tiers

Evaluations are automatically categorized into tiers based on the cumulative score:

| Total Score | Priority Tier | Recommendation |
|-------------|---------------|----------------|
| 13 - 15 | Strategic Priority (Tier 1) | Immediate pursuit |
| 10 - 12 | Strong Candidate (Tier 2) | High priority development |
| 7 - 9 | Tactical Partnership (Tier 3) | Pursue if resources allow |
| 3 - 6 | Pass | Not recommended |

## Installation

### Prerequisites
- Python 3.12 or higher
- Access to the `conduit` LLM gateway
- Environment variables configured for the `conduit` library

### Setup
1. Clone the repository and its required sibling dependencies.
2. Ensure the following directory structure:
   ```text
   .
   ├── conduit-project/
   ├── dbclients-project/
   ├── kramer-project/
   └── rubric-project/
   ```
3. Install using `uv` or `pip` from the `rubric-project` directory:
   ```bash
   pip install -e .
   ```

## Basic Usage

### CLI Commands
The `score` entry point provides two primary functions:

**Score a certificate:**
```bash
score "AWS Certified Cloud Practitioner"
```

**View the scoring rubric:**
```bash
score --rubric
```

### Library Usage
The `PartnershipEvaluation` model can be used directly in Python scripts for structured data handling:

```python
from rubric.evaluation import PartnershipEvaluation

eval = PartnershipEvaluation(
    partner_name="Adobe",
    certificate_topic="Creative Cloud Mastery",
    general_recognition_score=5,
    general_recognition_reasoning="Adobe is a household name...",
    domain_authority_score=5,
    domain_authority_reasoning="Adobe is the industry standard...",
    career_impact_score=4,
    career_impact_reasoning="Essential for design roles..."
)

print(eval.total_score)        # 14
print(eval.priority_tier)     # Strategic Priority (Tier 1)
```

## Data Processing

For batch operations, the project includes utilities to process LLM outputs stored in JSONL format into flattened CSV files for analysis.

Run the loading script to consolidate evaluations:
```bash
python src/rubric/load.py
```

This script performs:
- Deduplication of partners (keeping the highest score).
- Sorting by partner name.
- Transformation of nested LLM responses into a flat `evaluations.csv`.
