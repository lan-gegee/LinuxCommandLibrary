# TAGLINE

交互式命令行速查表

# TLDR

**查看**速查表

```cheat [tar]```

**列出**可用的速查表

```cheat -l```

**搜索**速查表

```cheat -s [keyword]```

**编辑**速查表

```cheat -e [command]```

**创建**新速查表

```cheat -e [newcommand]```

# SYNOPSIS

**cheat** [_options_] [_command_]

# DESCRIPTION

**cheat** 允许你在命令行上创建和查看交互式速查表。它提供对常见命令示例和用法模式的快速访问，让复杂的命令语法更容易记忆。

该工具旨在成为日常使用中比 man page 更实用的替代品。

# PARAMETERS

**-l**, **--list**
> 列出可用的速查表

**-s**, **--search** _keyword_
> 搜索速查表

**-e**, **--edit** _sheet_
> 编辑速查表

**-p**, **--path**
> 显示速查表路径

**-d**, **--directories**
> 列出速查表目录

**-v**, **--version**
> 显示版本

# CONFIGURATION

**~/.config/cheat/conf.yml**
> 主配置文件，用于编辑器、速查表目录和语法高亮设置。

**~/.config/cheat/cheatsheets/personal/**
> 存放用户自建自定义速查表的目录。

# CAVEATS

需要初始设置。社区速查表需要另行下载。不如 man page 全面。自定义速查表需手动创建。默认不随系统安装。

# HISTORY

**cheat** 由 Chris Lane 于 **2013** 年前后创建，旨在提供快速访问的命令示例，灵感来自 tldr 等项目。

# INSTALL

```dnf: sudo dnf install cheat```

```zypper: sudo zypper install cheat```

```brew: brew install cheat```

```nix: nix profile install nixpkgs#cheat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tldr](/man/tldr)(1), [man](/man/man)(1), [info](/man/info)(1)

# RESOURCES

```[Source code](https://github.com/cheat/cheat)```

<!-- verified: 2026-06-22 -->
