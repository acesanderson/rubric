from conduit.config import settings
from conduit.sync import Prompt, Conduit, GenerationParams, ConduitOptions, Verbosity
from rubric.evaluation import PartnershipEvaluation
from rubric.partners import prompt_str
from pathlib import Path
import argparse
import sys

background = (
    Path("~/Brian_Code/rubric-project/src/rubric/LinkedIn Professional Context.md")
    .expanduser()
    .read_text()
)


def score_cert(cert_title: str) -> PartnershipEvaluation:
    prompt = Prompt(prompt_str)
    params = GenerationParams(
        model="claude",
        temperature=0.0,
        response_model=PartnershipEvaluation,
        output_type="structured_response",
    )
    options = ConduitOptions(
        project_name="rubric",
        cache=settings.default_cache("rubric"),
        verbosity=Verbosity.PROGRESS,
    )
    conduit = Conduit(
        prompt=prompt,
        params=params,
        options=options,
    )
    response = conduit.run(
        input_variables={"title": cert_title, "background": background}
    )
    return response.last.parsed


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
