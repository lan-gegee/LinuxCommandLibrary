# TAGLINE

低误报的源代码拼写检查器

# TLDR

**检查**当前目录中的拼写错误

```typos```

**检查指定的**文件或目录

```typos [path/to/file_or_dir]```

**自动就地修复**检测到的拼写错误

```typos --write-changes```

**以 unified diff 形式预览**建议的修复

```typos --diff```

**以 JSON 格式输出结果**便于工具集成

```typos --format json```

**包含隐藏文件**和被忽略的路径

```typos --hidden --no-ignore```

**使用指定的**英语变体

```typos --locale en-gb```

**使用自定义配置文件进行检查**

```typos --config [path/to/_typos.toml]```

# SYNOPSIS

**typos** [_OPTIONS_] [_PATH_...]

# PARAMETERS

**-w**, **--write-changes**
> 将建议的修正写入文件，而不只是报告。

**--diff**
> 以 unified diff 打印拟议更改，不修改文件。

**--format** _FORMAT_
> 输出格式：_silent_、_brief_、_long_（默认）、_json_。

**--config** _FILE_
> 配置文件的路径（通常是 _\_typos.toml_）。

**--locale** _LOCALE_
> 设置英语方言：_en_、_en-us_、_en-gb_、_en-ca_、_en-au_。

**--exclude** _GLOB_
> 跳过匹配给定 gitignore 风格模式的路径。

**--force-exclude**
> 即使路径在命令行中被显式给出，也强制跳过被排除的路径。

**--hidden**
> 包含隐藏文件和目录。

**--no-ignore**
> 不遵守任何 ignore 文件。

**--no-ignore-vcs**
> 不遵守版本控制目录内的 ignore 文件。

**--no-ignore-dot**
> 不遵守 _.ignore_ 文件。

**--no-ignore-global**
> 不遵守全局 ignore 文件。

**--no-ignore-parent**
> 不遵守来自父目录的 ignore 文件。

**--binary**
> 将二进制文件也当作文本进行检查。

**--no-unicode**
> 将标识符限制为 ASCII。

**--type-list**
> 打印所有已知文件类型及其 glob 模式。

**--type** _TYPE_
> 只检查给定类型的文件（如 _rust_、_py_）。

**--type-not** _TYPE_
> 排除给定类型的文件。

**-V**, **--version**
> 打印版本并退出。

**-h**, **--help**
> 打印帮助。

# DESCRIPTION

**typos** 是一款专为源代码打造的快速拼写检查器。它遍历文件树，默认遵守 _.gitignore_ 规则，标记标识符、注释和字符串中拼错的单词，同时将误报率控制在足够低，可以直接放进 pull request 门禁中运行。

检测由一个精选的常见代码拼写错误词典驱动，而非完整的自然语言词典，因此能容忍 camelCase、snake_case、缩写以及领域专有术语。检测结果可以打印出来、用 **--write-changes** 写回磁盘，或输出为 JSON 供编辑器和 CI 工具使用。

该检查器还通过文件类型映射了解各语言的约定，可以用 **--locale** 切换英式或美式英语，并遵守在 **\_typos.toml**、**typos.toml**、**Cargo.toml** 或 **pyproject.toml** 中定义的项目级覆盖配置。

# CONFIGURATION

项目配置位于 **\_typos.toml**（或 **pyproject.toml** / **Cargo.toml** 内的 **[tool.typos]** 表）。常用配置节：

```
[default]
locale = "en-us"
extend-ignore-re = ["(?Rm)^.*#\\s*spellchecker:disable-line$"]

[default.extend-words]
mater = "mater"

[default.extend-identifiers]
HashMa = "HashMap"

[type.rust]
extend-glob = ["*.rs"]
check-file = true
```

**[default.extend-words]** 和 **[default.extend-identifiers]** 表既可以把手误重映射为正确拼写，也可以通过把单词/标识符映射到自身来将其标记为有效。

# CAVEATS

**typos** 不是通用的英语拼写检查器：它只标记内置手误词典中的单词，因此会漏掉许多不在列表中的真实拼写错误。反过来，项目专有的名称、缩写词和非英语词汇也可能触发误报，需要在 **\_typos.toml** 中添加条目。使用 **--write-changes** 会就地修改文件：请先用 **--diff** 审查，尤其是在词典内容不熟悉的情况下。

# HISTORY

**typos** 由 **Ed Page**（crate-ci）创建，于 **2019 年**作为开源项目发布，使用 **Rust** 编写。它的设计目标是足够快、足够准，能在大型 monorepo 的每次提交上运行；其灵感来自 **misspell** 和 **scspell** 等早期面向代码的拼写检查器，但专注于一个精选的低误报语料库。

# INSTALL

```pacman: sudo pacman -S typos```

```apk: sudo apk add typos```

```nix: nix profile install nixpkgs#typos```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aspell](/man/aspell)(1), [hunspell](/man/hunspell)(1), [codespell](/man/codespell)(1)
