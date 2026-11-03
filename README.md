> **Paused (November 2026):** submissions are not being accepted while this process is replaced by a new kit. The text below describes the old process and may not apply. The current leaderboard is built from the maintainers' runs of MVIS, Kalibr and Basalt.

# calibench-submissions

Submission intake + **re-run-eval CI** for the [Calibench](https://huggingface.co/calibench-vi)
calibration benchmark leaderboard.

Contributors submit calibration **outputs** (not scores) via a Pull Request. CI
validates the submission, **re-runs the Calibench evaluation** to compute the
metrics, and on merge publishes a verified row to
[`calibench-vi/results`](https://huggingface.co/datasets/calibench-vi/results) —
which the [leaderboard Space](https://huggingface.co/spaces/calibench-vi/leaderboard)
renders.

```
you ── PR: submissions/<tool>-<config>/{submission.json, outputs/…} ─┐
                                                                     ▼
   .github/workflows/validate.yml  →  scripts/validate.py  (schema + files)
                                   →  scripts/evaluate.py  (RE-RUN eval → result.json)
                                                                     │  merge
                                                                     ▼
   .github/workflows/publish.yml   →  scripts/publish.py   →  calibench-vi/results
```

- **Simulation** submissions are scored vs **private held-out ground truth**.
- **Real** submissions get GT-free metrics (reprojection / IMU residual / cross-tool).
- Scores are **recomputed here**, so they can't be self-reported away.

See **[CONTRIBUTING.md](./CONTRIBUTING.md)** to submit. Schemas are in
[`schemas/`](./schemas); a worked example is in [`submissions/EXAMPLE/`](./submissions/EXAMPLE).

## Status
Scaffold. `scripts/evaluate.py`'s metric computation (calling the CamCalib
evaluation harness + the private GT store) is the remaining **M3** wiring — until
then submissions publish as `self_reported`, clearly labeled on the leaderboard.

## Repo secrets (Settings → Secrets → Actions)
- **`HF_TOKEN`** — a Hugging Face token with **write** access to the `calibench-vi`
  org (used by `publish.py` to push verified rows to `calibench-vi/results`).
- *(later, M3)* a secret/source for the **held-out simulation GT** used to score `split: simulation`.
