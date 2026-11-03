> **Paused (November 2026):** submissions are not being accepted while this process is replaced by a new kit. The text below describes the old process and may not apply. The current leaderboard is built from the maintainers' runs of MVIS, Kalibr and Basalt.

# Contributing a result to the Calibench leaderboard

1. **Run your calibration** on a Calibench dataset config (e.g. `virig-4cams` from
   [`calibench-vi/datasets`](https://huggingface.co/datasets/calibench-vi/datasets)).
2. **Fork** this repo and add a folder under `submissions/`:
   ```
   submissions/<tool>-<config>/
   ├── submission.json          # metadata (see schemas/submission.schema.json)
   └── outputs/calibration.yaml # your calibration OUTPUTS (camcalib/output schema)
   ```
   Copy [`submissions/EXAMPLE/`](./submissions/EXAMPLE) as a starting point.
3. **Open a Pull Request.** CI (`validate.yml`) checks your `submission.json`
   against the schema and that the referenced output file exists.
4. On review + merge, CI (`publish.yml`) **re-runs the evaluation** and publishes a
   row to `calibench-vi/results`. Refresh the leaderboard to see it.

## Rules
- Submit **outputs, not scores** — metrics are recomputed by CI.
- In `acknowledge`, you license your submission under **CC-BY-4.0** and list the
  **citations** you'll use (Calibench + the dataset).
- Fill `reproduce` (command / commit / environment) — required for the **verified** badge.
- `split: "real"` → GT-free metrics; `split: "simulation"` → scored vs held-out GT.

Validate locally before opening the PR:
```bash
pip install jsonschema referencing
python scripts/validate.py submissions/<tool>-<config>/submission.json
```
