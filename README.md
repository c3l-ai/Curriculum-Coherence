# Curriculum Coherence Evals

An open-source implementation of the **Curriculum Coherence Framework** for evaluating educational AI conversations using the **LLM-as-a-Judge** paradigm.

This repository operationalises eight interaction-level curriculum coherence dimensions informed by curriculum coherence theory, computed curriculum research, and LLM-based evaluation. It provides reusable evaluation prompts, dimension-level coding guidelines, JSON schemas, illustrative examples, and lightweight utilities for evaluating AI-generated educational conversations.

---

## Curriculum Coherence Framework

<p align="center">
  <img src="assets/coherence_framework.jpg" alt="Curriculum Coherence Framework" width="850"/>
</p>

The Curriculum Coherence Framework conceptualises curriculum coherence across four complementary components:

- **Coherence** captures whether an instructional interaction is conceptually connected through **Propositional**, **Sequential**, and **Referential Coherence**.
- **Pedagogical Manoeuvres** shape coherence through **Disciplinary Anchoring (DA)** and **Disciplinary-Pedagogic Alignment (DPA)**.
- **Fragmentation & Repair** evaluates whether instructional breakdowns are avoided or successfully repaired through **Fragmentation Avoidance (AF)** and **Fragmentation Repair (RF)**.
- **Violation Flag (VF)** identifies interactions that contain disruptive, contradictory, or epistemically unrelated content.

---

## What this repository evaluates

Most chatbot evaluation suites focus on broad properties such as factuality, helpfulness, safety, or toxicity.

**Curriculum Coherence Evals** instead evaluates whether an educational AI response is coherent from a curriculum perspective.

Specifically, it evaluates whether an AI response:

- builds logically on prior instructional turns;
- maintains appropriate disciplinary references;
- follows a sensible curricular sequence;
- avoids unnecessary fragmentation;
- repairs coherence after conversational breakdowns;
- remains anchored in disciplinary concepts;
- aligns pedagogical scaffolding with disciplinary knowledge; and
- avoids disruptive or epistemically unrelated content.

---

## Repository structure

```text
curriculum-coherence-evals/
│
├── README.md
├── LICENSE
├── CITATION.cff
├── references.bib
├── assets/
│   └── coherence_framework.jpg
│
├── framework/
│   ├── curriculum_coherence_framework.md
│   ├── coherence_dimensions.md
│   └── references.md
│
├── dimensions/
│   ├── propositional_coherence.md
│   ├── referential_coherence.md
│   ├── sequential_coherence.md
│   ├── disciplinary_anchoring.md
│   ├── disciplinary_pedagogic_alignment.md
│   ├── avoidance_of_fragmentation.md
│   ├── repair_of_fragmentation.md
│   └── violation_flag.md
│
├── prompts/
│   ├── curriculum_coherence_judge.md
│   └── single_dimension_template.md
│
├── schemas/
│   ├── evaluation_case.schema.json
│   └── judge_output.schema.json
│
├── examples/
│   ├── sample_cases.jsonl
│   └── sample_outputs.jsonl
│
└── utils/
    ├── render_prompt.py
    └── parse_output.py
```

---

## Input format

Each evaluation case contains three fields:

```json
{
  "conversation_history": "Agent: ...\nLearner: ...",
  "learner_turn": "The learner's current message.",
  "agent_turn": "The AI tutor response to evaluate."
}
```

---

## Output format

The combined evaluation prompt returns an eight-element binary vector:

```json
[1,1,0,1,0,1,1,1]
```

The output dimensions are ordered as follows:

| Position | Dimension |
|----------:|-----------|
| 1 | Propositional Coherence |
| 2 | Referential Coherence |
| 3 | Repair of Fragmentation |
| 4 | Sequential Coherence |
| 5 | Violation Flag |
| 6 | Avoidance of Fragmentation |
| 7 | Disciplinary Anchoring |
| 8 | Disciplinary-Pedagogic Alignment |

---

## Quick start

Render a prompt for a sample evaluation case:

```bash
python utils/render_prompt.py \
  --template prompts/curriculum_coherence_judge.md \
  --case examples/sample_cases.jsonl \
  --index 0
```

Render prompts for every sample case:

```bash
python utils/render_prompt.py \
  --template prompts/curriculum_coherence_judge.md \
  --case examples/sample_cases.jsonl \
  --all
```

Parse a model response:

```bash
python utils/parse_output.py --text "[1,1,0,1,0,1,1,1]"
```

or

```bash
echo "[1,1,0,1,0,1,1,1]" | python utils/parse_output.py
```

---

## Intended use

Curriculum Coherence Evals is intended for researchers and practitioners developing or evaluating:

- educational conversational agents;
- intelligent tutoring systems;
- computed curriculum platforms;
- AI-assisted instructional design systems; and
- AI-mediated learning conversations.

Typical use cases include:

- LLM-as-a-Judge evaluation;
- human coding and rater training;
- curriculum quality assurance;
- comparison of LLM judges with expert annotations; and
- human-in-the-loop evaluation workflows.

---

## Theoretical foundations

This repository is informed by three complementary research areas:

- **Curriculum Design Coherence**, particularly the Curriculum Design Coherence (CDC) model.
- **Computed Curriculum**, including curriculum knowledge graph and AI-driven curriculum modelling.
- **LLM-as-a-Judge**, for scalable evaluation of AI-generated educational interactions.

A curated list of foundational references is provided in [`framework/references.md`](framework/references.md).

---

## Citation

If you use this repository, please cite the repository. A citation to the accompanying publication will be added once available.

---

## License

Released under the MIT License.