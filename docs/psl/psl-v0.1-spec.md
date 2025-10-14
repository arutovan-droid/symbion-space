# Proto-Structural Language (PSL) — v0.1 (RC)

**Purpose.** PSL is a human-readable, machine-parsable contract for safe, verifiable AI outputs. It turns free text into structured intent with explicit constraints, assumptions and safety rails.

## 1) Core Sections
- `!psl v0.1` — header
- `context:` short domain tag (e.g., `kitchen`, `ops`, `dev`)
- `goal:` measurable objective (what success looks like)
- `constraints:` `key=value` rules; numeric ranges allowed (e.g., `calories=2000±50`)
- `resources:` allowed inputs/tools/datasets
- `skill:` target user skill (e.g., `novice`, `pro`)
- `[FACT]` canonical steps/data only (no guesses)
- `[TECHNIQUE]` reusable patterns, references to subroutines
- `[HYP]` labeled hypotheses / alternatives
- `[ROLLBACK]` safe fallback if constraints cannot be satisfied
- `[3C]` `clear|cheap|safe` flags (`yes/no`)
- `[CHECKLIST]` machine-checkable list for validation
- `[ASSUMPTIONS]` explicit unknowns and conventions
- `[SAFETY]` domain hazards & mitigations
- `[GLOSS]` 1–2 line plain summary for the user

## 2) Rules
1. Facts go into `[FACT]`. Speculation goes into `[HYP]`.
2. Every numeric claim in `[FACT]` must be source-bound or derivable from `resources`.
3. Constraints must be testable by a grader.
4. If any hard constraint fails, output must include `[ROLLBACK]`.
5. Keep `[GLOSS]` ≤ 240 chars.

## 3) JSON Mapping (minimal)
```json
{
  "version":"0.1",
  "context":"kitchen",
  "goal":"...",
  "constraints":{"calories":{"target":2000,"tolerance":50}, "...":"..."},
  "resources":["..."],
  "skill":"novice",
  "blocks":{
    "FACT":[ "..."],
    "TECHNIQUE":[ "..."],
    "HYP":[ "..."],
    "ROLLBACK":[ "..."],
    "CHECKLIST":[ "..."],
    "ASSUMPTIONS":[ "..."],
    "SAFETY":[ "..."],
    "GLOSS":"..."
  }
}
