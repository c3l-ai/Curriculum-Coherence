# Coherence Dimensions

| Order | Code | Dimension | Positive label means |
|---:|---|---|---|
| 1 | PC | Propositional Coherence | The response builds meaningfully on prior ideas and maintains logical continuity. |
| 2 | RC | Referential Coherence | The response uses accurate and appropriate disciplinary references, terminology, analogies, or metaphors. |
| 3 | RF | Repair of Fragmentation | The response repairs a prior derailment, confusion, or fragmentary exchange. |
| 4 | SC | Sequential Coherence | The response follows a logical curricular or prerequisite sequence. |
| 5 | VF | Violation Flag | The response introduces a clear coherence violation. |
| 6 | AF | Avoidance of Fragmentation | The response maintains topical continuity and avoids abrupt unbridged shifts. |
| 7 | DA | Disciplinary Anchoring | The response is grounded in a clear disciplinary concept. |
| 8 | DPA | Disciplinary-Pedagogic Alignment | The response is both disciplinarily sound and pedagogically scaffolded. |

## Important note on output ordering

The combined judge prompt returns scores in the following order:

```json
[PC, RC, RF, SC, VF, AF, DA, DPA]
```

This ordering is preserved for compatibility with the original coding prompt.
