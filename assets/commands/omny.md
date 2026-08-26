# TAGLINE

终端界面的 SSH 连接管理器

# TLDR

**启动**交互式 SSH 管理器

```omny```

**使用**自定义配置文件

```omny -c [path/to/config.toml]```

**覆盖**配色主题

```omny -t [dracula]```

**启用**详细的调试日志

```omny -v```

**显示**版本号

```omny --version```

# SYNOPSIS

**omny** [_options_]

# DESCRIPTION

**omny**（来自 OmnySSH 项目）是一个快速、键盘驱动的终端用户界面，用于管理 SSH 连接。它组织你的主机，让你可以在单一控制台应用中打开会话、传输文件和运行保存的命令。

它的主要视图包括：带彩色 CPU、内存和磁盘用量指标的实时仪表盘；用于在本地与远程系统之间移动文件的分栏 SFTP 文件管理器；可保存常用命令并向多台服务器同时广播的代码片段管理器；以及带 PTY 标签页和分屏视图的多会话终端。模糊搜索让主机和片段触手可及，外观与按键绑定均可配置。

在 TUI 中，数字键切换视图（**1** 仪表盘、**2** 文件管理器、**3** 片段、**4** 终端），**/** 打开模糊搜索，**?** 显示帮助。

# PARAMETERS

**-c** _file_, **--config** _file_

> 使用指定的配置文件代替默认配置。

**-t** _theme_, **--theme** _theme_

> 覆盖配色主题（例如 default、dracula、nord、gruvbox）。

**-v**, **--verbose**

> 启用调试日志。

**-h**, **--help**

> 打印帮助信息。

**-V**, **--version**

> 打印版本信息。

# CONFIGURATION

omny 读取 TOML 配置文件，其中定义了主机、主题和可重新映射的按键绑定。路径可通过 **--config** 覆盖。

# CAVEATS

omny 是一个用 Rust 编写的年轻第三方工具；其配置格式和特性可能在版本间发生变化。二进制文件名为 **omny**，而项目和软件包名为 **omnyssh**。

# SEE ALSO

[ssh](/man/ssh)(1), [sftp](/man/sftp)(1), [sshfs](/man/sshfs)(1), [mosh](/man/mosh)(1), [tmux](/man/tmux)(1)

# RESOURCES

```[Source code](https://github.com/timhartmann7/omnyssh)```

<!-- verified: 2026-06-16 -->
