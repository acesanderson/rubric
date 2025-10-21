from conduit.sync import Prompt, Model, Conduit, Response, ConduitCache
from conduit.parser.parser import Parser
from rubric.evaluation import PartnershipEvaluation
from rubric.partners import prompt_str
from pathlib import Path
import argparse
import sys

conduit_cache = ConduitCache()
Model.conduit_cache = conduit_cache

conduit_cache = ConduitCache()
Model.conduit_cache = conduit_cache

background = (
    Path("~/Brian_Code/rubric-project/src/rubric/LinkedIn Professional Context.md")
    .expanduser()
    .read_text()
)


def score_cert(cert_title: str) -> PartnershipEvaluation:
    prompt = Prompt(prompt_str)
    parser = Parser(PartnershipEvaluation)
    model = Model("claude")
    conduit = Conduit(
        model=model,
        prompt=prompt,
        parser=parser,
    )
    response = conduit.run(
        input_variables={"title": cert_title, "background": background}
    )
    assert isinstance(response, Response)
    assert isinstance(response.content, PartnershipEvaluation)
    return response.content


def main():
    parser = argparse.ArgumentParser(description="Score a certification title.")
    parser.add_argument(
        "cert_title", type=str, nargs="?", help="The certification title to score."
    )
    parser.add_argument(
        "-r",
        "--rubric",
        action="store_true",
        help="Display the scoring rubric.",
    )
    args = parser.parse_args()
    if args.rubric:
        print(PartnershipEvaluation.rubric)
        sys.exit()
    else:
        evaluation = score_cert(args.cert_title)
        print(evaluation.human_readable_summary)


if __name__ == "__main__":
    main()
