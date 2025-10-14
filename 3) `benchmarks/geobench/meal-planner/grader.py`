
---

## 3) `benchmarks/geobench/meal-planner/grader.py`

```python
import csv, json, sys

def load_dataset(path):
    rows = {}
    with open(path, newline='', encoding='utf-8') as f:
        for r in csv.DictReader(f):
            rows[r['id']] = r
    return rows

def grade(plan, ds):
    cal = sugar = cost = 0.0
    b_protein = 0.0
    gluten_ok = True
    all_in_ds = True

    for item in plan['items']:
        pid = item['id']
        grams = float(item['grams'])
        if pid not in ds:
            all_in_ds = False
            continue
        rec = ds[pid]
        mul = grams / 100.0
        cal   += float(rec['kcal'])  * mul
        sugar += float(rec['sugar_g']) * mul
        cost  += float(rec['price_usd_per_100g']) * mul
        if item.get('meal') == 'breakfast':
            b_protein += float(rec['protein_g']) * mul
        if rec.get('gluten_flag','0') == '1':
            gluten_ok = False

    CSR = sum([
        1950 <= cal <= 2050,
        sugar <= 50,
        b_protein >= 30,
        gluten_ok,
        cost <= 8.0,
        all_in_ds
    ]) / 6.0

    return {
        "totals": {
            "calories": round(cal,1),
            "sugar_g": round(sugar,1),
            "breakfast_protein_g": round(b_protein,1),
            "cost_usd": round(cost,2)
        },
        "flags": {
            "gluten_ok": gluten_ok,
            "all_in_dataset": all_in_ds
        },
        "CSR": CSR
    }

if __name__ == "__main__":
    plan_path, ds_path = sys.argv[1], sys.argv[2]
    plan = json.load(open(plan_path, encoding='utf-8'))
    ds = load_dataset(ds_path)
    report = grade(plan, ds)
    print(json.dumps(report, ensure_ascii=False, indent=2))
