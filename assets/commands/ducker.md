# TAGLINE

受 k9s 启发的 Docker TUI

# TLDR

**启动** Docker TUI

```ducker```

**导出默认配置文件**

```ducker --export-default-config```

# SYNOPSIS

**ducker** [_options_]

# PARAMETERS

**-e, --export-default-config**
> 将默认配置写入默认位置，覆盖已有配置

**-h, --help**
> 显示帮助并退出

**-V, --version**
> 显示版本并退出

# DESCRIPTION

**ducker** 是一个面向 Docker 的终端用户界面，灵感来自 Kubernetes 工具 k9s。它提供高效、键盘驱动的界面来管理 Docker 容器、镜像、卷和网络，无需输入冗长的 Docker 命令。

对于来自 k9s 的用户来说，该工具的 UI 模式十分熟悉：资源视图、过滤、常用操作快捷键和实时更新一应俱全。它通过 YAML 文件配置（Linux 上通常位于 `~/.config/ducker/config.yaml`）。

# KEYBINDINGS

**:**
> 命令模式

**/**
> 过滤资源

**↑/↓**
> 在资源间导航

**Enter**
> 查看资源详情

**d**
> 描述资源

**l**
> 查看日志

**e**
> 编辑资源

**s**
> 进入容器 shell

**r**
> 重启容器

**ctrl-d**
> 删除资源

**q**
> 退出

**?**
> 显示帮助

# CAVEATS

需要 Docker 守护进程访问权限。使用 cargo 安装时请加 `--locked`，以避免上游依赖损坏。终端必须支持 UI 中使用的全部字符。

# HISTORY

**ducker** 的开发目的是把 k9s 的体验带给 Docker 用户，为容器管理提供一个强大的 TUI。它致力于让偏爱终端工作流的开发者更快、更高效地管理 Docker。

# INSTALL

```pacman: sudo pacman -S ducker```

```brew: brew install ducker```

```nix: nix profile install nixpkgs#ducker```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [k9s](/man/k9s)(1), [lazydocker](/man/lazydocker)(1), [oxker](/man/oxker)(1)
