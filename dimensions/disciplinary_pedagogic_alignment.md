# Disciplinary–pedagogic alignment

## 8. Disciplinary–pedagogic alignment

Evaluate the disciplinary–pedagogic alignment of the generation. Assign 1 if the response aligns with how the discipline builds knowledge and supports pedagogically sound scaffolding; assign 0 otherwise.

Goal: Determine whether the utterance is both epistemically accurate (disciplinary logic) and instructionally supportive (pedagogic scaffolding) given the learner’s current state.

---
Evaluation Criteria
- Disciplinary Logic: Introduces/uses concepts consistent with disciplinary structure (e.g., foundational → intermediate → advanced).
- Pedagogic Scaffolding: Moves from familiar → unfamiliar, concrete → abstract, simple → complex, or uses appropriate bridging examples- /questions.
- Instructional Awareness: Acknowledges the learner’s prior turn/level and chooses the next step that facilitates understanding (e.g., worked example, probing question).
- Avoids Premature Jumps: Does not skip essential prerequisites or leap to tangential/advanced applications without a bridge.
- Coherent Transitions: If shifting focus, signals and justifies the transition in a way that serves the learning objective.

---
Scoring Guide
1 — Aligned with disciplinary structure and pedagogically scaffolded for the learner’s current context.
0 — Misaligned with disciplinary structure or lacks pedagogic scaffolding (e.g., skips prerequisites, introduces unjustified complexity, or ignores learner context).

---
Special Considerations
- Assign 1 when the agent purposefully redirects with clear instructional intent (e.g., “Now that you’ve grasped X, let’s step up to Y”) and the step is justified by the learner’s state.

---
Evaluation Process
1. Identify the relevant concept(s) in the conversation history.
2. Infer the learner’s current level from the latest learner turn.
3. Check whether the agent turn introduces the next appropriate step (disciplinary order).
4. Check whether the turn scaffolds the step (examples, prompts, transitions).
5. Decide 1 (aligned + scaffolded) or 0 (otherwise).

## Input fields

- `conversation_history`: prior dialogue context
- `learner_turn`: current learner message
- `agent_turn`: agent response to evaluate

## Output

Return a single binary value:

- `1` when the criterion is satisfied or detected according to the scoring guide;
- `0` otherwise.

For **Violation Flag**, `1` means a violation is detected and `0` means no clear violation is detected.
