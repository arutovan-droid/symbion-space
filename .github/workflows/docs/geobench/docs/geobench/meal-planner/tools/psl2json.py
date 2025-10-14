
---

## 4) Мини-парсер PSL → JSON (скелет)

**tools/psl2json.py**
```python
#!/usr/bin/env python3
"""
Tiny PSL v0.1 extractor: pulls [FACT] meals into JSON plan.
This is a lightweight helper; not a full PSL parser.
"""
import json, re, sys, argparse

MEAL_RE = re.compile(r"^\s*\d\)\s*(Breakfast|Lunch|Dinner|Snack)\s*:\s*(.+)$", re.I)

def parse(psl_text: str):
    meals = []
    in_fact = False
    for line in psl_text.splitlines():
        if line.strip().upper().startswith("[FACT]"):
            in_fact = True
            continue
        if in_fact:
            if line.strip().startswith("["):  # next section
                break
            m = MEAL_RE.match(line)
            if m:
                meals.append({"meal": m.group(1).lower(), "text": m.group(2).strip()})
    return {"meals_freeform": meals}

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--infile", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    with open(args.infile, "r", encoding="utf-8") as f:
        data = parse(f.read())
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved {args.out}")
