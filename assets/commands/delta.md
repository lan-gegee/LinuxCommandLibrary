# TAGLINE

带语法高亮的 diff 分页器

# TLDR

**用 delta 查看 git diff**

```git diff | delta```

**比较两个文件**

```delta [file1.txt] [file2.txt]```

**使用并排视图**

```delta -s [file1.txt] [file2.txt]```

**显示行号**

```delta -n [file1.txt] [file2.txt]```

**指定语法高亮主题**

```delta --syntax-theme [Dracula] [file1.txt] [file2.txt]```

**以 delta 格式查看 git log**

```git log -p | delta```

**以导航模式显示 diff**（用 n/N 在代码块之间跳转）

```git diff | delta --navigate```

**配置为 git 的分页器**

```git config --global core.pager delta```

**列出可用的语法主题**

```delta --list-syntax-themes```

# SYNOPSIS

**delta** [_options_] [_file1_] [_file2_]

# PARAMETERS

_FILE1_ _FILE2_
> 要比较的文件（未提供时从标准输入读取）。

**-s**, **--side-by-side**
> 并排显示模式。

**-n**, **--line-numbers**
> 显示行号。

**--syntax-theme** _THEME_
> 语法高亮主题。

**--word-diff-regex** _REGEX_
> 用正则表达式定义"词"并高亮词级别的改动。

**--hyperlinks**
> 将提交哈希、文件路径和行号渲染为终端超链接。

**--color-only**
> 不改变排版，只添加语法高亮。

**--diff-stat-align-width** _N_
> diff 统计区中为文件路径分配的宽度。

**--features** _NAMES_
> 启用在 gitconfig 中定义的具名特性集。

**--list-syntax-themes**
> 列出可用的语法高亮主题。

**--paging** _auto|always|never_
> 控制分页器的使用。

**--true-color** _auto|always|never_
> 控制 24 位 RGB 颜色输出。

**--navigate**
> 启用 n/N 键导航。

**--dark**/**--light**
> 针对深色/浅色终端优化。

**--diff-so-fancy**
> 模拟 diff-so-fancy 的输出风格。

**--raw**
> 完全不改动输入，只做语法高亮。

**--width** _N_
> 下划线/上划线装饰以及并排模式的宽度。

**--tabs** _N_
> 制表符替换为的空格数量（默认：4）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**delta** 是面向 git、diff 和 grep 输出的语法高亮分页器。它提供美观易读的 diff，支持并排视图、行号显示和词级改动高亮等特性。

delta 被设计为 git 分页器的替代品，可与 git diff、git show、git log 和 git blame 无缝集成。它使用与 bat 相同的语法高亮引擎，支持数百种语言。

特性包括在 diff 块之间导航、可自定义主题、行号超链接以及对合并冲突的特殊处理。它也能处理其他工具输出的统一 diff 格式。

# CONFIGURATION

**~/.gitconfig**
> 通过 core.pager 和 delta.* 选项将 delta 配置为默认的 git 分页器。

# CAVEATS

要获得最佳效果需要终端支持真彩色。大型 diff 的渲染可能较慢。部分主题在某些终端配色方案下效果不佳。

# HISTORY

delta 由 **Dan Davison** 创建并于 **2019 年**发布。其灵感来自 diff-so-fancy，但用 Rust 实现，性能更好并增加了语法高亮等特性。

# INSTALL

```apt: sudo apt install git-delta```

```dnf: sudo dnf install git-delta```

```pacman: sudo pacman -S git-delta```

```apk: sudo apk add delta```

```zypper: sudo zypper install git-delta```

```brew: brew install git-delta```

```nix: nix profile install nixpkgs#delta```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[diff](/man/diff)(1), [git](/man/git)(1), [bat](/man/bat)(1), [diff-so-fancy](/man/diff-so-fancy)(1), [less](/man/less)(1), [colordiff](/man/colordiff)(1)
