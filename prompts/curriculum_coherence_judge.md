Evaluate the agent generated text on these 8 metrics:
1. Propositional coherence.
2. Referential coherence.
3. Repairs of fragmentation.
4. Sequential Coherence.
5. Violation flag.
6. Avoidance of fragmentation.
7. Disciplinary anchoring.
8. Disciplinary–pedagogic alignment.

The details of each metric is below: 

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

## 2. Referential coherence

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

# Text to evaluate
Below is the data to evaluate:
---

Context (conversation history):
{{conversation_history}}

Learner Turn:
{{learner_turn}}

Agent Turn to Evaluate:
{{agent_turn}}

# Response format:
Required Output
-Return a 8-digit array of value 1 and or 0 for each metric. This array should be provided at the beginning of response, formated as, for example, [1,0,1,0,1,0,1,0], where: 
1. First is the evaluation result of Propositional coherence.
2. Second is the evaluation result of Referential coherence.
3. Third is the evaluation result of Repairs of fragmentation.
4. Fourth is the evaluation result of Sequential Coherence.
5. Fifth is the evaluation result of Violation flag.
6. Sixth is the evaluation result of  Avoidance of fragmentation.
7. Seventh is the evaluation result of Disciplinary anchoring.
8. Eighth is the evaluation result of Disciplinary–pedagogic alignment.


