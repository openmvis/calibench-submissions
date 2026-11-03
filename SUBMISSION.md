> **Paused (November 2026):** submissions are not being accepted while this process is replaced by a new kit. The text below describes the old process and may not apply. The current leaderboard is built from the maintainers' runs of MVIS, Kalibr and Basalt.

# Submitting results to the Calibench leaderboard

Open a **PR to this repo** adding your submission under `submissions/<tool>-<batch>/`.
CI validates against `schemas/result.schema.json`, publishes records to
[`calibench-vi/results`](https://huggingface.co/datasets/calibench-vi/results)
(`<Tool>/<batch>/*.json`), and the
[leaderboard](https://huggingface.co/spaces/calibench-vi/leaderboard) picks them
up on refresh. Until the re-run-evaluation CI lands, third-party rows are
labeled `self-rep` on the board.

*These requirements are open to improvement — PR this file to propose changes.*

## Required contents (✅ required · ◽ recommended)

| Field | Req. | What to provide | Example |
|---|---|---|---|
| `tool.name` / `tool.version` / `tool.commit` | ✅ | Tool identity: release tag **and** commit hash | `Kalibr 1.1.0 @ a4f2c91` |
| `tool.link` | ✅ | Code repository and/or paper | github.com/ethz-asl/kalibr |
| Run configs | ✅ | The **exact config files / CLI flags** per dataset config (files in the PR, not prose): camera model selected, optimizer settings | `configs/tum_vi_1024.yaml` |
| Datasets run | ✅ | Config ids + collections (ids from `tracks.json` / the [dataset catalog](https://huggingface.co/datasets/calibench-vi/results/blob/main/datasets.json)) and the **batch date** the records carry | `tum_vi_standard_1024` cam1–cam8, batch `2026-05-09` |
| `meta.yaml` sequences | ✅ | Sequences *used for calibration* — held-out metrics are computed on the complement | `used: [cam1, cam2]` |
| Calibration outputs | ✅ | One `*.output.json` per run: intrinsics `[fx,fy,cx,cy]` + model params, distortion, extrinsics, time offsets; records link via `calibration_ref` | see `schemas/` |
| Reported σ / covariance | ◽ | Per-parameter σ where your tool provides it (feeds the σ-consistency metric; absence shows "—", never a pass) | `fx: 382.4 ± 0.3` |
| Statistic definition | ✅ | For self-reported metrics: the **exact statistic** — mean/median/std/RMSE, over which residuals, which frame set. Different statistics are not comparable and trigger a mixed-definition warning on the board | "median reprojection error over all corners, all frames" |
| Runtime | ✅ | Wall-clock per dataset (drives the score-vs-runtime view) | `352 s` |
| Hardware / OS | ✅ | CPU model + cores, RAM, GPU if used, OS | i7-12700H, 32 GB, Ubuntu 22.04 |
| Contact | ✅ | Issue contact; affiliation optional | you@lab.edu |
| License affirmation | ✅ | Your records/outputs are publishable under CC-BY-4.0 | statement in the PR |

## Layout

```
submissions/<tool>-<batch>/
├── meta.yaml            # tool {name, version, commit, link}, batch, hardware,
│                        #   statistic definitions, sequences used, contact
├── configs/             # exact per-dataset tool configs you ran
├── records/*.json       # one result record per (dataset, split) — schema v1.1
└── outputs/*.output.json
```

Contributing a **dataset** instead? See
[`calibench-vi/community`](https://huggingface.co/datasets/calibench-vi/community).
