# natural-editing

[English](README.md) | **简体中文**

一个中英文都能用的去 AI 味 skill，附带零依赖的 Python 检查脚本。Skill 要求 Agent 删掉 AI 腔、保留全部事实；因为没有出处而删掉的说法会在文末提示，不会自己编内容补上。检查脚本不调用模型，可以直接查任意 Markdown 或文本文件。

安装 skill：

```bash
npx skills add wanikua/natural-editing
```

或者只用检查脚本：

```bash
python3 scripts/scan.py README.md docs/*.md
```

支持 Claude Code、Codex、Gemini CLI，以及其他兼容 `SKILL.md` 的 Agent。

## 示例

改之前：

> **茴香笔记 2.0：开启笔记新纪元**
>
> 在当今日新月异的数字时代，高效整理信息至关重要。茴香笔记 2.0 具有里程碑意义，充当着写作者、研究者和终身学习者的一站式解决方案。
>
> 这不是一次简单的更新，而是一次彻底的重塑。在超过 1 万条笔记的资料库里，搜索速度提升到原来的 4 倍，彰显了我们对性能的不懈追求。此外，离线模式进行了重构，确保笔记随时随地都能被访问。专家认为，无缝同步是提升效率的关键。
>
> **核心亮点：**
>
> - 🚀 **极致速度：** 搜索结果 50 毫秒内返回
> - 🔒 **全方位安全：** 端到端加密，默认开启
> - 🌍 **充满活力的社区：** 来自 40 个国家的 1.2 万名用户
>
> 本次更新历时 14 个月开发，于 3 月 3 日发布。升级后部分功能可能在一定程度上需要被重新配置。综上所述，茴香笔记 2.0 是迈向未来的关键一步。希望对你有帮助，未来可期！

改之后（Gemini 4 Argon 只加载了这个 skill，没有其他提示词）：

> **茴香笔记 2.0**
>
> 我们花了 14 个月开发茴香笔记 2.0，已在 3 月 3 日发布。目前有 40 个国家的 1.2 万名用户在用。
>
> 超过 1 万条笔记的资料库，搜索速度提升到原来的 4 倍，50 毫秒内就能返回结果。我们还重构了离线模式，在哪都能打开笔记。端到端加密默认开启。
>
> 升级后，部分功能可能需要你重新配置。
>
> 需要你补充：如果想保留同步能提高工作效率的说法，请注明具体出处，并写明升级后具体是哪些设置需要用户重新调整。

数字和日期全部保留。那句没有出处的 `专家认为` 删掉了，文末有一行提示。检查脚本在原稿里查出 31 处，改写稿 0 处。茴香笔记是虚构的产品。这两份文件、英文那一组和 Claude Sonnet 的改写结果都在 [examples/](examples/)。

## 该用哪个

下表数据截至 2026 年 11 月。

| | natural-editing | [blader/humanizer](https://github.com/blader/humanizer) | [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh) |
|---|---|---|---|
| 语言 | 中英文在同一个 skill 里 | 英文 | 中文 |
| 不调用模型的检查脚本 | `scripts/scan.py` | 没有 | 没有 |
| 验证 | 两个模型共 4 次试跑，结果在 `examples/` | 一次盲测，16 比 0 | 18 个测试用例 |
| 原文缺具体内容时 | 删掉空话，文末提示缺什么 | 补充它确知为真的细节 | 不补 |
| 交付内容 | 最终稿，删了无出处的说法时多一行提示 | 初稿、残留问题和最终稿 | 最终稿 |

只处理一种语言，humanizer 和 Humanizer-zh 是经过验证的默认选择。下面三种情况用 natural-editing：

- 想要一个不调用模型的检查脚本，能查本地文件，也能放进 CI
- 想让空话被删掉并提示，不想让模型自己补内容
- 中文和英文都写

## 安装

开头那条 Skills CLI 命令最省事。也可以直接克隆到 Agent 读取 skill 的目录：

```bash
git clone https://github.com/wanikua/natural-editing ~/.claude/skills/natural-editing
```

```bash
git clone https://github.com/wanikua/natural-editing ~/.codex/skills/natural-editing
```

```bash
git clone https://github.com/wanikua/natural-editing ~/.gemini/skills/natural-editing
```

## 使用

照平常说话的方式提就行：「去 AI 味」「太 AI 了」「改得自然一点」「humanize this email」。附上一段你平时写的文字当样本，改写稿会模仿你的句子长短和标点习惯。

你拿到的是最终稿。如果有说法因为没有出处被删掉，文末会多一行，说明需要你补什么。

## 它做什么

- **句子**：十一类痕迹，从夸大重要性到自问自答。每类都有短语表、原因和改法，[中文](references/patterns-zh.md)和[英文](references/patterns-en.md)各一份
- **段落**：开头先铺垫、一个意思说三遍、段落长得一样、结尾升华。改法是压缩，所以稿子会变短
- **语气**：找回长短句交错的节奏，有话直说。不硬塞口语词和碎句，装出来的松弛感和原来的 AI 腔一样好认
- **事实**：规则要求原文的每个事实都保留下来，包括数字和引语，并且禁止编造。模型仍然可能出错，重要稿件里的数字请自己核对一遍
- **文体**：界面文案和法律文本只删不加，参考文档保留结构，邮件、帖子和文章才完整处理

## 检查脚本

`scripts/scan.py` 只用 Python 3 标准库。

```bash
python3 scripts/scan.py examples/before-zh.md
```

```text
examples/before-zh.md:1: [format] heading with colon
examples/before-zh.md:1: [significance] 新纪元
examples/before-zh.md:3: [copula] 充当
...
examples/before-zh.md: 31 hits (format 8, significance 5, promo 5, vocab 4, chatbot 4, ...)
```

每行方括号里是类别，后面是命中的原文。格式类的命中显示的是规则名。

有命中时退出码是 1，没有是 0。代码和引用块默认跳过，因为那通常是别人的话。加 `--all` 可以连它们一起查。

想在 CI 里检查文档，把 `scripts/scan.py` 复制进你的仓库，再加一步：

```yaml
- run: python3 scripts/scan.py README.md docs/*.md
  continue-on-error: true
```

先带着 `continue-on-error` 跑。脚本只要有一处命中就返回 1，而这些说法人也会写，看过几次报告再决定要不要让它拦住合并。

命中只说明这一行值得看一眼，不能说明是谁写的。脚本只匹配词句，识别不了段落结构，段落层面的问题靠 skill 通读全文来处理。

## 常见问题

### 能过 AI 检测器吗？

不能。它只管人读起来是否自然，不管检测器给几分。检测器的分数不稳定，这里也没有针对检测器做过测试。

### 会不会为了显得真实而编细节？

规则禁止这样做。一篇没有任何事实的稿子，改完会非常短，文末附一行说明缺什么。

### 中文部分是英文规则翻译过来的吗？

不是。中文清单列的是这些痕迹在中文里的样子，比如 `赋能`、`不是……而是……`、`进行优化`、`综上所述`，例子也都是中文的。

### 检查脚本能判断一段话是不是 AI 写的吗？

不能。这些说法人也会写。它只告诉你该看哪里。

### 哪些 Agent 能用？

遵循 [Agent Skills](https://agentskills.io/specification) 格式的都可以。实际跑过的是 Claude Sonnet 和 Gemini 4 Argon。

## 怎么做出来的

最初是一份很短的中文提示词《自然编辑指南》：十类要删的模式，五条找回人味的做法，三遍必做的流程。Claude 把它写成了 skill，再交给 Gemini 4 Argon 审稿。Gemini 指出三个问题：二十个改写示例里有八个凭空多出了原文没有的事实，等于在教模型编造；语气规则容易让模型故意装随意；没有段落层面的规则。改掉这三处，效果比后面所有修改加起来都明显。之后两个模型各自只拿着 skill 在样稿上试跑，执行时有歧义的规则也都改了。

## 致谢

这些模式的分类来自维基百科的 [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)，[blader/humanizer](https://github.com/blader/humanizer) 和 [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh) 也都建立在它之上。

## 目录

```text
SKILL.md                    Agent 加载的指令
references/patterns-en.md   英文模式清单
references/patterns-zh.md   中文模式清单
scripts/scan.py             检查脚本
examples/                   改写前后的完整样稿
```

## 许可

MIT
