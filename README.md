# natural-editing

An agent skill that edits text until it reads like a person wrote it. It works in Claude Code, Codex, Gemini CLI and any other agent that loads `SKILL.md` folders. It handles English and Chinese.

Most "humanizer" prompts are a list of banned words. This one treats the word list as the smaller half of the job:

- **Sentence level.** Eleven families of tells, from inflated significance ("stands as a testament to") to staged reveals ("The result?"). Each has a phrase list, a reason and a repair.
- **Paragraph level.** Openers that announce, one claim said three times, matching paragraphs, closing morals. The repair is compression.
- **Voice.** Rhythm and a direct stance come back. Slang and fragments are never bolted on, because fake-casual is as easy to spot as the original.
- **Facts.** Every name, number, date and quote survives. Nothing is invented. A claim with no source is cut and reported on a `Needs you:` line.
- **Register.** UI strings and legal text get cuts only. Reference docs keep their structure. Emails, posts and essays get the full treatment.

## Install

Clone the repository into the folder your agent reads skills from.

```bash
git clone https://github.com/wanikua/natural-editing ~/.claude/skills/natural-editing
```

```bash
git clone https://github.com/wanikua/natural-editing ~/.codex/skills/natural-editing
```

```bash
gemini skills install https://github.com/wanikua/natural-editing
```

## Use

Ask in ordinary words: "make this sound less like AI", "humanize this email", "去AI味", "改得自然一点". Paste your own earlier writing as a voice sample and the rewrite follows your sentence length and punctuation.

You get the final text and nothing else.

## The scanner

`scripts/scan.py` flags the tells a regex can see. It needs only the Python 3 standard library.

```bash
python3 scripts/scan.py examples/before-en.md
```

```text
examples/before-en.md:3: [copula] stands as
examples/before-en.md:3: [significance] testament to
examples/before-en.md:5: [fake-depth] , highlighting
...
examples/before-en.md: 35 hits (format 9, vocab 6, significance 4, promo 4, chatbot 4, ...)
```

It exits 1 when there are hits and 0 when there are none. A hit is a reason to look at the line, never proof. The skill uses the scanner for its audit pass and still rereads the draft for paragraph shape, which no regex catches.

## Example

Before (excerpt):

> In today's rapidly evolving digital landscape, staying organized is more crucial than ever. Fennel 2.0 stands as a testament to our commitment to innovation, serving as a comprehensive solution for writers, researchers, and lifelong learners.
>
> It's not just an update — it's a complete reimagining. Search is now four times faster on libraries over 10,000 notes, highlighting our dedication to performance.

After (excerpt, Gemini 4 Argon):

> We shipped Fennel 2.0 on March 3 after 14 months of development. Search is four times faster on libraries over 10,000 notes. Results come back in under 50 ms.

The full inputs and outputs are in [examples/](examples/): one English and one Chinese announcement, each rewritten by Gemini 4 Argon and by Claude Sonnet following this skill with no other guidance. All four results scan clean. Fennel is a made-up product.

## How it was made

The starting point was a short Chinese prompt, 自然编辑指南 (Natural Editing Guide): ten patterns to delete, five ways to add voice, three required passes. Claude turned it into a skill. Gemini 4 Argon reviewed the draft and found that eight of the reference examples invented facts in their "After" lines, that the voice rules pushed toward a fake-casual tone, and that paragraph shape was missing. Those three findings changed the skill more than anything else. Both models then ran it cold on the sample texts, and the ambiguities they reported were fixed.

## Limits

The skill writes for a careful human reader. It makes no promise about AI detectors, whose scores are noisy. It will not invent details to make text feel lived-in, so a draft with no facts in it comes back very short.

## Layout

```text
SKILL.md                    instructions the agent loads
references/patterns-en.md   English catalogue
references/patterns-zh.md   Chinese catalogue
scripts/scan.py             tell scanner
examples/                   before and after pairs
```

## License

MIT
