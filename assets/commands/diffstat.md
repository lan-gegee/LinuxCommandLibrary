# TAGLINE

补丁文件统计信息生成器

# TLDR

**显示 diff 统计信息**

```diffstat [patch.diff]```

**显示来自管道的 diff**

```diff -u [old] [new] | diffstat```

**以指定的文件名格式显示**

```diffstat -f [0|1|2|3|4] [patch.diff]```

**像 patch -p 一样剥离路径组成部分**

```diffstat -p [1] [patch.diff]```

**以表格形式显示**

```diffstat -t [patch.diff]```

**设置直方图输出宽度**

```diffstat -w [80] [patch.diff]```

# SYNOPSIS

**diffstat** [_options_] [_file_]

# PARAMETERS

**-C**
> 解析前剥离 ANSI 颜色转义序列。处理 colordiff 输出时有用。

**-c**
> 显示简洁输出，每个文件只用一个直方图代码：`+`（插入）、`-`（删除）、`!`（修改）。

**-D** _dir_
> 存放结果文件的目录，用于计算未变更的行数。

**-f** _format_
> 文件名格式：0=路径，1=名称，2=自动，3=目录，4=计数。

**-l**
> 仅列出文件名。

**-m**
> 合并各块的插入/删除计数，估算修改行数。

**-p** _num_
> 剥离 num 个前置路径组成部分（类似 `patch -p`）。

**-S** _dir_
> 包含原始文件（应用 diff 之前）的目录。

**-t**
> 以逗号分隔的表格形式输出。

**-u**
> 假定补丁在创建时新旧文件被颠倒了。

**-w** _width_
> 设置输出宽度（直方图绝不短于 10 列）。

# DESCRIPTION

**diffstat** 读取 `diff` 的输出（或任何统一/上下文格式的 diff，包括 `git diff`、`svn diff`、`hg diff` 或 `patch` 文件），并生成一个直方图，展示每个文件的插入、删除和修改情况。它常用于汇总补丁的大小与改动量。

默认情况下 `diffstat` 从 stdin 读取；给定文件参数时则从该文件读取。头部行中的文件名决定分组方式；`-p` 选项剥离前置路径组成部分的方式与 `patch -p` 相同。

# CAVEATS

直方图是按比例缩放的——宽度（由 `-w` 控制）只设定条形最大长度，并不代表变更的绝对数量。当处理的 diff 同时包含新增和删除的文件时，可用 `-c` 获得紧凑摘要。二进制文件和空 diff 不产生输出。

# HISTORY

**diffstat** 由 **Thomas E. Dickey** 于 1992 年编写，作为 GNU diff 的配套工具。大多数 Linux 发行版都以 `diffstat` 软件包的形式提供它。

# INSTALL

```apt: sudo apt install diffstat```

```dnf: sudo dnf install diffstat```

```pacman: sudo pacman -S diffstat```

```zypper: sudo zypper install diffstat```

```brew: brew install diffstat```

```nix: nix profile install nixpkgs#diffstat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[diff](/man/diff)(1), [patch](/man/patch)(1), [git-diff](/man/git-diff)(1), [colordiff](/man/colordiff)(1)
