<p align="center"><img src="docs/images/app-icon.png" width="128" alt="TwinScript icon"></p>

<h1 align="center">TwinScript</h1>

<p align="center">Traditional and Simplified Chinese, twelve romanizations and a full Chinese–English dictionary, for the Mac.</p>

<p align="center">
  <a href="https://github.com/eabrodie74/TwinScript/releases/latest"><b>⬇︎ Download TwinScript for Mac</b></a>
  &nbsp;·&nbsp; free &nbsp;·&nbsp; macOS 12 or later &nbsp;·&nbsp; Apple silicon &nbsp;·&nbsp; signed and notarized by Apple
</p>

![TwinScript Home](docs/images/home-screen.png)

TwinScript converts Chinese between Traditional and Simplified, and writes it in Pinyin, Zhuyin, Jyutping, Tâi-lô, Hakka and seven other romanizations. It works on documents (keeping their formatting), file and folder names, song tags and lyrics, the clipboard, web pages in Chrome and Safari, and pictures. It also has an offline Chinese–English dictionary, a reader that puts the reading over every word, and a study list with flashcards and drills.

## Contents

- [Features](#features)
- [Install](#install)
- [First steps](#first-steps)
- [Chrome and Safari](#chrome-and-safari)
- [Dictionary extras](#dictionary-extras)
- [Updates](#updates)
- [Privacy](#privacy)
- [Uninstall](#uninstall)
- [Troubleshooting](#troubleshooting)
- [Credits and licenses](#credits-and-licenses)

## Features

### Home
- **Your day in one place:** words due for review, a word of the day, Quick Convert for a line of text, your recent searches and files, watch folders and the clipboard. **Customize** rearranges and resizes the cards.
- **⌘K** opens one box to go to any page, run any action or look up a word.

### Convert anything with Chinese in it
- **Documents keep their formatting:** Word, Excel, PowerPoint, OpenDocument, EPUB, RTF and PDF come out in the same format.
- **Any old encoding:** plain text, web pages, CSV, subtitles and lyrics in GBK, GB18030, Big5, Big5-HKSCS, EUC-TW, HZ, UTF-16 and more are detected automatically and saved as UTF-8.
- **Pictures and scanned PDFs** are read on your Mac (OCR) and saved as converted text.
- **Subtitles** keep their timings; in `.ass` files, fonts and effects stay untouched.
- **Words, not just characters:** 头发 becomes 頭髮 and 发展 becomes 發展. Characters with more than one Traditional form are marked in the preview. Choose one for this document only, or **Always** to add it to your word list.
- **Taiwan or Hong Kong** character forms, optionally with regional vocabulary (软件 → 軟體, 悉尼 → 雪梨).
- **Romanization above, below or beside** the characters (Word phonetic guides, HTML ruby, PDF, extra lines in text).

### Rename files and folders
- See every new name first. Rename whole folders and everything inside them.
- **⌘Z undoes a rename** and ⇧⌘Z redoes it, including renames made from Finder's right-click menu.
- **Renaming back from Pinyin** gives the characters back: TwinScript remembers them on the file.
- Repairs names garbled by old Windows systems (Big5 or GBK shown as accented Latin letters).
- **Name styles** for romanized names: with or without tones, hyphens, capitals joined (QingTian) or underscores.

### Music
- Converts titles, artists, albums and lyrics inside **MP3, M4A, FLAC, APE and Ogg** files; the sound isn't touched.
- Converts songs in your **Apple Music library**: the selected ones or all of them, after showing how many will change.
- **Pinyin sort names** so Music lists Chinese songs, artists and albums in alphabetical order.
- **Repairs garbled tags** saved by old Chinese software in GBK or Big5.
- **Find Lyrics** searches six sources and saves plain lyrics into the song, plus an optional line- or word-synced copy. Play the song to see the lyrics follow along, nudge the timing, and add a reading line under each line for karaoke.

### Learn
<img src="docs/images/dictionary-page.png" alt="Dictionary">

- **Dictionary:** CC-CEDICT, Wiktionary, the Ministry of Education's Revised Mandarin Dictionary and idioms, CC-Canto, NAER technical terms, Wikipedia names and Wikidata. Readings in Mandarin, Cantonese, Taiwanese and Hakka, with sound. Stroke-order animation, example sentences, how each character is built, and filters by radical, strokes and HSK, TOCFL or TBCL level. Draw a character, or pick its parts, to find it. Browse it **as a book**, page by page, with bookmarks; see each character's **parts** as a tree; keep **notes** on any word.
- **Look up anywhere:** press ⌃⌥⌘L and drag over Chinese anywhere on screen, even in pictures and videos; or select Chinese in any app and choose **Services › Look Up in TwinScript**, or ⌥-click a word in a TwinScript preview.
- **Reader:** paste or open any text to see the reading over every word (Zhuyin goes beside each character, the Taiwanese way). Hover for the meaning, underline words by learner level, read it aloud, and save it as a PDF.

<img src="docs/images/reader-page.png" alt="Reader with readings over every word">

- **Study List:** star words anywhere. Review them as flashcards with spaced repetition, practise writing them stroke by stroke, drill listening, pinyin and tones toward a daily goal, or export them to Anki.

### Everywhere else
- **Finder right-click menu:** convert documents, rename items and convert song tags without opening a window.
- **Clipboard:** keyboard shortcuts, or convert everything you copy automatically.
- **Watch folders:** new files that land in a folder are converted on their own.
- **Interface in English, 繁體中文 or 简体中文** (Settings › General).

<img src="docs/images/study-page-traditional.png" alt="Study List, with the interface in Traditional Chinese">

## Install

1. Download **TwinScript-1.2.pkg** from the [latest release](https://github.com/eabrodie74/TwinScript/releases/latest).
2. Open it and follow the installer. It's signed and notarized by Apple, so macOS opens it without warnings.
   - Under **Customize** you can untick **Fonts for rare characters**: Jigmo and Plangothic, about 100 MB, installed into `/Library/Fonts` so every app on your Mac can show characters macOS has no font for. TwinScript itself works without them.
3. Open **TwinScript** from Applications. A short welcome tour shows the main features. You can open it again any time from **Help › Welcome Tour**.

**Requirements:** macOS 12 Monterey or later on an Apple silicon Mac.

## First steps

| To… | Do this |
|---|---|
| Convert documents | **Convert Text**: drop files or folders in, check the preview, click **Convert**. |
| Rename files | **Rename Files & Folders**, or right-click in Finder › **TwinScript**. |
| Fix song tags | **Music Tags**: drop songs or a music folder in. **Apple Music** converts your library. |
| Look up a word | **Dictionary**, or select text in any app › **Services › Look Up in TwinScript**. |
| Read with help | **Reader**: paste text and choose a romanization. |
| Convert the clipboard | Set shortcuts in **Settings › Shortcuts**, or turn on **Convert › Auto-Convert Copied Text**. |

**Permissions macOS may ask for:**
- **Automation (Finder, Music):** renaming the items selected in Finder, and converting your Apple Music library.
- **Accessibility:** only if you use shortcuts that copy and paste selected text for you.
- **Finder extension:** if the right-click menu is missing, turn on TwinScript in **System Settings › General › Login Items & Extensions › Finder**.

The full guide is in **Help › TwinScript Help** inside the app.

## Chrome and Safari

On any web page you can convert to Traditional or Simplified with or without readings, show the reading and meaning only on hover, underline words by level, read aloud, ⌥-click a word to open it in TwinScript, and add words to your Study List. Everything runs through TwinScript on your Mac.

**Safari:** open **Safari › Settings › Extensions** and tick **TwinScript**. It comes with the app.

**Chrome, Brave, Edge, Arc or Vivaldi:**
1. In TwinScript, go to **Settings › General › TwinScript in Chrome › Set Up…**. This connects TwinScript to your browsers and copies its location to the clipboard.
2. In the Extensions page that opens, turn on **Developer mode** (top right) and click **Load unpacked**.
3. Press **⇧⌘G**, paste, press Return, then **Select**.

You only do this once. The extension updates itself whenever TwinScript updates.

## Dictionary extras

The app comes with everything needed for conversion and romanization. The Dictionary's data is a separate download of about 520 MB: Wiktionary and CC-CEDICT, the Ministry of Education's dictionaries, Cantonese, technical terms, names, example sentences, learner levels, stroke order and the character finder. Open the **Dictionary** and click **Download the Dictionary**, or pick pieces in **Settings › Plugins** (**Download**, or **Download All Extras**). They arrive ready to use: nothing is built on your Mac. **Check for Updates** keeps them current, and new data is used without a restart.

## Updates

TwinScript checks this repository's releases once a day and offers new versions. You can also check from **TwinScript › Check for Updates…**. Updates download the new installer, check its SHA-256, and open it.

## Privacy

- Conversion, romanization, OCR and the dictionary all run **on your Mac**. Your documents and text are never uploaded.
- TwinScript only goes online when you ask it to: lyric searches (the song's title and artist go to the lyric sites), Wikidata lookups, Taiwanese pronunciation audio, plugin downloads and update checks.
- No accounts, no analytics, no tracking.

## Uninstall

1. Quit TwinScript and move **/Applications/TwinScript.app** to the Trash.
2. Optionally remove its data: `~/Library/Application Support/TwinScript` (dictionaries and word lists) and `~/Library/Preferences/local.twinscript.mac.plist` (settings).
3. If you installed the fonts, remove `Jigmo*.ttf` and `PlangothicP*.ttf` from `/Library/Fonts`.
4. In Chrome, remove the extension from the Extensions page.

## Troubleshooting

- **The right-click menu is missing in Finder:** System Settings › General › Login Items & Extensions › Finder › turn on TwinScript, then relaunch Finder (⌥-right-click Finder in the Dock › Relaunch).
- **A file converted to gibberish:** its encoding was guessed wrong. In Convert Text, choose the right one in its **Read As** menu.
- **Chrome says the helper isn't set up:** run **Settings › General › TwinScript in Chrome › Set Up Again…**, then reload the extension.
- **Check that conversions are right:** **Settings › Plugins › Check Conversions** runs the built-in test set.

Found a problem or have an idea? [Open an issue](https://github.com/eabrodie74/TwinScript/issues).

## Credits and licenses

TwinScript is free to use. © 2026 Evan Brodie. All rights reserved. This repository holds the releases and documentation; the app's source code isn't published.

TwinScript is built on the work of many open projects. Each source's version and license is also shown in **Settings › Plugins**. See [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md) for the full list.
