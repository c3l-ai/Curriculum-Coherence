# Sequential Coherence

## 4. Sequential Coherence

Evaluate whether the agent's turn follows a logical curricular order. Assign 1 if the turn respects prerequisite sequencing (as implied by the conversation and/or knowledge graph) and avoids premature jumps to advanced or unrelated content. Assign 0 otherwise.

Goal: Determine if the turn progresses through concepts in a developmentally and pedagogically sound order (e.g., prerequisites first, then dependents), as if guided by a knowledge graph or structured learning path.

---
Evaluation Criteria

Score 1 when all of the following hold (or are explicitly satisfied by the turn):
- Prerequisite Respect: The concept in the agent turn is not introduced before its prerequisites have been established or the turn explicitly backfills the missing prerequisite(s) before proceeding.
- No Premature Jumps: The turn does not leap to a significantly more advanced or unrelated concept without a justified bridge.
- Order Awareness: Any transition between adjacent topics is signaled and justified (e.g., "Now that we covered variables, we can discuss functions.").
- Context Fit: The turn is appropriate given the learner's most recent state (what the learner just asked/said).

Score 0 if any of the following occurs:
- A required prerequisite is skipped with no remediation in the same turn.
- The turn makes an unjustified jump to advanced or off‑path content.
- The turn contradicts the implied curricular order in the recent context.

---
Binary Scoring Guide
1 — Sequencing is valid: prerequisites are met (or explicitly backfilled), transitions are justified, and the step aligns with the learner’s current state.
0 — Sequencing is invalid: skipped prerequisites, unjustified jumps, or off‑path progression.

Tie‑break rule: If the turn introduces an advanced concept but explicitly and sufficiently backfills the missing prerequisite(s) before proceeding, score 1. If the backfill is absent or superficial, score 0.

---
Special Considerations

- Bridged Redirection: Purposeful redirection is acceptable only if it explicitly references the dependency (e.g., "Before recursion, we need loops—let's cover loops first"), and the turn actually teaches/addresses that prerequisite.
- Staying Put: Restatement or minor elaboration on the current concept (no progression) is still sequentially coherent if it does not violate dependency order.
- Knowledge Graph Aid (if available): Use listed prerequisites to check path validity (e.g., variables → expressions → functions → recursion).

---
Evaluation Process

1. Identify the target concept in the agent turn.
2. From the conversation (and optional KG input), list the prerequisites expected for that concept.
3. Check whether those prerequisites have been covered in prior turns or are explicitly backfilled in the current turn.
4. Check for unjustified jumps or off‑path transitions.
5. Return 1 if sequencing is valid; otherwise 0.

## Input fields

- `conversation_history`: prior dialogue context
- `learner_turn`: current learner message
- `agent_turn`: agent response to evaluate

## Output

Return a single binary value:

- `1` when the criterion is satisfied or detected according to the scoring guide;
- `0` otherwise.

For **Violation Flag**, `1` means a violation is detected and `0` means no clear violation is detected.
