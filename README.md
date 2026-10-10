# Smart Campus Analytics - Student Success Platform

Python (pandas) pipeline + interactive HTML/CSS/JavaScript dashboard (Chart.js).

## Run
```bash
pip install -r requirements.txt
python run.py            # builds data, scores students, opens http://localhost:8000
```
Options: `--regen` (regenerate synthetic CSVs), `--no-serve` (just run the pipeline), `--port 9000`.
Internet is needed once in the browser to load Chart.js from a CDN.
To use your own data, replace the 7 CSVs in `data/raw/` (keep column names) and run `python run.py`.

## Structure
```
run.py                  one-command launcher
src/generate_data.py    creates 7 messy source CSVs (academic, attendance, lms, engagement, placement, skills, feedback)
src/pipeline.py         clean -> integrate -> Success Score -> risk -> segments -> explainability
data/raw/               source CSVs          data/processed/  unified + at-risk CSVs + quality report
dashboard/              index.html, style.css, app.js, data.js (generated)
docs/STUDENT_SUCCESS_SCORE.md   methodology note (deliverable)
```

## Dashboard features
KPIs - filters (dept/year/risk/segment/search) - score histogram - risk by department - segment doughnut (click to filter) -
indicator radar vs campus - attendance-vs-CGPA scatter (click a dot) - year trend - sortable student table -
**explainable per-student driver chart** + suggested action - CSV export of at-risk students - data-quality modal.
