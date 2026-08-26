# TAGLINE

bat 文件查看器在 Debian/Ubuntu 上的名称

# TLDR

> 在 Debian 和 Ubuntu 上，**bat** 二进制文件安装为 **batcat**。以下所有选项均为 **bat** 的选项。

**打印**文件并显示语法高亮和行号

```batcat [path/to/file]```

**拼接**多个文件（类似 **cat**）

```batcat [file1] [file2]```

**打印**纯文本（无行号、文件头或边框）

```batcat --plain [path/to/file]```

**显示**不可打印字符

```batcat --show-all [path/to/file]```

**高亮**指定的行范围

```batcat --line-range [40:60] [path/to/file]```

**强制**指定高亮语言

```batcat --language [json] [path/to/file]```

**让** bat 别名在你的 Shell 配置中永久生效

```alias bat=batcat```

# SYNOPSIS

**batcat** [_options_] [_file_...]

# DESCRIPTION

**batcat** 是 **bat** 二进制程序在 Debian 和 Ubuntu 上使用的命令名。该软件包以 **batcat** 的名义发布此程序，因为 **bat** 这个名字已被无关的 **bacula-console-qt** 软件包占用。其功能与 **bat** 完全相同：一个支持语法高亮、Git 集成、自动分页和文件头的 **cat** 克隆。

除 Debian/Ubuntu 外的许多发行版都将其安装为 **bat**。要在基于 Debian 的系统上使用 **bat** 这个名字，可以在 Shell 配置中添加 `alias bat=batcat`，或创建诸如 `~/.local/bin/bat` 的符号链接。

完整选项和配置请参阅 **bat**。常用选项包括 **-p**/**--plain**、**-A**/**--show-all**、**-n**/**--number**、**--language**、**--theme**、**--style**、**--paging**、**--line-range** 和 **--diff**。

# ENVIRONMENT

**BAT_THEME**
> 默认语法高亮主题。

**BAT_PAGER**
> bat 使用的分页器命令（默认为 **less**）。

**BAT_STYLE**
> **--style** 选项的默认值。

# CONFIGURATION

**~/.config/bat/config**
> 自动应用的默认命令行选项。与 bat 共用。运行 `batcat --config-file` 可查看当前生效的路径。

# INSTALL

```apt: sudo apt install bat```

```dnf: sudo dnf install bat```

```pacman: sudo pacman -S bat```

```zypper: sudo zypper install bat```

```brew: brew install bat```

```nix: nix profile install nixpkgs#bat```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[bat](/man/bat)(1), [cat](/man/cat)(1), [less](/man/less)(1), [highlight](/man/highlight)(1)

# RESOURCES

```[Source code](https://github.com/sharkdp/bat)```

<!-- verified: 2026-06-19 -->
