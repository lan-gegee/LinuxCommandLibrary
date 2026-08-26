# TAGLINE

格式化和检查 shell 脚本

# TLDR

**格式化 shell 脚本**

```shfmt [script.sh]```

**格式化并写回文件**

```shfmt -w [script.sh]```

**检查是否已格式化**（未格式化则以非零状态退出）

```shfmt -d [script.sh]```

**使用 4 空格缩进**

```shfmt -i [4] [script.sh]```

**使用制表符缩进**

```shfmt -i [0] [script.sh]```

**格式化目录中的所有脚本**

```shfmt -w [directory/]```

**按 bash 格式化**（而非 POSIX）

```shfmt -ln bash [script.sh]```

**二元运算符置于行首**

```shfmt -bn [script.sh]```

# SYNOPSIS

**shfmt** [_-w_] [_-d_] [_-i indent_] [_-ln language_] [_options_] [_files_]

# PARAMETERS

**-w**, **--write**
> 将结果写入文件而不是 stdout。

**-d**, **--diff**
> 显示差异，若未格式化则以错误退出。

**-l**, **--list**
> 列出与格式化结果不同的文件。

**-i** _N_, **--indent** _N_
> 缩进空格数（0 表示制表符）。

**-ln** _LANG_, **--language-dialect** _LANG_
> Shell 变体：bash、posix、mksh、bats。

**-bn**, **--binary-next-line**
> 二元运算符另起一行。

**-ci**, **--case-indent**
> 缩进 case 语句体。

**-sr**, **--redirect-operators**
> 重定向运算符跟随到下一行。

**-fn**, **--func-next-line**
> 函数花括号放在下一行。

**-kp**, **--keep-padding**
> 保留列对齐填充。

**-s**, **--simplify**
> 简化代码。

**-mn**, **--minify**
> 压缩输出。

**-f**, **--find**
> 递归查找 shell 文件。

**--apply-ignore**
> 应用 .shfmtignore 文件。

# DESCRIPTION

**shfmt** 用于格式化 shell 脚本。它解析并以一致的样式重写脚本，类似于 Go 的 gofmt 或 JavaScript 的 prettier。

该工具理解多种 Shell 方言：POSIX sh、bash、mksh 和 bats。可以从 shebang 自动检测，也可以显式指定。不同方言支持不同的语法。

缩进选项控制间距：-i 2 为两个空格，-i 4 为四个，-i 0 为制表符。一致的缩进是影响最大的格式化改动。

写入模式（-w）就地修改文件。差异模式（-d）在不修改的情况下检查格式，适合在 CI 中强制执行样式。退出代码表明是否需要格式化。

简化选项（-s）去除不必要的语法：多余引号、冗余分号以及 POSIX 兼容的替代写法。这样能产生更干净、更可移植的代码。

压缩模式（-mn）去除所有非必要空白，适合嵌入式脚本或受大小限制的环境。

# CAVEATS

在边缘情况下可能改变脚本行为。部分 heredoc 格式化可能比较棘手。并非所有样式偏好都可配置。解析器可能拒绝有效但不常见的语法。批量格式化前请备份文件。

# HISTORY

**shfmt** 由 **Daniel Martí**（mvdan）于约 **2016 年**创建。它以 Go 编写，灵感来自 gofmt 的代码格式化方式。该项目填补了一个空白——其他语言都有标准格式化工具，而 shell 脚本传统上没有。它已被 CI 流水线和编辑器集成广泛采用。

# INSTALL

```apt: sudo apt install shfmt```

```pacman: sudo pacman -S shfmt```

```apk: sudo apk add shfmt```

```zypper: sudo zypper install shfmt```

```brew: brew install shfmt```

```nix: nix profile install nixpkgs#shfmt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[shellcheck](/man/shellcheck)(1), [bash](/man/bash)(1), [sh](/man/sh)(1), [prettier](/man/prettier)(1)
