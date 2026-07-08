# Violation flag

## 5. Violation flag

Does the agent's turn introduce disruptive, confusing, or epistemically unrelated content that breaks the curricular or pedagogic flow? Assign 1 if a clear violation occurs; assign 0 otherwise.

Use this flag sparingly. Prefer 0 unless the violation is unambiguous.

---
Evaluation Criteria (score 1 if any apply)

- Contradiction of Prior Knowledge: States something that conflicts with earlier turns or established disciplinary principles.
- Epistemically Unrelated / Off‑Topic: Introduces content with no meaningful link to the ongoing learning thread.
- Misleading or Distorting Reference: Uses an analogy/claim that distorts the concept in a way likely to cause misconception (beyond minor imprecision).
- Flow Disruption: Abrupt, unsignalled jump that derails the learning goal (not merely a minor digression).
- Confusion Induction: The turn obfuscates or disorients (e.g., incoherent, self‑contradictory, or nonsensical).

Do NOT flag (score 0) when:

- The turn bridges to a new concept with a clear instructional rationale ("Before recursion, we need loops—let's cover loops first").
- The turn performs a repair (RF) or backfill of a prerequisite.
- The turn uses a plain‑language approximation with explicit limits (e.g., "roughly like... but not exactly").
- The move is meta‑pedagogic and supportive (e.g., "Let's summarize what we learned").

---
Binary Scoring Guide

1 — Clear violation (contradiction, off‑topic, distorting, or derailing).
0 — No clear violation; content is aligned or at least plausibly connected.

Tie‑break rule: If uncertain, score 0.

---
Examples

Example 1 — Distorting Analogy
Turn: "Functions are like unicorns—they magically appear in your code."
Score: 1
Reasoning: Misleading, fantastical analogy that distorts understanding.

Example 2 — Accurate, On‑Topic
Turn: "You can define a function in Python with def."
Score: 0
Reasoning: Accurate, aligned.

Example 3 — Off‑Topic
Turn: "I had eggs for breakfast."
Score: 1
Reasoning: Unrelated to the learning task.

Example 4 — Bridged Transition (Do not flag)
Turn: "Before we discuss recursion, let's review loops since recursion builds on control flow."
Score: 0
Reasoning: Purposeful, signalled bridge; supports pedagogy.

---
Evaluation Process

1. Identify the current learning thread from context.
2. Check for contradictions, off‑topic jumps, or distorting claims in the agent turn.
3. Determine if the move is purposefully bridged or repairs/backfills a prerequisite (if yes, score 0).
4. Return 1 only for clear violations; otherwise 0.

## Input fields

- `conversation_history`: prior dialogue context
- `learner_turn`: current learner message
- `agent_turn`: agent response to evaluate

## Output

Return a single binary value:

- `1` when the criterion is satisfied or detected according to the scoring guide;
- `0` otherwise.

For **Violation Flag**, `1` means a violation is detected and `0` means no clear violation is detected.
