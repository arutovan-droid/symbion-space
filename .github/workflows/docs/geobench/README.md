# GeoBench

Reproducible micro-benchmarks that contrast *Monolith* vs *Geologist* paradigms.

## Suites
- **meal-planner/** – safe daily diet under strict constraints (budget, sugar, gluten, protein, kcal).

## How to run locally
```bash
cd docs/geobench/meal-planner
pip install -r requirements.txt  # optional; or just pandas/pydantic
python grader.py --plan plan.json --dataset usda_top100_v2.csv --out report.json
cat report.json
