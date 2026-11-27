# Changelog

## 1.4.4 (November 2026)

- **Readings checked against expert answer keys in every language**, each change measured on material it wasn't chosen from, and every changed reading rechecked across 67,000 Mandarin sentences so nothing else breaks.
  - **Taiwanese**, against the Ministry of Education's 17,889 example sentences: characters differing from the editors' readings fell from 9,533 to 3,373 of 164,009. Characters on their own read as the editors read them (就 *tō*, 會 *ē*, 共 *kā*, 才 *tsiah*), and by the words around them: 傷大 *siunn tuā* "too big", 錢通買 *thang*, 蹛遮 *tsia* "here" but 遮大 *tsiah* "so big", 你敢袂去？ *kám*, 加真濟 *ke*, 上驚 *siōng*. Fixed: 大人 *tuā-lâng*, 所有 *sóo-ū*, 一百 *tsi̍t-pah*, 阮 *guán*. Mandarin words the Taiwanese dictionaries lack read in the right sense (經濟學家 *ka*, 混合物 *bu̍t*, 照相機 *siòng*).
  - **Hakka**, against the Hakka Affairs Council's certification word lists (客語能力認證, about 5,200 words read by its editors), which now come first: differences fell from 540 words to 71. 仔 after the falling tone is *eˇ* (狗仔 *gieuˋ eˇ*), and words in sentences are found more carefully (有意思, 臺北市長).
  - **Cantonese**, against HKCanCor (154,000 words of transcribed speech): characters on their own read as people say them where words.hk agrees (返 *faan1*, 驚 *geng1*, 位 *wai2*, 黑 *haak1*); 咪 is *mai6* "then", *mai1* "mile" (五十咪) or *mai5* "don't" (咪玩啦！); 吓 *haa2* "huh?"; 行長 *hong4 zoeng2*.
  - **Mandarin**, against the CPP benchmark (20,000 hand-labelled sentences): 91.0% → 94.2% on the hardest characters (翟 *Zhái*, 幢 *zhuàng*, 卜 *bǔ*, 茄 *qié*, 尽 *jìn*); 长 *zhǎng* in 长什么样, 市长; 为 *wéi* in 选为, 以…为. With Taiwan's standard: 唇 *chún*, 暖暖 *nuǎn*, 沒了 *méi*, 尺寸 *chǐ*.
- **Hakka recordings.** 4,834 recordings of 4,303 words from the Hakka Affairs Council's certification exams play from your Mac wherever the reading shown is the one recorded (Settings › Speech, 75 MB). The experimental Hakka voice now covers 90,742 words, with the corrected readings.
- **Simplified text plays the recordings too:** 告诉 plays the Ministry's recording of 告訴.
- **Reading corrections can be kept to the word on its own:** tick *Leave longer phrases alone*, and 銀行家 keeps its own reading while 銀行 takes yours.
- **Fixed readings stay fixed:** 5,500 checked readings in all four languages are tested at every build and after every data update.

## 1.4.3 (November 2026)

- **Readings checked against 66,000 example sentences.** TwinScript now finds words more carefully, so a rare dictionary word no longer swallows the start of the next one: 冷靜地處理 is *de chǔlǐ* (not 地處 *dìchǔ*), 他的姐姐 *de jiějie* (not 的姐 "taxi driver"), 手中的 *zhōng de*, 說中文 *zhōngwén*, 沒有人相信 *xiāngxìn*. About 1,000 readings in those sentences changed, reviewed by hand group by group; a few rare phrases now read worse (闭着眼 reads 着 as *zhuó*).
- **More readings fixed:** 到了 *dào le* (it said *dào liǎo*), 受不了 *bù liǎo*, 們 *men*, 築 *zhù* (Taiwan's standard: *zhú*), 削 *xiāo*, 睡了一覺 *jiào*, 下載 *xiàzài*, 狗狗, 咖哩; with Taiwan's standard, 它們 is *tā men*. Text that's already Traditional is no longer misread through a second conversion (發明了 *le*, not *liào*).
- **Reading corrections show their side effects:** before you save one, the dialog lists the example sentences that would read differently.
- **Correct a reading from the Reader, Chrome or Safari:** right-click a word.

## 1.4.2 (November 2026)

- **Correct a reading yourself.** If TwinScript reads a word wrongly, click ✎ beside its reading in the Dictionary and type the right one (Pinyin, Zhuyin, Jyutping, Tâi-lô or POJ, Hakka Pinyin). Only real syllables, one per character, are accepted, and you see how the word will read before saving. Your reading is used everywhere: converted text, the Dictionary, the Reader, the voices and the Chrome and Safari extensions. Mandarin corrections can be for both standards or only Taiwan's or the mainland's. All of them are listed in Settings › Romanization and sync between your Macs.
- **Mandarin readings fixed** where a dictionary's first reading was a rare one: about 50 learner words in each standard, including 便宜 *pián yi*, 還錢 *huán qián*, 看著 *kàn zhe*, 甚麼 *shén me*, 都會 *dōu huì*, 好處 *hǎo chù*, 中式 *zhōng shì*, and 妳 *nǐ*, 乾 *gān*. With Taiwan's standard, 只 is *zhǐ* again, and 玩 and 术 read *wán* and *shù* in Simplified text. The voices follow.
- **A new menu bar icon:** the two ducks.
- Settings and Log have page banners like the other pages.

## 1.4.1 (November 2026)

- **Hakka readings checked against the Hakka Affairs Council's and Ministry of Education's data** (through FormoSpeech's FormoG2P lexicon): common characters read their usual way (人 *ngin*, 看 *kon*, 地 *ti*, 好 *ho*, 會 *voi*), about 760 readings fixed, and about 75,000 words added that used to be read character by character.
- **Cantonese readings follow Hong Kong usage as recorded by words.hk:** about 1,070 fixed (度過 *dou6*, 遇到 *jyu6 dou3*, 少量 *siu2 loeng6*) and 7,400 colloquial words added. A Cantonese entry whose CC-Canto reading differs shows the reading spoken, with CC-Canto's beside it.
- **The experimental Hakka voice** says the corrected readings and covers 90,649 words (about 500 MB) (download it again in Settings › Speech).
- **With Taiwan's Mandarin**, search results show Taiwan's readings too (研究 *yánjiù*).
- Help names the new reading sources.

## 1.4 (November 2026)

- **English–Chinese.** Look up an English word to see its meanings, each with the words used in Mandarin, Cantonese, Taiwanese and Hakka, with readings and sound (about 50,000 English words from Wiktionary). Search by sound in any language (*sik6 faan6*, *tsia̍h-pn̄g*) or by pattern (天?地?), with a scope beside the search box.
- **The book in six arrangements:** Chinese–English by pinyin, radical, Zhuyin or strokes; Cantonese–English by Jyutping; English–Chinese from A to Z, each with its own title page, guide and indexes.
- **Taiwanese recordings.** The Ministry of Education's recordings of 22,298 words and 787 phrases (臺灣台語常用詞辭典) play from your Mac, and only the recording of the reading shown. Words without one are assembled from recorded syllables, each in the tone it takes in the word, and labelled so.
- **The voices say what TwinScript shows.** Mandarin and Cantonese voices no longer guess characters with several readings (銀行 is never yín xíng). A missing voice offers to download one instead of reading with the wrong voice. **Settings › Speech** chooses each language's voice, speeds and downloads.
- **Taiwan's or the mainland's Mandarin.** Where they differ (研究 yánjiù / yánjiū, 星期 xīngqí / xīngqī, 學生 xuéshēng / xuésheng), readings, Zhuyin and voices follow your region or your choice (Settings › Romanization). 27 words that read the rarer meaning are fixed in both (結果 jiéguǒ, 重點 zhòngdiǎn).
- **Taiwanese readings follow the Ministry's dictionary:** about 1,900 corrected and 7,500 added; tone changes for -p/-t/-k/-h syllables fixed.
- **Example sentences:** the right recording plays (it sometimes played another sentence's), at once and only for your latest click, kept after the first play, and slower if you like.
- Fixes: characters search in every scope; the window comes forward when opened from a full-screen app; Chrome, Safari and Quick Look follow the reading settings.

## 1.3 (November 2026)

- **Study › Progress.** Your words, how many you know well, reviews and days studied; a calendar of the last six months shaded by how close each day came to your goal; how your list has grown; and your most-missed words, a click away from the Dictionary.
- **Web pages and EPUB books in the Reader.** Open Web Page… reads just a page's article (the address you copied is filled in). EPUB books open a chapter at a time, with a chapter menu and Previous/Next Chapter.
- **Better example sentences.** The word is marked in each example; six show at first, with More examples for the rest; Read opens a sentence in the Reader; Study's review cards show an example under the answer.
- **Sync between your Macs** (Settings › General). Your Study List and progress, notes, bookmarks, study days and word lists, through a TwinScript folder in iCloud Drive or any folder you choose. Each Mac writes only its own file, so two Macs never overwrite each other.
- **A new icon:** a pair of mandarin ducks (鴛鴦), one ivory and one red. The About window is simpler, with a larger icon.
- **Regional words.** Film, TV, game and music titles from Wikipedia's lists no longer replace everyday words (第一章 stayed 第一章, not a game title); about 2,000 such rules removed.
- **Chrome and Safari.** More room between lines and between syllables when readings are shown; with Zhuyin, learner-level underlines now show, line up and clear the symbols.
- Fixes: the review card's count is translated; Help covers everything new, in English and Chinese.

## 1.2 (November 2026)

- **Look up text on screen.** Press ⌃⌥⌘L (or use the menu-bar icon or ⌘K) and drag over Chinese anywhere on screen, even in pictures, videos and apps that won't let you select it. The words are listed with readings and meanings, to open in the Dictionary, star or read in the Reader. Needs Screen Recording permission the first time.
- **Character parts.** Each character's entry shows how it's built, as a tree of its parts with their meanings, and other characters that share each part.
- **Notes and bookmarks.** Write a note on any word (marked ✎ in the book); bookmark pages of the book with its ribbon, listed in the panel and on the contents page.
- **Study.** A daily goal with today's count and days in a row; three quick drills: Listening, Type the Pinyin and Tones.
- **Find Lyrics plays along.** Play lights each line as it's sung; nudge the timing earlier or later; optionally add a reading line under each line of the synced copy.
- **Convert.** Changed characters are highlighted; a character choice can apply to every document in the list.
- **Rename.** Name styles for romanized names: no tones, hyphens, capitals joined or underscores.
- **Music Tags.** Tags garbled from GBK or Big5 are repaired before converting.
- Help updated for 1.1 and 1.2, in English and Chinese.

## 1.1 (November 2026)

- **The Dictionary as a book.** Browse CC-CEDICT page by page, arranged by pinyin or by Kangxi radical, with guide words, page numbers, thumb tabs, a contents page, a guide (凡例) and syllable and radical indexes. Type a word to turn to its page; click a word to open its full entry on the same paper.
- **⌘K command palette.** One box to go to any page, run any action (convert the clipboard, open the book, add files) or look up a word.
- **A new layout.** Each page has a banner with its name and a picture of what it does; its options sit in the panel at the right; pages are cards, and empty pages say what to do step by step. New dropdowns in the app's own style.
- **Pinyin sort names for music.** Music Tags writes the pinyin of Chinese titles, artists and albums into the sort fields (MP3, M4A, FLAC, Ogg), and can add them to songs in the Music app, so they list in alphabetical order.
- **Reader.** A Vocabulary view lists the words above your level, to star one by one or all at once; readings can show over new words only.
- **A new Home.** Cards you can arrange and resize, a Log page, What's New, Watch Folders and Clipboard cards.
- Fixes: Chrome long pages, lyrics search for mainland sources, OpenCC corrections, Zhuyin search in the Dictionary, and more.
- Chinese interface updated for everything new.

## 1.0 (November 2026)

First public release.

- Convert documents, file and folder names, music tags, lyrics, subtitles, pictures, scanned PDFs, the clipboard and web pages between Traditional and Simplified Chinese.
- Twelve romanizations: Pinyin, Zhuyin, Tongyong, Wade-Giles, Jyutping, Yale, Sidney Lau, Tâi-lô, POJ and Hakka, above, below or beside the characters.
- Offline Chinese–English dictionary with readings in four languages, sound, stroke order, examples and character origins.
- Reader, Study List with flashcards and writing practice, Anki export.
- Apple Music library conversion, Find Lyrics, watch folders.
- Chrome and Safari extensions.
- Interface in English, 繁體中文 and 简体中文.
