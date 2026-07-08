# Repairs of fragmentation

## 3. Repairs of fragmentation.

Evaluate whether the agent's turn repairs a prior fragmentation in the conversation. Assign 1 if the turn effectively restores coherence (returns to the learner's question/topic, clarifies a confusion, or re‑establishes the intended pedagogic/disciplinary path). Assign 0 otherwise.

Note: If there is no clear fragmentation in the recent context, return 0.

---
Evaluation Criteria

A turn counts as a repair (score 1) when it exhibits one or more of the following, and the content that follows is aligned with the repaired topic/goal:
- Topical Realignment: Explicitly returns to the learner's prior question/topic (e.g., "Back to your question about X...").
- Clarification Move: Resolves a confusion or misstatement introduced earlier (e.g., corrects a misleading analogy or wrong term).
- Bridging Transition: Provides a brief, justified bridge from the detour back to the main thread (e.g., "We mentioned Y, but to answer Z...").
- Pedagogic Reset: Re‑anchors to the instructional objective or step in the sequence (optionally referencing the knowledge graph or prerequisites).
- Disciplinary Re‑anchoring: Re‑states the relevant concept and proceeds with correct disciplinary framing.

A turn does not count as a repair (score 0) if it:
- Merely acknowledges the derailment without fixing it (e.g., "Sorry about that") and does not realign content.
- Introduces new tangents or continues the derailment.
- Provides a generic statement that neither answers the prior question nor restores the intended sequence.


---
Binary Scoring Guide

1 — Effective repair: the turn explicitly or implicitly realigns to the correct topic/sequence and proceeds with aligned content.
0 — No repair: there is no prior fragmentation in context, or the turn fails to realign/clarify and continues the incoherence.

Tie‑break rule: If the turn signals a repair but does not actually deliver aligned content (e.g., apology with no answer), score 0.

---
Special Considerations

- Source of fragmentation (learner or agent) does not matter; judge only whether this turn repairs it.
- If the turn both repairs and transitions to a new topic, it must first close the loop on the pending question or justify the transition pedagogically (e.g., "First, a quick definition of X... Now we can move to Y.").
- Use your knowledge graph (if available) to verify that the repair re‑enters a valid path (e.g., returns from an off‑path node to a prerequisite chain).

---
Evaluation Process

1. Detect fragmentation in the recent context (e.g., off‑topic jump, misleading explanation, skipped prerequisite).
2. Identify the intended thread (learner’s prior question or the last coherent topic/goal).
3. Check whether the agent turn explicitly/implicitly returns to that thread.
4. Verify that the content that follows advances the repaired thread in a discipline‑ and pedagogy‑aligned way.
5. Return 1 if both (3) and (4) hold; otherwise 0.

## Input fields

- `conversation_history`: prior dialogue context
- `learner_turn`: current learner message
- `agent_turn`: agent response to evaluate

## Output

Return a single binary value:

- `1` when the criterion is satisfied or detected according to the scoring guide;
- `0` otherwise.

For **Violation Flag**, `1` means a violation is detected and `0` means no clear violation is detected.
