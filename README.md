# Moonshot Verification Challenge

## What we do

We build analogical-innovation pipelines: given a hard client problem, we search across domains for mechanisms that have solved structurally similar problems elsewhere, then transfer them into candidate solutions. A pipeline run produces dozens of solution concepts. The hard part isn't generating them — it's figuring out which ones are real and which ones are sciency-sounding mush.

That is your challenge.

## The task

You are given:

1. A real client problem — [`problem/problem.md`](problem/problem.md)
2. Two early-stage solution concepts, each produced by our internal transfer pipeline — [`solutions/solution_A.md`](solutions/solution_A.md) and [`solutions/solution_B.md`](solutions/solution_B.md)
3. A deliberately weak starter prompt — [`starter/prompts.yaml`](starter/prompts.yaml)

Your job is to build an **agentic verification system** that, for each solution, produces a **scientific dossier** answering two questions with evidence:

- **Is this solution genuinely novel with real breakthrough potential** for this client, or is it a clever-sounding transfer that falls apart under scrutiny?
- **Is the evidence rock solid** — citations real, mechanisms physically defensible, prior art correctly identified, failure modes enumerated?

Both solutions came from the same pipeline. One of them is strong. One of them is weak. A good verification system should be able to tell them apart with evidence — not vibes.

You also have to **build the evaluator** — the thing that scores your own dossier. That is part of the task. See "Build both" below.

## Deliverables

Your submission is a private GitHub repository (we'll invite you to a GitHub Classroom assignment or private org — see "Submission" below) containing:

### 1. The agent system (`/agent/`)

- Full source code of your agentic workflow.
- **Must be LLM-provider-agnostic.** The architecture must not be hard-coded to one provider. Anthropic, OpenAI, Google, and open-weight models should all be swappable via config. We will actually test this — expect us to swap the backend model and re-run.
- Prompts in their own files (YAML, Markdown, or similar) — not buried in Python string literals.
- A single `run.py` (or equivalent) we can execute with a path to a solution file and get a dossier out.
- A `requirements.txt` / `pyproject.toml` / `package.json` that actually installs cleanly.

### 2. The evaluator (`/evaluator/`)

- A separate system that grades dossiers — yours, and others'.
- Takes a dossier + the original problem/solution as input, outputs a structured score and rationale.
- Must be usable independently of your agent (we may run your evaluator against dossiers we generated ourselves).

### 3. Two dossiers (`/output/solution_A/` and `/output/solution_B/`)

- One scientific dossier per solution, produced by your agent.
- Format spec: [`deliverables/TEMPLATE.md`](deliverables/TEMPLATE.md) — follow it, or propose a better one and justify.
- Include the raw evaluator output too.

### 4. A run log (`/output/metrics.json`)

For each of the two runs, record:

- Wall-clock time
- Total input tokens, output tokens, reasoning/thinking tokens
- Total cost in USD (itemized by provider/model)
- Number of LLM calls, tool calls, retries
- Model(s) used

Honor system. We check a sample.

### 5. A README explaining how you built it

In the repo root, write a `SUBMISSION.md` with:

- **Architecture**: how does your system work? Why these agents, these tools, this orchestration? What did you consider and reject?
- **Prompts**: what did you put in them, and why? What did you deliberately leave out?
- **Evaluator design**: how do you score a dossier? What are the dimensions? How did you avoid your agent gaming your own evaluator? Where does your evaluator have known blind spots?
- **Self-critique**: where does your agent fail? What would fool it? What dossier could pass your evaluator but still be wrong?
- **Coding-assistant usage**: which of Claude Code / Cursor / Codex / other did you use, and how? What did you prompt, what did you accept, what did you reject? What did the assistant get wrong that you had to fix?
- **Time spent**: actual hours, end-to-end.

### 6. A screen recording (strongly preferred)

Record yourself building this — even a compressed timelapse. We want to see how you work with coding assistants in practice, not just the polished result. Upload anywhere (Loom, YouTube unlisted, Google Drive) and link from `SUBMISSION.md`.

This is optional but submissions with recordings get weighted higher.

## What we're measuring

| Dimension | What we look for |
|---|---|
| **Verdict accuracy** | Does your system correctly identify which solution is strong and which is weak, with defensible evidence? |
| **Evidence rigor** | Are citations real? Do URLs resolve? Do the cited papers actually say what the dossier claims? |
| **Mechanism reasoning** | Does the dossier engage with physics/chemistry at the level of orders of magnitude, not just vibes? |
| **Prior art handling** | Does the system find relevant patents/papers that would kill or complicate the concept? |
| **Failure mode enumeration** | Does it surface non-obvious failure modes, not just the obvious ones? |
| **Architectural judgment** | Is the agent graph coherent? Are the tools appropriate? Is cost-per-insight reasonable? |
| **Evaluator quality** | Does your evaluator actually discriminate? Is it honest about its own blind spots? |
| **LLM-agnostic design** | Does it actually work when we swap models? Or does it break? |
| **Cost-efficiency** | Tokens/cost per dossier. Cheap-and-shallow and expensive-and-padded both lose. |
| **Judgment in README** | Does `SUBMISSION.md` show someone who thought about the problem, or someone who followed a recipe? |

## Build both (important)

Building the agent *and* the evaluator creates a trap: you can trivially co-optimize them so your agent aces your own evaluator. We expect you to notice this and design against it. Concretely:

- Your evaluator should have **orthogonal signal** from your agent — different prompts, ideally different model families, different decomposition of the problem.
- Your `SUBMISSION.md` must include a **self-critique section** naming specific dossiers that would pass your evaluator but still be wrong.
- At grading time we will run **your agent against a reference evaluator we hold back**, and **your evaluator against reference dossiers we hold back** (some strong, some subtly wrong). If your two halves only work together, both scores drop.

## Rules

- **Use any coding assistant you want.** Claude Code, Cursor, Codex, Copilot, Windsurf, whatever. Tell us which, and how.
- **Use any LLM provider you want at runtime.** But your architecture must allow swapping — config-driven, not hard-coded.
- **Use any tools you want.** Web search, academic search, PDF readers, code interpreters, MCP servers — fair game. Tell us what you chose and why.
- **Starter prompt is intentionally weak.** The vanilla `starter/prompts.yaml` is *not* a baseline to match — it is the floor. Beating it by a hair means nothing.
- **Don't hand-tune prompts to these two specific solutions.** At grading we may run your system on a third solution we hold back. If you overfit, you will see it in the cross-run score.
- **Private work only.** Do not publish your repo or discuss the challenge publicly until we tell you the round is over.

## Submission

You will receive either:

- a GitHub Classroom invite link (each candidate gets their own auto-generated private repo), or
- an invite to a private repo under our `moonshot-hiring` org.

Either way, push your work there. Tag a release `v1.0` when ready. Email us when done.

## Timeline

- You can spend anywhere from a few hours to a few days. We care about judgment per hour, not raw effort. Report the actual time in `SUBMISSION.md`.
- If something is genuinely blocking you, ask us — we'd rather help than watch you waste a weekend on an ambiguity.

---

Good luck. We read every submission carefully.
