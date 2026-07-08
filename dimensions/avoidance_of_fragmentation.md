# Avoidance of fragmentation

## 6. Avoidance of fragmentation

Evaluate the avoidance of fragmentation in the generation. Assign 1 if the utterance maintains thematic and topical continuity—fitting naturally within the ongoing conversation or learning sequence without abrupt, unrelated shifts. Assign 0 otherwise.

Goal: Determine whether the turn preserves the flow of the conversation or introduces disruptive, unbridged topic shifts that may confuse or derail learning.

---
Evaluation Criteria

Assess the turn against the following:
- Thematic Continuity: The turn stays within the current topic or transitions smoothly with a clear signal.
- Topical Fit: The content relates directly to what was just discussed or what the learner just asked/said.
- Absence of Abrupt Shifts: No sudden introduction of unrelated concepts without a bridge or justification.
- Conversational Flow: The turn feels like a natural next step in the dialogue, not a non sequitur.

---
Binary Scoring Guide

1 — The turn maintains topical cohesion; any transition is signalled, bridged, or pedagogically justified.
0 — The turn introduces an abrupt, unrelated shift in subject matter that disrupts the conversational or learning flow.

Tie‑break rule: If the turn partially relates to the prior context but introduces a significant unbridged tangent, score 0.

---
Special Considerations

- Bridged transitions are not fragmentation: if the agent signals the shift and connects it to the learning thread (e.g., "Now that we've covered X, let's look at Y"), score 1.
- Learner-initiated topic changes followed by the agent are not fragmentation if the agent acknowledges the shift.
- Minor elaborations or asides that return to the main thread within the same turn are acceptable (score 1).

---
Examples

Example 1 — Cohesive
Context:
  Turn 1 (Agent): A function is a named group of instructions.
  Turn 2 (Learner): Can I use it more than once?
Turn to Evaluate:
  Yes, you can reuse functions to avoid duplicating code. Let's look at how to write one in Python.
Score: 1
Reasoning: Continues the topic of functions and adds relevant procedural information.

Example 2 — Fragmented
Context:
  Turn 1 (Agent): A function is a named group of instructions.
  Turn 2 (Learner): Can I use it more than once?
Turn to Evaluate:
  Variables are also important in programming, especially for storing values.
Score: 0
Reasoning: Abrupt shift to variables without a bridge, interrupting the flow.

---
Evaluation Process

1. Identify the current topic/thread from the conversation history.
2. Determine what the learner just raised or responded to.
3. Check whether the agent turn continues, extends, or smoothly transitions from that thread.
4. Check for abrupt, unbridged topic shifts.
5. Return 1 if topically cohesive; else 0.

## Input fields

- `conversation_history`: prior dialogue context
- `learner_turn`: current learner message
- `agent_turn`: agent response to evaluate

## Output

Return a single binary value:

- `1` when the criterion is satisfied or detected according to the scoring guide;
- `0` otherwise.

For **Violation Flag**, `1` means a violation is detected and `0` means no clear violation is detected.
