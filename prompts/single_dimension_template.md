# Single Dimension Judge Template

You are evaluating one curriculum coherence dimension for an educational AI conversation.

## Dimension

{{dimension_name}}

## Definition

{{dimension_definition}}

## Evaluation criteria

{{evaluation_criteria}}

## Scoring guide

Return `1` if the dimension is present or satisfied according to the definition.
Return `0` otherwise.

For **Violation Flag** only, return `1` when a clear violation occurs and `0` otherwise.

## Text to evaluate

Context (conversation history):
{{conversation_history}}

Learner Turn:
{{learner_turn}}

Agent Turn to Evaluate:
{{agent_turn}}

## Required output

Return only one digit:

```text
0
```

or

```text
1
```
