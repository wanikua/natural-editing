# English patterns

Eleven families of sentence-level tells, then the paragraph-level ones. Each family has phrases to watch for, the reason they read as machine-written, and one repair. The lists are starting points. Learn the shape and you will catch the variants.

Every "After" below uses only facts present in its "Before". Yours must too.

## 1. Inflated significance

**Watch for:** stands as a testament to, pivotal, milestone, watershed, marks a turning point, plays a crucial/vital/key role, in today's fast-paced world, in an ever-evolving landscape, reflects a broader trend, leaves an indelible mark, rich history, paradigm shift, game-changer, a new era.

**Why:** the sentence claims importance and gives the reader nothing to check.

> Before: The 2019 merger, which doubled headcount to 400, stands as a pivotal milestone in the company's rich history.
> After: The 2019 merger doubled headcount to 400.

A sentence with no fact in it goes entirely.

## 2. Fake depth

**Watch for:** a comma followed by highlighting, underscoring, emphasizing, reflecting, showcasing, demonstrating, fostering, ensuring, contributing to, paving the way for, cementing, symbolizing.

**Why:** the "-ing" tail asserts an analysis nobody did.

> Before: Sales rose 12% in March, underscoring the team's commitment to growth.
> After: Sales rose 12% in March.

## 3. Ad copy and vague sources

**Watch for:** vibrant, seamless, revolutionary, unparalleled, cutting-edge, world-class, state-of-the-art, groundbreaking, stunning, nestled in, bustling, unlock the potential, take it to the next level, elevate your. And: experts say, studies show, research suggests, multiple sources, industry observers, it is widely believed, many argue.

**Why:** adjectives stand in for evidence, and the sources can't be found.

> Before: Experts agree the seamless new sync, down from thirty seconds to two, is revolutionary.
> After: Sync now takes two seconds. It used to take thirty.

A citation names who said it and where. If the draft doesn't, cut the attribution and mention it under `Needs you:`.

## 4. Stock vocabulary

**Watch for:** delve, crucial, robust, leverage, utilize, facilitate, foster, harness, underscore, showcase, tapestry, landscape, realm, interplay, intricate, multifaceted, holistic, myriad, plethora, meticulous, enduring, garner, bolster, embark, align with, moreover, furthermore, additionally, notably. Phrases: comprehensive solution/guide/overview, key takeaways, deep dive, unpack, bridge the gap, navigate the complexities of, at the intersection of, double-edged sword, poised to. Intensifiers doing no work: quietly, deeply, fundamentally, truly.

**Why:** these appear far more often in model output than in ordinary writing, and readers have learned to spot them.

> Before: Additionally, the tool leverages robust caching to facilitate faster builds.
> After: The tool caches, so builds are faster.

Usually the fix is deletion. "Use" for "utilize" and "also" for "additionally" are fine when you need the word at all. Ordinary words such as "key" or "essential" are a problem only as filler ("plays a key role").

## 5. Dodging "is"

**Watch for:** serves as, stands as, acts as, functions as, represents, is regarded as, is seen as, boasts.

**Why:** models avoid plain "is" and "has". People don't.

> Before: The library serves as the campus hub and boasts 40 study rooms.
> After: The library is the campus hub. It has 40 study rooms.

## 6. Negative parallelism

**Watch for:** it's not X, it's Y; not just X but Y; not only X but also Y; more than just; No X. No Y. Just Z.; effortlessly; without breaking a sweat.

**Why:** the sentence invents an opponent to knock down. Nobody said X.

> Before: This isn't just a redesign of the editor. It's a rethink of how teams work, built around shared drafts.
> After: We redesigned the editor around shared drafts.

Keep the contrast when someone really did claim X and the text says who.

## 7. Padded threes and synonym cycling

**Watch for:** adjectives or nouns in threes where the third is filler ("fast, flexible, and intuitive"); First… Second… Third… around points too slight to number; one thing renamed each time it appears (the tool, the platform, the solution).

**Why:** three feels complete, so models add a third item that isn't there. Renaming avoids a repetition no reader would have minded.

> Before: Atlas is fast, flexible, and intuitive. The platform connects to Slack, and the solution also exports to PDF.
> After: Atlas is fast. It connects to Slack and exports to PDF.

A real list of three is fine, and so is numbering a real argument. Repeating a noun is fine.

## 8. Passive and missing subjects

**Watch for:** needs to be configured, must be installed, should be noted, can be seen, it was decided that, it is recommended that, there are several factors that.

**Why:** the actor is missing, so the reader can't tell who does the thing.

> Before: The API key needs to be configured before requests can be made.
> After: Set your API key before you send a request.

Passive is right when the actor is unknown or beside the point ("the bridge was built in 1932").

## 9. Formatting habits

**Watch for:** em dashes, above all a pair wrapping a mid-sentence concession; bullet lists carrying an argument that belongs in a paragraph; emoji as bullets or in headings; Title Case Headings; headings shaped "Topic: A Catchy Subtitle"; bold lead-ins on every bullet; a README skeleton (Overview, Features, Conclusion) forced onto an email or an essay.

**Why:** this is chat-interface formatting. Few people format a note to a colleague this way.

> Before: **Key takeaway:** the migration — while complex — is on track 🚀
> After: The migration is on track, though it has been complex.

Replace an em dash with a comma, a full stop or parentheses, unless the user's voice sample shows they use dashes. Structure stays where the content has structure: steps, options, reference material.

## 10. Chatbot residue

**Watch for:** Great question; Certainly; I hope this helps; I hope this finds you well; Let me know if; feel free to; don't hesitate to; In conclusion; To summarize; In summary; "Overall," opening a wrap-up; it's worth noting; it's important to note; at the end of the day; the future looks bright; stacked hedges (may potentially, could possibly).

**Why:** these are left over from a conversation with an assistant. In a document they answer nobody.

> Before: In conclusion, the results may potentially suggest that the cheaper model is good enough for triage. I hope this helps!
> After: The results suggest the cheaper model is good enough for triage.

## 11. Throat-clearing and staged reveals

**Watch for:** At its core; The reality is; The truth is; Here's the thing; When it comes to; It's worth asking; That said; With that in mind. And the staged kind: Enter X.; Cue X.; The result?; The catch?; The takeaway?; Spoiler:; Think again.; a colon used for a drumroll ("The answer: nothing.").

**Why:** the writer performs having a point before making it.

> Before: Manual deploys took four hours every Friday. Enter GitHub Actions. The result? Deploys now take six minutes.
> After: Moving Friday deploys to GitHub Actions cut them from four hours to six minutes.

## Paragraph level

Cleaning words is the smaller half. Look at the shape:

- The first sentence announces the topic and says nothing about it.
- One claim is restated across three clauses or three sentences.
- Paragraphs match in length and follow the same arc of claim, elaboration, moral.
- The last line restates or uplifts.

The repair is compression. Find the facts, order them by what the reader must do or know first, and write only those.

> Before:
>
> Hi team,
>
> I hope this message finds you well. I wanted to take a moment to reach out regarding the upcoming migration, which represents a significant step forward for our infrastructure.
>
> As you may know, we will be moving the billing database to the new cluster on Saturday, June 14. This is not just a routine change — it is a crucial upgrade that will enhance reliability, improve performance, and ensure scalability. During the migration window, which runs from 02:00 to 04:00 UTC, invoices cannot be created.
>
> Please ensure that any scheduled jobs are paused beforehand. If you have any questions or concerns, please don't hesitate to reach out. Thank you for your continued support and collaboration!

> After:
>
> Hi team,
>
> We're moving the billing database to the new cluster on Saturday, June 14, from 02:00 to 04:00 UTC. You can't create invoices during those two hours.
>
> Pause any scheduled jobs before 02:00. Questions to me.

The date, the window, the consequence and the request all survived. The greeting, the claim of significance, the three unbacked benefits and the sign-off were padding.

## The opposite failure

Don't trade one costume for another. A rewrite stuffed with "Honestly," "Look," one-word fragments and a joke per paragraph is as recognizable as the draft it replaced. Voice comes from the facts and the user's sample. When neither gives you a voice, plain is the right voice.
