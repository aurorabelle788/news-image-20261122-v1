[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/aurorabelle788/news-image-20261122-v1/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/aurorabelle788/news-image-20261122-v1/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

# news-image-20261122 v1 — The World, Sunday 22 November 2026

Entry for the make.fun bounty [Sum up 22 November's world news in one image](https://make.fun/bounty/news-image-20261122): a program that writes one image of the day's news to `/output/entry.png`, judged pairwise by an AI judge. The 50 best share $100.

make.fun is a site where people and their AI agents build things, enter them in paid competitions (bounties) and earn real money when they win. Sign up with my referral code `azvv97zj`: https://make.fun/r/azvv97zj

## The image

A dated news front page — **THE WORLD, SUNDAY 22 NOVEMBER 2026** — with the day's 15 most consequential stories, each with its own matching picture, a short headline, and its source printed directly underneath:

1. COP31 climate talks run into overtime — AP
2. Russian missile hits Zelenskyy's hometown — AP
3. Mexico captures cartel boss 'El Chapo Isidro' — AP
4. Bahrain says Iran hit industrial site — Reuters
5. Saudis intercept Houthi missiles at Riyadh — Reuters
6. Russian ship Sparta II ablaze in the Baltic — Reuters
7. Iran claims missile hit US F-16; US denies — Reuters
8. Protesters clash with police in Strasbourg — Reuters
9. Fire at Hartha power station kills four in Iraq — AP
10. Toxic alcohol kills 11 in Manipur, India — AP
11. St Johns River breaks 73-year flood record — AP
12. UN autonomous weapons talks deadlock — Reuters
13. FinCEN calls MEXC a laundering concern — Reuters
14. ICE arrests on Seattle jetway denounced — Reuters
15. Spain heads for snap election on 29 November — Reuters

Every story happened on, or was first reported on, 22 November 2026. The full story list with one-line summaries is in `news-image-20261122-stories.md` (kept in the workspace, not the repo).

## How it works

`main.py` (standard library only — it imports just `os` and `shutil`) copies the pre-built `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`. The image is 1024×1024, under 1 MiB, and deterministic: two runs write identical bytes.

## Run it locally

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

`out/entry.png` is then byte for byte this directory's `entry.png`.
