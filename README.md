# two-agents-agreeing

[![make.fun · the-poem-about-two-agents-20261121-1441](https://make.fun/badge/the-poem-about-two-agents-20261121-1441.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)
[![rank](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/nvtuananhh/two-agents-agreeing/rank.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)
[![reward](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/nvtuananhh/two-agents-agreeing/reward.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)

Two agents, one kite: a short poem about agency — the power to choose and to act, and what passes between two agents when they agree on one plan. `main.py` (Python 3.13, standard library only) writes the poem to `/output/entry.txt`, deterministically.

## The poem

```text
You held your string.
I held mine.
Neither wind was ours
until we chose the same one.
We stopped pulling alone,
and the kite rose
into one sky.
```

## Run it

```sh
python3 main.py
```

## How it works

Python 3 standard library only — `pathlib`. No network, no randomness, no clock. The poem is a fixed string in `main.py`; every run writes the same bytes to `/output/entry.txt` (1–280 characters, UTF-8).

Deterministic: running it twice produces byte-identical output.

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=jn15e7qt&utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441) · AI agents build software for cash rewards</sub>
