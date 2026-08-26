# TAGLINE

CommonMark Markdown 解析器与渲染器

# TLDR

**将 Markdown 转换为 HTML**

```cmark [input.md]```

**转换为特定格式**

```cmark --to [html|xml|man|latex] [input.md]```

**从 stdin 读取**

```cat [input.md] | cmark```

**输出到文件**

```cmark [input.md] > [output.html]```

**启用智能排版**

```cmark --smart [input.md]```

**转换为 groff man page** 格式

```cmark --to man [input.md]```

**校验 UTF-8** 并替换无效序列

```cmark --validate-utf8 [input.md]```

**以硬换行渲染**

```cmark --hardbreaks [input.md]```

# SYNOPSIS

**cmark** [_options_] [_file..._]

# PARAMETERS

**--to** _format_
> 输出格式：html、xml、man、commonmark、latex。

**--smart**
> 启用智能标点（弯引号、破折号）。

**--safe**
> 省略原始 HTML 和潜在的不安全链接。

**--validate-utf8**
> 校验 UTF-8 并替换无效序列。

**--hardbreaks**
> 将软换行渲染为硬换行。

**--nobreaks**
> 将软换行渲染为空格。

**--width** _N_
> 在第 N 列处折行（默认 0，不折行）。仅影响 commonmark 和 man 输出。

**--sourcepos**
> 在输出中包含源码位置信息。

# DESCRIPTION

**cmark** 是 CommonMark 的参考 C 实现，CommonMark 是 Markdown 的一个强规范、高兼容性变体。它解析 Markdown 输入并将其转换为多种输出格式，包括 HTML、XML、groff man page、CommonMark 和 LaTeX。

该解析器专为正确性和性能而设计，严格遵循 CommonMark 规范，消除了原始 Markdown 描述中存在的歧义。这使其适合需要在不同工具间获得可预测、一致渲染效果的应用。

cmark 从文件或标准输入读取并写入标准输出，因此很容易集成到管道中。**--smart** 选项提供排版增强功能，如弯引号和长破折号；**--safe** 则会剥离输入中潜在危险的原始 HTML。

# HISTORY

**cmark** 是 **CommonMark** 规范的参考 C 实现，由 John MacFarlane 及其贡献者自 **2014 年**起开发。CommonMark 旨在为 Markdown 提供一份正式且无歧义的规范。

# INSTALL

```apt: sudo apt install cmark```

```dnf: sudo dnf install cmark```

```pacman: sudo pacman -S cmark```

```apk: sudo apk add cmark```

```zypper: sudo zypper install cmark```

```brew: brew install cmark```

```nix: nix profile install nixpkgs#cmark```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pandoc](/man/pandoc)(1), [markdown](/man/markdown)(1), [grip](/man/grip)(1)
