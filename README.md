<div align="center">
  <img src="assets/logo.png" alt="Analogical Engines" width="240" />

  <h1>Verification Challenge</h1>

  <p><strong>A practical assignment for engineers who want to build rigorous agentic systems.</strong></p>

  <p>
    <a href="#how-to-apply"><strong>How to apply →</strong></a>
    &nbsp;·&nbsp;
    <a href="mailto:vikram@analogicalengines.com">vikram@analogicalengines.com</a>
  </p>

  <p><sub><strong>Submissions close: 10 May 2026.</strong></sub></p>
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
- The list of questions the dossier must answer — [`deliverables/DOSSIER_QUESTIONS.md`](deliverables/DOSSIER_QUESTIONS.md)
- A deliberately trivial starter in [`starter/`](starter/), purely to demonstrate how a concept file is loaded. **Not a template to extend** — throw it out and build your own.

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

- **Fully automated.** A single command produces a dossier from a concept file. No manual copy-paste, no interactive loops.
- **Live web search.** The system consults the open web — news, company pages, product pages, patent offices — not just the model's training data.
- **Academic / paper search.** The system consults a scientific corpus. Every scientific claim of consequence should cite a real paper. *Which corpus, and how — your call. Part of the challenge is picking the right tools.*
- **LLM-provider agnostic, runtime-configurable.** See [Configuration and provider-agnostic design](#configuration-and-provider-agnostic-design) below.
- **Bring your own keys.** We do not issue API keys. Your system should read all credentials from environment variables, and your submission's `README.md` should list exactly which env vars we need to set. (A `.env.example` is welcome.)
- **Reproducible install.** A clean clone and one setup command should run it on a fresh machine.

### Free to choose

- Any LLM provider(s), any models.
- Any coding assistant — Claude Code, Cursor, Codex, Copilot, Windsurf, or none. We want you to use one; we want you to tell us which.
- Any tools, MCP servers, search APIs, retrievers.
- Any orchestration framework — LangGraph, DSPy, raw SDKs, in-house — or no framework at all.

### Configuration and provider-agnostic design

Your system must let us swap the LLM backend at runtime without code changes. Concretely:

- A single configuration file in the repo root — `config.json` (or `.yaml`, same spirit) — drives which provider / model each part of your system uses.
- Running `<your-entry-point> --config config.alt.json solutions/solution_A.md` (or your equivalent) should work with a different config without any source edits.
- Your submission's `README.md` must include a short **"How to switch providers"** section with a concrete example — at minimum, what to change in `config.json` to run the same pipeline end-to-end on a second provider.
- Your submission's `README.md` must also include a **"How to run"** section with the exact command(s) to reproduce each dossier from a clean clone.

We will run your system against at least two providers at grading time. If it only works with one, that's a score hit.

### A note on cost and effort

You are free to use "deep research" modes if you want. In our own experience they are overkill for this task: expensive, slow, and they tend to return what they would return for any well-known topic. These concepts are not well-known topics. They do not exist as finished ideas anywhere on the internet.

What they *are* is combinations of parts that do exist — a mechanism from one domain, a material from another, a consumer constraint from a third. The skill we're testing is decomposing the concept into those parts, researching the parts with normal web and paper search, and using LLM judgment to assemble the verdict. Going straight to deep-research over the whole concept usually misses this and costs more.

A good submission is typically in the low single-digit dollars per dossier. If yours costs more, that's fine — just make sure the extra cost buys extra rigor, and say so in `DESIGN.md`.

## Deliverables

Commit the following into the private submission repo we invite you to (see [How to apply](#how-to-apply)).

### 1. The code

Your complete agentic system. Prompts in their own files (YAML / Markdown / JSON) — not buried in string literals inside Python.

### 2. Two dossiers

- `output/solution_A.md`
- `output/solution_B.md`

The product of running your system on each concept. Well-formatted Markdown. Every question in [`deliverables/DOSSIER_QUESTIONS.md`](deliverables/DOSSIER_QUESTIONS.md) must be answered. **Structure is entirely your call.** We are grading content, not adherence to a template — how you organize the dossier is itself a signal.

### 3. `DESIGN.md` — your rationale

How does your system work, and why? What did you consider and reject? How did you verify your own outputs are correct? Where do you think the system still has blind spots? This is the document we read most closely.

### 4. `PROCESS.md` — how you built it

- Which coding assistant(s) you used, and how you used them.
- What they got right, what they got wrong, what you had to fix yourself.
- Time spent, end-to-end.
- Challenges you hit and how you got unstuck.

### 5. `output/metrics.json` — the run

Per-dossier run statistics, in the schema below. Honor system; we spot-check.

```json
{
  "solution_A": {
    "wall_clock_seconds": 142.3,
    "llm_calls": 27,
    "web_searches": 14,
    "paper_searches": 8,
    "tokens": {
      "input": 384000,
      "output": 42000,
      "reasoning": 18000
    },
    "cost_usd": 4.37,
    "models_used": ["anthropic/claude-sonnet-4-6", "openai/gpt-4o"]
  },
  "solution_B": {
    "wall_clock_seconds": 156.9,
    "llm_calls": 31,
    "web_searches": 17,
    "paper_searches": 11,
    "tokens": {
      "input": 410000,
      "output": 48000,
      "reasoning": 21000
    },
    "cost_usd": 5.02,
    "models_used": ["anthropic/claude-sonnet-4-6", "openai/gpt-4o"]
  }
}
```

If a field does not apply to your setup (e.g., no reasoning tokens), use `0` or `null` — don't omit it.

### 6. (Optional) Screen recording

A timelapse or walkthrough of you building this — including how you worked with your coding assistant. Loom, YouTube unlisted, or a Drive link pasted into `PROCESS.md`. Optional, but submissions with recordings are weighted higher.

## What we are evaluating you for

We are hiring for **engineering judgment and scientific taste applied to agentic systems**, not for prompt-fluency. Submissions are scored on:

| What we look for | What we mean |
| --- | --- |
| **Decision quality** | Would a domain scientist, reading your dossier cold, agree with your GO / NO-GO recommendation on the evidence you presented? |
| **Evidence rigor** | Are citations real? Do URLs resolve? Do cited papers actually say what the dossier claims they say? |
| **Mechanism reasoning** | Does the dossier engage with physics and chemistry at the level of order-of-magnitude numbers, not vibes? |
| **Prior-art handling** | Does the system surface patents, papers, and products that would block, narrow, or kill the concept? |
| **Failure-mode surfacing** | Does it find the non-obvious failure modes, not just the generic ones? |
| **Dossier structure** | You chose the structure — does it serve the reader? Does it stand up as a coherent document, or read like a question-by-question form? |
| **Architectural taste** | Is the agent graph coherent? Are tools used where they earn their cost? Is cost-per-insight sensible? |
| **Provider-agnostic discipline** | Does the system actually work when we swap the model — or does it quietly break? |
| **Design judgment in `DESIGN.md`** | Does your rationale read like someone who thought, or like someone who followed a recipe? |
| **Process honesty in `PROCESS.md`** | Do we get a faithful account of how you worked, including what your coding assistant got wrong? |

Cheap-and-shallow and expensive-and-padded both lose. We want the tightest, most rigorous system you can build — and a faithful account of how you built it.

## The starter

The files under [`starter/`](starter/) show the simplest possible shape of a one-shot pipeline: read the concept file, read the problem file, format a prompt, make one LLM call. That is all. **It is not a scaffold to build on.** It exists so you can see how the input files are laid out and sanity-check your runtime. Your own system should replace it entirely — different entry point, different structure, different everything.

Do not submit something that looks like a longer version of the starter.

## How to apply

This repo is the public challenge brief. Submissions are not made here — they are made in a private per-candidate repo we invite you to.

1. Email **[vikram@analogicalengines.com](mailto:vikram@analogicalengines.com)** with:
    - Your name
    - Your GitHub username
    - One line on how you heard about the challenge
2. We will invite you to a private submission repo under the Analogical Engines hiring org.
3. Clone that repo, build your submission inside it, and push.
4. Email us when you're done. No tag-and-release ceremony needed — the most recent commit on `main` is what we grade.

Please keep your work and this challenge's details confidential until we tell you the round has closed.

## Deadline

**Submissions close on 10 May 2026.** Earlier is fine and often better — we review in rolling batches.

Spend as little or as much of that window as you like. We measure judgment per hour, not hours. Report your actual time honestly in `PROCESS.md`.

## Questions

If anything in the brief is genuinely ambiguous, email **[vikram@analogicalengines.com](mailto:vikram@analogicalengines.com)**. We would rather clarify than have you guess.

---

<div align="center">
  <sub>© Analogical Engines · <a href="mailto:vikram@analogicalengines.com">vikram@analogicalengines.com</a></sub>
</div>
