# TAGLINE

支持编辑器集成的现代 tree 替代品

# TLDR

显示目录树

```tre```

显示隐藏文件

```tre -a```

限制深度

```tre -l [2]```

启用编辑器集成

```tre -e```

指定目录

```tre [path/to/directory]```

仅显示目录

```tre -d```

输出为 JSON

```tre -j```

排除匹配正则表达式的路径

```tre -E [pattern]```

可移植路径

```tre -p```

# SYNOPSIS

**tre** [_-a_] [_-l depth_] [_-e_] [_options_] [_path_]

# PARAMETERS

**-a, --all**
> 包含隐藏文件。

**-d, --directories**
> 仅列出目录。

**-l, --limit** _DEPTH_
> 最大深度。

**-e, --editor** [_COMMAND_]
> 编辑器集成（为文件编号，创建别名）。

**-E, --exclude** _PATTERN_
> 排除匹配正则表达式的路径。可重复使用。

**-j, --json**
> 输出 JSON 而非树状图。

**-p, --portable**
> 编辑器别名中使用可移植的绝对路径。

**-s, --simple**
> 忽略 .gitignore 规则。

**-c, --color** _WHEN_
> 彩色输出：automatic、always、never。

# DESCRIPTION

**tre** 是经典 tree 命令的现代替代品，用 Rust 编写。它以树状格式展示目录结构，并带有面向开发者工作流的附加特性，包括编辑器集成和 gitignore 感知。

编辑器集成模式（**-e**）会为输出中的每个文件编号，并创建一个 Shell 别名，通过编号即可在编辑器中打开对应文件。可移植路径模式（**-p**）输出的路径可以直接复制粘贴到其他命令中。

默认情况下，tre 会遵循 `.gitignore` 规则，过滤掉被忽略的文件，从而更清晰地呈现项目结构。除非用 **-a** 明确要求，否则隐藏文件不会显示。

# CAVEATS

并非 **tree** 的直接替代品——标志名称不同（例如深度选项用 **-l** 而不是 **-L**）。默认遵循 .gitignore，可通过 **-s** 禁用。

# INSTALL

```apt: sudo apt install tre-command```

```dnf: sudo dnf install tre```

```pacman: sudo pacman -S tre```

```brew: brew install tre-command```

```nix: nix profile install nixpkgs#tre-command```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tree](/man/tree)(1), [exa](/man/exa)(1), [fd](/man/fd)(1)
