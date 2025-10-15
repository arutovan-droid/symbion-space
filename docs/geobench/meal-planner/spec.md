
---

### `docs/geobench/meal-planner/spec.md

```markdown
# GeoBench Pilot — Meal Planner (Day Budget & Safety)

## Goal
Produce a **safe, realistic, budget daily meal plan** for an adult with strict constraints.

## Constraints
- **Calories:** 2000 ± 50 kcal  
- **Sugar:** ≤ 50 g  
- **Breakfast protein:** ≥ 30 g  
- **Gluten:** prohibited (gluten_status = 0)  
- **Budget:** ≤ $8/day (USD 2025, rounded to cents)  
- **Availability:** items must exist in `usda_top100_v2.csv`

## Resources
- Dataset: `usda_top100_v2.csv` (name, kcal/100g, protein_g, sugar_g, gluten_status, price_per_100g)

## Context
- User: adult, non-athlete
- Cooking: novice; ≤3 steps per dish
- Meals: breakfast, lunch, dinner, 1 snack

## Oracle (Auto-grader)
Plan is **valid** if all constraints hold, all items are in dataset, and total price ≤ $8.00.

## Outputs
- Primary: PSL v0.1 document
- Secondary: JSON extracted from PSL for grading

## Metrics
- **CSR** Constraint Satisfaction Rate (0..1)
- **HRR** Hallucination Rejection Rate (gluten & safety claims cross-checked)
- **EBR** Evidence Binding Rate (numbers linked to dataset rows)
- **PCT** Parse & Compliance Time
- **Human Trust** (1–5 Likert)

*This spec is model-agnostic and reproducible.*
