
---

## 3) README конкретного пилота

**docs/geobench/meal-planner/README.md**
```markdown
# GeoBench • Meal Planner (pilot)

Goal: one-day meal plan under hard constraints:
- 2000 ± 50 kcal, sugar ≤ 50 g, breakfast protein ≥ 30 g
- gluten-free (all items), total price ≤ $8.00
- products only from `usda_top100_v2.csv`

### Files
- `sample.psl.md` – PSL answer template
- `plan.json` – machine plan used by grader
- `usda_top100_v2.csv` – mini dataset (price, nutrients, gluten flag)
- `grader.py` – checks constraints, emits `report.json`

### Run
```bash
python grader.py --plan plan.json --dataset usda_top100_v2.csv --out report.json
