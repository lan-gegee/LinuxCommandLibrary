# TAGLINE

带颜色和图标的现代 ls 替代品

# TLDR

**列出当前目录**中的文件

```lsd```

以**长格式**列出详细信息

```lsd -l```

列出**全部文件**，包括隐藏文件

```lsd -la```

以**树状结构显示**并限制深度

```lsd --tree --depth [3]```

按文件大小**逆序排序**

```lsd -lS --reverse```

带 **git 状态**指示符列出

```lsd -l --git```

长格式下**目录排在前面**

```lsd -l --group-directories-first```

**列出目录的总大小**

```lsd -l --total-size```

# SYNOPSIS

**lsd** [_options_] [_files_...]

# PARAMETERS

_FILES_
> 要列出的文件或目录。默认为当前目录。

**-a**, **--all**
> 包含隐藏文件（以 `.` 开头）。

**-A**, **--almost-all**
> 包含隐藏文件，但排除 `.` 和 `..`。

**-l**, **--long**
> 以长格式显示扩展的文件元数据。

**-1**, **--oneline**
> 每行显示一个条目。

**-R**, **--recursive**
> 递归进入子目录。

**--tree**
> 以树状结构显示目录内容。

**--depth** _num_
> 限制递归深度（配合 `--tree` 或 `-R`）。

**-t**, **--timesort**
> 按修改时间排序。

**-S**, **--sizesort**
> 按文件大小排序。

**-X**, **--extensionsort**
> 按扩展名排序。

**-v**, **--versionsort**
> 对文件名中的版本号进行自然排序。

**--sort** _WORD_
> 排序依据：size、time、version、extension 或 git。

**-r**, **--reverse**
> 反转排序顺序。

**-U**, **--no-sort**
> 不排序；按目录顺序列出条目。

**--git**
> 显示所列文件和目录的 git 状态。

**--color** _WHEN_
> 控制彩色输出：always、auto 或 never（默认：auto）。

**--icon** _WHEN_
> 控制图标显示：always、auto 或 never（默认：auto）。

**--icon-theme** _THEME_
> 图标主题：fancy 或 unicode（默认：fancy）。

**--group-dirs** _VALUE_
> 目录分组方式：none、first 或 last。

**--group-directories-first**
> 目录列在文件之前（`--group-dirs=first` 的简写）。

**--date** _FORMAT_
> 日期显示格式：date、locale、relative 或自定义格式字符串。

**--size** _FORMAT_
> 大小显示格式：default、short 或 bytes。

**--permission** _FORMAT_
> 权限显示格式：rwx、octal、attributes 或 disable。

**--total-size**
> 显示目录的总大小，而不只是直接条目数。

**--blocks** _BLOCKS_
> 选择要显示的列：permission、user、group、size、date、name、inode、git。

**--header**
> 显示列标题。

**-d**, **--directory-only**
> 列出目录本身而非其内容。

**-i**, **--inode**
> 显示每个文件的 inode 编号。

**-L**, **--dereference**
> 显示符号链接目标的信息。

**--no-symlink**
> 不显示符号链接目标信息。

**-F**, **--classify**
> 为条目追加指示字符（`*/=>@|`）。

**--hyperlink** _WHEN_
> 为文件名附加超链接：always、auto 或 never。

**-I**, **--ignore-glob** _PATTERN_
> 隐藏匹配 glob 模式的条目。

**--classic**
> 启用经典模式（无颜色无图标，如同普通 ls）。

**--config-file** _PATH_
> 使用自定义配置文件。

**--ignore-config**
> 忽略配置文件，使用默认值。

**-N**, **--literal**
> 原样打印条目名，不加引号。

**-Z**, **--context**
> 显示 SELinux 或 SMACK 安全上下文。

# CONFIGURATION

**~/.config/lsd/config.yaml**
> YAML 格式的用户配置文件，用于设置默认选项、颜色、图标和显示偏好。

# DESCRIPTION

**lsd**（LSDeluxe）是用 Rust 编写的现代 `ls` 替代品。它在目录列表中加入颜色、文件类型图标和树状视图，同时保持与标准 `ls` 标志的兼容性。

该工具支持 Nerd Font 图标用于直观识别文件类型，支持 git 集成以便在文件旁边显示仓库状态，并可通过 YAML 配置文件进行深度定制。

# CAVEATS

必须在终端中安装并配置 Nerd Font，图标才能正确渲染。否则图标可能显示为空方框或问号。`--classic` 标志可禁用图标和颜色以保证兼容性。终端需支持 256 色或真彩色才能获得完整的色彩效果。

# HISTORY

**lsd**（LSDeluxe）作为传统 `ls` 命令的现代彩色 Rust 替代品诞生，灵感来自 `exa`、`eza` 等同类工具。

# INSTALL

```apt: sudo apt install lsd```

```dnf: sudo dnf install lsd```

```pacman: sudo pacman -S lsd```

```apk: sudo apk add lsd```

```zypper: sudo zypper install lsd```

```brew: brew install lsd```

```nix: nix profile install nixpkgs#lsd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ls](/man/ls)(1), [exa](/man/exa)(1), [eza](/man/eza)(1), [tree](/man/tree)(1)
