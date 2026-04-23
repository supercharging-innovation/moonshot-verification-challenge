"""
THIS IS A MINIMAL EXAMPLE, NOT A TEMPLATE.

It shows the simplest possible shape of a one-shot pipeline: read the problem
file, read one concept file, interpolate them into a prompt, make a single LLM
call. That's it. No tools, no web search, no paper search, no agent loop, no
structured output.

Your submission should NOT look like a longer version of this file. Throw it
out and build your own system — different entry point, different structure,
different everything.

This file is kept here only so you can sanity-check that the repo layout and
concept files are what you expect before you start building.
"""

import argparse
import pathlib

import yaml

HERE = pathlib.Path(__file__).parent
REPO = HERE.parent


def load_prompts() -> dict:
    with open(HERE / "prompts.yaml") as f:
        return yaml.safe_load(f)


def build_messages(solution_path: pathlib.Path) -> list[dict]:
    prompts = load_prompts()
    problem_md = (REPO / "problem" / "problem.md").read_text()
    solution_md = solution_path.read_text()
    return [
        {"role": "system", "content": prompts["system"]},
        {
            "role": "user",
            "content": prompts["user"].format(
                problem_markdown=problem_md,
                solution_markdown=solution_md,
            ),
        },
    ]


def call_llm(messages: list[dict]) -> str:
    """
    Intentionally unwired. Your system will pick its own provider(s). This
    placeholder just reports what it received so you can confirm the inputs
    are shaped the way you expect.
    """
    raise NotImplementedError(
        f"Received {len(messages)} messages totaling "
        f"{sum(len(m['content']) for m in messages)} characters. "
        "Wire this to an LLM provider — or, better, throw this file out and "
        "build your own system."
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("solution", type=pathlib.Path, help="Path to a solution_*.md file")
    args = ap.parse_args()
    messages = build_messages(args.solution)
    print(call_llm(messages))


if __name__ == "__main__":
    main()
