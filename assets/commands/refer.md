# TAGLINE

处理 troff 文档中的参考文献

# TLDR

**处理带有参考文献的文档**

```refer [document.ms] | troff -ms```

**使用指定的文献数据库**

```refer -p [references.bib] [document.ms]```

**配合 groff 处理**

```groff -ms -R [document.ms]```

**以脚注风格生成参考文献**

```refer -e [document.ms]```

# SYNOPSIS

**refer** [**-p** _bibfile_] [**-e**] [**-n**] [**-l** _m,n_] [_file_...]

# PARAMETERS

**-p** _bibfile_
> 搜索指定的文献文件（可重复使用）

**-e**
> 累积参考文献并在文末打印（尾注风格）

**-n**
> 不搜索默认文献文件

**-l** _m_,_n_
> 用 m 个有效字母和 n 个数字为参考文献加标签

**-a** _n_
> 反转前 n 个作者姓名（姓在前）

**-b**
> 裸模式；抑制自动编号

**-c** _fields_
> 按指定方式将字段大写

**-k** _field_
> 使用指定字段作为引用键

**-s** _spec_
> 按规范排序参考文献

**-B** _field.macro_
> 设置文献模式

**-S**
> 生成与 sortbib 兼容的参考文献

# DESCRIPTION

**refer** 是一个 troff 预处理器，用于处理文档中的参考文献。它会在文献数据库中搜索引用，并按指定样式进行格式化。

文档中的引用用 **.[** 和 **.]** 定界符标记，其中包含用于识别参考文献的关键词。Refer 在文献库中搜索匹配条目，并插入格式化后的引用和参考文献列表条目。

文献文件采用简单格式，字段由单个字母标识（%A 表示作者、%T 表示标题、%J 表示期刊等）。每条参考文献之间用空行分隔。

Refer 通常在管道中与其他 troff 预处理器（eqn、tbl、pic）以及 troff/groff 格式化器一起使用。groff 的 **-R** 选项会自动调用 refer。

# BIBLIOGRAPHY FORMAT

**%A**: 作者名（可重复）
**%T**: 标题
**%J**: 期刊名
**%V**: 卷号
**%N**: 期号
**%P**: 页码
**%D**: 日期
**%I**: 出版商
**%C**: 城市

# CAVEATS

Refer 是为 troff/groff 文档处理设计的，不适用于 LaTeX 或 Markdown 等现代格式。对于这些格式，请使用 BibTeX 或其他特定格式的工具。

默认文献位置因系统而异。请用 **-p** 显式指定文献文件。

引用匹配基于关键词，可能产生错误匹配。请在引用中使用唯一标识符以确保可靠匹配。

# HISTORY

Refer 由贝尔实验室的 **Mike Lesk** 于 20 世纪 70 年代编写，是 Unix 文档准备系统的一部分。它早于 BibTeX，确立了文献管理的许多惯例。当前的实现是 groff 的组成部分。

# INSTALL

```apt: sudo apt install groff```

```dnf: sudo dnf install groff```

```pacman: sudo pacman -S groff```

```apk: sudo apk add groff```

```zypper: sudo zypper install groff```

```brew: brew install groff```

```nix: nix profile install nixpkgs#groff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[groff](/man/groff)(1), [troff](/man/troff)(1), [lookbib](/man/lookbib)(1)
