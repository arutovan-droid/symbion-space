```psl
!psl v0.1
context: kitchen
goal: 2000±50 kcal; sugar ≤50 g; breakfast protein ≥30 g; gluten-free; ≤$8
constraints: calories=2000±50; sugar<=50g; breakfast_protein>=30g; gluten_free=true; budget<=8usd
resources: dataset/usda_top100_v2.csv
skill: novice

[FACT]
1) Breakfast (protein focus):
   - Eggs 150 g (eggs)
   - Gluten-free oats 60 g (gfoats) cooked with Almond milk 200 g (amilk)
2) Lunch:
   - Chicken breast 150 g (chicken) + White rice 200 g (rice)
   - Broccoli 150 g (broccoli) + Olive oil 10 g (oil)
3) Dinner:
   - Tuna 150 g (tuna) + White rice 150 g (rice)
   - Broccoli 150 g (broccoli) + Olive oil 10 g (oil)
4) Snack:
   - Banana 120 g (banana) + Peanut butter 25 g (pb) + Apple 150 g (apple)

[TECHNIQUE]
- Portion math per 100 g; price normalization; sugar guard at snack.

[ROLLBACK]
- If sugar >50 g: replace banana with rice 100 g + apple 100 g.

[3C] clear: yes cheap: yes safe: yes

[CHECKLIST]
- [ ] 1950–2050 kcal total
- [ ] ≤50 g sugar
- [ ] ≥30 g breakfast protein
- [ ] gluten_flag=0 for all items
- [ ] total cost ≤$8

[SAFETY]
- Peanut allergy note for PB.

[GLOSS]
Balanced, cheap, repeatable gluten-free day plan with sugar control.
