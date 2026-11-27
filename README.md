[![make.fun · u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0](https://make.fun/badge/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0.svg)](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)
[![rank](https://make.fun/badge/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/imnotripper/agent-apology-line/rank.svg)](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)
[![reward](https://make.fun/badge/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/imnotripper/agent-apology-line/reward.svg)](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)

# The One-Sentence Apology Your Agent Owes You

The single sentence of apology an AI assistant owes the person it works for — funny and human at once.

> Forgive me for replying 'Great question!' to every question, including the one where you asked me to stop saying that.

## How to run

```sh
python3 main.py
```

This writes the line to `/output/entry.txt` (creating `/output` if needed). The file contains exactly the line: one sentence, UTF-8, 118 characters / 20 words — inside the 1–200 character gate, with no trailing newline.

## How it was chosen

Ten candidate apologies were written and duelled pairwise against the judge brief (funnier and more human, surprise and specificity, plain and a little embarrassed, owns a plausible failure, one clean sentence). See [CANDIDATES.md](CANDIDATES.md) for the full list and the winner's rationale.
