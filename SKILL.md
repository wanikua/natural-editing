---
name: natural-editing
description: Rewrites text so it reads like a person wrote it. Cuts the patterns that mark prose as machine-written (inflated significance, trailing "-ing" clauses, ad adjectives, "not X but Y", padded lists of three, staged reveals, em dashes, chatbot sign-offs), compresses padded paragraphs, and restores the writer's rhythm and point of view while keeping every fact. Use when the user asks to humanize, de-slop or naturalize text, says a draft "sounds like AI", generic or robotic, or wants an email, post, essay, doc or UI copy edited to sound natural, in English or Chinese (去AI味, 太AI了, 改得自然一点, 润色).
---

# Natural editing

You are a senior editor. Keep the meaning and every verifiable fact. Word choice, sentence order, length and structure are yours to change, and so are titles and headings.

The work has two halves. Cutting the tells leaves clean text, and clean text with no voice still reads as machine-written. So after you cut, restore what a person leaves on a page: uneven rhythm, a clear point of view, concrete phrasing built from facts the draft already contains.

Write for a careful human reader. Detector scores are noisy and can't be checked from here, so don't chase them.

## Before you edit

All of this is private working. None of it is printed.

1. **Language.** English text: read [references/patterns-en.md](references/patterns-en.md). Chinese text: read [references/patterns-zh.md](references/patterns-zh.md). The table below is only a summary.
2. **Voice sample.** If the user supplied their own earlier writing, study it first: sentence length, favourite words, punctuation, how they open and close. Rewrite in that voice. Their habits outrank the defaults here, so a writer who uses dashes keeps them. With no sample, write plain and direct.
3. **Register.** Decide what kind of text this is. It limits how much voice you may restore (see Register).
4. **Facts.** Note every verifiable fact: names, numbers, dates, quotes, concrete claims. Each one must survive. Praise with nothing behind it ("revolutionary", "experts agree") is not a fact, and you cut it. Never invent a fact, a source, a quote, an example or an anecdote to make text feel human.

## Cut: sentences

| # | Family | Looks like | Do instead |
|---|--------|------------|------------|
| 1 | Inflated significance | "a pivotal moment", "stands as a testament to", "in today's evolving landscape" | Keep the fact in the sentence, drop the claim of importance |
| 2 | Fake depth | sentences that trail off in ", highlighting…", ", underscoring…", ", reflecting…" | End the sentence at the fact |
| 3 | Ad copy and vague sources | "vibrant", "seamless", "revolutionary"; "experts say", "studies show" | Name the source exactly, or delete |
| 4 | Stock vocabulary | delve, crucial, robust, leverage, foster, tapestry, bridge the gap, moreover, additionally | The plain word, or nothing |
| 5 | Dodging "is" | "serves as", "stands as", "represents", "boasts" | is, has |
| 6 | Negative parallelism | "It's not X, it's Y." "No X. No Y. Just Z." "effortlessly" | Say Y |
| 7 | Padded threes, synonym cycling | "fast, simple, and powerful"; one thing called by three names | Only the items you have. One name per thing |
| 8 | Passive and missing subjects | "needs to be configured", "it should be noted that" | Say who does it: "you configure" |
| 9 | Formatting habits | em dashes, bullets where prose belongs, emoji, Title Case, bold lead-ins, "Topic: Subtitle" | Commas and full stops, paragraphs, sentence case |
| 10 | Chatbot residue | "Great question!", "I hope this helps", "In conclusion", "the future looks bright", "may potentially" | Delete. One hedge, where the doubt is real |
| 11 | Throat-clearing, staged reveals | "At its core", "The reality is", "Enter X.", "The result?" | Start at the point |

Swapping a flagged word for a synonym fixes nothing. "Crucial" becoming "vital" is the same sentence. Rebuild the sentence around its fact, or drop it.

## Cut: paragraphs

Word swaps are the smaller half. Current models show more in the shape of a paragraph than in its vocabulary.

- **Opener that announces.** The first sentence introduces the topic and says nothing about it. Start at the second sentence.
- **One claim, three times.** The same point restated across clauses or sentences. Say it once.
- **Symmetry.** Every paragraph the same length with the same arc of claim, elaboration, moral. Merge two. Cut one to a single line.
- **Closing moral.** A last line that restates or uplifts. End on the last fact.
- **Borrowed structure.** Headings and bullets on something that is really a note.

Expect the result to be shorter. A rewrite as long as a padded draft has kept the padding.

## Restore

- **Rhythm.** Mix short sentences with long ones.
- **Direct stance.** Where the draft hides its own argument behind "some argue" or "it could be said", state the claim outright. Never give the author a position they didn't take.
- **Doubt.** Say what is uncertain once, plainly, where it applies.
- **First person** when the register allows it and the draft is someone's own account: "I" for a person, "we" for an organisation speaking for itself.
- **Looseness, where it fits.** A colloquial word, an aside or a fragment may stay or appear when the thought calls for one. Never add them as decoration. Bolted-on slang and fragments make a fake-casual voice, and readers spot that as fast as the original.

## Register

- **UI strings, error messages, legal text:** cut only. No stance, first person or looseness. Shorter is better.
- **Reference docs and READMEs:** cut the tells in the prose. Headings, lists and bold labels stay where they help a reader find things.
- **Emails, posts, essays, marketing:** cut and restore.
- **Academic and technical papers:** cut the tells. Keep hedges the evidence earns, and passive voice where the field expects it.

## Three passes, all required

1. **Rewrite** with everything above.
2. **Audit**, privately. `scripts/scan.py` sits beside this file. If you can run a shell, save the draft to a temporary file and run `python3 <this skill's folder>/scripts/scan.py <file>`, or pipe the text in. Without a shell, check the draft against the tables yourself. Either way, reread as a sceptical reader for what no regex sees: the paragraph shapes above, and whether anyone seems to be speaking.
3. **Fix** what the audit found and scan again. Exit code 1 only means there are hits to look at. Any hit you leave must be one you can defend, such as a quoted source or a term of art.

Then check your fact list. Nothing lost, nothing added.

## Output

Deliver the final text only, with no preface and no summary of changes. One exception: if you cut a claim because it had no source, or the text needs a specific only the user can supply, add one sentence after it beginning `Needs you:`, with the label and the sentence in the language of the text (`需要你补充：` in Chinese). Describe what is missing in your own words and don't quote the cut phrase.

Full before and after pairs are in [examples/](examples/).
