<div align="center">
  <img src="assets/logo.png" alt="Analogical Engines" width="240" />

  <h1>Verification Challenge</h1>

  <p><strong>A practical assignment for engineers who want to build rigorous agentic systems.</strong></p>

  <p>
    <a href="#how-to-submit"><strong>How to submit →</strong></a>
    &nbsp;·&nbsp;
    <a href="mailto:moonshot-verification-challenge-01@analogicalengines.com">moonshot-verification-challenge-01@analogicalengines.com</a>
  </p>

  <p><sub><strong>Submissions close 10 May 2026, 11:59pm ET. We reply with a decision within 10 business days.</strong></sub></p>
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
- **Bring your own keys.** We do not issue API keys. Your system must read all credentials from environment variables. Ship a `.env.example` at the root of your submission listing every variable your code reads (names only, no real values), and have your `README.md` explain what each is for.
- **Reproducible install.** A clean clone and one setup command should run it on a fresh machine.
- **Production-grade code.** Write it as if someone — or something — will read and extend it without talking to you. Increasingly that someone is an AI coding agent working only from your code, not a human reading your notes. Clear module boundaries, typed interfaces, explicit error handling, sensible logging, no committed secrets, no dead code. The system should also be **robust** — it keeps going when a search returns garbage, a provider rate-limits, or a paper can't be fetched — and **scalable**, in the sense that if we pointed it at 100 concepts instead of 2, it wouldn't silently fall over. Winning architectures become real production pipelines; yours may be one of them.

### Free to choose

- Any LLM provider(s), any models.
- Any coding assistant — Claude Code, Cursor, Codex, Copilot, Windsurf, or none. We want you to use one; we want you to tell us which.
- Any tools, MCP servers, search APIs, retrievers.
- Any orchestration framework — LangGraph, DSPy, raw SDKs, in-house — or no framework at all.

### Configuration and provider-agnostic design

Your system must let us swap the LLM backend at runtime without code changes. Concretely:

- A `config.json` at the root of your submission drives which provider and model each part of your system uses. Its shape is your design decision — we care that it exists, that it covers every model call in your pipeline, and that your `README.md` documents it.
- Running your entry point with a different config file (for example, `--config config.alt.json`) should work without any source edits.
- Your submission's `README.md` must include a **"How to switch providers"** section with a concrete example — at minimum, what to change in `config.json` to run the same pipeline end-to-end on a second provider.
- Your submission's `README.md` must also include a **"How to run"** section with the exact command(s) to reproduce each dossier from a clean install.

We will run your system against at least two providers at grading time. If it only works with one, that's a score hit.

### A note on cost and effort

You are free to use "deep research" modes if you want. In our own experience they are overkill for this task: expensive, slow, and they tend to return what they would return for any well-known topic. These concepts are not well-known topics. They do not exist as finished ideas anywhere on the internet.

What they *are* is combinations of parts that do exist — a mechanism from one domain, a material from another, a consumer constraint from a third. The skill we're testing is decomposing the concept into those parts, researching the parts with normal web and paper search, and using LLM judgment to assemble the verdict. Going straight to deep-research over the whole concept usually misses this and costs more.

A good submission is typically in the low single-digit dollars per dossier. If yours costs more, that's fine — just make sure the extra cost buys extra rigor, and say so in `DESIGN.md`.

## Deliverables

You submit by emailing us a zip (see [How to submit](#how-to-submit)). Everything below should be inside that zip — a single self-contained directory we can unzip, read, and run from.

### 1. The code

Your complete agentic system. Prompts in their own files (YAML / Markdown / JSON) — not buried in string literals inside Python.

### 2. `README.md` — how to set up and run your submission

A README at the root of your submission, written for a reviewer who has never seen your code before and is going to run it from a fresh install. At a minimum:

- Install steps for a clean machine (`pip install -r requirements.txt`, `uv sync`, `npm ci`, whatever).
- The exact command(s) to produce each dossier end-to-end.
- Which environment variables the code reads (pointing at your `.env.example`), and what each is for.
- A **"How to switch providers"** section with a concrete, copy-pasteable example — what to change in `config.json` to run the same pipeline end-to-end on a second provider.

Assume the reviewer is competent but not psychic.

### 3. `config.json` — the runtime configuration

A single JSON file at the root of your submission that drives which provider and model each part of your system uses. Shape is your design decision, but every model call in your pipeline should be reachable from this file, and the file should be swappable at runtime without code changes.

### 4. `.env.example` — the secrets contract

A file at the root listing every environment variable your code reads, with names only and no real values. One line per variable, with a short comment explaining what it is and where to get it.

### 5. Two dossiers

- `output/solution_A.md`
- `output/solution_B.md`

The product of running your system on each concept. Well-formatted Markdown. Every question in [`deliverables/DOSSIER_QUESTIONS.md`](deliverables/DOSSIER_QUESTIONS.md) must be answered. **Structure is entirely your call.** We are grading content, not adherence to a template — how you organize the dossier is itself a signal.

### 6. `DESIGN.md` — your rationale

How does your system work, and why? What did you consider and reject? How did you verify your own outputs are correct? Where do you think the system still has blind spots? This is the document we read most closely.

### 7. `PROCESS.md` — how you built it

- Which coding assistant(s) you used, and how you used them.
- What they got right, what they got wrong, what you had to fix yourself.
- Time spent, end-to-end.
- Challenges you hit and how you got unstuck.

### 8. `output/metrics.json` — the run

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

### 9. (Optional) Screen recording

A timelapse or walkthrough of you building this — including how you worked with your coding assistant. Loom, YouTube unlisted, or a Drive link. Paste the link at the top of `PROCESS.md`. Optional, but submissions with recordings are weighted higher.

## What we are evaluating you for

When we hand an engineer a hard, open-ended problem at Analogical Engines, three meta-skills decide whether they succeed:

1. **Architectural judgment under ambiguity.** When nobody has told you how the pipeline should decompose — agents, tools, checkpoints, retries, structured outputs — can you choose a shape that fits the problem instead of defaulting to a framework's happy path?
2. **Fluency with modern coding assistants.** Claude Code, Cursor, Codex and their peers are not toys. An engineer who uses them well ships a week of work in a day. An engineer who uses them badly ships plausible-looking code that collapses on second contact. We want to see how you actually work with them — what you delegate, what you review line-by-line, what you throw out.
3. **A point of view on designing LLM-based systems.** Where do you spend tokens and where do you refuse to? How do you test a probabilistic system? How do you know your agent isn't hallucinating past a silent failure? How do you keep costs sane?

Everything below rolls up to those three. Submissions are scored on:

| What we look for | What we mean |
| --- | --- |
| **Architecture under ambiguity** | Is the agent graph chosen for this problem, not borrowed from a tutorial? Do the pieces do work only an agent can do, and nothing else? |
| **Decision quality** | Would a domain scientist, reading your dossier cold, agree with your GO / NO-GO recommendation on the evidence you presented? |
| **Evidence rigor** | Are citations real? Do URLs resolve? Do cited papers actually say what the dossier claims they say? |
| **Mechanism reasoning** | Does the dossier engage with physics and chemistry at the level of order-of-magnitude numbers, not vibes? |
| **Prior-art handling** | Does the system surface patents, papers, and products that would block, narrow, or kill the concept? |
| **Failure-mode surfacing** | Does it find the non-obvious failure modes, not just the generic ones? |
| **Dossier structure** | You chose the structure — does it serve the reader? Does it stand up as a coherent document, or read like a question-by-question form? |
| **Code quality** | Is this production-grade? Would we be comfortable merging it into a real pipeline? |
| **Provider-agnostic discipline** | Does the system actually work when we swap the model — or does it quietly break? |
| **Coding-assistant fluency (`PROCESS.md`)** | Do we get a specific, honest account of what your assistant got right, what it got wrong, what bugs came out of that, and how you worked past them? |
| **LLM-systems judgment (`DESIGN.md`)** | Does your rationale read like someone with a point of view on building these systems, or like someone who followed a recipe? |

Cheap-and-shallow and expensive-and-padded both lose. We want the tightest, most rigorous system you can build — and a faithful account of how you built it.

## The starter

The files under [`starter/`](starter/) show the simplest possible shape of a one-shot pipeline: read the concept file, read the problem file, format a prompt, make one LLM call. That is all. **It is not a scaffold to build on.** It exists so you can see how the input files are laid out and sanity-check your runtime. Your own system should replace it entirely — different entry point, different structure, different everything.

Do not submit something that looks like a longer version of the starter.

## Why take this challenge

You would be working on one of the harder problems in applied AI right now: getting LLM-based systems to tell the truth about the world under adversarial conditions — adversarial in the sense that the concepts *look* plausible, the citations *look* real, and the physics *looks* right, even when it isn't. The concepts in this challenge are not toy problems. They come straight out of the pipeline we ship to real R&D clients working on real product launches. A good verification dossier is not an academic exercise; it is the thing that determines whether a Fortune-500 client commits months of lab time and millions of dollars.

If you join us, you build the next version of this. You work directly on the system you were evaluated on, ship to real clients, see your work cited in actual stage-gate meetings, and have more leverage on the product than you would anywhere else. We are a small team; you would be one of a handful of engineers who decide what this platform becomes.

If you don't join us — because the fit isn't right, or because you take something else — you still walk away with a rigorous agentic system in your portfolio, a screen recording of you using modern coding assistants at their best, and a concrete point of view on how LLM-based systems should be designed. That's worth the weekend by itself.

## How to submit

This repo is the public challenge brief — read it, build against it, submit when ready.

1. Zip your submission directory. It should contain, at minimum: your source code, `README.md`, `config.json`, `.env.example`, `DESIGN.md`, `PROCESS.md`, and an `output/` folder holding `solution_A.md`, `solution_B.md`, and `metrics.json`. See [Deliverables](#deliverables) for details.
2. Email the zip to **[moonshot-verification-challenge-01@analogicalengines.com](mailto:moonshot-verification-challenge-01@analogicalengines.com)** with the subject line **`Verification Challenge Submission — <Your Name>`**. Include in the body:
    - Your name and, if you'd like, your GitHub profile
    - One or two lines about yourself — what you're working on, where you heard about the challenge
3. **If the zip is over 25 MB**, don't attach it — link to it from the email instead. A Drive / Dropbox / WeTransfer link or a private GitHub repo you've shared with us all work. The email itself is still required; we only track submissions that arrive in our inbox. No model weights, no `.venv`, no `node_modules`, no real secrets.
4. **Make sure we can run it.** The most common self-own is a submission we can't reproduce. Before zipping, unzip your own file into a fresh directory, follow your own README, and confirm it runs end-to-end.
5. **Resubmissions are fine** as long as they arrive before the deadline. Reply on the same email thread with the new zip or link so we grade the latest version.
6. We will reply with a decision within **10 business days** of receiving your email. No separate acknowledgement — the decision email is the reply.

Please keep your work and this challenge's details confidential until we tell you the round has closed.

## Deadline

**Submissions close 10 May 2026 at 11:59pm ET.** Earlier is fine and often better — we review in rolling batches.

Spend as little or as much of that window as you like. We measure judgment per hour, not hours. Report your actual time honestly in `PROCESS.md`.

## Questions

If anything in the brief is genuinely ambiguous, email **[moonshot-verification-challenge-01@analogicalengines.com](mailto:moonshot-verification-challenge-01@analogicalengines.com)**. We would rather clarify than have you guess.

---

<div align="center">
  <sub>© Analogical Engines · <a href="mailto:moonshot-verification-challenge-01@analogicalengines.com">moonshot-verification-challenge-01@analogicalengines.com</a></sub>
</div>
