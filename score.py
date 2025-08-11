from Chain import Prompt, Parser, Model, Chain, Response
from rubric.evaluation import PartnershipEvaluation
from rubric.partners import prompt_str
from pathlib import Path
import argparse

background = (
    Path("~/Brian_Code/rubric/LinkedIn Professional Context.md")
    .expanduser()
    .read_text()
)


def score_cert(cert_title: str) -> PartnershipEvaluation:
    prompt = Prompt(prompt_str)
    parser = Parser(PartnershipEvaluation)
    model = Model("claude")
    chain = Chain(
        model=model,
        prompt=prompt,
        parser=parser,
    )
    response = chain.run(
        input_variables={"title": cert_title, "background": background}
    )
    assert isinstance(response, Response)
    assert isinstance(response.content, PartnershipEvaluation)
    return response.content


def main():
    parser = argparse.ArgumentParser(description="Score a certification title.")
    parser.add_argument(
        "cert_title", type=str, help="The certification title to score."
    )
    args = parser.parse_args()
    evaluation = score_cert(args.cert_title)
    print(evaluation.human_readable_summary)


if __name__ == "__main__":
    main()
