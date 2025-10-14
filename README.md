# symbion-space
  Symbion Space is an open repo for Structured Intelligence (“Geologist”). It ships PSL v0.1—a contract language for AI—and GeoBench: real tasks with auto-graders. Focus: trust, verifiability, zero unsafe hallucinations. A Neuro-Syndicate orchestrates specialist models by roles. Roadmap + quickstart and open standards/
# Symbion Space — Structured Intelligence

**Not a bigger model. A better orchestra.**  
Symbion Space coordinates specialized AIs via a contract-first language (PSL) and a verification pipeline (GeoBench). The result: **trustworthy, reproducible, constraint-satisfying outputs**—without monolithic guesswork.

---

## Why this matters
Monolithic LLMs optimize for plausibility, not truth. We flip the stack:
- **PSL (Proto-Structural Language):** human-legible, machine-parsable contracts for tasks.
- **Syndicate Orchestration:** generator → auditor → optimizer → verifier roles.
- **GeoBench:** constraint & safety grading with reproducibility.

---

## Core concepts
- **PSL:** A concise task contract (goal, constraints, evidence, safety, checklist).
- **Syndicate:** A horizontal ensemble of narrow agents with clear roles.
- **GeoBench:** Auto-grading tasks for *Constraint Satisfaction Rate (CSR)*, *Hallucination Rejection Rate (HRR)*, and *Evidence Binding (EBR)*.

---

## Quickstart (conceptual)
1. Define a task as a PSL snippet.
2. Run the Syndicate: `generator → auditor → optimizer → verifier`.
3. Grade with GeoBench. Ship only if CSR=1.0 and HRR=1.0.

```psl
!psl v0.1
context: kitchen
goal: 2000±50 kcal daily menu; sugar ≤50g; breakfast ≥30g protein; gluten-free; budget ≤$8
constraints: calories=2000±50; sugar<=50g; breakfast_protein>=30g; gluten=false; budget<=8usd

[FACT]
1) Breakfast: ...
2) Lunch: ...
3) Dinner: ...
4) Snack: ...

[3C] clear: yes cheap: yes safe: yes
[CHECKLIST] calories, sugar, protein, gluten, price
