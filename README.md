# TwinScript language data

The readings and recordings people have contributed to [TwinScript](https://github.com/eabrodie74/TwinScript), each
accepted only after it was checked. TwinScript's data builds take everything here, and its self-test keeps every
accepted reading from then on, so a fix stays fixed.

## How a contribution gets here

1. Someone reports a wrong reading or a missing word, from TwinScript (the correction dialog's *Also send it to
   TwinScript*, or the Help menu) or with the [issue forms](https://github.com/eabrodie74/TwinScript/issues/new/choose).
2. It's checked against the standard dictionaries (Taiwan's and the mainland's for Mandarin, words.hk and CC-Canto
   for Cantonese, the Ministry of Education's Taiwanese and Hakka dictionaries, the Hakka Affairs Council's lists)
   and against example sentences, so a change can't break other words. Regional readings are welcome; they're
   recorded as such rather than replacing the standard one.
3. If it's right, a pull request into this branch adds it, naming the issue. The check below runs on it; merging it
   accepts it, and the issue gets a reply saying which data update brings it.

## What's here

- `readings.json`: accepted readings, one object each:
  `{"issue": 12, "scope": "mandarin", "word": "便宜", "reading": "pian2 yi5", "contributor": "…", "source": "…"}`.
  `scope`: `mandarin` (both standards), `mandarin-taiwan`, `mandarin-mainland`, `cantonese`, `taiwanese`, `hakka`.
  `word`: Traditional characters (TwinScript reads Simplified text through its Traditional form). `reading`: as
  TwinScript stores it: Pinyin with tone numbers (`pian2 yi5`), Jyutping (`pin4 ji2`), Tâi-lô (`pân-gî`), Hakka
  Pinyin with tone numbers 1–4 (`pien4 ngi2`), one syllable per character.
- `audio/`: recordings people have made of words TwinScript has no recording of (see `audio/README.md`).
- `syllables/`: every syllable TwinScript knows in each language, for the check.
- `CONTRIBUTORS.md`: who contributed what.

`python3 validate.py` checks the files; it runs on every pull request.

## License

Contributions here are published under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): anyone may use
them, crediting the contributors (CONTRIBUTORS.md). Contributing means agreeing to that.
