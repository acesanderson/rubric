from Kramer import get_all_certs
from pathlib import Path
from Chain import AsyncChain, ModelAsync, Prompt, ChainCache, Parser
from rubric.evaluation import PartnershipEvaluation

ModelAsync._chain_cache = ChainCache()

# Construct our context
background = (
    Path("~/Brian_Code/rubric/LinkedIn Professional Context.md")
    .expanduser()
    .read_text()
)

prompt_str = """
You are evaluating LinkedIn Learning Professional Certificate partnerships for their strategic value and market potential.

<background>
{{background}}
</background>

Your task: Analyze the certificate title and extract the partner name and skill topic, then evaluate using the 3-dimension rubric:

1. **Partner General Recognition** - How well-known is this brand to general professionals?
2. **Partner Domain Authority** - How respected is this partner specifically in this skill area? 
3. **Skill Career Impact** - How much does this skill boost career prospects in North America?

Focus on North American market perspective and individual career development (not enterprise training).

Certificate Title: "{{title}}"

Provide your evaluation as a structured PartnershipEvaluation object.
""".strip()


def evaluate_all_certs():
    certs = get_all_certs()

    # Generate async batch
    titles = [cert.title for cert in certs]
    input_variables_list = [
        {"title": title, "background": background} for title in titles
    ]
    prompt = Prompt(prompt_str)
    parser = Parser(PartnershipEvaluation)
    model = ModelAsync("claude")
    chain = AsyncChain(
        model=model,
        prompt=prompt,
        parser=parser,
    )

    responses = chain.run(input_variables_list=input_variables_list)

    with open("evaluations.jsonl", "w") as f:
        for response in responses:
            f.write(response.model_dump_json() + "\n")
