# natural-editing

**English** | [简体中文](README.zh-CN.md)

A humanizer skill for coding agents, in English and Chinese, with a zero-dependency Python scanner. The skill tells the agent to cut AI-writing tells and keep every fact. When it cuts a claim for lack of a source, it says so and leaves the gap unfilled. The scanner checks any Markdown or text file with no model involved.

Install the skill:

```bash
npx skills add wanikua/natural-editing
```

Or run the scanner on its own:

```bash
python3 scripts/scan.py README.md docs/*.md
```

It works in Claude Code, Codex, Gemini CLI and any other agent that loads `SKILL.md` folders.

## Example

Before:

> **Introducing Fennel 2.0: A New Era of Note-Taking**
>
> In today's rapidly evolving digital landscape, staying organized is more crucial than ever. Fennel 2.0 stands as a testament to our commitment to innovation, serving as a comprehensive solution for writers, researchers, and lifelong learners.
>
> It's not just an update — it's a complete reimagining. Search is now four times faster on libraries over 10,000 notes, highlighting our dedication to performance. Additionally, offline mode has been rebuilt from the ground up, ensuring your notes can be accessed anywhere. Experts agree that seamless sync is key to productivity.
>
> **Key highlights:**
>
> - 🚀 **Blazing speed:** Search results in under 50 ms
> - 🔒 **Robust security:** End-to-end encryption, enabled by default
> - 🌍 **Vibrant community:** Over 12,000 users across 40 countries
>
> The update was shipped on March 3 after 14 months of development. Some features may potentially need to be configured after upgrading. In conclusion, Fennel 2.0 represents a pivotal step forward. We hope this helps, and the future looks bright!

After (Gemini 4 Argon, given this skill and nothing else):

> **Fennel 2.0**
>
> We shipped Fennel 2.0 on March 3 after 14 months of development. Over 12,000 people across 40 countries use Fennel.
>
> Search is four times faster on libraries over 10,000 notes. Results come back in under 50 ms. We also rebuilt offline mode from the ground up so you can open your notes anywhere, and end-to-end encryption is on by default.
>
> You may need to reconfigure some features after upgrading.
>
> Needs you: Add a named source if you want to keep the claim about syncing and efficiency, and list the specific settings users have to set up again after the upgrade.

Every number and date is still there. The claim with no source is gone, and the last line says so. The scanner reports 35 hits on the first text and none on the second. Fennel is a made-up product. Both files, the Chinese pair and Claude Sonnet's versions are in [examples/](examples/).

## Which humanizer to use

The table is accurate as of November 2026.

| | natural-editing | [blader/humanizer](https://github.com/blader/humanizer) | [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh) |
|---|---|---|---|
| Languages | English and Chinese in one skill | English | Chinese |
| Scanner that runs without a model | `scripts/scan.py` | None | None |
| Evidence | Four runs on two models, published in `examples/` | A blind test, 16 of 16 | 18 test cases |
| When a draft lacks specifics | Cuts the filler and adds a `Needs you:` line | Adds a detail it knows to be true | Does not add any |
| What you get back | Final text, plus the `Needs you:` line when a claim was cut | First rewrite, surviving tells, final text | Final text |

humanizer and Humanizer-zh are the tested defaults for one language. natural-editing is for three cases:

- You want a scanner that runs on files and in CI with no model.
- You want generic text cut and flagged, with nothing filled in.
- You write in both English and Chinese.

## Install

The Skills CLI command at the top is the short way. You can also clone the repository into the folder your agent reads skills from:

```bash
git clone https://github.com/wanikua/natural-editing ~/.claude/skills/natural-editing
```

```bash
git clone https://github.com/wanikua/natural-editing ~/.codex/skills/natural-editing
```

```bash
git clone https://github.com/wanikua/natural-editing ~/.gemini/skills/natural-editing
```

## Use

Ask in ordinary words: "make this sound less like AI", "humanize this email", "去AI味", "改得自然一点". Paste your own earlier writing as a voice sample and the rewrite follows your sentence length and punctuation.

You get the final text. If the skill cut a claim because it had no source, one line after the text says what you need to supply.

## What the skill does

- **Sentences.** Eleven families of tells, from inflated significance to staged reveals. Each has a phrase list, a reason and a repair, in [English](references/patterns-en.md) and [Chinese](references/patterns-zh.md).
- **Paragraphs.** Openers that announce, one claim said three times, matching paragraphs, closing morals. The repair is compression, so the result is shorter.
- **Voice.** Rhythm and a direct stance come back. Slang and fragments are never bolted on, because a fake-casual voice is as easy to spot as the original.
- **Facts.** The rules require every name, number, date and quote to survive. They forbid inventing anything. A model can still slip, so check the numbers in anything that matters.
- **Register.** UI strings and legal text get cuts only. Reference docs keep their structure. Emails, posts and essays get the full treatment.

## The scanner

`scripts/scan.py` needs only the Python 3 standard library.

```bash
python3 scripts/scan.py examples/before-en.md
```

```text
examples/before-en.md:1: [format] heading with colon
examples/before-en.md:1: [significance] New Era
examples/before-en.md:3: [copula] stands as
...
examples/before-en.md: 35 hits (format 9, vocab 6, significance 4, promo 4, chatbot 4, ...)
```

Each line gives the family in brackets, then the text that matched. Format hits give the name of the rule.

It exits 1 when there are hits and 0 when there are none. It skips code and blockquotes, which usually hold someone else's words. Pass `--all` to scan those too.

To check docs in CI, copy `scripts/scan.py` into your repository and add a step:

```yaml
- run: python3 scripts/scan.py README.md docs/*.md
  continue-on-error: true
```

Start with `continue-on-error`. The scanner exits 1 on a single hit, and people write some of these phrases too, so read a few reports before you let it block a merge.

A hit is a reason to look at the line. It says nothing about who wrote it. The scanner sees phrases. It can't see paragraph shape, and the skill rereads the draft for that.

## Questions

### Does it get text past AI detectors?

No. It edits for a human reader and ignores detector scores. Those scores are noisy, and nothing here was tested against them.

### Will it make up details so the text feels lived-in?

The rules forbid it. A draft with no facts in it comes back very short, with a line saying what is missing.

### Is the Chinese part a translation of the English rules?

No. The Chinese catalogue lists the forms the tells take in Chinese, such as `赋能`, `不是……而是……`, `进行优化` and `综上所述`, with Chinese examples.

### Does the scanner tell me whether an AI wrote something?

No. People write these phrases too. It tells you where to look.

### Which agents can use it?

Any agent that follows the [Agent Skills](https://agentskills.io/specification) format. It was run on Claude Sonnet and on Gemini 4 Argon.

## How it was made

The starting point was a short Chinese prompt, 自然编辑指南 (Natural Editing Guide): ten patterns to delete, five ways to add voice, three required passes. Claude turned it into a skill. Gemini 4 Argon reviewed the draft and found three problems. Eight of the twenty reference examples invented facts in their "After" lines, so the examples were teaching the model to hallucinate. The voice rules pushed toward a fake-casual tone. Paragraph shape was missing. Fixing those changed the skill more than anything else. Both models then ran the skill on the sample texts with no other guidance, and the ambiguities they reported were fixed.

## Credits

The pattern families trace back to Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), the guide that [blader/humanizer](https://github.com/blader/humanizer) and [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh) are built on.

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
