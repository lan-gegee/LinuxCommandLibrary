# TAGLINE

源代码和文本文件的拼写检查工具

# TLDR

**在当前目录中检查拼写错误**

```codespell```

**检查指定文件**或目录

```codespell [path/to/file.py] [path/to/directory]```

**以交互方式修复拼写错误**

```codespell -i 3 [path/to/directory]```

**将修正自动写入**文件

```codespell -w [path/to/directory]```

**忽略特定单词**

```codespell -I [wordlist.txt] [path/to/directory]```

**跳过特定文件**或目录

```codespell --skip="[*.min.js,node_modules]" [path/to/directory]```

**只检查特定文件类型**

```codespell --include-file="[*.py,*.md]" [path/to/directory]```

# SYNOPSIS

**codespell** [_options_] [_path_...]

# PARAMETERS

**-w**, **--write-changes**
> 自动将修正写入文件。

**-i** _N_, **--interactive** _N_
> 交互模式：0=否，1=询问，2=询问+确认，3=询问+显示上下文。

**-I** _FILE_, **--ignore-words** _FILE_
> 包含要忽略单词的文件（每行一个）。

**-L** _WORDS_, **--ignore-words-list** _WORDS_
> 要忽略的单词列表，以逗号分隔。

**--skip** _PATTERNS_
> 要跳过文件的 glob 模式列表，以逗号分隔。

**--include-file** _PATTERNS_
> 只检查匹配这些 glob 模式的文件。

**-d**, **--disable-colors**
> 禁用彩色输出。

**--builtin** _DICT_
> 指定要使用的内置词典。

**-q** _N_, **--quiet-level** _N_
> 设置安静级别（0=正常，1=隐藏警告，2=隐藏全部）。

**--count**
> 仅输出拼写错误的数量。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**codespell** 是一个用于查找并修复源代码、文档和文本文件中常见拼写错误的工具。它使用一份精心整理的常见拼写错误及其纠正词的词典，因此能有效捕捉普通拼写检查器容易漏掉的错误。

该工具在 CI/CD 流水线中尤为实用，可以在拼写错误进入代码库之前将其拦截。它能理解编程语境，避免对有意使用的技术术语、变量名和代码模式产生误报。

codespell 可以以仅检查模式进行验证、以交互模式进行人工审核，或以写入模式进行自动修正。自定义忽略列表可以适配项目特有的术语，避免被误判为错误。

# CAVEATS

自动写入模式可能会错误地"修正"有意使用的非标准拼写或技术行话。内置词典侧重于英语和常见编程术语，某些合法的技术术语可能需要加入忽略列表。

# HISTORY

codespell 由 Lucas De Marchi 创建，目前作为一个开源项目维护。它的诞生源于在大规模代码库（尤其是有许多贡献者的开源项目）中捕捉常见拼写错误的需求。该工具已被众多项目采用，其中包括 Linux 内核。

# INSTALL

```dnf: sudo dnf install codespell```

```pacman: sudo pacman -S codespell```

```apk: sudo apk add py3-codespell```

```zypper: sudo zypper install codespell```

```brew: brew install codespell```

```nix: nix profile install nixpkgs#codespell```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aspell](/man/aspell)(1), [hunspell](/man/hunspell)(1), [spell](/man/spell)(1)

# RESOURCES

```[Source code](https://github.com/codespell-project/codespell)```

<!-- verified: 2026-06-22 -->
