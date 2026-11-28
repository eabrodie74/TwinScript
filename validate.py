#!/usr/bin/env python3
"""Checks this branch's files: readings.json (each reading real syllables of its language, one per character, no word
twice in one scope) and audio/index.json (files present, small, consented and licensed). Exits 1 on any problem."""
import json, os, re, sys, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
SCOPES = {'mandarin': 'mandarin', 'mandarin-taiwan': 'mandarin', 'mandarin-mainland': 'mandarin',
          'cantonese': 'cantonese', 'taiwanese': 'taiwanese', 'hakka': 'hakka'}
HAN = re.compile(r'^[㐀-鿿豈-﫿\U00020000-\U0003ffff〇]+$')
def nfc(s): return unicodedata.normalize('NFC', s)
known = {l: set(nfc(x.strip()) for x in open(os.path.join(HERE, 'syllables', l + '.txt'), encoding='utf-8') if x.strip())
         for l in set(SCOPES.values())}
problems = []
readings = json.load(open(os.path.join(HERE, 'readings.json'), encoding='utf-8'))
if not isinstance(readings, list): problems.append('readings.json: should be a list')
seen = set()
for k, e in enumerate(readings if isinstance(readings, list) else []):
    where = f"readings.json #{k + 1} ({e.get('word', '?')})"
    for f in ['scope', 'word', 'reading']:
        if not isinstance(e.get(f), str) or not e.get(f): problems.append(f'{where}: "{f}" is missing')
    if problems and problems[-1].startswith(where): continue
    if e['scope'] not in SCOPES: problems.append(f"{where}: scope must be one of {', '.join(SCOPES)}"); continue
    if not HAN.match(e['word']): problems.append(f'{where}: the word must be Chinese characters only')
    syl = [x for x in re.split(r'[\s\-]+', nfc(e['reading'].lower())) if x]
    if len(syl) != len(e['word']): problems.append(f'{where}: {len(e["word"])} characters but {len(syl)} syllables')
    unknown = [x for x in syl if x not in known[SCOPES[e['scope']]]]
    if unknown: problems.append(f"{where}: not a {SCOPES[e['scope']]} syllable TwinScript knows: {', '.join(unknown)} (check the spelling and tone; a real one goes in syllables/)")
    if (e['scope'], e['word']) in seen: problems.append(f'{where}: this word is already in readings.json for {e["scope"]}')
    seen.add((e['scope'], e['word']))
audio = json.load(open(os.path.join(HERE, 'audio', 'index.json'), encoding='utf-8'))
for name, a in (audio.items() if isinstance(audio, dict) else []):
    where = f'audio/index.json {name}'
    p = os.path.join(HERE, 'audio', name)
    if not os.path.exists(p): problems.append(f'{where}: the file is missing'); continue
    if not name.endswith('.m4a'): problems.append(f'{where}: recordings are .m4a')
    if os.path.getsize(p) > 1_000_000: problems.append(f'{where}: larger than 1 MB')
    if a.get('scope') not in SCOPES: problems.append(f'{where}: scope must be one of {", ".join(SCOPES)}')
    if a.get('unit') not in ('character', 'word', 'phrase', 'sentence'): problems.append(f'{where}: unit must be character, word, phrase or sentence')
    if a.get('consent') is not True or a.get('license') != 'CC BY 4.0': problems.append(f'{where}: needs the speaker\'s consent and CC BY 4.0')
    for f in ['text', 'reading', 'region', 'speaker']:
        if not a.get(f): problems.append(f'{where}: "{f}" is missing')
print('\n'.join(problems) if problems else f'OK: {len(readings)} readings, {len(audio)} recordings')
sys.exit(1 if problems else 0)
