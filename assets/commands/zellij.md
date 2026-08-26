# TAGLINE

现代终端工作区多路复用器

# TLDR

**启动新会话**

```zellij```

**启动命名会话**

```zellij -s [session_name]```

**列出现有会话**

```zellij list-sessions```

**附加到现有会话**

```zellij attach [session_name]```

**使用指定布局运行**

```zellij --layout [layout_name]```

**脱离会话（快捷键）**

```Ctrl+o d```

# SYNOPSIS

**zellij** [_options_] [_command_]

# PARAMETERS

**-s**, **--session** _name_
> 新会话的名称

**--layout** _layout_
> 使用指定的布局文件

**-l**, **--layout-path** _path_
> 布局文件的路径

**-c**, **--config** _file_
> 配置文件的路径

**--config-dir** _dir_
> 配置目录的路径

**-n**, **--new-session-with-layout** _layout_
> 使用布局创建新会话

# SUBCOMMANDS

**attach** _name_
> 附加到现有会话

**list-sessions**, **ls**
> 列出活动会话

**kill-session** _name_
> 终止指定会话

**kill-all-sessions**
> 终止所有会话

**setup**
> 设置向导与 Shell 集成

**options**
> 更改会话选项

# DESCRIPTION

**zellij** 是一个终端工作区管理器（多路复用器），类似于 tmux 和 screen，但采用了更现代的方式。它提供窗格、标签页和会话，界面键盘驱动且易于发现。

主要特性包括浮动窗格、插件系统（基于 WebAssembly）、面向常见工作流的内置布局，以及显示可用快捷键的状态栏。

默认快捷键通过 **Ctrl+按键** 进入不同模式：**Ctrl+p** 窗格模式、**Ctrl+t** 标签页模式、**Ctrl+n** 调整大小模式、**Ctrl+h** 移动模式、**Ctrl+s** 滚动模式、**Ctrl+o** 会话模式。

配置位于 **~/.config/zellij/config.kdl**，采用 KDL 格式。布局定义了窗格排列方式，便于复用工作区设置。

# CAVEATS

某些组合键可能与 Shell 或应用程序的绑定冲突。Zellij 的模式系统有助于避免冲突。

插件开发需要 Rust 和 WebAssembly 知识。

会话会一直保留直到被显式终止，若被遗忘可能持续占用资源。

# INSTALL

```pacman: sudo pacman -S zellij```

```apk: sudo apk add zellij```

```zypper: sudo zypper install zellij```

```brew: brew install zellij```

```nix: nix profile install nixpkgs#zellij```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tmux](/man/tmux)(1), [screen](/man/screen)(1), [byobu](/man/byobu)(1)
