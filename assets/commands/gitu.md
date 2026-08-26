# TAGLINE

受 Magit 启发的 TUI Git 客户端

# TLDR

在当前仓库中启动 gitu

```gitu```

打开特定文件

```gitu [filename]```

在特定目录中启动

```gitu [directory]```

# SYNOPSIS

**gitu** [_options_] [_path_]

# PARAMETERS

**-c, --config** _FILE_
> 配置文件路径

**--log-level** _LEVEL_
> 设置日志级别

**-v, --version**
> 显示版本并退出

**-h, --help**
> 显示帮助并退出

# DESCRIPTION

**gitu** 是一个受 Magit（Emacs）启发的 Git 终端用户界面。它提供键盘驱动的常用 Git 操作界面，可视化地完成暂存、提交、分支和变基。

该工具按已暂存/未暂存更改、分支和最近提交等分区显示仓库状态，让复杂的 Git 操作无需死记命令即可轻松完成。

# KEYBINDINGS

**s**
> 暂存文件/hunk

**u**
> 取消暂存文件/hunk

**c**
> 提交

**b**
> 分支菜单

**r**
> 变基菜单

**l**
> 日志视图

**d**
> 差异视图

**p**
> 推送

**P**
> 拉取

**q**
> 退出

**?**
> 帮助

# CAVEATS

需要在 Git 仓库中运行。部分高级 Git 功能可能不受支持。大型仓库可能有性能问题。

# HISTORY

**gitu** 受 Magit 启发而创建，目的是把类似的功能带到独立的终端应用中。

# INSTALL

```pacman: sudo pacman -S gitu```

```apk: sudo apk add gitu```

```brew: brew install gitu```

```nix: nix profile install nixpkgs#gitu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [lazygit](/man/lazygit)(1), [tig](/man/tig)(1)
