"""
Vanilla one-shot runner — the floor, not the target.

Reads the problem markdown and a solution markdown, interpolates them into the
weak starter prompt, makes one LLM call, and dumps the raw response. No tools,
no evidence checking, no evaluator, no structured output.

A good submission replaces this entire file with a real agentic system.
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
    Placeholder. Wire this to whatever LLM you want — Anthropic, OpenAI,
    Google, local. This is the only part of the starter you *must* replace.
    """
    raise NotImplementedError(
        f"Wire this to an LLM provider. Received {len(messages)} messages "
        f"totaling {sum(len(m['content']) for m in messages)} characters. "
        "The starter is intentionally not hard-coded to any vendor — your "
        "submission should support multiple."
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("solution", type=pathlib.Path, help="Path to a solution_*.md file")
    args = ap.parse_args()
    messages = build_messages(args.solution)
    print(call_llm(messages))


if __name__ == "__main__":
    main()
