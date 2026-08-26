# TAGLINE

快速的交互式全代码库查找替换工具

# TLDR

**交互式替换字符串**于当前目录

```fastmod "[old_string]" "[new_string]"```

**使用正则表达式替换**并支持多行匹配

```fastmod -m "[pattern]" "[replacement]"```

**在指定目录中替换**

```fastmod "[old]" "[new]" [path/to/directory]```

**只在具有指定扩展名的文件中替换**

```fastmod -e "[py,js]" "[old]" "[new]"```

**接受所有替换**而不逐个提示

```fastmod --accept-all "[old]" "[new]"```

**预览匹配结果**而不修改文件

```fastmod --print-only "[old]" "[new]"```

**将模式视为字面字符串**而非正则表达式

```fastmod --fixed-strings "[old.string()]" "[new.string()]"```

# SYNOPSIS

**fastmod** [_options_] _pattern_ [_replacement_] [_paths_...]

# DESCRIPTION

**fastmod** 对文件执行快速、交互式的 codemod 操作。它搜索正则表达式模式，并在每次替换前提示确认，使批量代码修改更安全。

该工具使用与 ripgrep 相同的正则引擎进行快速搜索，并结合对变更的交互式审查。默认情况下，模式被视为正则表达式。如果未提供替换文本，fastmod 会删除匹配的文本。如果未提供路径，它会递归搜索当前目录。

交互模式下，按 **y** 接受、**n** 跳过、**e** 编辑替换文本、**a** 接受所有剩余项，或 **q** 退出。

# PARAMETERS

**-m**, **--multiline**
> 启用多行正则匹配（`.` 可匹配换行符）。

**-i**, **--ignore-case**
> 不区分大小写匹配。

**-e**, **--extensions** _exts_
> 要处理的文件扩展名的逗号分隔列表（如 py,js,ts）。

**--accept-all**
> 应用所有替换，不进行交互式确认。

**--print-only**
> 只显示匹配项，不修改文件。

**-d**, **--dir** _path_
> 设置根搜索目录（默认：当前目录）。

**--glob** _pattern_
> 按 glob 模式包含/排除文件（加 ! 前缀表示排除）。

**--hidden**
> 在搜索中包含隐藏文件和目录。

**--fixed-strings**, **-F**
> 将模式视为字面字符串，而非正则表达式。

**--count**
> 显示匹配/替换的总数。

# CAVEATS

使用 Rust 的正则语法，在某些边界情况下可能与 PCRE 或 POSIX 正则不同。交互模式需要终端。使用 **--accept-all** 时，变更将在无确认的情况下应用——请先用 **--print-only** 预览。

# HISTORY

**fastmod** 由 **Facebook**（Meta）开发，是用于大规模代码修改的工具。它满足了在海量代码库中进行交互式、安全重构的需求。该项目以开源形式发布，用 Rust 编写以保证性能。

# INSTALL

```brew: brew install fastmod```

```nix: nix profile install nixpkgs#fastmod```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sed](/man/sed)(1), [codemod](/man/codemod)(1), [comby](/man/comby)(1), [rg](/man/rg)(1)
