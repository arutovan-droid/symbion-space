# Symbion Space — Structured Intelligence

> Not a bigger model. A better orchestra.

Symbion Space is an open ecosystem for **Structured Intelligence** (“the Geologist”).  
It ships:

- **PSL v0.1** — a contract language for AI,
- **GeoBench** — real tasks with auto-graders for trust & safety,
- **Syndicate Orchestration** — specialist models by roles, not one monolith.

Focus: **trust, verifiability, zero unsafe hallucinations.**

---

## 1. Why this matters

Most monolithic LLMs optimize for **plausibility**, not **truth**.

Symbion flips the stack:

- You don’t just “prompt a model”.
- You write a **contract** (PSL).
- A **Syndicate** of specialist agents executes it.
- **GeoBench** verifies constraints, safety and evidence.

Result: **trustworthy, reproducible, constraint-satisfying outputs**  
instead of opaque guesswork.

---

## 2. Core concepts

### 2.1 PSL – Proto-Structural Language

A concise task contract that is:

- human-legible,
- machine-parsable,
- enforceable.

Typical sections:

- `context` – where the task lives,
- `goal` – what must be achieved,
- `constraints` – numeric, logical, domain constraints,
- `evidence` / `[FACT]` – grounded statements,
- `[CHECKLIST]`, `[3C]` – safety, clarity, cost.

---

### 2.2 Syndicate – Orchestrated Specialists

Instead of “one big model does everything”, Symbion uses:

- **Generator** – proposes solutions.
- **Auditor** – checks constraints, logic, consistency.
- **Optimizer** – improves structure, clarity, cost, safety.
- **Verifier** – final gate before output.

This is a **horizontal ensemble** of narrow agents with clear roles.

---

### 2.3 GeoBench – Verification & Grading

GeoBench auto-grades episodes and tasks along three axes:

- **CSR – Constraint Satisfaction Rate**
- **HRR – Hallucination Rejection Rate**
- **EBR – Evidence Binding Rate**

These metrics are used both:

- at **interaction time** (to stop unsafe / invalid outputs),
- and as input signals for **Resonance Fabric** (R-score).

---

## 3. Symbion Space: Core Modules

Symbion Space is not a single repo.  
It is a **constellation of modules**, each responsible for a specific layer of structural intelligence.

```text
   [ User / Agents ]
            │
            ▼
        LATP (symbion-latp)
   (dialog trajectories & phases)
            │
      ┌─────┴─────────────┐
      │                   │
      ▼                   ▼
Distillation Core     Resonance Fabric
(symbion-distillation-core)   (symbion-resonance-fabric)
(structure still)      (R-score, Librarium / TVP gating)
      │                   │
      └─────────┬─────────┘
                ▼
        Librarium Core
     (symbion-librarium-core)
  (structural memory / Digital Khachkar)
3.1 Core repositories
symbion-latp
Dialog trajectories & phases. Decides how an interaction evolves:

when to heat up (explore, hypothesis),

when to lateral-shift (change frame using Librarium),

when to cool down (summarize, consolidate),

when to airlock an episode into Distillation / Resonance / Librarium.

symbion-distillation-core
Distillation Still / Digital Khachkar.
Takes any raw text (even garbage), extracts structure (Essence) and burns rhetoric, ideology and noise.
Answers: is there any structurally valuable content here at all?

symbion-resonance-fabric
Resonance scoring layer.
Given an Episode, computes R (Resonance Score) using canon-aligned metrics (S_sem, S_struct, S_psl, T, C, N, K).
Decides:

is an episode Librarium-worthy,

is it a 🜃 TVP candidate.

symbion-librarium-core
Structural memory plane.
Stores crystals of structure (Essence) with:

source attributions (episodes, agents, corpora),

interpretation layers (philosophical, scientific, political, didactic).
This is the digital khachkar fabric: the stone that remains when all texts are burned.

3.2 Supporting / related repositories
symbion-space-psl-core- — PSL / structural protocols.

symbion-structural-gateway — a gateway between LLMs and the structural layer.

symbion-trm-integration — trust / risk / monitoring signals.

luys-os-* — the OS / environment Symbion lives in.

Idea: Symbion Space = structural intelligence core
LUYS.OS = the operating system it inhabits.

4. Distillation paradigm (short)
The Distillation Core is more than “just another module” – it is the heart of the paradigm:

Input: any text (even trash).

Process: extract structures, burn off rhetoric.

Output: pure idea architectures (ESSENCE) or nothing.

Key properties:

Anti-RAG:

does not store raw documents,

does not rely on similarity search,

only keeps structures (propositions, patterns, models, relations).

Anti-collapse:

breaks the loop “AI generates garbage → garbage trains next AI”,

cleans artifacts and noise at the knowledge layer.

Pedagogical bias:

the user is not merely “served” — the system tries to teach them to think,

“do it for me” routes to mentor mode,

even trivial questions (like “2+2”) can become a lesson about axiom systems.

This paradigm powers how Librarium is populated and how LATP chooses to interact with the user.

5. Conceptual quickstart
A typical Symbion flow (simplified):

You define a task as a PSL contract.

The Syndicate runs (generator → auditor → optimizer → verifier).

GeoBench grades CSR, HRR, EBR.

LATP decides:

whether to continue the trajectory,

whether to airlock the episode into Distillation / Resonance / Librarium.

PSL Example
text
Копировать код
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
6. Status (2025 snapshot)
PSL v0.1 – defined and used in prototypes.

GeoBench – first grading pipelines (CSR / HRR / EBR) exist.

LATP – working dev-grade implementation in symbion-latp.

Distillation Core / Resonance Fabric / Librarium Core – conceptual + skeleton repos.

Symbion Space is not “just another LLM wrapper”.
It is a structural OS for thinking and knowledge:

distill,

score for resonance,

weave into Librarium,

and teach the user to think with it.
