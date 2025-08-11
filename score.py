from Chain import Prompt, Parser, Model, Chain, Response
from evaluation import PartnershipEvaluation
from pathlib import Path
from partners import prompt_str
import argparse

background = Path("LinkedIn Professional Context.md").read_text()


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
