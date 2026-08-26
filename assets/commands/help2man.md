# TAGLINE

根据程序的 --help 和 --version 输出生成 man page

# TLDR

**根据程序的帮助输出生成 man page**

```help2man [program] > [program.1]```

**指定 man page 区号生成**

```help2man -s [1] [program] > [program.1]```

**为 NAME 区添加名称/描述**

```help2man -n "program description" [program] > [program.1]```

**从 include 文件中补充内容**

```help2man --include [extra.h2m] [program] > [program.1]```

**直接写入文件输出**

```help2man -o [program.1] [program]```

**抑制生成的页面中的 "info" 指引**

```help2man -N [program] > [program.1]```

# SYNOPSIS

**help2man** [_options_] _executable_

# PARAMETERS

_EXECUTABLE_
> 其 --help 与 --version 输出将被用于生成 man page 的程序。

**-n**, **--name** _STRING_
> NAME 区的简短描述。

**-s**, **--section** _NUM_
> Man page 区号（默认：1）。

**-i**, **--include** _FILE_
> 从文件中包含额外内容。该文件使用 `[section]` 标头来放置文本。

**-I**, **--opt-include** _FILE_
> 类似 **-i**，但文件缺失时不报错。

**-N**, **--no-info**
> 不生成 "参见 info 页面" 的指引。

**-o**, **--output** _FILE_
> 将输出写入文件而不是 stdout。

**-m**, **--manual** _TEXT_
> 手册名称（例如 "User Commands"）。

**-S**, **--source** _TEXT_
> 程序来源（例如 "FSF"、"Debian"）。

**-L**, **--locale** _STRING_
> 获取帮助输出时使用的 locale（默认："C"）。

**-l**, **--libtool**
> 从程序名中去掉 libtool 的 `lt-` 前缀。

**-p**, **--info-page** _TEXT_
> 要引用的 Texinfo 手册名称。

**-h**, **--help-option** _STRING_
> 替代 --help 使用的帮助选项字符串。

**-v**, **--version-option** _STRING_
> 替代 --version 使用的版本选项字符串。

**--version-string** _STRING_
> 使用此版本字符串，而不运行程序的版本选项。

**--no-discard-stderr**
> 解析选项输出时包含 stderr 输出。

**--version**
> 显示 help2man 版本。

# DESCRIPTION

**help2man** 根据程序的 `--help` 和 `--version` 输出生成 man page。它解析结构化的帮助文本并将其格式化为 troff 风格的 man page 源码，自动创建基础文档。

该工具生成的 man page 较为精简，适合遵循 GNU 帮助输出约定的程序。可以通过 include 文件（`.h2m`）添加更多内容，此类文件支持使用 `[section]` 标头在自动生成的各区之前或之后插入文本。

# CAVEATS

输出质量在很大程度上取决于程序 `--help` 输出的格式。对于 GNU 风格的选项格式（前置连字符、描述对齐）效果最佳。帮助文本不规范的程序可能生成格式欠佳的 man page，需要手动编辑。不会记录 `--help` 输出中未提及的功能。

# HISTORY

help2man 由 **Brendan O'Dea** 创建，是 **GNU** 项目的一部分，用于在构建过程中自动生成 GNU 实用工具的 man page。

# INSTALL

```apt: sudo apt install help2man```

```dnf: sudo dnf install help2man```

```pacman: sudo pacman -S help2man```

```apk: sudo apk add help2man```

```zypper: sudo zypper install help2man```

```brew: brew install help2man```

```nix: nix profile install nixpkgs#help2man```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[man](/man/man)(1), [pod2man](/man/pod2man)(1), [ronn](/man/ronn)(1)
