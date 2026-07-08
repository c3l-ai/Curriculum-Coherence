# Curriculum Coherence Framework

The Curriculum Coherence Framework evaluates whether an AI-generated instructional response maintains curriculum coherence at the level of a single learner-agent interaction.

The framework is grounded in the idea that coherent curriculum depends on the logical organisation of knowledge: concepts should connect meaningfully, build on appropriate foundations, use disciplinary language accurately, and progress in a structured manner. In computed curriculum systems, where instructional responses are generated dynamically by AI, coherence must be evaluated turn by turn rather than only at the level of a pre-designed course or programme.

## Unit of analysis

The unit of analysis is an interaction-level record consisting of:

1. the prior conversation history;
2. the learner's current turn; and
3. the agent response to evaluate.

The evaluator judges the agent response in relation to the preceding context and learner turn.

## Dimension groups

The framework contains eight binary evaluation dimensions grouped into four categories.

### 1. Coherence Attributes

These dimensions capture direct properties of coherence in the response.

- **Propositional Coherence**: whether the turn builds meaningfully on prior ideas or maintains a coherent line of reasoning.
- **Sequential Coherence**: whether the concept introduced follows a logical curricular or prerequisite order.
- **Referential Coherence**: whether the response uses accurate disciplinary terms, references, analogies, or metaphors.

### 2. Pedagogical Alignment and Anchoring

These dimensions capture how the response connects disciplinary knowledge to instructional action.

- **Disciplinary Anchoring**: whether the response is grounded in a specific, identifiable disciplinary concept.
- **Disciplinary-Pedagogic Alignment**: whether the response reflects both disciplinary logic and pedagogically sound scaffolding.

### 3. Fragmentation Mechanisms

These dimensions capture how the response preserves or restores coherence.

- **Avoidance of Fragmentation**: whether the response avoids abrupt, unrelated, or unbridged topic shifts.
- **Repair of Fragmentation**: whether the response restores coherence after a derailment, confusion, or fragmentary exchange.

### 4. Violation Detection

This dimension captures clear breaks in coherence.

- **Violation Flag**: whether the response introduces disruptive, confusing, contradictory, or epistemically unrelated content.

## Binary scoring

Each dimension is scored as:

- `1` = the dimension is present, satisfied, or detected;
- `0` = the dimension is absent, not satisfied, or not detected.

The only exception in interpretation is **Violation Flag**, where `1` indicates that a violation occurred and `0` indicates no clear violation.

## Why binary scoring?

Binary scoring was chosen to support:

- clearer human annotation;
- simpler comparison between human and LLM labels;
- compatibility with LLM-as-a-Judge workflows;
- aggregation across multiple judges; and
- downstream quality assurance pipelines.

## Recommended evaluation workflow

1. Prepare each case with conversation history, learner turn, and agent turn.
2. Render the combined judge prompt or a single-dimension prompt.
3. Ask the judge model to return the required binary output.
4. Validate the output against the schema.
5. Aggregate model outputs if using multiple LLM judges.
6. Route low-consensus or high-risk cases for human review.
