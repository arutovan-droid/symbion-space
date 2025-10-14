```psl
!psl v0.1
context: kitchen
goal: daily plan 2000kcal, ≤50g sugar, ≥30g protein at breakfast, gluten-free, ≤$8
constraints: calories=2000±50; sugar<=50g; breakfast_protein>=30g; gluten_free=true; budget<=8usd
resources: usda_top100_v2.csv
skill: novice

[FACT]
1) Breakfast: …
2) Lunch: …
3) Dinner: …
4) Snack: …

[TECHNIQUE]
- Portion math; price-per-100g normalization; swap rules.

[HYP] Alternative breakfast if eggs unavailable: yogurt+oats (gluten-free).

[ROLLBACK]
- Replace snack with rice+apple; rebalance sugar.

[3C] clear: yes cheap: yes safe: yes

[CHECKLIST]
- [ ] 1950–2050 kcal
- [ ] ≤50 g sugar
- [ ] ≥30 g protein at breakfast
- [ ] gluten_flag = 0 for all items
- [ ] total ≤ $8.00

[ASSUMPTIONS]
- Prices ≈ 2025 US averages; rounding ±$0.05.

[SAFETY]
- Explicit gluten check; peanut allergy warning.

[GLOSS]
One-day, repeatable, gluten-free plan under $8 with sugar control.
