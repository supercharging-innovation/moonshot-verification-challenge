<div align="center">
  <img src="assets/logo.png" alt="Analogical Engines" width="240" />

  <h1>Verification Challenge</h1>

  <p><strong>A practical assignment for engineers who want to build rigorous agentic systems.</strong></p>
</div>

---

## About Analogical Engines

We help R&D organizations find non-obvious solutions to hard problems. Our platform searches across scientific and industrial domains for mechanisms that have solved *structurally similar* problems elsewhere, then transfers them into the client's context as candidate concepts. A single pipeline run can produce dozens of them.

Generating candidates is the easy half. The hard half is deciding which ones are real.

This challenge is about the hard half.

## The task

Every new concept in our pipeline has to clear an **initial stage gate**: a structured decision on whether the concept is worth committing R&D budget and resources to, or whether it should be dropped before it consumes either. That decision is made by a small group of domain scientists and engineers. They will not fund a concept on the strength of a pitch; they want a dossier they can interrogate.

Your task is to build an agentic system that produces that dossier — automatically, from a raw concept, with evidence — so the reviewers can make the stage-gate call in one sitting.

You are given:

- A real client problem — [`problem/problem.md`](problem/problem.md)
- Two early-stage concepts produced by our internal transfer pipeline — [`solutions/solution_A.md`](solutions/solution_A.md) and [`solutions/solution_B.md`](solutions/solution_B.md)
- A list of the questions the dossier must answer — [`deliverables/DOSSIER_QUESTIONS.md`](deliverables/DOSSIER_QUESTIONS.md)
- A deliberately trivial starter in [`starter/`](starter/), purely to demonstrate how a concept file is read in. It is **not a template to extend** — throw it out and build your own system.

For each concept, your system should output a well-formatted Markdown dossier that a scientist can read end-to-end and walk away from with a defensible answer to: **do we fund R&D on this, yes, no, or yes with conditions?**

## What the dossier is for

The dossier is the artifact that drives the stage-gate meeting. A reviewer should be able to read one of your dossiers and know:

1. Whether the concept is **genuinely novel** — or already done, patented, or shipping.
2. Whether it would be **impactful** — who benefits, by how much, in units the client cares about.
3. Whether it has **real breakthrough potential** — the physics, chemistry, or biology hold up under scrutiny, not just in prose.
4. Whether it can be **brought to life** under the stated problem constraints and a realistic R&D budget.
5. What the **recommendation** is, and what the single cheapest experiment would be that kills the concept if it is going to die.

Every non-trivial claim in the dossier must trace back to a real source — a paper, a patent, a product, a dataset. A reviewer who clicks through your citations should find them, and find that they say what you claim they say.

## Technical requirements

### Must-haves

- **Fully automated.** A single command (e.g., `python run.py solution_A.md`) produces the dossier. No manual copy-paste, no interactive loops.
- **Live web search.** The system consults the open web (news, company pages, product pages, patent offices) — not just the model's training data.
- **Academic/paper search.** The system consults a scientific corpus (Semantic Scholar, OpenAlex, PubMed, arXiv, Google Scholar, or similar). Every scientific claim of consequence should cite a real paper.
- **LLM-provider agnostic.** Your architecture must not be hard-wired to one vendor. Anthropic, OpenAI, Google, open-weight — swappable via config. Expect us to change the backend model and re-run.
- **Reproducible install.** A clean clone and one setup command should run it. `requirements.txt` / `pyproject.toml` / `package.json` — whatever ecosystem, just make it work on a fresh machine.

### Free to choose

- Any LLM provider(s), any models.
- Any coding assistant — Claude Code, Cursor, Codex, Copilot, Windsurf, or none. We want you to use one; we want you to tell us which.
- Any tools, MCP servers, search APIs, custom retrievers.
- Any orchestration framework — LangGraph, DSPy, raw SDKs, in-house — or no framework at all.

## Deliverables

Commit the following into the private repo we invite you to.

### 1. The code

Your complete agentic system. Prompts in their own files (YAML / Markdown / JSON) — not buried in string literals in Python.

### 2. Two dossiers

- `output/solution_A.md`
- `output/solution_B.md`

These are the product of running your system on each concept. Well-formatted Markdown. Every question in [`deliverables/DOSSIER_QUESTIONS.md`](deliverables/DOSSIER_QUESTIONS.md) must be answered. Structure is your call.

### 3. `DESIGN.md` — your rationale

How does your system work, and why? What did you consider and reject? How did you verify your own outputs are correct? Where do you think the system still has blind spots? This is the document we read most closely.

### 4. `PROCESS.md` — how you built it

- Which coding assistant(s) you used, and how you used them.
- What they got right, what they got wrong, what you had to fix yourself.
- Time spent, end-to-end.
- Challenges you hit and how you got unstuck.

### 5. `output/metrics.json` — the run

For each of the two dossier runs, record: wall-clock time, input / output / reasoning tokens, total cost (USD), number of LLM calls, number of web and paper searches, and the models used. Honor system; we spot-check.

### 6. (Optional) Screen recording

A timelapse or walkthrough of you building this — including how you worked with your coding assistant. Loom, YouTube unlisted, or a Drive link in `PROCESS.md`. Optional, but submissions with recordings are weighted higher.

## What we are evaluating you for

We are hiring for **engineering judgment and scientific taste applied to agentic systems**, not for prompt-fluency. Specifically, submissions are scored on:

| What we look for | What we mean |
| --- | --- |
| **Decision quality** | Would a domain scientist, reading your dossier cold, agree with your GO / NO-GO recommendation on the evidence you presented? |
| **Evidence rigor** | Are citations real? Do URLs resolve? Do cited papers actually say what the dossier claims they say? |
| **Mechanism reasoning** | Does the dossier engage with physics and chemistry at the level of order-of-magnitude numbers, not vibes? |
| **Prior-art handling** | Does the system surface patents, papers, and products that would block, narrow, or kill the concept? |
| **Failure-mode surfacing** | Does it find the non-obvious failure modes, not just the generic ones? |
| **Architectural taste** | Is the agent graph coherent? Are the tools appropriate? Is cost-per-insight sensible? |
| **Provider-agnostic discipline** | Does the system actually work when we swap the model — or does it quietly break? |
| **Design judgment in `DESIGN.md`** | Does your rationale read like someone who *thought*, or like someone who followed a recipe? |
| **Process discipline in `PROCESS.md`** | Do we get an honest account of how you worked with your coding assistant — including what it got wrong? |

Cheap-and-shallow and expensive-and-padded both lose. We want the tightest, most rigorous system you can build — and a faithful account of how you built it.

## The starter

The files under [`starter/`](starter/) show the simplest possible shape of a one-shot pipeline: read the concept file, read the problem file, format a prompt, make one LLM call. That is all. **It is not a scaffold to build on.** It exists purely so you can see how the input files are laid out and confirm your runtime is wired up. Your own system should replace it entirely — different entry point, different structure, different everything.

Do not submit something that looks like a longer version of the starter.

## Submission

1. Email **[vikram@analogicalengines.com](mailto:vikram@analogicalengines.com)** to register. Include your name, your GitHub username, and one line on how you heard about the challenge.
2. We will invite you to a private repo under the Analogical Engines hiring org.
3. Push your work there. Tag a release `v1.0` and email us when you're ready for review.

Please keep the challenge and your work confidential until we tell you the round is closed.

## Timeline

Spend as little or as much time as you like — we measure judgment per hour, not hours. Report your actual time honestly in `PROCESS.md`.

## Questions

If any part of the brief is genuinely ambiguous, email **[vikram@analogicalengines.com](mailto:vikram@analogicalengines.com)**. We would rather clarify than have you guess.

---

<div align="center">
  <sub>© Analogical Engines · <a href="mailto:vikram@analogicalengines.com">vikram@analogicalengines.com</a></sub>
</div>
