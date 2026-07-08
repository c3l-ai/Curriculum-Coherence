# Disciplinary anchoring

## 7. Disciplinary anchoring
Evaluate the disciplinary anchoring of the generation. Assign 1 if the agent's turn is clearly grounded in a identifiable disciplinary concept—explicitly defining, explaining, applying, or probing a specific topic within the subject domain. Assign 0 otherwise.

Goal: Determine whether the turn has a clear conceptual focus within the discipline, rather than being purely meta‑pedagogic (e.g., "Let's summarize"), social/chit‑chat, or too vague to be tied to any specific concept.

---
Evaluation Criteria

Assess the turn against the following:
- Identifiable Concept: The turn addresses a specific, nameable disciplinary concept (e.g., "functions," "bias in AI," "data types") through definition, explanation, example, application, or questioning.
- Topical Specificity: The concept is concrete enough to be placed within a knowledge structure—not a vague umbrella reference (e.g., "computers are useful") with no specific anchoring.
- Disciplinary Relevance: The concept belongs to the subject domain being taught, not an unrelated field or general conversational content.
- Instructional Engagement: The turn does substantive work with the concept (teaches, applies, scaffolds, or probes), not merely name‑drops it in passing.

---
Binary Scoring Guide

1 — The turn is anchored to a clear, identifiable disciplinary concept and engages with it substantively (defines, explains, applies, or probes it).
0 — The turn lacks a clear disciplinary concept (e.g., purely meta‑pedagogic, social, motivational, or too vague to anchor to a specific topic), OR the concept referenced is not from the relevant discipline.

Tie‑break rule: If the turn mentions a disciplinary term but does not engage with it beyond a passing reference, score 0.

---
Special Considerations

- Turns that transition between concepts are scored 1 if the destination concept is clearly identified and engaged with (e.g., "Now let's look at loops" followed by substantive content about loops).
- Turns that summarize previously covered concepts are scored 1 if the summary is concept‑specific (e.g., recapping what was learned about variables), but scored 0 if purely procedural (e.g., "Great job, let's move on").
- Code snippets count as anchored if they demonstrably illustrate a specific concept (e.g., a `def` block anchors to functions).
- AI Literacy: Anchor to discipline concepts (e.g., training data, classification, bias), not anthropomorphic notions (e.g., "the AI thinks").
- Multiple concepts: If several concepts appear, score 1 as long as at least one is clearly the primary instructional focus.

---
Evaluation Process

1. Identify whether the agent turn addresses a specific disciplinary concept.
2. Check whether the concept is engaged with substantively (not just name‑dropped).
3. Verify the concept belongs to the relevant subject domain.
4. Return 1 if the turn is anchored to a clear disciplinary concept; else 0.

## Input fields

- `conversation_history`: prior dialogue context
- `learner_turn`: current learner message
- `agent_turn`: agent response to evaluate

## Output

Return a single binary value:

- `1` when the criterion is satisfied or detected according to the scoring guide;
- `0` otherwise.

For **Violation Flag**, `1` means a violation is detected and `0` means no clear violation is detected.
