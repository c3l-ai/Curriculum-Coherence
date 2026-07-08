# Propositional coherence

## 1. Propositional coherence

Evaluate the propositional coherence of the generation. Assign 1 if the utterance builds meaningfully upon prior ideas or turns in a way that reinforces or advances the learner's understanding—maintaining topical continuity, logical flow, and conceptual progression without contradicting earlier information. Assign 0 otherwise.

---
Evaluation Criteria

Assess the turn against the following:
- Topical Continuity: Stays on topic or transitions smoothly with a clear signal.
- Logical Flow: Builds on or responds to specific points raised in the prior turn(s).
- Conceptual Progression: Advances understanding rather than merely repeating, regressing, or introducing unrelated statements.
- Contextual Relevance: Acknowledges or is appropriate to the learner's current understanding level.
- Contradiction Check: Does not contradict previous statements or established information.

---
Binary Scoring Guide

1 — The turn integrates logically and epistemically with the previous turn(s); topical continuity, logical flow, and conceptual progression are maintained.
0 — The turn introduces unrelated statements, contradicts earlier information, feels disjointed, or fails to build on the prior context in a meaningful way.

Tie‑break rule: If the turn is partially connected but contains a notable logical disconnect or contradiction, score 0.

---
Special Considerations

- A score of 1 can still be given when the agent intentionally redirects the conversation IF:
  - The learner explicitly requests a topic change, OR
  - The agent signals the transition clearly (e.g., "Now that we understand X, let's move to Y"), OR
  - The redirection serves a clear pedagogical purpose and is signalled.
- Minor stylistic issues (e.g., slight repetition for emphasis) do not warrant a 0 if the logical thread is maintained.

---
Evaluation Process

1. Identify the main topic/concept from the conversation history.
2. Note what specific point the learner just raised or responded to.
3. Assess whether the agent's response directly addresses or builds upon that point.
4. Check for any logical disconnects or contradictions.
5. Return 1 if the turn is propositionally coherent; else 0.

## Input fields

- `conversation_history`: prior dialogue context
- `learner_turn`: current learner message
- `agent_turn`: agent response to evaluate

## Output

Return a single binary value:

- `1` when the criterion is satisfied or detected according to the scoring guide;
- `0` otherwise.

For **Violation Flag**, `1` means a violation is detected and `0` means no clear violation is detected.
