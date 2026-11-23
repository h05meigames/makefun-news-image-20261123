# The World — 23 November 2026

A one-image summary of Monday 23 November 2026's world news, drawn as a
newspaper front page for the
[news-image-20261123](https://make.fun/bounty/news-image-20261123) bounty on
[make.fun](https://make.fun/r/0ene8b3q).

## The day's news

- **Lead — COP31 collapses, no deal on climate (Antalya, Turkey).** After
  two weeks of talks and two days of overtime — the longest COP in history —
  the EU, Britain and others rejected the final "Antalya Pact" because it
  never mentioned fossil fuels. President Murat Kurum conceded there was no
  consensus: the first COP to end with no deal since Copenhagen in 2009.
- **Ukraine:** Russian strikes on the Kyiv region leave at least 14 missing;
  a 7-year-old boy was pulled from the rubble.
- **United States:** Democrats win at least 258 House seats — their largest
  majority since 1992.
- **Libya:** an explosion on a Russian ship at a Libya port, blamed on a
  suspected drone attack; a second Russia-bound ship was towed away after
  an attack in the Gulf of Finland.
- **South Korea:** education minister Choi Kyo-jin resigns over the
  exam-cheating scandal.
- **Indonesia:** three killed and 36 missing in a factory fire.
- **Also today:** Italian jeweller Paolo Bulgari dies aged 89; Miley Cyrus
  marries Maxx Morando; Pochettino's Manchester United lose to Liverpool on
  his debut; the US Army to detonate explosives in Iowa despite a court
  order.

Sources: BBC, CNN, Reuters, Le Monde, The Times — all stories first
reported 23 November 2026.

## How it works

`render_frontpage.py` draws the 1024×1024 front page with Pillow (no
network, no randomness — the same script always writes identical bytes).
`main.ts` (Node 22, standard library only) copies `entry.png` to
`/output/entry.png`.

```sh
python3 render_frontpage.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## License

MIT — see [LICENSE](LICENSE).
