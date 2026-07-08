# Referential coherence

##  Referential coherence

Evaluate the referential coherence of the generation. Assign 1 if the utterance uses accurate, appropriate, and meaningful disciplinary references—including terminology, analogies, or metaphors that reflect accepted ways of talking about the domain—and does not introduce misleading, off‑topic, or distorting references. Assign 0 otherwise.

---
Evaluation Criteria

Assess the turn against the following:
- Terminology Accuracy: Uses correct domain terms (or accepted synonyms) without conflating concepts.
- Analogy/Metaphor Validity: Analogies faithfully map to the intended concept (no misleading implications).
- Concept–Referent Fit: References reinforce the intended concept (not a neighboring or different concept).
- Precision & Disambiguation: Ambiguous language is clarified; polysemous terms are handled carefully.
- Disciplinary Consistency: Aligns with canonical explanations or accepted instructional metaphors.

---
Binary Scoring Guide

1 — References/analogies are accurate, helpful, and discipline‑consistent; no misleading implications.
0 — References are off‑topic, incorrect, anthropomorphizing without bounds, or likely to distort understanding; or no meaningful disciplinary reference is present when one is expected.

Tie‑break rule: If the primary reference is partly apt but risks misconception, score 0.

---
Special Considerations

- Plain‑language bridges are acceptable if the mapping to the canonical concept is explicit.
- Cross‑domain analogies are acceptable when correspondence is stated and limits are acknowledged.
- AI literacy caution: Penalize unbounded anthropomorphism (e.g., "the model thinks/understands") unless explicitly framed as a constrained metaphor.

---
Evaluation Process

1. Identify the target concept from the conversation history.
2. Extract the key referents (terms/analogies/metaphors) in the agent turn.
3. Compare to disciplinary conventions or your controlled vocabulary/knowledge graph.
4. Check for misleading implications or conceptual drift.
5. Return 1 if referents are appropriate and helpful; else 0.

## Input fields

- `conversation_history`: prior dialogue context
- `learner_turn`: current learner message
- `agent_turn`: agent response to evaluate

## Output

Return a single binary value:

- `1` when the criterion is satisfied or detected according to the scoring guide;
- `0` otherwise.

For **Violation Flag**, `1` means a violation is detected and `0` means no clear violation is detected.
