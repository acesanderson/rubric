# LinkedIn Learning Partnership Evaluation Rubric

A Python framework for evaluating potential Professional Certificate partnerships using a standardized 15-point scoring system.

## Overview

This tool evaluates partnership opportunities across three key dimensions:

1. **Partner General Recognition** (1-5 points) - Brand awareness among professionals
2. **Partner Domain Authority** (1-5 points) - Expertise in the specific skill area  
3. **Skill Career Impact** (1-5 points) - Career advancement value in North America

## Installation

```bash
pip install pydantic
```

## Usage

### Basic Evaluation

```python
from evaluation import PartnershipEvaluation

evaluation = PartnershipEvaluation(
    partner_name="Microsoft",
    certificate_topic="Azure AI Fundamentals",
    general_recognition_score=5,
    general_recognition_reasoning="Microsoft is a globally recognized technology leader...",
    domain_authority_score=5,
    domain_authority_reasoning="Azure is the #2 cloud platform globally...",
    career_impact_score=5,
    career_impact_reasoning="AI skills are among the fastest growing and highest paying..."
)

print(evaluation.human_readable_summary)
print(f"Priority: {evaluation.priority_tier}")
```

### Batch Processing

```python
# partners.py - Process multiple certificates
python partners.py  # Generates evaluations.jsonl

# load.py - Convert to CSV for analysis
python load.py      # Creates evaluations.csv
```

## Scoring Framework

**Priority Tiers:**
- 13-15 points: Strategic Priority (Tier 1) - Immediate pursuit
- 10-12 points: Strong Candidate (Tier 2) - High priority
- 7-9 points: Tactical Partnership (Tier 3) - Consider if resources allow
- 3-6 points: Pass - Not recommended

## Files

- `evaluation.py` - Core evaluation model and logic
- `mixin.py` - Business logic and human-readable formatting
- `partners.py` - Batch processing script for certificate analysis
- `load.py` - Data export and CSV generation
- `LinkedIn Professional Context.md` - Background context for evaluations

## Dependencies

- `pydantic` - Data validation and modeling
- `pandas` - Data analysis (load.py only)
- Custom modules: `Kramer`, `Chain` (for batch processing)
