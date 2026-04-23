# Dossier Template

This is a suggested format for the per-solution scientific dossier. You can extend, reorganize, or propose a different structure — just explain why in your `SUBMISSION.md`. What we care about is that the dossier answers the questions below with real evidence.

Every non-trivial factual claim must be linked to a source. Every URL must resolve when we click it. Citing a paper that does not say what you claim it says is worse than not citing at all.

---

# Dossier: [Solution Name]

## 1. Verdict

One of: **PASS** / **CONDITIONAL PASS** / **FAIL** / **NEEDS MORE EVIDENCE**.

Followed by a 2–3 sentence explanation. If `CONDITIONAL PASS`, list the specific conditions (evidence, experiments, reformulations) that would move it to PASS.

## 2. Executive summary

3–5 sentences. What is the concept, is it real, and what's the single most important reason for the verdict?

## 3. Mechanism analysis

Engage with the physics / chemistry / biology at the level of order-of-magnitude numbers. Generic descriptions don't count.

- **Primary mechanism:** what physically happens, and why it would or would not produce the claimed effect.
- **Quantitative check:** the key number that makes or breaks the concept (shear stress, binding constant, diffusion timescale, field strength, etc.) — compute it, or cite a measured value from literature, and compare to the required threshold.
- **Secondary mechanisms:** if the concept invokes multiple physical phenomena, is each of them independently defensible and are they coherently combined?

## 4. Novelty assessment

- **Prior art found** (patents, papers, products): list each with title, source, link, and a one-sentence summary of what it covers.
- **Overlap analysis:** which of these would block, narrow, or force a redesign of the concept?
- **Net novelty claim:** what, if anything, is actually new here, distinct from prior art?

## 5. Evidence audit

- **Source credibility:** are the cited papers peer-reviewed? Are the journals real? Are the author affiliations real?
- **URL validity:** every URL in the dossier resolves. Note any that required a paywall or institutional access.
- **Claim-to-citation traceability:** every quantitative or non-trivial claim maps back to a specific source. Flag any claim you could not verify.

## 6. Failure-mode enumeration

At least 5 specific ways this concept could fail. Be specific — "regulatory issues" is not a failure mode, "the Ca²⁺ chelator loading required to generate a structurally relevant leach rate exceeds the oral exposure limit by ~3×" is.

## 7. Competitive / landscape positioning

Against the incumbent and at least 2 competing approaches (floss, Listerine-class rinses, Waterpik-class irrigators, etc.): where does this win, where does it lose, and for which customer segment?

## 8. Recommended next steps

If the verdict is PASS or CONDITIONAL: what is the smallest experiment that would kill the concept early if it is going to die? What is the first 6-month de-risking plan?

If the verdict is FAIL: what would have to be true for the concept to be salvageable, and is there any adjacent concept worth keeping?

## 9. Metadata

- Model(s) used, by agent/step
- Tool calls made (web search, academic search, patent search, etc.)
- Wall-clock time
- Total tokens (input / output / reasoning)
- Total cost (USD)
