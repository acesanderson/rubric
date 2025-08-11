from evaluation import PartnershipEvaluation
import json
import pandas as pd

evals = []
with open("evaluations.jsonl", "r") as f:
    text = f.read()
    lines = text.splitlines()
    for line in lines:
        if line.strip():
            evals.append(
                PartnershipEvaluation.model_validate(
                    json.loads(line)["message"]["content"]
                )
            )

# Sort evals by eval.partner_name
evals.sort(key=lambda x: x.partner_name)
# Remove duplicates based on partner_name, keeping the one with the highest total_score
unique_evals = {}
for eval in evals:
    if (
        eval.partner_name not in unique_evals
        or eval.total_score > unique_evals[eval.partner_name].total_score
    ):
        unique_evals[eval.partner_name] = eval

evals = list(unique_evals.values())
# Create a dataframe with the following columns:
## partner_name
## general_recognition_score
## domain_authority_score
## career_impact_score
## total_score
## priority_tier

df = pd.DataFrame(
    [
        {
            "partner_name": eval.partner_name,
            "general_recognition_score": eval.general_recognition_score,
            "general_recognition_reasoning": eval.general_recognition_reasoning,
            "domain_authority_score": eval.domain_authority_score,
            "domain_authority_reasoning": eval.domain_authority_reasoning,
            "career_impact_score": eval.career_impact_score,
            "career_impact_reasoning": eval.career_impact_reasoning,
            "total_score": eval.total_score,
            "priority_tier": eval.priority_tier,
        }
        for eval in evals
    ]
)

df.to_csv("evaluations.csv", index=False)
