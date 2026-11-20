#!/usr/bin/env python3
"""Flag machine-writing tells in English or Chinese text.

usage: scan.py [file ...]      reads stdin when no file is given
exit:  0 = clean, 1 = hits

A hit is a reason to look at the line, never proof. Fenced code is skipped.
"""
import re
import statistics
import sys

EN = {
    "significance": r"testament to|pivotal|milestone|watershed|turning point|ever-evolving|(?:rapidly |constantly )?evolving (?:digital )?landscape|in today's [\w -]{0,20}(?:world|age|era|landscape)|plays? an? (?:crucial|key|vital|pivotal|significant) role|game[- ]chang\w+|paradigm shift|rich (?:history|heritage|tapestry)|indelible mark|broader (?:trend|shift)s?|new era",
    "fake-depth": r",\s+(?:highlighting|underscoring|emphasizing|reflecting|showcasing|demonstrating|fostering|ensuring|contributing to|paving the way|cementing|solidifying|illustrating|signaling|symbolizing)\b",
    "promo": r"vibrant|seamless(?:ly)?|revolutionary|unparalleled|cutting-edge|world-class|state-of-the-art|groundbreaking|stunning|breathtaking|nestled|bustling|blazing|unlock(?:s|ing)? [\w ]{0,15}potential|next level|elevate your|experts (?:say|agree|believe|argue)|studies (?:show|suggest)|research (?:shows|suggests)|multiple sources|industry (?:observers|analysts|reports)|it is widely (?:believed|regarded|accepted)|many (?:believe|argue)",
    "vocab": r"delv(?:e|es|ing)|crucial|robust|leverag(?:e|es|ing)|utiliz(?:e|es|ing)|facilitat(?:e|es|ing)|foster(?:s|ing)?|harness(?:es|ing)?|underscor(?:e|es|ing)|showcas(?:e|es|ing)|tapestry|landscape|realm|interplay|intricate|intricacies|multifaceted|holistic|myriad|plethora|meticulous(?:ly)?|enduring|garner(?:s|ed)?|bolster(?:s|ed)?|embark(?:s|ing)?|aligns? with|moreover|furthermore|additionally|notably|comprehensive (?:solution|guide|overview|approach|suite)|key (?:highlights?|takeaways?|insights?)|deep dive|unpack|bridg(?:e|es|ing) the gap|navigat(?:e|es|ing) the complexit\w+|at the intersection of|double-edged sword|poised to|quietly|fundamentally",
    "copula": r"serves? as|stands? as|acts? as an?|functions? as|represents? an?|is (?:widely )?(?:regarded|seen|viewed) as|boasts?",
    "negation": r"\bnot (?:just|only|merely|simply)\b|n't (?:just|only|merely|simply)\b|more than just|no \w+[.,] no \w+[.,] just|effortless(?:ly)?|without breaking a sweat|\b(?:it|this|that)(?:'s| is|'s) not [^.?!\n]{1,50}[,.;] (?:it|this|that)(?:'s| is)\b|\b(?:isn't|wasn't) [^.?!\n]{1,50}[,.;] (?:it|this|that)(?:'s| is| was)\b",
    "threes": r"\b[\w'-]+, [\w' -]{1,25}, and [\w'-]+",
    "passive": r"needs? to be \w+(?:ed|en)|(?:must|should|can|has|have) be(?:en)? \w+(?:ed|en)\b|it (?:is|was) (?:decided|determined|found|believed|recommended) that|it should be noted",
    "chatbot": r"great question|hope this (?:helps|\w+ finds you)|let me know if|feel free to|(?:don't|do not) hesitate to|in conclusion|to summarize|in summary|to sum up|^overall,|certainly!|absolutely!|as an ai|future (?:looks|is) bright|(?:important|worth) (?:to note|noting)|at the end of the day|rest assured|(?:may|might|could) (?:potentially|possibly|perhaps)",
    "framing": r"at its core|the (?:reality|truth) is|here's the thing|when it comes to|it's worth asking|with that in mind|\benter [A-Z][\w ]{0,30}\.|\bcue [\w ]{1,30}\.|the (?:result|catch|takeaway|answer|upshot|problem|kicker)\?|spoiler(?: alert)?:|think again\.",
}

ZH = {
    "significance": r"里程碑|至关重要|意义深远|意义重大|具有重要意义|更广泛的?趋势|持续演变|在当今|日新月异|划时代|举足轻重|浓墨重彩|随着.{2,20}的(?:不断|快速|飞速|持续)?发展|新纪元|新篇章",
    "fake-depth": r"[，,](?:进一步)?(?:突出|凸显|彰显|反映|促进|证明|体现|展现|标志着|印证|折射)了?",
    "promo": r"植根于|充满活力|革命性|无与伦比|颠覆性|极致|匠心|一站式|全方位|赋能|助力|打造|引领|保驾护航|专家(?:认为|表示|指出)|多个来源|研究表明|业内人士|有观点认为|众所周知",
    "vocab": r"必不可少|不可或缺|错综复杂|值得注意的是|与此同时|同样地|旨在|致力于|全景|底层逻辑|颗粒度|对齐|打法|心智|破局|沉淀|反哺|抓手|闭环|维度|格局|生态|组合拳|最后一公里|定海神针|的(?:关键|核心)(?![一-鿿])|(?:关键|核心)(?:一步|所在|亮点|价值|优势|竞争力)|深入(?:利用|探讨|挖掘|剖析|了解)|(?:^|[。！？\n])此外",
    "copula": r"充当|构成了|代表着|被视为|被誉为|堪称|扮演着?.{0,8}角色|作为.{1,12}的存在",
    "negation": r"不是.{1,30}而是|并非.{1,30}而是|不只是|不仅仅是|不仅.{1,30}(?:而且|更|还)|无需.{1,20}只需|毫不费力|不费吹灰之力",
    "threes": r"首先.{1,200}其次|第一.{1,80}第二.{1,80}第三|[一-鿿]{2,4}、[一-鿿]{2,4}、[一-鿿]{2,4}(?![、一-鿿]{0,6}、)",
    "passive": r"需要被|应当被|应该被|被广泛|得到了?(?:广泛)?(?:应用|认可|关注)|进行了?(?:配置|优化|处理|分析|探讨|升级|重构)",
    "chatbot": r"希望(?:这)?(?:能)?对[你您]有(?:所)?帮助|很棒的问题|好问题|总而言之|总的来说|综上所述|为了总结|期待[你您]的回复|未来充满希望|未来可期|拭目以待|欢迎随时|一直以来的支持|在一定程度上|或许可能",
    "framing": r"本质上|归根结底|从某种意义上说?|某种程度上|不可否认|毫无疑问|不难发现|由此可见|的背景下|那么问题来了|果真如此吗|答案是(?:显而易见|肯定|否定)的|究竟意味着什么",
}

FORMAT = {
    "em dash": r"—",
    "emoji": r"[\U0001F300-\U0001FAFF☀-➿⭐✅]",
    "bold lead-in": r"^[ \t]*(?:[-*•][ \t]+)?(?:\S{1,3}[ \t]+)?\*\*[^*\n]{1,40}[:：]\*\*",
    "heading with colon": r"^#{1,6} .*[:：] ?\S",
    "title case heading": r"^#{1,6} (?:[A-Z][\w'-]*(?: (?:a|an|and|as|at|by|for|in|of|on|or|the|to|with))* ){2,}[A-Z][\w'-]*\W*$",
}

CJK = re.compile(r"[一-鿿]")


def strip_code(text):
    return re.sub(r"```.*?```", lambda m: "\n" * m.group().count("\n"), text, flags=re.S)


def rhythm(text):
    """Return a message when sentence lengths barely vary, else None."""
    zh = len(CJK.findall(text)) > len(text) * 0.2
    prose = "\n".join(l for l in text.split("\n") if not re.match(r"\s*(?:#|[-*•]\s|\d+\.\s|\|)", l))
    parts = [s.strip() for s in re.split(r"[.!?。！？]+", prose) if s.strip()]
    sizes = [len(CJK.findall(s)) if zh else len(s.split()) for s in parts]
    sizes = [n for n in sizes if n > 0]
    if len(sizes) < 8:
        return None
    mean, sd = statistics.mean(sizes), statistics.pstdev(sizes)
    if sd / mean < 0.35:
        return f"sentence lengths barely vary (mean {mean:.0f}, sd {sd:.1f}, {len(sizes)} sentences)"
    return None


def scan(text):
    text = strip_code(text)
    hits = []
    for table, flags in ((EN, re.I | re.M), (ZH, re.M), (FORMAT, re.M)):
        for family, pattern in table.items():
            for m in re.finditer(pattern, text, flags):
                line = text.count("\n", 0, m.start()) + 1
                if table is FORMAT:
                    hits.append((line, "format", family))
                else:
                    hits.append((line, family, m.group().strip()))
    note = rhythm(text)
    if note:
        hits.append((0, "rhythm", note))
    return sorted(hits)


def main(paths):
    sources = [(p, open(p, encoding="utf-8").read()) for p in paths] or [("stdin", sys.stdin.read())]
    total = 0
    for name, text in sources:
        hits = scan(text)
        total += len(hits)
        for line, family, shown in hits:
            where = f"{name}:{line}" if line else name
            print(f"{where}: [{family}] {shown}")
        counts = {}
        for _, family, _ in hits:
            counts[family] = counts.get(family, 0) + 1
        summary = ", ".join(f"{k} {v}" for k, v in sorted(counts.items(), key=lambda kv: -kv[1]))
        print(f"{name}: {len(hits)} hits" + (f" ({summary})" if summary else ""))
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
